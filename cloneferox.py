import requests
from tabulate import tabulate
import time
url='https://rabop-backend.onrender.com/'
list_of_dict=[]
with open('tryword.txt') as f:
   for line in f:
       time.sleep(4)
       r=requests.get(f'{url}{line}')
       status=r.status_code
       requrl=f'{url}{line}'
       words=line.strip()
       dicto={
           'status':status,
           'urls':requrl,
           'words-tried':words
       }
       list_of_dict.append(dicto)
print(tabulate(list_of_dict,headers='keys'))

       
