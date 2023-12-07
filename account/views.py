
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from account.forms import UserRegistrationForm
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
from main.views import home
import re


def inscriptionView(request):
    User = get_user_model()
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            role = form.cleaned_data['role']

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email déjà existant")
                return redirect(inscriptionView)
            if User.objects.filter(username=username).exists():
                messages.error(request, "Nom d'utilisateur déjà pris")
                return redirect(inscriptionView)

        
            user = User.objects.create_user(username=username, email=email, password=password)

            if role == "admin":
                group = Group.objects.get(name="admin")
            elif role == "client":
                group = Group.objects.get(name="client")
            user.groups.add(group)

            messages.success(request, 'Inscription réussie. Vous pouvez vous connecter.')
            return redirect(user_login)
        else:
            # Handle form validation errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    return render(request, 'account/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if username == "":
            messages.info(request, "Le nom d'utilisateur est requis")
            return redirect(user_login)

        if user is not None:
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                user_groups = Group.objects.filter(user=user)  # Utiliser filter() au lieu de get()
                if user_groups.exists():  # Vérifier si le queryset n'est pas vide
                    role = user_groups.first().name.lower()  # Récupérer le premier groupe et le convertir en minuscules
                    if role == "admin":
                        return redirect(home)  # Rediriger vers le dashboard du patient
                    elif role == "client":
                        return redirect(home)  # Rediriger vers le dashboard du médecin
                    else:
                        messages.error(request, 'Role utilisateur invalide')
                else:
                    messages.error(request, 'Utilisateur sans groupe')
        else:
                messages.error(request, 'Identifiant ou mot de passe incorrect')
                return redirect(user_login)

    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    return redirect(user_login)

