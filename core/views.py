from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages

# Create your views here.
def index(request):
    print (str(request.user))
    if str(request.user) == 'AnonymousUser':
        logado = 'Entrar no sistema'
    else:
        logado = 'Bem vindo ' + str(request.user)

    context = {
        'logado': logado
    }

    return render(request, 'index.html', context)

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    return render(request, 'produto.html')