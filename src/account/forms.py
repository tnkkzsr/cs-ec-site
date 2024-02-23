from django import forms
from django.contrib.auth import get_user_model  # ユーザーモデルを取得するため
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       UserCreationForm)

# ユーザーモデル取得
User = get_user_model()


'''ログイン用フォーム'''
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='ユーザー名かメールアドレス', max_length=254)
    # bootstrap4対応
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる

class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email','username', 'address', 'phone_number', 'profile_image', 'bio')
        labels = {
            'address':'住所',
            'phone_number':'電話番号',
            'profile_image':'プロフィール画像',
            'bio':'自己紹介文'
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['profile_image'].required = False
        self.fields['bio'].required = False
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


            # オートフォーカスとプレースホルダーの設定
            print(field.label)
            if field.label == '姓':
                field.widget.attrs['autofocus'] = '' # 入力可能状態にする
                field.widget.attrs['placeholder'] = '田中'
            elif field.label == '名':
                field.widget.attrs['placeholder'] = '一郎'
            elif field.label == 'メールアドレス':
                field.widget.attrs['placeholder'] = '***@gmail.com'

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email', 'username','address', 'phone_number', 'profile_image', 'bio')
        labels = {
            'address':'住所',
            'phone_number':'電話番号',
            'profile_image':'プロフィール画像',
            'bio':'自己紹介文'
        }
    # bootstrap4対応
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['profile_image'].required = False
        self.fields['bio'].required = False
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class MyPasswordChangeForm(PasswordChangeForm):

    # bootstrap4対応で、classを指定
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

