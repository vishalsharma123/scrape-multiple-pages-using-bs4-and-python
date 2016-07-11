import requests
from bs4 import BeautifulSoup
from itertools import izip
from itertools import izip_longest
from itertools import chain
import urllib2
import codecs
import cStringIO
import requests
import re
import csv

myfile = open("myfile.csv",'wb')
spamwriter = csv.writer(open("myfile.csv",'wb'))
fieldnames = ['g_data','g_data1','g_data2']
writer = csv.DictWriter(myfile, fieldnames=fieldnames)
spamwriter = csv.writer(myfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)



count = 0
for index in range(1,12):
    url = "http://www.urllink.php?page=" + str(index) + "&limit=20"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    soup.find_all("a")
    for link in soup.find_all("a"):
        print link.get("href")
     g_data = soup.body.findAll("div" ,{"class":"search-result-text"})[0].text #parent class
     g_data1 = soup.body.findAll("div", {"class": "col-xs-8"})[1].text #child class
     g_data2 = soup.body.findAll("div", {"class": "col-xs-4"})[1].text
     g_data3 = soup.body.findAll("div", {"class": "col-xs-8"})[2].text
     
      
     try:
          writer.writeheader()
          list0 = g_data
          list1 = g_data1
          list2 = g_data2
          list = list0,list1,list2

            spamwriter.writerow([g_data1,g_data2,g_data3])
            print g_data1,g_data2,g_data3
     except IndexError:
            spamwriter.writerow([g_data1,g_data2,g_data3])
            print g_data1,g_data2,g_data3
            i+=1
     break
myfile.close()

        

