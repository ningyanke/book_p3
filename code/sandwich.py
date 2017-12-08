#!/usr/bin/evn python
# coding = utf-8



def top_sandwich(func):
	def wrapper():
		print(r'</--------\>')
		func()
	return wrapper

def bottom_sandwich(func):
	def wrapper():
		func()
		print(r'<\________/>')
	return wrapper


@bottom_sandwich
@top_sandwich
def sandwich():
	print("-- beaf --")
	print('--potato--')


sandwich()