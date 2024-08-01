from django.shortcuts import render, redirect  # Importa as funções 'render' e 'redirect' do Django para renderização e redirecionamento de páginas
from .models import Produto, Venda, ItensVenda, Cliente, Fornecedor, Vendedor  # Importa os modelos da aplicação atual
from .forms import UserRegisterForm, ClienteForm  # Importa os formulários personalizados da aplicação atual
from django.contrib.auth import authenticate, login  # Importa funções de autenticação e login do Django
from django.contrib.auth.forms import AuthenticationForm  # Importa o formulário de autenticação padrão do Django
from django.contrib import messages  # Importa a biblioteca de mensagens do Django para feedbacks ao usuário

# Função para renderizar a página inicial
def home(request):
    return render(request, 'trade/home.html')

# Função para o cadastro de clientes
def cadastro_clientes(request):
    if request.method == 'POST':  # Se o método de requisição for POST, processa o formulário
        form = ClienteForm(request.POST)
        if form.is_valid():  # Se o formulário for válido, salva os dados e redireciona para a página inicial
            form.save()
            return redirect('home')
    else:  # Se o método de requisição não for POST, exibe um formulário vazio
        form = ClienteForm()
    return render(request, 'trade/cadastro_clientes.html', {'form': form})

# Função para exibir tabelas de dados de clientes, fornecedores, produtos e vendas
def demonstrativo_tabelas(request):
    clientes = Cliente.objects.all()
    fornecedores = Fornecedor.objects.all()
    produtos = Produto.objects.all()
    vendas = Venda.objects.all()
    return render(request, 'trade/demonstrativo_tabelas.html', {
        'clientes': clientes,
        'fornecedores': fornecedores,
        'produtos': produtos,
        'vendas': vendas,
    })

# Função para exibir a galeria de produtos
def galeria_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'trade/galeria_produtos.html', {'produtos': produtos})

# Função para processar a realização de uma venda
def realizar_venda(request):
    if request.method == 'POST':  # Se o método de requisição for POST, processa os dados da venda
        cliente_id = request.POST.get('cliente')
        produto_id = request.POST.get('produto')
        quantidade = request.POST.get('quantidade')
        cliente = Cliente.objects.get(idcli=cliente_id)
        produto = Produto.objects.get(idprod=produto_id)
        vendedor = Vendedor.objects.first()  # Supondo que há um vendedor padrão
        fornecedor = produto.idforn

        # Calcula o valor da venda
        valor_venda = produto.valorprod * int(quantidade)
        venda = Venda.objects.create(
            codivend='12345',  # Código de venda gerado automaticamente
            idcli=cliente,
            idforn=fornecedor,
            idvende=vendedor,
            valorvend=valor_venda,
            descvend=0,
            totalvend=valor_venda,
            datavend='2023-07-19',  # Data atual
            valorcomissao=valor_venda * vendedor.porcvende / 100
        )

        # Cria um item de venda associado à venda
        ItensVenda.objects.create(
            idvend=venda,
            idprod=produto,
            valoritvend=produto.valorprod,
            qtditvend=quantidade,
            descitvend=0
        )

        return redirect('home')  # Redireciona para a página inicial após concluir a venda

    # Se o método de requisição não for POST, exibe os dados dos clientes e produtos
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    return render(request, 'trade/realizar_venda.html', {
        'clientes': clientes,
        'produtos': produtos,
    })

# Função para realizar o login do usuário
def login_view(request):
    if request.method == 'POST':  # Se o método de requisição for POST, processa o formulário de login
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():  # Se o formulário for válido, autentica o usuário
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Realiza o login do usuário
                return redirect('home')  # Redireciona para a página inicial
    else:
        form = AuthenticationForm()  # Se o método de requisição não for POST, exibe um formulário vazio
    return render(request, 'trade/login.html', {'form': form})

# Função para cadastrar um novo usuário
def cadastroUser(request):
    if request.method == 'POST':  # Se o método de requisição for POST, processa o formulário de cadastro
        form = UserRegisterForm(request.POST)
        if form.is_valid():  # Se o formulário for válido, salva os dados do usuário
            user = form.save()
            username = user.username
            messages.success(request, 'Cadastro realizado com sucesso!')  # Exibe uma mensagem de sucesso
            return redirect('cadastroUser')  # Redireciona para a página de cadastro
    else:
        form = UserRegisterForm()  # Se o método de requisição não for POST, exibe um formulário vazio
    return render(request, 'trade/cadastroUser.html', {'form': form})
