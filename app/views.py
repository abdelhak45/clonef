from django.shortcuts import render 
from django.http import JsonResponse
from .forms import *
import requests
from tabulate import tabulate
# Create your views here.

def clone(request):
    if request.method=='POST':
       form=UploadFileForm(request.POST,request.FILES)
       
       if form.is_valid():
           url=request.POST['url']
           thetxtfile=request.FILES['file']
        #    check=thetxtfile.split('.')[-1] == 'txt'
        #    print(check)
           
           p=cloneferox(url,txt_file=thetxtfile)
           
    else:
      form=UploadFileForm()
      p=''
    context={
        'form':form,
        'p':p
        }
           


    return render(request,'index.html',context)
def cloneferox(url, txt_file):
    list_of_dict = []
    
    for line in txt_file.readlines():
        line = line.decode('utf-8')  # Decode bytes to string if needed
        r = requests.get(f'{url}{line}')
        status = r.status_code
        requrl = f'{url}{line}'
        words = line.strip()
        
        dicto = {
            'status': status,
            'urls': requrl,
            'words_tried': words
        }
        list_of_dict.append(dicto)
    
    return list_of_dict
