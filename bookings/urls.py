from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_sal, name='lista_sal'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_sal, name='lista_sal'),
    path('book/<int:sala_id>/', views.rezerwuj_sale, name='rezerwuj_sale'), # Новая строка
]