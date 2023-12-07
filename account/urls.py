from django.urls import path
from account.views import user_login,inscriptionView,logout_view

urlpatterns =[
path('login',user_login),
path('register',inscriptionView),
path('logout',logout_view)

]