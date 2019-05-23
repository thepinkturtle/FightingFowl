from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from StockerChecker.forms import DocumentForm
from django.http import HttpResponseRedirect
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
            return HttpResponseRedirect( request.path_info )
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

def calculate_success( orders_list, restock_list ):
    month = 0
    quantity_left = 0
    results = ''

    for orders in orders_list:

        order_number = 0
        quantity_left = int(restock_list[month][0][2])
        for tuple_ in orders:
            quantity_left = quantity_left - int(tuple_[1])
            if( quantity_left > -1 ):
                results = 'success ' + 'quantity left: ' + str(quantity_left)
            else:
                results = 'month: ' + str( month ) + ' day: ' + str(tuple_[1]) + " quantity left: " + str(quantity_left) + ' fail'
                break
            order_number = order_number + 1

        restock_list[month].append( results )
        month = month + 1

def parse_json(request):
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
    relative_path = os.path.join( os.getcwd(), 'media', 'documents', 'orders.json')
    relative_path_restock = os.path.join( os.getcwd(), 'media', 'documents', 'restocks.json')

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
        
        if( i['item_stocked'] == 'skis' ):
            item = ( 'skis', int( month ), int( i['item_quantity'] ) )
            skis_restock[ int( month ) - 1 ].append( item )
    
        if( i['item_stocked'] == 'shovel' ):
            item = ( 'shovel', int( month ), int( i['item_quantity'] ) )
            shovels_restock[ int( month ) - 1 ].append( item )
    
        if( i['item_stocked'] == 'sled' ):
            item = ( 'sled', int( month ), int( i['item_quantity'] ) )
            sleds_restock[ int( month ) - 1 ].append( item )
    
        if( i['item_stocked'] == 'snowblower' ):
            item = ( 'snowblower', int( month ), int( i['item_quantity'] ) )
            snowblowers_restock[ int( month ) - 1 ].append( item )
    
        if( i['item_stocked'] == 'tires' ):
            item = ( 'tires', int( month ), int( i['item_quantity'] ) )
            tires_restock[ int( month ) - 1 ].append( item )
    
    calculate_success( skis, skis_restock )
    calculate_success( sleds, sleds_restock )
    calculate_success( shovels, shovels_restock )
    calculate_success( snowblowers, snowblowers_restock )
    calculate_success( tires, tires_restock )

    return render(request, 'results.html', 
            {
                'skis_results': [ x[1] for x in skis_restock ],
                'sleds_results': sleds_restock,
                'shovels_results': shovels_restock,
                'snowblowers_results': snowblowers_restock,
                'tires_results': tires_restock,
                'message':'I made it',
            }
        )
