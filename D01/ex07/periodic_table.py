#   42 KKIM - DJANGO & PYThON PISCINE - HEADER
#		finish date: 7/27
#		passed date:
def	ft_periodic_table_init_str_to_dict(lin):
	dic = dict()
	sp1 = lin.split("=")
	dic['name'] = sp1[0].strip(" ")
	sp2 = sp1[1].split(",")
	for dat in sp2:
		sp3 = dat.split(":")
		dic[sp3[0].strip(" ")] = sp3[1].strip(" \n")
	return dic

def	ft_periodic_table_init(nam):
	with open(nam) as fil:
		tab = []
		for lin in fil:
			dic = ft_periodic_table_init_str_to_dict(lin)
			tab.append(dic)
		return tab



def	ft_periodic_table_write_header(fil):
	fil.write("<!DOCTYPE html>\n")
	fil.write("<html lang='en'>\n")
	fil.write("\t<head>\n")
	fil.write("\t\t<title>Periodic table</title>\n")
	fil.write("\t\t<style>\n")
	fil.write("\t\t\tbody\t{ background-color: #424242; font-size: 20px; color: white; }\n")
	fil.write("\t\t\ttable\t{ background-color: black; margin: 50px; border-collapse: collapse; }\n")
	fil.write("\t\t\ttd\t\t{ border: 1px solid white; padding: 10px; }\n")
	fil.write("\t\t\th4\t\t{ font-weight: bold; font-size: 25px; text-align: center; }\n")
	fil.write("\t\t</style>\n")
	fil.write("\t</head>\n")

def	ft_periodic_table_write_body(fil, tab):
	fil.write("\t<body>\n")
	pre = 0
	cur = 0
	rst = "\t\t<table>\n"
	for lin in tab:
		cur = int(lin['position'])
		if cur == 0:
			rst +="\t\t\t<tr>\n"
		if cur - pre > 1:
			rst += "\t\t\t\t<td colspan='" + str(cur - pre - 1) + "'></td>\n"
		rst += "\t\t\t\t<td>\t<h4>" + lin['name'] + "</h4>"
		if len(lin['name']) > 10:
			rst += "\t<hr>\t"
		elif len(lin['name']) > 6:
			rst += "\t\t<hr>\t"
		else:
			rst += "\t\t\t<hr>\t"
		rst += "<ul><li>" + lin['number'] +"</li><li>" + lin['small'] +"</li><li>" + lin['molar'] + "</li></ul></td>\n"
		if cur == 17:
			rst += "\t\t\t</tr>\n"
			cur = 0
		pre = cur
	rst += "\t\t</table>\n"	
	fil.write(rst)
	fil.write("\t</body>\n")

def	ft_periodic_table_write_footer(fil):
	fil.write("</html>\n")

def	ft_periodic_table_write(tab, nam):
	with open(nam, "w") as fil:
		ft_periodic_table_write_header(fil)
		ft_periodic_table_write_body(fil, tab)
		ft_periodic_table_write_footer(fil)



def	ft_periodic_table():
	tab = ft_periodic_table_init("periodic_table.txt")
	ft_periodic_table_write(tab, "periodic_table.html")



if __name__ == '__main__' :
	ft_periodic_table()