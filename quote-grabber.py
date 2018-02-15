#!/usr/bin/python
#I found that all the python applications to pull stock market data from google
#and YAHOO! were broken and there was no working replacement.

#This script will take any arguments and pull the latest stock data for that symbol from nasdaq.com
#it will not output anything if the symbol doesn't return anything. 

#if there is any interest, I will reconfigure the application to return a python dictionary.


from lxml import html 
import requests
import sys
for i in range(len(sys.argv)-1):
	page = requests.get('https://www.nasdaq.com/symbol/'+sys.argv[(i+1)].lower())
	tree = html.fromstring(page.content)

	curr = tree.xpath('//div[@id="qwidget_lastsale"]/text()')
	net = tree.xpath('//div[@id="qwidget_netchange"]/text()')
	pct = tree.xpath('//div[@id="qwidget_percent"]/text()')
	comp = tree.xpath('//div[@id="qwidget_pageheader"]/h1/text()')
	if curr:
		company = comp.pop(0)
		companyShort = company[:-34]
		price = curr.pop(0)
		netchange = net.pop(0)
		pctchange = pct.pop(0)
		print(companyShort + "\nPrice: " + price + "\nNet Change: " + netchange + "\nPercent Change: "+pctchange+"\n\n")
