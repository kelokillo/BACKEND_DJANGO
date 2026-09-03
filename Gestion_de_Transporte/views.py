from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home_view(request):   
    return render(request, 'index.html')
def custom_404_view(request, exception):    
    return render(request, '404.html', status=404)