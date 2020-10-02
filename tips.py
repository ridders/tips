from xml.dom import minidom
import re

xmldoc = minidom.parse('data.xml')
itemlist = xmldoc.getElementsByTagName('property') 

for s in itemlist :
    if s.attributes['type'].value == 'text_body':
    	string = (s.firstChild.nodeValue)
    	regex = (re.findall(r'\d.*',string))
    	if regex:
    		print(regex[0])