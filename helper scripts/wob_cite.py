from sys import argv
import requests
from bs4 import BeautifulSoup
template=["@misc{",
", title=\"{"," \\","}\", howpublished={Coppermind, \\url{",
"}}, note={Word of Brandon}, author={Sanderson, Brandon}, year={",
"}, month={",
"}}"]
def merge(a,b):
	ret=[a[0]]
	for i in range(len(b)):
		ret.append(b[i])
		ret.append(a[i+1])
	return ret
def extract(citekey,url):
	id=url[url.rfind("#e")+2:]
	#print(id)
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	test=soup.select('.eventDetails tr:not(.w3-hide-large)')
	data={}
	for l in test:
		key=l.select('th')
		value=l.select('td')
		if len(key)>0 and len(value)>0:
			data[key[0].text.strip()]=value[0].text.strip()
	#print (data)
	month=data["Date"].split()
	month=month[0].strip().replace('.','')
	id=soup.select("[data-entry-id=\""+id+"\"]")[0]
	id=id.select("a:not(.optionelement)>span")[0].text.strip()

	year=data["Date"]
	year=year[year.find(",")+1:].strip()
	ret=[citekey,data["Name"].replace("&","\\&").replace("#","\\#"),id,url,year,month]
	
	return "".join(merge(template,ret))
output=open("output.txt",'w')
#print(extract("blah","https://wob.coppermind.net/events/105-17th-shard-forum-qa/#e1090"))
def extractAll(list):
	for line in list:
		
		try:
			temp=line.split()
			#print((temp[0][1:-1],temp[1]))
			ret=extract(temp[0][1:-1],temp[1].lower())
			output.write(ret+"\n")
			output.flush()
			print(ret)
		except:
			print("Error on "+line)
extractAll(open(argv[1]))
output.close()