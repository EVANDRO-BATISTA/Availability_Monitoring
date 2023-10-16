from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # redirecione para a página inicial após o login
        else:
            error_message = 'Credenciais inválidas. Por favor, tente novamente.'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def login(request):
    return render(request, 'registration/login.html')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
def base(request):
    return render(request, 'base.html')
def config(request):
    return render(request, 'config/config.html')
def add_ips(request):
    return render(request, 'add_ips/add_ips.html')
def relatorio(request):
    return render(request, 'relatorio/relatorio.html')