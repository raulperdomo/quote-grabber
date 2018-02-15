#!/usr/bin/python
from lxml import html 
import requests
import sys
for i in range(len(sys.argv)-1):
	page = requests.get('https://www.nasdaq.com/symbol/'+sys.argv[(i+1)].lower())
	tree = html.fromstring(page.content)

	#price = tree.xpath('//div[@id="qwidget_lastsale"]/text()').pop(0)
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
