from .models import Character
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.db import IntegrityError
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignupForm

# Create your views here.
class Login (LoginView):
    template_name = "accounts/login.html"
    next_page = reverse_lazy("evolution_prompt:job")  

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context["error"] = "ユーザー名またはパスワードが正しくありません。"
        return self.render_to_response(context)


class Signup(CreateView):
    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("evolution_prompt:job")  

    def form_valid(self, form):
        try:
            self.object = form.save()
            Character.objects.get_or_create(user=self.object)
            login(self.request, self.object)
            return super().form_valid(form)
        except IntegrityError:
            form.add_error(None, "このメールアドレスは既に登録されています")
            return self.form_invalid(form)



class Logout(LogoutView):
    template_name = "accounts/login.html"
    #ログイン画面に遷移させる
    success_url = reverse_lazy("login")
