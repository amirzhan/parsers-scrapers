import urllib.request
import os
import requests                 
from urllib.parse import urljoin
from urllib.parse import urlparse
from bs4 import BeautifulSoup

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }

with open("output.txt","r",encoding="utf-8") as infile:
	st = infile.read()
arr = st.split()
used = {}


for ch in arr:
	base_url = "http://name.kazakh.ru/?letter=%c" % ch

	used.clear()
	
#	r = requests.get(base_url, headers = headers)
#	with open('test.html', 'w',encoding="utf-8") as output_file:
 # 		output_file.write(r.text)
#	base_content = r.text

	q = []
	qh=0
	qt=0
	q.append(base_url)
	qt+=1
	used['PAGEN_1=1']=1
	while qh<qt:
		url = q[qh]
		print(url)
		qh+=1
		r = requests.get(url,headers=headers)
		content = r.text
		
		for link in BeautifulSoup(content,"lxml").find_all("td",class_="first-cell rate-number"):
			name = link.a.contents[0]
		#	print(name)
			with open("names.txt", "a",encoding="utf-8") as outfile:
				outfile.write(name+',\n')
		
		for link in BeautifulSoup(content,"lxml").find_all("div", class_="next-prev"):
				
	#		print(link.contents[5])
			try: 
				href = urljoin(base_url,link.contents[5]["href"])
				print("wanna go to " + href)
			except KeyError:
				print('oops')
				continue
			par = urlparse(href)
			params = par.query.split('&')
			if len(params)<2: continue		


			if used.get(params[1])!=None:
				continue
			used[params[1]]=1
			q.append(href)
			qt+=1
