from django.shortcuts import render
from django.views.generic import View

from .models import Data
from .forms import FindForm

# index関数　トップページ 　条件を指定する前の状態
class Index(View):    
    def get(self, request, *args, **kwargs):
        # GETリクエスト用のメソッド
        data = Data.objects.all().order_by('account_date').reverse()
        params = {
                'form': FindForm(),
                'data': data,
                } 
        # トップ画面用のテンプレートに値がからの空のフォームをレンダリングする
        return render(request, 'index.html', params)
    
    def post(self, request, *args, **kwargs):
            # POSTリクエスト用のメソッド
        data = Data.objects\
        .filter(account_date__gte = request.POST['start_date'],\
                account_date__lte = request.POST['end_date'])\
                .filter(shop = request.POST['shop'])\
                .filter(category = request.POST['category'])\
                .order_by('account_date')\
                .reverse()

        params = {
                'form':FindForm(request.POST),
                'data': data,
                }
        return render(request, 'index.html', params)
