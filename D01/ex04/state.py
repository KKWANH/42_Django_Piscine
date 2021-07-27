import sys

def	ft_capital(argu):
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	for	abbC, capC in capital_cities.items():
		if argu == capC:
			for	sttS, abbS in states.items():
				if abbS == abbC:
					print(sttS)
					return
	print("Unknown capital city!")

if __name__ == '__main__':
	if len(sys.argv) == 2:
		ft_capital(sys.argv[1])