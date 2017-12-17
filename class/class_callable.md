Python how callables work

> `callable`的概念是Python的基础.当思考什么能被`called`(调用)时,最显而易见的就是`functions`(函数).不论是用户自定义的函数,还是系统的`builtin functions`(用C 实现).函数意味着能被`called` (调用)
>
> 当然还要`class methods` , 只要一个类实现了`__call__` 这个方法,它就是能被调用的.通过类创建的实例也是可调用的.
>
> ```python
> class Joe:
>   ... [contents of class]
>
> joe = Joe()
> ```
>
> Here we "call" `Joe` to create a new instance. So classes can act as functions as well!
>
> 事实证明，所有这些概念在CPython实现中都很好地结合在一起。 Python中的所有东西都是一个对象，包括前面段落中描述的每个实体（用户＆内建函数，方法，对象，类）。 所有这些调用都由一个机制来完成。 这个机制很优雅，不难理解，所以值得了解。 但是让我们从头开始。
>
> 以下是原文:
>
> *[The Python version described in this article is 3.x, more specifically - the 3.3 alpha release of CPython.]*
>
> The concept of a *callable* is fundamental in Python. When thinking about what can be "called", the immediately obvious answer is functions. Whether it's user defined functions (written by you), or builtin functions (most probably implemented in C inside the CPython interpreter), functions were meant to be called, right?
>
> Well, there are also methods, but they're not very interesting because they're just special functions that are bound to objects. What else can be called? You may, or may not be familiar with the ability to call *objects*, as long as they belong to classes that define the `__call__` magic method. So objects can act as functions. And thinking about this a bit further, classes are callable too. After all, here's how we create new objects:
>
> ```
> class Joe:
>   ... [contents of class]
>
> joe = Joe()
>
> ```
>
> Here we "call" `Joe` to create a new instance. So classes can act as functions as well!
>
> It turns out that all these concepts are nicely united in the CPython implementation. Everything in Python is an object, and that includes every entity described in the previous paragraphs (user & builtin functions, methods, objects, classes). All these calls are served by a single mechanism. This mechanism is elegant and not that difficult to understand, so it's worth knowing about. But let's start at the beginning.
>
> ### Compiling calls
>
> CPython executes our program in two major steps:
>
> 1. The Python source code is compiled to bytecode.
> 2. A VM executes that bytecode, using a toolbox of built-in objects and modules to help it do its job.
>
> In this section I'll provide a quick overview of how the first step applies to making calls. I won't get too deep since these details are not the really interesting part I want to focus on in the article. If you want to learn more about the flow Python source undergoes in the compiler, read [this](http://eli.thegreenplace.net/2010/06/30/python-internals-adding-a-new-statement-to-python/).
>
> Briefly, the Python compiler identifies everything followed by `(arguments...)` inside an expression as a call [[1\]](https://eli.thegreenplace.net/2012/03/23/python-internals-how-callables-work/#id7). The AST node for this is `Call`. The compiler emits code for `Call` in the `compiler_call` function in `Python/compile.c`. In most cases, the `CALL_FUNCTION` bytecode instruction is going to be emitted. There are some variations I'm going to ignore for the purpose of the article. For example, if the call has "star args" - `func(a, b, *args)`, there's a special instruction for handling that - `CALL_FUNCTION_VAR`. It and other special instructions are just variations on the same theme.
>
> ### CALL_FUNCTION
>
> So `CALL_FUNCTION` is the instruction we're going to focus on here. This is [what it does](http://docs.python.org/dev/library/dis.html):
>
> > **CALL_FUNCTION(argc)**
> >
> > Calls a function. The low byte of *argc* indicates the number of positional parameters, the high byte the number of keyword parameters. On the stack, the opcode finds the keyword parameters first. For each keyword argument, the value is on top of the key. Below the keyword parameters, the positional parameters are on the stack, with the right-most parameter on top. Below the parameters, the function object to call is on the stack. Pops all function arguments, and the function itself off the stack, and pushes the return value.
>
> CPython bytecode is evaluated by the the mammoth function `PyEval_EvalFrameEx` in `Python/ceval.c`. The function is scary but it's nothing more than a fancy dispatcher of opcodes. It reads instructions from the code object of the given frame and executes them. Here, for example, is the handler for `CALL_FUNCTION` (cleaned up a bit to remove tracing and timing macros):
>
> ```
> TARGET(CALL_FUNCTION)
> {
>     PyObject **sp;
>     sp = stack_pointer;
>     x = call_function(&sp, oparg);
>     stack_pointer = sp;
>     PUSH(x);
>     if (x != NULL)
>         DISPATCH();
>     break;
> }
>
> ```
>
> Not too bad - it's actually very readable. `call_function` does the actual call (we'll examine it in a bit), `oparg` is the numeric argument of the instruction, and `stack_pointer` points to the top of the stack [[2\]](https://eli.thegreenplace.net/2012/03/23/python-internals-how-callables-work/#id8). The value returned by `call_function` is pushed back to the stack, and `DISPATCH` is just some macro magic to invoke the next instruction.
>
> `call_function` is also in `Python/ceval.c`. It implements the actual functionality of the instruction. At 80 lines it's not very long, but long enough so I won't paste it wholly here. Instead I'll explain the flow in general and paste small snippets where relevant; you're welcome to follow along with the code open in your favorite editor.
>
> ### Any call is just an object call
>
> The most important first step in understanding how calls work in Python is to ignore most of what `call_function` does. Yes, I mean it. The vast majority of the code in this function deals with optimizations for various common cases. It can be removed without hurting the correctness of the interpreter, only its performance. If we ignore all optimizations for the time being, all `call_function` does is decode the amount of arguments and amount of keyword arguments from the single argument of `CALL_FUNCTION` and forwards it to `do_call`. We'll get back to the optimizations later since they are interesting, but for the time being, let's see what the core flow is.
>
> `do_call` loads the arguments from the stack into `PyObject` objects (a tuple for the positional arguments, a dict for the keyword arguments), does a bit of tracing and optimization of its own, but eventually calls `PyObject_Call`.
>
> `PyObject_Call` is a super-important function. It's also available to extensions in the Python C API. Here it is, in all its glory:
>
> ```
> PyObject *
> PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw)
> {
>     ternaryfunc call;
>
>     if ((call = func->ob_type->tp_call) != NULL) {
>         PyObject *result;
>         if (Py_EnterRecursiveCall(" while calling a Python object"))
>             return NULL;
>         result = (*call)(func, arg, kw);
>         Py_LeaveRecursiveCall();
>         if (result == NULL && !PyErr_Occurred())
>             PyErr_SetString(
>                 PyExc_SystemError,
>                 "NULL result without error in PyObject_Call");
>         return result;
>     }
>     PyErr_Format(PyExc_TypeError, "'%.200s' object is not callable",
>                  func->ob_type->tp_name);
>     return NULL;
> }
>
> ```
>
> Deep recursion protection and error handling aside [[3\]](https://eli.thegreenplace.net/2012/03/23/python-internals-how-callables-work/#id9), `PyObject_Call` extracts the `tp_call` attribute [[4\]](https://eli.thegreenplace.net/2012/03/23/python-internals-how-callables-work/#id10) of the object's type and calls it. This is possible since `tp_call` holds a function pointer.
>
> Let it sink for a moment. *This is it*. Ignoring all kinds of wonderful optimizations, this is what *all calls in Python* boil down to:
>
> * Everything in Python is an object [[5\]](https://eli.thegreenplace.net/2012/03/23/python-internals-how-callables-work/#id11).
> * Every object has a type; the type of an object dictates the stuff that can be done to/with the object.
> * When an object is called, its type's `tp_call` attribute is called.
>
> As a user of Python, your only direct interaction with `tp_call` is when you want your objects to be callable. If you define your class in Python, you have to implement the `__call__` method for this purpose. This method gets directly mapped to `tp_call` by CPython. If you define your class as a C extension, you have to assign `tp_call` in the type object of your class manually.
>
> But recall that classes themselves are "called" to create new objects, so `tp_call` plays a role here as well. Even more fundamentally, when you define a class there is also a call involved - on the class's metaclass. This is an interesting topic and I'll cover it in a future article.