from urllib.request import urlopen
from bs4 import BeautifulSoup 
import requests
import operator
st="http://www.burjeel.com/abu-dhabi/dr/"
page = requests.get("http://www.burjeel.com/abu-dhabi/doctors/")
dr1=[]
soup = BeautifulSoup(page.content, 'html.parser')
list1=((soup.find_all('h4')))
dr2=[name1.get_text() for name1 in list1 ]
dr1 = [name for name in dr2 if name.startswith("Dr.")]
for jj in range(0,len(dr1)):
    dr1[jj]=dr1[jj].lower()
    dr1[jj]=dr1[jj].replace(" ","-")
    dr1[jj]=dr1[jj].replace(".","")
    dr1[jj]=dr1[jj][:-1]
    link = st+dr1[jj]+"/"
    page1 = requests.get(link)
    dr11=[]
    soup = BeautifulSoup(page1.content, 'html.parser')
    list11=((soup.find_all('h3')))
    dr11 = [name12.get_text() for name12 in list11 ]
    dr21=[name11 for name11 in dr11 if operator.contains(name11,"Specialist") or operator.contains(name11,"Consultant")or operator.contains(name11,"General")or operator.contains(name11,"Chief")]
    print (dr1[jj],end=" -> ")
    print(dr21)
    