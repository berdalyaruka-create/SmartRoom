from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages # Добавили модуль сообщений
from .models import Sala, Rezerwacja
from .forms import RezerwacjaForm

@login_required
def lista_sal(request):
    min_capacity = request.GET.get('min_capacity')
    sale = Sala.objects.filter(pojemnosc__gte=min_capacity) if min_capacity else Sala.objects.all()
    moje_rezerwacje = Rezerwacja.objects.filter(uzytkownik=request.user).order_by('data_start')
    
    return render(request, 'bookings/lista_sal.html', {
        'sale': sale, 
        'moje_rezerwacje': moje_rezerwacje
    })

@login_required
def rezerwuj_sale(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)
    if request.method == 'POST':
        form = RezerwacjaForm(request.POST)
        if form.is_valid():
            nowa_rezerwacja = form.save(commit=False)
            
            # Проверка на пересечение времени (US2: Rezerwacja sali)
            kolizja = Rezerwacja.objects.filter(
                sala=sala,
                data_start__lt=nowa_rezerwacja.data_koniec,
                data_koniec__gt=nowa_rezerwacja.data_start
            ).exists()
            
            if kolizja:
                messages.error(request, 'Ta sala jest już zajęta w wybranym terminie!')
            else:
                nowa_rezerwacja.uzytkownik = request.user
                nowa_rezerwacja.sala = sala
                nowa_rezerwacja.save()
                messages.success(request, f'Sala {sala.numer} została zarezerwowana!')
                return redirect('lista_sal')
    else:
        form = RezerwacjaForm()
    return render(request, 'bookings/rezerwuj.html', {'form': form, 'sala': sala})