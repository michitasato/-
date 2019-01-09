from django.shortcuts import render
from .models import Data

def index(request):
    data = Data.objects.all()
    params = {
            'title': '最初のレコード表示',
            'message': 'これはサンプルページです。',
            'data': data
    } 
    
    return render(request, 'index.html', params)