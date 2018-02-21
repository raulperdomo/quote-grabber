#!/usr/bin/python
#I found that all the python applications to pull stock market data from google
#and YAHOO! were broken and there was no working replacement.

#This script will take any arguments and pull the latest stock data for that symbol from nasdaq.com
#it will not output anything if the symbol doesn't return anything. 

#if there is any interest, I will reconfigure the application to return a python dictionary.


from lxml import html 
import requests
import re
import sys
import datetime
for i in range(len(sys.argv)-1):
    page = requests.get('https://www.nasdaq.com/symbol/'+sys.argv[(i+1)].lower())
    tree = html.fromstring(page.content)

    curr = tree.xpath('//div[@id="qwidget_lastsale"]/text()')
    net = tree.xpath('//div[@id="qwidget_netchange"]/text()')
    pct = tree.xpath('//div[@id="qwidget_percent"]/text()')
    comp = tree.xpath('//div[@id="qwidget_pageheader"]/h1/text()')
    if curr:
        company = comp.pop(0)
        companyShort = company[:-20]
        price = curr.pop(0)
        netchange = net.pop(0)
        pctchange = pct.pop(0)
        print("%s\nPrice: %s\nNet Change: %s\nPct Change: %s\n" % (companyShort, price, netchange, pctchange))
		
        data = tree.xpath('//div[@id="left-column-div"]/div[1]/div/div/div/div/text()')
        values = []
        for i in data[2::3]:
            values.append(re.findall(r'[\d.,]+', i))
        
        print("\nBid / Ask: \n")
        bid = float(values[0].pop(0).replace(',',''))
        ask = float(values[0].pop(0).replace(',',''))
        print(bid,ask)
 
        print("\n1 Year Target: \n")
        oneYrTgt = float(values[1].pop(0))
        print(oneYrTgt)

        print("\nToday's High / Low: \n")
        high = float(values[2].pop(0).replace(',',''))
        low = float(values[2].pop(0).replace(',',''))
        print(high,low)

        print("\nShare Volume: \n")
        vol = int(values[3].pop(0).replace(',',''))
        print(vol)

        print("\n50 Day Average Daily Volume: \n")
        fiftyDay = int(values[4].pop(0).replace(',',''))
        print(fiftyDay)
        
        print("\nPrevious Close: \n")
        prevClose = float(values[5].pop(0).replace(',',''))
        print(prevClose)

        print("\n52 Week High / Low: \n")
        yrHigh = float(values[6].pop(0).replace(',',''))
        yrLow = float(values[6].pop(0).replace(',',''))
        print(yrHigh,yrLow)
       
        print('\nMarket Cap: \n')
        cap = int(values[7].pop(0).replace(',',''))
        print(cap)

        print("\nP/E Ratio: \n")
        PEratio = float(values[8].pop(0).replace(',',''))
        print(PEratio)
        print("\nForward P/E (1yr): \n")
        forwardPE = float(values[9].pop(0).replace(',',''))
        print(forwardPE)
        print("\nEarnings Per Share (EPS): \n")
        EPS = float(values[10].pop(0).replace(',',''))
        print(EPS)
        print("\nAnnualized Dividend: \n")
        dividendAnnual = float(values[11].pop(0).replace(',',''))
        print(dividendAnnual)  

        print("\nEx Dividend Date: \n")
        ExDivDate = datetime.date(int(values[12].pop(2)),int(values[12].pop(0)),int(values[12].pop(0)))
        print(ExDivDate)

        print("\nDividend Payment Date: \n")
        DivPayDate = datetime.date(int(values[13].pop(2)),int(values[13].pop(0)),int(values[13].pop(0)))
        print(DivPayDate)
        print("\nCurrent Yield: \n")
        currentYield = float(values[14].pop(0))
        print(currentYield)
        print("\nBeta: \n")
        beta = float(values[15].pop(0).replace(',',''))
        print(beta)
