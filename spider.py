#!/usr/bin/python2

import requests, sys
import re

selection = sys.argv[1]
#page = requests.get(selection)
#page_to_parse = page.text

#print(page_to_parse)

def find_links(target):
    global selection
    page = requests.get(target)
    page_text = page.text
    links = re.findall("<a href=\"(\S+)\">",page_text)
    
    for element in links:
        print(requests.get(selection + "/" + element).text)
    return links


#for element in links:
    #captured_links.append(element)
    #print(element)

#find_links(selection)

def spider(website):
    global selection
    found_links = find_links(website)
    for element in found_links:
        #print(selection + element)
        find_links(selection + "/" + element)



spider(selection)
    

