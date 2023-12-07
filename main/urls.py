
from django.urls import path
from main.views import home,liste_domaine,detail_domaine,reserver_domaine


urlpatterns = [
    path('',home),
    path('liste-domaine',liste_domaine),
    path('detail/<int:id>',detail_domaine,name="detail_domain"),
    path('reserver/str:nom_domaine>/',reserver_domaine,name="reserver")
]