from django.shortcuts import render,redirect,reverse
from django.contrib import messages

from main.forms import DomaineDisponibiliteForm
from main.models import Domaine
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = DomaineDisponibiliteForm(request.POST)
        if form.is_valid():
            nom_domaine = form.cleaned_data['nom_domaine']

            # Vérifiez la disponibilité du nom de domaine
            if Domaine.objects.filter(nom_domaine=nom_domaine).exists():
                # Le nom de domaine est déjà pris
                messages.error(request, 'Le nom de domaine n est pas dispinible')
                return render(request, 'main/home.html', {'nom_domaine': nom_domaine,'form': form})
            elif not (nom_domaine.endswith('.benin') or nom_domaine.endswith('.cotonou')):
                # Le nom de domaine ne se termine pas par .benin ou .cotonou
                messages.warning(request, 'Le nom de domaine ne se termine pas par .benin ou .cotonou')
                return render(request,'main/home.html', {'nom_domaine':nom_domaine})
            else:
                # Le nom de domaine est disponible
                
                messages.success(request, f'Le nom de domaine "{nom_domaine}" est disponible')
                return render(request,'main/home.html', {'nom_domaine':nom_domaine, 'form':form})

    else:
        form = DomaineDisponibiliteForm()

    return render(request, 'main/home.html', {'form': form})


def liste_domaine(request):
    domaines = Domaine.objects.filter(client=request.user)
    params ={
        'domaines':domaines
    }
    return render(request,'main/liste-domaine.html',params)



def detail_domaine(request,id):
    domaine = Domaine.objects.get(id=id)
    params ={
        'domain':domaine
    }
    return render(request,'main/detail-domaine.html',params)

