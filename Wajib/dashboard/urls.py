from django.urls import path
from dashboard.views import indexDashboardAtlet, indexDashboardPelatih, indexDashboardUmpire

app_name = 'dashboard'

urlpatterns = [
    path('dashboard_atlet/', indexDashboardAtlet, name='index'),
    path('dashboard_pelatih/', indexDashboardPelatih, name='index'),
    path('dashboard_umpire/', indexDashboardUmpire, name='index'),    
]