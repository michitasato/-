from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

import locale

from .models import Data
from .forms import FindForm

class Index(View):
    def get(self, request, *args, **kwargs):
        data = Data.objects.all().order_by('account_date').reverse()
        params = {
                'form': FindForm(),
                'data': data,
                }
        return render(request, 'index.html', params)

    def post(self, request, *args, **kwargs):
        data = Data.objects\
        .filter(account_date__gte = request.POST['start_date'],\
                account_date__lte = request.POST['end_date'])\
                .filter(shop = request.POST['shop'])\
                .filter(category = request.POST['category'])\
                .order_by('account_date')\
                .reverse()
         #グラフのラベル(日付）
        x =  data.values_list('account_date', flat=True).reverse()
        locale.setlocale(locale.LC_ALL, '')
        labels =[n.strftime('%Y年%m月') for n in x]
        #グラフの値（金額）
        y = data.values_list('account', flat=True).reverse()
        default_items = list(y)

        params = {
                'form':FindForm(request.POST),
                'data': data,
                'labels': labels,
                'default_items': default_items,
                'chart_title': request.POST['shop'] + ' ' + request.POST['category'],
                }
        return render(request, 'index.html', params)


