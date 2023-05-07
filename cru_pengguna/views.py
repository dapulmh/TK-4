from django.shortcuts import render

def indexEarly(request):
    return render(request, 'early_register.html')

def indexRegistAtlet(request):
    return render(request, 'regist_atlet.html')

def indexRegistPelatih(request):
    return render(request, 'regist_pelatih.html')

def indexRegistUmpire(request):
    return render(request, 'regist_umpire.html')