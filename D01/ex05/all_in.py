#   42 KKIM - DJANGO & PYThON PISCINE - HEADER
#		finish date: 7/27
#		passed date:
import sys

def	ft_all_in_find_state(sval, states, capital_cities):
	for	abbC, capC in capital_cities.items():
		if sval.lower() == capC.lower():
			for	sttS, abbS in states.items():
				if abbS.lower() == abbC.lower():
					return [capC, sttS]
	return None

def	ft_all_in_find_capital(sval, states, capital_cities):
	for	skey in states:
		if skey.lower() == sval.lower():
			if capital_cities.get(states.get(skey)):
				return [capital_cities.get(states.get(skey)), skey]
	return None

def	ft_all_in_main(arrs, states, capital_cities):
	for	valu in arrs:
		sval = valu.strip(" ")
		if sval:
			rstt = ft_all_in_find_state(sval, states, capital_cities)
			rcap = ft_all_in_find_capital(sval, states, capital_cities)
			if rstt:
				print("{0} is the capital of {1}".format(rstt[0], rstt[1]))
			elif rcap:
				print("{0} is the capital city of {1}".format(rcap[0], rcap[1]))
			else:
				print("{0} is neither a capital city nor a state".format(sval))

def	ft_all_in(argu):
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
	if ",," in argu:
		return
	arrs = argu.split(",")
	ft_all_in_main(arrs, states, capital_cities)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		ft_all_in(sys.argv[1])