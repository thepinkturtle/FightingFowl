from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from StockerChecker.forms import DocumentForm
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
    cwd = os.getcwd()
    relative_path = os.path.join( os.getcwd(), 'media', 'documents', 'upload1test.json')
    print( relative_path )

    with open( relative_path ) as json_file:
        data = json.load( json_file )
        # for item_ordered in data[ 'item_ordered' ]:
        #     print("The item order was: " + item_ordered )
        #     print('')
    return render(request, 'model_form_upload.html')