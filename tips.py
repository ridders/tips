from xml.dom import minidom
import re
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    filepath = askopenfilename(
        filetypes=[("XML Files", "*.xml")]
    )
    if not filepath:
        return

    with open(filepath, "r") as input_file:
    	window.title(f"Simple Text Editor - {filepath}")
    	global path
    	path = filepath


def search():

	outtext = txt_edit.get('1.0', 'end')

	regex = []

	regex.append(outtext.rstrip())

	xmldoc = minidom.parse(path)
	itemlist = xmldoc.getElementsByTagName('property') 

	for s in itemlist :
	    if s.attributes['type'].value == 'text_body':
	    	string = (s.firstChild.nodeValue)
	    	combined = "(" + ")|(".join(regex) + ")"
	    	if re.findall(combined, string):
	    		print(string)


window = tk.Tk()
window.title("Text In Plain Sight:")
window.rowconfigure(0, minsize=200, weight=1)
window.columnconfigure(1, minsize=200, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_search = tk.Button(fr_buttons, text="Search", command=search)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_search.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()





