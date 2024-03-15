from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.shortcuts import (HttpResponseRedirect, redirect, render,
                              resolve_url)
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic

from items.models import Item

from .forms import (LoginForm, MyPasswordChangeForm, SetPasswordForm,
                    SignupForm, UserUpdateForm)
from .models import User


class AccountView(generic.TemplateView):
    template_name = 'accounts/top.html'

class Login(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

class Logout(LogoutView):
    template_name = 'accounts/logout.html'

'''自分しかアクセスできないようにするMixin(My Pageのため)'''
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのマイページのpkが同じなら許可
        user = self.request.user
        return user.pk == self.kwargs['pk']
    
'''マイページ'''
class MyPage(OnlyYouMixin, generic.DetailView):
    User = get_user_model()
    model = User
    template_name = 'accounts/my_page.html'
    # モデル名小文字(user)でモデルインスタンスがテンプレートファイルに渡される

'''サインアップ'''
class Signup(generic.CreateView):
    template_name = 'accounts/user_form.html'
    form_class =SignupForm

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        return redirect('account:signup_done')

    # データ送信
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Sign up"
        return context


'''サインアップ完了'''
class SignupDone(generic.TemplateView):
    template_name = 'accounts/signup_done.html'

class UserUpdate(OnlyYouMixin, generic.UpdateView):
    User = get_user_model()
    model = User
    form_class = UserUpdateForm
    template_name = 'accounts/user_form.html'

    def get_success_url(self):
        return resolve_url('account:my_page', pk=self.kwargs['pk'])

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Update"
        return context
    
class PasswordChange(PasswordChangeView):
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('account:password_change_done')
    template_name = 'accounts/user_form.html'

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Change Password"
        return context

class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'

class UserDeleteView(OnlyYouMixin, generic.DeleteView):
    User = get_user_model()
    model = User
    template_name = 'accounts/delete.html'
    def get_success_url(self):
        return resolve_url('account:delete_done')
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # 論理削除を行います。具体的な実装はモデルに依存します。
        self.object.is_active = 0
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class UserDeleteDoneView(generic.TemplateView):
    template_name = 'accounts/delete_done.html'

class PasswordReset(PasswordResetView):
    subject_template_name = 'accounts/password_reset/subject.txt'
    email_template_name = 'accounts/password_reset/email.txt'
    template_name = 'accounts/password_reset/reset.html'
    success_url = reverse_lazy('account:password_reset_sent')

class PasswordResetSent(PasswordResetDoneView):
    template_name = 'accounts/password_reset/sent.html'

class PasswordResetConfirm(PasswordResetConfirmView):
    success_url = reverse_lazy('account:password_reset_complete')
    template_name = 'accounts/password_reset/confirm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Password Reset"
        return context

class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'accounts/password_reset/complete.html'

def FavoriteItems(request):
    # ログインユーザーのお気に入りアイテムを取得    
    user = request.user
    # favorite_items = user.item_set.all()
    favorite_items = Item.objects.filter(LikeUsers=user)
    
    
    return render(request,'accounts/favorite_items.html', {'favorite_items':favorite_items})