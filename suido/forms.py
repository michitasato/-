# -*- coding: utf-8 -*-
from django import forms

# レコードを検索するフォーム
class FindForm(forms.Form):
    shop_data=[
            ('松茂店', '松茂店'),
            ('羽ノ浦店', '羽ノ浦店'),
            ]
    category_data=[
            ('電気代', '電気代'),
            ('水道代', '水道代'),
            ('ガス代', 'ガス代')
            ]
    start_date = forms.DateField(label='開始年月', required=False)
    end_date = forms.DateField(label='終了年月', required=False)
    shop = forms.MultipleChoiceField(label='店舗名', \
          choices=shop_data, widget=forms.SelectMultiple(attrs={'size':3}))
    category = forms.MultipleChoiceField(label='分類', \
          choices=category_data, widget=forms.SelectMultiple(attrs={'size':3}))
    