import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint

link="https://www.flipkart.com/search?q=Mi%20all%20mobile%20phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"

def flipkart_data(url):	
	page=requests.get(url)
	data=page.text
	soup=BeautifulSoup(page.text,"html.parser")

	sec_div=soup.find_all('div',class_="_1UoZlX")
	# print(sec_div)
	big_dict = []
	for i in sec_div:
		redmi=i.find('div',class_="_1-2Iqu row")
		# pprint(redmi)
		name=redmi.find('div',class_="_3wU53n").get_text()
		# print(name)
		price=i.find('div',class_="_1uv9Cb").get_text()
		# print(price)
		# rating=i.find('div',class_="hGSR34")
		# if rating!=None:
		# 	print(rating)
			# Dict["rating"]=rating.get_text()
		ram=i.find('li',class_="tVe95H").get_text()
	 	# print(ram)
		info=i.find_all('li',class_="tVe95H")
		# print(info)
		# break
		info_list = []
		Dict = {}
		for j in info:
			# a = j.getText().split("\n")
			a=j.get_text()
			info_list.append(a)
			# pprint(other_details)
		Dict["price"]=price
		Dict["name"]=name
		Dict["ram"] = info_list[0]
		Dict["display"] = info_list[1]
		Dict["camera"] = info_list[2]
		Dict["battery"] = info_list[3]
		Dict["processor"] = info_list[4]
		if len(info_list)==6:
			Dict["brand_warranty"]=info_list[5]
		# Dict = {"name":name,"price":price,"rating":rating,"ram":ram,"display":display,"camera":camera,"battery":battery,"processor":processor,"brand_warranty":brand_warranty}
		# pprint(Dict)
		big_dict.append(Dict)
		
	# pprint(big_dict)
	return(big_dict)
	# with open("flipkart.json","w")as json_file:
	# 	json.dump(big_dict,json_file)

# pprint(flipkart_data(link))


def flipkart_data_2():
	url="https://www.flipkart.com/search?q=Mi%20all%20mobile%20phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"
	page=requests.get(url)
	data=page.text
	soup=BeautifulSoup(page.text,"html.parser")

	div=soup.find('nav',class_="_1ypTlJ")
	link=div.find_all('a')
	# print(link)
	Dict={}
	add=1
	for x in link[:len(link) - 1]:
		a=(x["href"])
		all_link=("https://www.flipkart.com"+a)
		b=flipkart_data(all_link)

		# print(b)
		Dict[add]=b
		add+=1
	pprint(Dict)
	# with open("flipkart_1.json","w")as json_file:
	# 	json.dump(Dict,json_file)

flipkart_data_2()





