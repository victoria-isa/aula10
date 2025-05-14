from random import triangular

from biblioteca import  *
gato = Gato("Lila","marrom")
gato.miar()

cachorro = Cachorro("Romeu", "branco")
cachorro.latir()

coelho = Coelho("Bartolomeu","preto")
coelho.chia()

vaca = Vaca("Laura", "Azul")
vaca.mugir()

cinema = Ingresso(20)
cinema.imprimirValor()

cinemaVip = IngressoVip(20)
cinemaVip.imprimirValor()

triangulo = Triangulo(20,30)
triangulo.calcularArea()
triangulo.calcularPerimetro()

retangulo = Retangulo(30,15)
retangulo.calcularArea()
retangulo.calcularPerimetro()


