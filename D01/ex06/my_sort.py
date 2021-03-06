#   42 KKIM - DJANGO & PYThON PISCINE - HEADER
#		finish date: 7/27
#		passed date:
def	ft_sort_list_inv_dic(argu):
	rdic = dict()
	for name in argu:
		if rdic.get(argu.get(name)):
			rdic[argu[name]].append(name)
		else:
			rdic[argu[name]] = [name]
	return rdic

def	ft_sort_list():
	d = {
		'Hendrix' : '1942',
		'Allman' : '1946',
		'King' : '1925',
		'Clapton' : '1945',
		'Johnson' : '1911',
		'Berry' : '1926',
		'Vaughan' : '1954',
		'Cooder' : '1947',
		'Page' : '1944',
		'Richards' : '1943',
		'Hammett' : '1962',
		'Cobain' : '1967',
		'Garcia' : '1942',
		'Beck' : '1944',
		'Santana' : '1947',
		'Ramone' : '1948',
		'White' : '1975',
		'Frusciante': '1970',
		'Thompson' : '1949',
		'Burton' : '1939',
	}
	rdic = sorted(ft_sort_list_inv_dic(d).items())
	for indx in rdic:
		name = sorted(indx[1])
		for jndx in name:
			print(jndx)

if __name__ == '__main__' :
	ft_sort_list()