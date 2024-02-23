from django import forms

class Add_Item_Form(forms.Form):
    
    ITEM_CONDITION_CHOICES = [
        ('', '選択してください'),
        ('新品', '新品'),
        ('中古', '中古'),
    ]
    
    item_title = forms.CharField(label='商品名', max_length=100)
    item_explain = forms.CharField(label='商品説明',widget=forms.Textarea(attrs={'rows': 3}), max_length=1000)
    item_category = forms.CharField(label='カテゴリ', max_length=100)
    item_condition = forms.TypedChoiceField(
        choices=ITEM_CONDITION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        coerce=str,  # 選択された値を文字列に変換
        empty_value='',  # 空の選択肢を設定
        label='商品の状態'
    )
    item_price = forms.IntegerField(label='価格',min_value=0)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item_title'].widget.attrs['placeholder'] = '商品名を入力してください'
        self.fields['item_category'].widget.attrs['placeholder'] = 'カテゴリを入力してください'
        self.fields['item_price'].widget.attrs['placeholder'] = '価格を入力してください'
        for field in self.fields.values():
            if field.label != '商品の状態':
                field.widget.attrs['class'] = 'form-control'