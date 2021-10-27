# Sistema de vendas

class Produto():
    def __init__(self):
        self._titulo = None
        self._valor = None
        self._desconto = None

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, novo_titulo):
        self._titulo = novo_titulo

    def get_valor(self):
        return self._valor

    def set_valor(self, novo_valor):
        self._valor = novo_valor

    def get_desconto(self):
        return self._desconto

    def set_desconto(self, novo_desconto):
        self._desconto = novo_desconto

    def descreve_produto(self):
        self._desconto = self.get_desconto() / 100
        self._desconto = self.get_valor() * self._desconto
        print("===== DESCRIÇÃO DO PRODUTO ====")
        print("NOME DO PRODUTO:", self.get_titulo())
        print("VALOR: R$%.2f" % self.get_valor())
        print("DESCONTO: R$%.2f" % self.get_desconto())
        self._valor -= self.get_desconto()
        print("VALOR COM DESCONTO: R$%.2f" % self.get_valor(), "\n")


class Livro(Produto):
    def __init__(self):
        self._autor = None
        super().__init__()

    def get_autor(self):
        return self._autor

    def set_autor(self, novo_autor):
        self._autor = novo_autor

    def descreve_produto(self):
        self._desconto = self.get_desconto() / 100
        self._desconto = self.get_valor() * self._desconto
        print("===== DESCRIÇÃO DO LIVRO ====")
        print("PRODUTO:", self.get_titulo())
        print("NOME DO AUTOR:", self.get_autor())
        print("VALOR: R$%.2f" % self.get_valor())
        print("DESCONTO DE 10%")
        print("VALOR DO DESCONTO: R$%.2f" % self.get_desconto())
        self._valor -= self.get_desconto()
        print("VALOR COM DESCONTO: R$%.2f" % self.get_valor(), "\n")


class CD(Produto):
    def __init__(self):
        self._artista = None
        super().__init__()

    def get_artista(self):
        return self._artista

    def ser_artista(self, novo_artista):
        self._artista = novo_artista

    def descreve_produto(self):
        self._desconto = self.get_desconto() / 100
        self._desconto = self.get_valor() * self._desconto
        print("===== DESCRIÇÃO DO CD ====")
        print("PRODUTO:", self.get_titulo())
        print("ARTISTA: ", self.get_artista())
        print("VALOR: R$%.2f" % self.get_valor())
        print("DESCONTO DE 15%")
        print("VALOR DO DESCONTO: R$%.2f" % self.get_desconto())
        self._valor -= self.get_desconto()
        print("VALOR COM DESCONTO: R$%.f" % self.get_valor(), "\n")


class DVD(Produto):
    def __init__(self):
        self._duracao = None
        super().__init__()

    def get_duracao(self):
        return self._duracao

    def set_duracao(self, nova_duracao):
        self._duracao = nova_duracao

    def descreve_produto(self):
        self._desconto = self.get_desconto() / 100
        self._desconto = self.get_valor() * self._desconto
        print("===== DESCRIÇÃO DO DVD ====")
        print("PRODUTO:", self.get_titulo())
        print("DURAÇÃO:", self.get_duracao())
        print("VALOR: R$%.2f" % self.get_valor())
        print("DESCONTO DE 20%")
        print("VALOR DO DESCONTO: R$%.2f" % self.get_desconto())
        self._valor -= self.get_desconto()
        print("VALOR COM DESCONTO: R$%.2f" % self.get_valor(), "\n")


# Execução
listaDeProdutos = []  # para adicionar os produtos.
total = []  # para somar o valor total da compra.
descontos = []  # Para calcular a soma dos descontos.

produto1 = Produto()
produto1.set_titulo("Lápis de cor Faber Castell")
produto1.set_valor(5)
produto1.set_desconto(5)
produto1.descreve_produto()
print(produto1.get_titulo)
listaDeProdutos.append(produto1)

produto2 = Produto()
produto2.set_titulo("Pilhas Duraceel")
produto2.set_valor(2)
produto2.set_desconto(5)
produto2.descreve_produto()
listaDeProdutos.append(produto2)

livro1 = Livro()
livro1.set_titulo("A ARTE DA GUERRA")
livro1.set_valor(29)
livro1.set_desconto(20)
livro1.set_autor("SUN TZU")
livro1.descreve_produto()
listaDeProdutos.append(livro1)

livro2 = Livro()
livro2.set_titulo("O PODER DO HÁBITO")
livro2.set_valor(29)
livro2.set_desconto(20)
livro2.set_autor("CHARLES DUHIGG")
livro2.descreve_produto()
listaDeProdutos.append(livro2)

cd1 = CD()
cd1.set_titulo("Forró")
cd1.ser_artista("Zé Vaqueiro")
cd1.set_valor(40)
cd1.set_desconto(15)
cd1.descreve_produto()
listaDeProdutos.append(cd1)

cd2 = CD()
cd2.set_titulo("As Quatro Estações")
cd2.ser_artista("Legião Urbana")
cd2.set_valor(35)
cd2.set_desconto(15)
cd2.descreve_produto()
listaDeProdutos.append(cd2)

dvd1 = DVD()
dvd1.set_titulo("VINGADORES ULTIMATO - MARVEL STUDIOS")
dvd1.set_duracao("3h")
dvd1.set_valor(50)
dvd1.set_desconto(20)
dvd1.descreve_produto()
listaDeProdutos.append(dvd1)

dvd2 = DVD()
dvd2.set_titulo("O Jogo Da Imitação")
dvd2.set_duracao("1h 54min")
dvd2.set_valor(45)
dvd2.set_desconto(20)
dvd2.descreve_produto()
listaDeProdutos.append(dvd2)

for i in listaDeProdutos:
    total.append(i.get_valor())
    descontos.append(i.get_desconto())

print("======== COMPROVANTE ========= \n")
print("QUANT. ITENS:", len(listaDeProdutos))
print("TOTAL DE DESCONTO: R$%.2f" % sum(descontos))
print("TOTAL A PAGAR: R$%.2f" % sum(total), "\n")
print("AGRADECEMOS A PREFERÊNCIA!")
