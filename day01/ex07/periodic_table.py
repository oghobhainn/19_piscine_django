#! /usr/bin/env python3

def cell(atom):
    name  = atom[0][:atom[0].find('=')-1].strip()
    number= atom[1].replace("number:", "No ")
    small = atom[2].replace("small:","")
    molar = atom[3][atom[3].find(':')+1:]
    cell = "<h4>" + name + "</h4>\n<ul>\n<li>" + number + "</li>\n<li>" + small + "</li>\n<li>" + molar + "</li>\n</ul>\n"  
    
    return (cell)

def	generate_table():
	with open("periodic_table.txt", "r") as data:
		data = data.readlines()

		table = [0] * 7
		for i in range(7):
			table[i] = [0] * 18

		row = 0
		for element in data:
			content = element.split(',')
			position = content[0].find(':') + 1
			column = int(content[0][position:])
			table[row][column] = content
			if column == 17:
				row = row + 1
		html = """<!DOCTYPE html>\n<html lang='en'>\n<head>\n<meta charset="utf-8"/><title>Mendeleiev's Table</title>\n</head>\n<body>\n<table>"""

		for i in range(len(table)):
		    html = html + "<tr> "
		    for j in range(len(table[0])):
		        if table[i][j] == 0:
		            html = html + """<td style="border: 1px solid red;"></td>\n"""
		        else:
		            element = cell(table[i][j])
		            html = html + """<td style="border: 1px solid blue;">\n""" + element + "</td>\n"

		html = html + "</table>\n</html>"
		with open("periodic_table.html", "w") as periodic_html:
			periodic_html.write(html)

if __name__=='__main__':
	generate_table()
