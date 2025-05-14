from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def cadastro_cliente(request):
    if request.method == 'GET':
        return render(request, 'cadastro_cliente.html')
    else:
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'cadastro_cliente.html', {'error_message': 'As senhas não coincidem.'})

        user = User.objects.filter(email=email).first()
        if user:
            return render(request, 'cadastro_cliente.html', {'error_message': 'Já existe um usuário com esse email.'})
        try:
            username = email.split('@')[0]
            user = User.objects.create_user(
                username=username,
                first_name=nome,
                last_name=sobrenome,
                email=email,
                password=password1
            )
            return render(request, 'sucesso.html', {'nome': nome, 'email': email})
        except Exception as e:
            return render(request, 'cadastro_cliente.html', {'error_message': f'Erro ao cadastrar usuário: {str(e)}'})


def login_cliente(request):
    if request.method == 'GET':
        return render(request, 'login_cliente.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password1')
        user_obj = User.objects.filter(email=email).first()
        if user_obj:
            user = authenticate(username=user_obj.username, password=password)
            if user:
                login(request, user)
                return redirect('home')

        return render(request, 'login_cliente.html', {'error_message': 'Email ou senha inválidos!'})


def logout_cliente(request):
    logout(request)
    return redirect('login_cliente')

@login_required()
def sucesso_cad(request):
    return render(request, 'sucesso.html')