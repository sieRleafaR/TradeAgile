from django.db import models  # Importa o módulo de modelos do Django

# Modelo para representar um vendedor
class Vendedor(models.Model):
    idvende = models.AutoField(primary_key=True)  # Campo de chave primária auto-incremental
    codivende = models.CharField(max_length=10)  # Código do vendedor, campo de caracteres com tamanho máximo de 10
    nomevende = models.CharField(max_length=100)  # Nome do vendedor, campo de caracteres com tamanho máximo de 100
    razasocvende = models.CharField(max_length=100)  # Razão social do vendedor, campo de caracteres com tamanho máximo de 100
    fonevende = models.CharField(max_length=20)  # Telefone do vendedor, campo de caracteres com tamanho máximo de 20
    porcvende = models.FloatField()  # Percentual de comissão do vendedor, campo de ponto flutuante

    class Meta:
        db_table = 'vendedor'  # Define o nome da tabela no banco de dados

# Modelo para representar um produto
class Produto(models.Model):
    idprod = models.AutoField(primary_key=True)  # Campo de chave primária auto-incremental
    codiprod = models.CharField(max_length=20)  # Código do produto, campo de caracteres com tamanho máximo de 20
    descprod = models.CharField(max_length=100)  # Descrição do produto, campo de caracteres com tamanho máximo de 100
    valorprod = models.FloatField()  # Valor do produto, campo de ponto flutuante
    situprod = models.CharField(max_length=1)  # Situação do produto, campo de caracteres com tamanho máximo de 1
    idforn = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)  # Chave estrangeira para o fornecedor, deletando em cascata

    class Meta:
        db_table = 'produto'  # Define o nome da tabela no banco de dados

# Modelo para representar um fornecedor
class Fornecedor(models.Model):
    idforn = models.AutoField(primary_key=True)  # Campo de chave primária auto-incremental
    codiforn = models.CharField(max_length=10)  # Código do fornecedor, campo de caracteres com tamanho máximo de 10
    nomeforn = models.CharField(max_length=100)  # Nome do fornecedor, campo de caracteres com tamanho máximo de 100
    razasocforn = models.CharField(max_length=100)  # Razão social do fornecedor, campo de caracteres com tamanho máximo de 100
    foneforn = models.CharField(max_length=20)  # Telefone do fornecedor, campo de caracteres com tamanho máximo de 20

    class Meta:
        db_table = 'fornecedor'  # Define o nome da tabela no banco de dados

# Modelo para representar um cliente
class Cliente(models.Model):
    idcli = models.AutoField(primary_key=True)  # Campo de chave primária auto-incremental
    codcli = models.CharField(max_length=10)  # Código do cliente, campo de caracteres com tamanho máximo de 10
    nomecli = models.CharField(max_length=100)  # Nome do cliente, campo de caracteres com tamanho máximo de 100
    razasoccli = models.CharField(max_length=100)  # Razão social do cliente, campo de caracteres com tamanho máximo de 100
    datacli = models.DateField()  # Data de registro do cliente, campo de data
    cnpjcli = models.CharField(max_length=20)  # CNPJ do cliente, campo de caracteres com tamanho máximo de 20
    fonecli = models.CharField(max_length=20)  # Telefone do cliente, campo de caracteres com tamanho máximo de 20
    cidcli = models.CharField(max_length=50)  # Cidade do cliente, campo de caracteres com tamanho máximo de 50
    estcli = models.CharField(max_length=100)  # Estado do cliente, campo de caracteres com tamanho máximo de 100

    class Meta:
        db_table = 'cliente'  # Define o nome da tabela no banco de dados

# Modelo para representar itens de uma venda
class ItensVenda(models.Model):
    iditvend = models.AutoField(primary_key=True)  # Campo de chave primária auto-incremental
    idvend = models.ForeignKey('Venda', on_delete=models.CASCADE)  # Chave estrangeira para a venda, deletando em cascata
    idprod = models.ForeignKey('Produto', on_delete=models.CASCADE)  # Chave estrangeira para o produto, deletando em cascata
    valoritvend = models.FloatField()  # Valor do item da venda, campo de ponto flutuante
    qtditvend = models.IntegerField()  # Quantidade do item da venda, campo de inteiro
    descitvend = models.FloatField()  # Desconto do item da venda, campo de ponto flutuante

    class Meta:
        db_table = 'itensvenda'  # Define o nome da tabela no banco de dados

# Modelo para representar uma venda
class Venda(models.Model):
    idvend = models.AutoField(primary_key=True)  # Campo de chave primária auto-incremental
    codivend = models.CharField(max_length=10)  # Código da venda, campo de caracteres com tamanho máximo de 10
    idcli = models.ForeignKey('Cliente', on_delete=models.CASCADE)  # Chave estrangeira para o cliente, deletando em cascata
    idforn = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)  # Chave estrangeira para o fornecedor, deletando em cascata
    idvende = models.ForeignKey('Vendedor', on_delete=models.CASCADE)  # Chave estrangeira para o vendedor, deletando em cascata
    valorvend = models.FloatField()  # Valor da venda, campo de ponto flutuante
    descvend = models.FloatField()  # Desconto da venda, campo de ponto flutuante
    totalvend = models.FloatField()  # Valor total da venda, campo de ponto flutuante
    datavend = models.DateField()  # Data da venda, campo de data
    valorcomissao = models.DecimalField(max_digits=10, decimal_places=2)  # Valor da comissão, campo decimal com precisão de 10 dígitos e 2 casas decimais

    class Meta:
        db_table = 'venda'  # Define o nome da tabela no banco de dados

# Modelo de backup para representar um cliente
class ClienteBkp(models.Model):
    idcli = models.AutoField(primary_key=True)  # Campo de chave primária auto-incremental
    codcli = models.CharField(max_length=10)  # Código do cliente, campo de caracteres com tamanho máximo de 10
    nomecli = models.CharField(max_length=100)  # Nome do cliente, campo de caracteres com tamanho máximo de 100
    razasoccli = models.CharField(max_length=100)  # Razão social do cliente, campo de caracteres com tamanho máximo de 100
    datacli = models.DateField()  # Data de registro do cliente, campo de data
    cnpjcli = models.CharField(max_length=20)  # CNPJ do cliente, campo de caracteres com tamanho máximo de 20
    fonecli = models.CharField(max_length=20)  # Telefone do cliente, campo de caracteres com tamanho máximo de 20
    cidcli = models.CharField(max_length=50)  # Cidade do cliente, campo de caracteres com tamanho máximo de 50
    estcli = models.CharField(max_length=100)  # Estado do cliente, campo de caracteres com tamanho máximo de 100

    class Meta:
        db_table = 'clientesbkp'  # Define o nome da tabela no banco de dados
