#! /usr/bin/env python3

def	header_start(file, tabs, lang="en"):
	text = "<!DOCTYPE html>\n"
	text += tabs * "\t"
	tabs += 1
	text += "<html lang=" + lang + ">\n"
	try:
		file.write(text)
	except: pass

def header_close(file, tabs):
	text = "\t</html>"
	try:
		file.write(text)
	except: pass

def	generate_table():
	tabs = 0
	with open("my_periodic_table.html", "w") as file:
		header_start(file, tabs)
		with open("periodic_table.txt", "r") as txt:
			elements = txt.readlines()
		for atoms in elements:
			print(atoms)

		header_close(file, tabs)

if __name__=='__main__':
	generate_table()
