class Animal():
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor

    def comer(self):
        print(f"o seu {self.nome} foi comer...")

class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def miar(self):
        print(f"O  {self.nome} foi miando...")

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def latir(self):
        print(f"O  {self.nome} foi latindo...")

class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def chia(self):
        print(f"O  {self.nome} foi chiando...")

class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def mugir(self):
        print(f"O  {self.nome} foi mugindo...")

class Ingresso():
    def __init__(self,valor):
        self.valor = valor

    def imprimirValor(self):
        print(f"o valor do ingreso é {self.valor}")

class IngressoVip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor*1.5)
    def imprimirValor(self):
        print(f"O ingresso Vip custa {self.valor}")

class Formas():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Triangulo(Formas):
    def __init__(self,base,altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calcularArea(self):
        self.area = (self.base * self.altura)/2
        print(f"sua área é igual : {self.area}")

    def calcularPerimetro(self):
        self.perimetro = self.base * 3
        print(f"seu perímetro é igual : {self.perimetro}")

class Retangulo(Formas):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calcularArea(self):
        self.area = self.base * self.altura
        print(f"sua área é igaul : {self.area}")

    def calcularPerimetro(self):
        self.perimetro = 2*(self.base + self.altura)
        print(f"seu perímetro é igual : {self.perimetro}")
