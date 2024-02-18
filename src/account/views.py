from django.shortcuts import render, redirect, resolve_url
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from .forms import LoginForm, SignupForm, UserUpdateForm, MyPasswordChangeForm
from django.urls import reverse_lazy


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