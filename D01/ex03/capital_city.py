#   42 KKIM - DJANGO & PYThON PISCINE - HEADER
#		finish date: 7/27
#		passed date:
import sys

def	ft_capital_city(arg):
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
	if not states.get(arg):
		print("Unknown state")
		return
	if capital_cities.get(states.get(arg)):
		print(capital_cities.get(states.get(arg)))
	else:
		print("Error : no capital for this state!")

if __name__ == '__main__':
	if len(sys.argv) == 2:
		ft_capital_city(sys.argv[1])