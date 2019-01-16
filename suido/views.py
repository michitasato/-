from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

import locale

# csv読み込みに使うモジュール
import csv
import io
from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import CSVUploadForm
from datetime import datetime as dt


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


# PostImport関数：CSVファイルをインポートして、DBに保管する。
class PostImport(generic.FormView):
    template_name = 'upload.html'
    success_url = reverse_lazy('index')
    form_class = CSVUploadForm

    def form_valid(self, form):
        # csv.readerに渡すため、TextIOWrapperでテキストモードなファイルに変換
        csvfile = io.TextIOWrapper(form.cleaned_data['file'], encoding='cp932')
        reader = csv.reader(csvfile)
        header = next(reader) #headerを飛ばす処理
        # 1行ずつ取り出し、作成していく
        for row in reader:
            post, created = Data.objects.get_or_create(account_date = row[1], \
                                            shop = row[2], category = row[3])
            post.account_date = row[1]
            post.shop = row[2]
            post.category = row[3]
            post.account=int(row[4]) 
            post.save()
        return super().form_valid(form)