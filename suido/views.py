from django.shortcuts import render

def index(request):
    params = {
            'title': '最初のページ',
            'msg': 'これはサンプルページです。',      
    } 
    
    return render(request, 'index.html', params)