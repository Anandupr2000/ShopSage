from django.shortcuts import render
from .models.Product import Product
from django.http import JsonResponse
from .priceComparator import PriceComparator
import urllib.parse
import json

def getData(request):
    # Example of retrieving records
    # all_objects = Person.objects.all()
    # print(all_objects)
    # data = {'data':"1231",'athlete_list':[{'name':"hussain bolt"},{'name':"hussain bolt"}],'objects':all_objects}
    # return render(request, 'dummy.html',data)
    if request.method=="POST":
        # print(request.body)
        data = request.body
        
        print(data)
        # Decode bytes to string
        str_data = data.decode('utf-8')

        # Parse query string
        parsed_data = urllib.parse.parse_qs(str_data)
        print('Post request received')
        
        searchKeyword = parsed_data['search'][0]
        
        priceComparator = PriceComparator()
        result = priceComparator.startScrapping(product=searchKeyword)
        for element in result:
            name = element['name']
            price = element['price']
            imageUrl = element['imageUrl']
            redirectLink = element['redirectLink']
            websiteName = element['websiteName']
            obj = Product.objects.create(websiteName=websiteName, redirectLink=redirectLink, name=name, price=price, imageUrl=imageUrl)

    # return JsonResponse({'success':True})
    return JsonResponse({'result':result})

def viewData(request):
    # obj = Person(name='John', age=25, city='New York')
    # obj.save()
    all_objects = Product.objects.all()
    print(all_objects)
    return JsonResponse({'success':True})

def index(request):
    all_objects = Product.objects.all()
    print(all_objects)
    return render(request, 'index.html')

def loadData(request):
    all_objects = Product.objects.all()
    result = list(all_objects.values())
    return JsonResponse({'result':result})