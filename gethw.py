import json
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

html_fn = ['description','temp','feels','precip','humidity','wind']

req = Request('https://weather.com/weather/hourbyhour/l/ISXX0026:1:IS', headers={'User-Agent': 'Mozilla/5.0'})
taw_html = urlopen(req).read()

taw_soup = BeautifulSoup(taw_html, 'html.parser')

taw_wdat = taw_soup.find('table',{'class': 'twc-table'})

times = taw_wdat.find_all('span',{'class': 'dsx-date'})

fields = [taw_wdat.find_all('td',{'headers': f}) for f in html_fn]

jdict = {}

for zdat in zip(times, *fields):
	jdict[zdat[0].text] = {
		'DESC' : zdat[1].text,
		'TEMP' : zdat[2].text[0:-1],
		'FEEL' : zdat[3].text[0:-1],
		'PRECIP' : zdat[4].text,
		'HUMIDITY': zdat[5].text,
		'WIND' : zdat[6].text  
		}

print(json.dumps(jdict))
