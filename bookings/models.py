from django.db import models
from django.contrib.auth.models import User

class Sala(models.Model):
    numer = models.CharField(max_length=10, unique=True)
    pojemnosc = models.IntegerField()
    opis = models.TextField(blank=True)

    def __str__(self):
        return f"Sala {self.numer}"

class Rezerwacja(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    data_start = models.DateTimeField()
    data_koniec = models.DateTimeField()
    status = models.CharField(max_length=20, default='Potwierdzona')

    def __str__(self):
        return f"{self.uzytkownik} - {self.sala} ({self.data_start.date()})"