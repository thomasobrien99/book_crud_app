from functools import wraps
def my_first_decorator(fn):
	@wraps(fn)
	def inner():
		print("Hello")
	  return fn()
	return inner

@my_first_decorator # say_bye = my_first_decorator(say_bye)
def say_bye():
  print("Say bye")

 