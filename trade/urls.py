from django.urls import path  # Importa a função 'path' do módulo 'django.urls'
from . import views  # Importa o módulo 'views' do diretório atual

# Define a lista de URLs (endpoints) que o aplicativo irá reconhecer e associar a determinadas visualizações
urlpatterns = [
    path('', views.login_view, name='login'),  # URL raiz ('') chama a view 'login_view' e tem o nome 'login'
    path('home/', views.home, name='home'),  # URL 'home/' chama a view 'home' e tem o nome 'home'
    # path('', views.home, name='home'),  # Comentado: URL raiz ('') chama a view 'home' e tem o nome 'home'
    path('cadastroUser/', views.cadastroUser, name='cadastroUser'),  # URL 'cadastroUser/' chama a view 'cadastroUser' e tem o nome 'cadastroUser'
    path('cadastro_clientes/', views.cadastro_clientes, name='cadastro_clientes'),  # URL 'cadastro_clientes/' chama a view 'cadastro_clientes' e tem o nome 'cadastro_clientes'
    path('demonstrativo_tabelas/', views.demonstrativo_tabelas, name='demonstrativo_tabelas'),  # URL 'demonstrativo_tabelas/' chama a view 'demonstrativo_tabelas' e tem o nome 'demonstrativo_tabelas'
    path('galeria_produtos/', views.galeria_produtos, name='galeria_produtos'),  # URL 'galeria_produtos/' chama a view 'galeria_produtos' e tem o nome 'galeria_produtos'
    path('realizar_venda/', views.realizar_venda, name='realizar_venda'),  # URL 'realizar_venda/' chama a view 'realizar_venda' e tem o nome 'realizar_venda'
    path('login/', views.login_view, name='login'),  # URL 'login/' chama a view 'login_view' e tem o nome 'login'
]

