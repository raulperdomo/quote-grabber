#!/usr/bin/python
from lxml import html 
import requests
import re
import datetime

def generalInfo(ticker):        
        tree = pullData(ticker)
        table = tree.xpath('//div[@id="left-column-div"]/div[1]/div/div/div/div/text()')
        values = []
        data = {}
        for i in table[2::3]:
            values.append(re.findall(r'[\d.,]+', i))
        if values[0]:
            data['bid'] = float(values[0].pop(0).replace(',',''))
            data['ask'] = float(values[0].pop(0).replace(',',''))
        if values[1]:
            data['oneYrTgt'] = float(values[1].pop(0).replace(',',''))
        if values[2]:
            data['high'] = float(values[2].pop(0).replace(',',''))
            data['low'] = float(values[2].pop(0).replace(',',''))
        if values[3]:
            data['volume'] = int(values[3].pop(0).replace(',',''))
        if values[4]:
            data['fiftyDay'] = int(values[4].pop(0).replace(',',''))
        if values[5]:
            data['prevClose'] = float(values[5].pop(0).replace(',',''))
        if values[6]:
            data['yrHigh'] = float(values[6].pop(0).replace(',',''))
            data['yrLow'] = float(values[6].pop(0).replace(',',''))
        if values[7]:
            data['marketCap'] = int(values[7].pop(0).replace(',',''))
        if values[8]:
            data['PEratio'] = float(values[8].pop(0).replace(',',''))
        if values[9]:
            data['forwardPE'] = float(values[9].pop(0).replace(',',''))
        if values[10]:
            data['EPS'] = float(values[10].pop(0).replace(',',''))
        if values[11]:
            data['dividendAnnual'] = float(values[11].pop(0).replace(',',''))
        if values[12]:
            data['ExDivDate'] = datetime.date(int(values[12].pop(2)),int(values[12].pop(0)),int(values[12].pop(0)))
        if values[13]:
            data['DivPayDate'] = datetime.date(int(values[13].pop(2)),int(values[13].pop(0)),int(values[13].pop(0)))
        if values[14]:
            data['currentYield'] = float(values[14].pop(0))
        if values[15]:
            data['beta'] = float(values[15].pop(0).replace(',',''))
        return data

def pullData(ticker):

    page = requests.get('https://www.nasdaq.com/symbol/'+ticker.lower())
    tree = html.fromstring(page.content)
    return tree

def getPrice(ticker):
    tree = pullData(ticker)
    curr = tree.xpath('//div[@id="qwidget_lastsale"]/text()')[0].replace('$','').replace(',','')
    return float(curr)

def getChange(ticker):
    tree = pullData(ticker)
    values = {}
    values['currentPrice'] = float(tree.xpath('//div[@id="qwidget_lastsale"]/text()')[0].replace('$','').replace(',',''))
    values['netChange'] = float(tree.xpath('//div[@id="qwidget_netchange"]/text()')[0])
    values['pctChange'] = float(tree.xpath('//div[@id="qwidget_percent"]/text()')[0].replace('%',''))
    return values

def getEquityName(ticker):
    tree = pullData(ticker)
    equity = tree.xpath('//div[@id="qwidget_pageheader"]/h1/text()')[0]
    equityShort = equity[:-20]
    return equityShort

def getAll(ticker):
    data = {}
    data[ticker] = getEquityName(ticker)
    change = getChange(ticker)
    for i in change:
        data[i] = change[i]
    gen = generalInfo(ticker)
    for i in gen:
        data[i] = gen[i]
    return data

