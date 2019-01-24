# -*- coding: utf-8 -*-
from django import forms

# レコードを検索するフォーム
class FindForm(forms.Form):
    shop_data=[
            ('三加茂店', '三加茂店'),
            ('名東店', '名東店'),
            ('笠木店', '笠木店'),
            ('矢上店', '矢上店'),
            ('羽ノ浦店', '羽ノ浦店'),
            ('松茂店', '松茂店'),
            ('坂東店', '坂東店'),
            ('南小松島店', '南小松島店'),
            ('北鴨島店', '北鴨島店'),
            ('フレンド藍住店', 'フレンド藍住店'),
            ('ひとみ仁尾店', 'ひとみ仁尾店'),
            ('北島店', '北島店'),
            ('徳命店', '徳命店'),
            ('東中富店', '東中富店'),
            ('フクシア', 'フクシア'),
            ('三加茂・営業所', '三加茂・営業所'),
            ('本部', '本部'),
            ]
    category_data=[
            ('電気代', '電気代'),
            ('水道代', '水道代'),
            ('ガス代', 'ガス代'),
            ('水道代', '水道代'),
            ('通信費(電話・ｲﾝﾀｰﾈｯﾄ) ', '通信費(電話・ｲﾝﾀｰﾈｯﾄ)'),
            ('通信費(切手・郵送代・NHK)', '通信費(切手・郵送代・NHK)'),
            ]
    start_date = forms.DateField(label='開始年月', required=False, widget=forms.DateInput(attrs={'class': 'datepicker'}))
    end_date = forms.DateField(label='終了年月', required=False)
    shop = forms.MultipleChoiceField(label='店舗名', \
          choices=shop_data, widget=forms.SelectMultiple(attrs={'size':3}))
    category = forms.MultipleChoiceField(label='分類', \
          choices=category_data, widget=forms.SelectMultiple(attrs={'size':3}))

# CSVアップロード用のファーム
class CSVUploadForm(forms.Form):
    file = forms.FileField(label='CSVファイル', help_text='※拡張子csvのファイルをアップロードしてください。')

    def clean_file(self):
        file = self.cleaned_data['file']
        if file.name.endswith('.csv'):
            return file
        else:
            raise forms.ValidationError('拡張子がcsvのファイルをアップロードしてください')
