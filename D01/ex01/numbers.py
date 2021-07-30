#   42 KKIM - DJANGO & PYThON PISCINE - HEADER
#		finish date: 7/27
#		passed date:
def	ft_numbers(fil):
	with open(fil) as f:
		for l in f:
			l = l.split(",")
			for s in l:
				print(s.strip('\n'))

if __name__ == '__main__':
	ft_numbers("./numbers.txt")