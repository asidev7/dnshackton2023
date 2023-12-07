from django.db import models

# Create your models here.
# dans votre_app/models.py

from django.db import models
from django.contrib.auth.models import User  # Si vous utilisez le modèle User de Django

class Domaine(models.Model):
    STATUS_CHOICES = [
        ('en_attente', 'En attente'),
        ('active', 'Active'),
        ('expire', 'Expiré'),
    ]
    nom_domaine = models.CharField(max_length=255, unique=True)
    date_creation = models.DateField(auto_now_add=True)
    date_expiration = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='en_attente')
    nameservers = models.ManyToManyField('NameServer', related_name='domaines')
    ds_record = models.CharField(max_length=255)
    client = models.ForeignKey(User, on_delete=models.CASCADE)  # Assurez-vous que vous avez défini le modèle User correctement

    def __str__(self):
        return self.nom_domaine

class NameServer(models.Model):
    name = models.CharField(max_length=255)
    # Ajoutez d'autres champs si nécessaire

    def __str__(self):
        return self.name
