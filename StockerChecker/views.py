from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from StockerChecker.forms import DocumentForm
from pprint import pprint
from itertools import izip
import json
import os


# Create your views here.

def index(request):
    now = datetime.now()
    return render(
                  request,
                  "index.html",
                  {
                      'title': "Hello Stocker Checker",
                      'message': "Hello good sir!",
                      'content': " on " + now.strftime("%A, %d %B, %Y at %X")
                  }
            )

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'model_form_upload.html')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

def process_diff(request):
    skis_ = "Skis"
    shovels_ = "Shovels"
    sleds_ = "Sleds"
    snowblowers_ = "Snowblowers"
    winter_tires_ = "Winter tires"
    year = ""
    month = ""
    day_time = ""
    day = ""
    time = ""
    date = ""

    cwd = os.getcwd()
    relative_path = os.path.join( os.getcwd(), 'media', 'documents', 'upload1test.json')
    print( relative_path )

    with open( relative_path ) as json_file:
        data = json.load( json_file )
    for i in data:
        date = i['order_date'].split('-', 3 )
        year = date[0]
        month = date[1]
        day_time = date[2].split('T', 2)
        day = day_time[0]
        time = day_time[1]
        
        print ('item_ordered: ' + i['item_ordered'] + ': ' + i['item_quantity'] + ' Year: '  +  year + " Month: " + month + " Day: " + day + " time: " + time  )
        
   
            
    return render(request, 'model_form_upload.html')