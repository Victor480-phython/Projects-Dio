# Desafio Bicicletaria
# Criei uma classe e defini os objetos dela, inicializei os atributos e características

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): # isso daqui é um construtor, o self é uma referencia explicita para o objeto, quer dizer que é a instancia do objeto que foi passado
        # Atributos da instância
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor # esses self.item são atributos da classe
        self.marcha = 1
# Métodos são funções dentro das classes, a única diferença é que como primeiro argumento por convenção passa self
    # Métodos da classe
    def buzinar(self):
        print("plim plim")

    def parar(self):
        print("parando a bicicleta")
        print("bicicleta parada")

    def correr(self):
        print("bicicleta entrando em movimento")
        print("bicicleta correndo")
    
# Para conseguir olhar no print tudo oque está no Bicicleta2 por exemplo precisa fazer assim:
   #  def __str__(self):
   #     return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"   # Aqui se trata da mesma coisa de cima mas de maneira mais automatizada
    
    # passei um parametro ali no lugar de self, mas não muda nada
    def trocar_marcha(self, nro_marcha):
        print("Trocando Marcha")

    def _trocar_marcha():
        if nro_marcha > self.marcha:
            print("Marcha Trocada")
        else:
            print("Não Foi possível Trocar a marcha")


# Para instanciar a bicicleta agora
Bicicleta1 = Bicicleta("Vermelha", "Monark", 2015, 3500)
Bicicleta1.buzinar()
Bicicleta1.correr()
Bicicleta1.parar()
print(Bicicleta1.cor, Bicicleta1.modelo, Bicicleta1.ano, Bicicleta1.valor)

Bicicleta2 = Bicicleta("Verde", "caloi", 1999, 550)
Bicicleta.buzinar(Bicicleta2)
Bicicleta2.buzinar() # Essa daqui e a da linha de cima são a mesma coisa 


