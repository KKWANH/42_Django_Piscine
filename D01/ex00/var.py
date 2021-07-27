def what_is_type(val):
	print("{0} has a type {1}".format(val, type(val)))

def my_var():
	what_is_type(42)
	what_is_type("42")
	what_is_type("quarante-deux")
	what_is_type(42.0)
	what_is_type([42])
	what_is_type({42 :42})
	what_is_type((42,))
	what_is_type(set())

if __name__ == '__main__':
	my_var()