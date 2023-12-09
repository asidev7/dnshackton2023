
from django.urls import path
from main.views import home,liste_domaine,detail_domaine


urlpatterns = [
    path('',home),
    path('liste-domaine',liste_domaine),
    path('detail/<int:id>',detail_domaine,name="detail_domain"),
]