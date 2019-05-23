from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from StockerChecker.forms import DocumentForm
from pprint import pprint
import json
import os
import array


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
    skis =        [ list() for x in range( 12 ) ]
    shovels =     [ list() for x in range( 12 ) ]
    sleds =       [ list() for x in range( 12 ) ]
    snowblowers = [ list() for x in range( 12 ) ]
    tires =       [ list() for x in range( 12 ) ]
    
    skis_restock =        [ list() for x in range( 12 ) ]
    shovels_restock =     [ list() for x in range( 12 ) ]
    sleds_restock =       [ list() for x in range( 12 ) ]
    snowblowers_restock = [ list() for x in range( 12 ) ]
    tires_restock =       [ list() for x in range( 12 ) ]

    cwd = os.getcwd()
    relative_path = os.path.join( os.getcwd(), 'media', 'documents', 'upload1test.json')
    relative_path_restock = os.path.join( os.getcwd(), 'media', 'documents', 'upload2test.json')

    with open( relative_path ) as json_file:
        data = json.load( json_file )

    with open( relative_path_restock ) as json_file_restock:
        data_restock = json.load( json_file_restock )

    for i in data:
        date = i['order_date'].split('-', 3 )
        year = date[0]
        month = date[1]
        day_time = date[2].split('T', 1)
        day = day_time[0]

        if( i['item_ordered'] == 'skis'):
            item = ( day, int(i['item_quantity']) )
            skis[ int( month ) - 1 ].append( item  )
        
        if( i['item_ordered'] == 'shovel'):
            item = ( day, int(i['item_quantity']) )
            shovels[ int( month ) - 1 ].append( item  )

        if( i['item_ordered'] == 'sled'):
            item  = ( day, int(i['item_quantity']) )
            sleds[ int( month ) - 1 ].append( item  )
        
        if( i['item_ordered'] == 'snowblower'):
            item  = ( day, int(i['item_quantity']) )
            snowblowers[ int( month ) - 1 ].append( item  )
        
        if( i['item_ordered'] == 'tires'):
            item  = ( day, int(i['item_quantity']) )
            tires[ int( month ) - 1 ].append( item  )


    for i in data_restock:
        date = i['restock_date'].split('-', 3 )
        month = date[1]
        
        if( i['item_stocked'] == 'shovel' ):
            item = ( 'shovel', int( month ), int( i['item_quantity'] ) )
            shovels_restock[ int( month ) - 1 ].append( item )
    
    for m in shovels_restock:
        print( 'month: ' + str(m) )
    #print( '\n')
    #for m in shovels:
    #    print( 'month: ' + str(m) )
    #print( '\n')
    #for m in sleds:
    #    print( 'month: ' + str(m) )
    #print( '\n')
    #for m in snowblowers:
    #    print( 'month: ' + str(m) )
    #print( '\n')    
    #for m in tires:
    #    print( 'month: ' + str(m) )

    return render(request, 'model_form_upload.html')
