def	ft_var_to_dict():
	d = [
		('Hendrix' , '1942'),
		('Allman' , '1946'),
		('King' , '1925'),
		('Clapton' , '1945'),
		('Johnson' , '1911'),
		('Berry' , '1926'),
		('Vaughan' , '1954'),
		('Cooder' , '1947'),
		('Page' , '1944'),
		('Richards' , '1943'),
		('Hammett' , '1962'),
		('Cobain' , '1967'),
		('Garcia' , '1942'),
		('Beck' , '1944'),
		('Santana' , '1947'),
		('Ramone' , '1948'),
		('White' , '1975'),
		('Frusciante', '1970'),
		('Thompson' , '1949'),
		('Burton' , '1939')
	]
	v_dic = dict()
	for	v_pair in d:
		if v_dic.get(v_pair[1]):
			v_dic[v_pair[1]].append(v_pair[0])
		else:
			v_dic[v_pair[1]] = [v_pair[0]]
	for	v_num in v_dic:
		for v_nam in v_dic[v_num]:
			print("{0} : {1}".format(v_num, v_nam))

if __name__ == '__main__':
	ft_var_to_dict()