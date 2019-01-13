from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

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

        params = {
                'form':FindForm(request.POST),
                'data': data,
                }
        return render(request, 'index.html', params)

def get_data(request, *args, **kwargs):
    data = {
        'sales': 100,
        'customers': 10,
    }
    return JsonResponse(data)

