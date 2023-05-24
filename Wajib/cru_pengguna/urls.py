from django.urls import path
from cru_pengguna.views import indexEarly, indexRegistAtlet, indexRegistPelatih, indexRegistUmpire

app_name = 'cru_pengguna'

urlpatterns = [
    path('early_register/', indexEarly, name='index'),
    path('regist_atlet/', indexRegistAtlet, name='index'),
    path('regist_pelatih/', indexRegistPelatih, name='index'),
    path('regist_umpire/', indexRegistUmpire, name='index'),

]