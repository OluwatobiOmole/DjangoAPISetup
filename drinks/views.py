from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view

@api_view('GET', 'POST')
def drink_list(request):

    #get all drinks 
    #serialize them
    #return json

    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        print("Data",serializer.data)
        return JsonResponse({'drinks': serializer.data} , safe=False)
    
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        

    
