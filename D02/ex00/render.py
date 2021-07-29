import sys
import os

class	FileReader:
	def	__init__(self, name):
		self.name = name
	def ft_FileReader_readfile(self):
		pass

class	Render(FileReader):
	def	__init__(self, name, sett):
		super().__init__(name)
		self.sett = Settings(sett)
	def	ft_Render_process_line(self, line):
		html = line
		for indx in self.sett.parm:
			html = html.replace("{" + indx + "}", self.sett.parm[indx])
		return html
	def ft_Render_write_html(self, name):
		f
	

# class	Settings(FileReader)


def		ft_render(name):
		file, flex = os.path.splitext(name)
		if flex == ".template":
			tmp = Render(name, "setting.py")
			tmp.write_html(file+".html")

if		__name__ == '__main__' :
		if len(sys.argv) == 2:
			ft_render(sys.argv[1])