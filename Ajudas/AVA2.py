''' PARADIGMA ORIENTADO A OBJETOS '''
## Interface
class Poligono:
    ## Atributos da Classe
    elementos = ['Lados', 'Vértices',
                 'Ângulos Internos',
                 'Ângulos Externos',
                 'Diagonais', 'Convexidade']
    ## Métodos Abstratos
    def numeroLados(self)->int:
        pass
    def numeroVertices(self)->int:
        pass
    def angulosInternos(self)->int:
        pass
    def angulosExternos(self)->int:
        pass
    def numeroDiagonais(self)->int:
        pass
    def ehConvexo(self)->bool:
        pass

## Classe
class Retangulo(Poligono):
    ## Atributos da Classe
    contador = 0
    __lados = 4             ## 
    __vertices = 4          ## Atributos
    __angulos = 360         ## Encapsulados
    __diagonais = 2         ##
    __convexidade = True    ##

    ## Método Construtor
    def __init__(self, altura:int, largura:int):
        if (altura and largura > 0):
            ## Atributos do Objeto
            '''
            setAltura(self, altura)
            setLargura(largura)
            '''
            self.__altura = altura
            self.__largura = largura
            Retangulo.contador += 1

    '''
    ## Métodos Setter
    def __setAltura(self, altura:int):
        ## Encapsulamento
        self.__altura = altura

    def setLargura(self, largura:int):
        ## Encapsulamento
        self.__largura = largura
    '''
    ## Métodos Getter
    def getAltura(self)->int:
        return self.__altura

    def getLargura(self)->int:
        return self.__largura

    ## Métodos da Interface
    def numeroLados(self)->int:
        return self.__lados
    
    def numeroVertices(self)->int:
        return self.__vertices
    
    def angulosInternos(self)->int:
        return self.__angulos
    
    def angulosExternos(self)->int:
        return self.__angulos
    
    def numeroDiagonais(self)->int:
        return self.__diagonais
    
    def ehConvexo(self)->bool:
        return self.__convexidade

    ## Métodos básicos
    def area(self)->int:
        return self.__altura * self.__largura

    def perimetro(self)->int:
        return 2*(self.__altura + self.__largura)
    
## Herança
class Quadrado(Retangulo):
    ## Atributos da Classe
    contador = 0
    ## Polimorfismo de Sobrescrita
    def __init__(self, lado:int):
        Retangulo.__init__(self, lado, lado)
        self.__lado = lado
        Quadrado.contador += 1
        
    ## Método Getter
    def getLado(self)->int:
        return  self.__lado

## Aplicação
def main():
    print("A P L I C A Ç Ã O\n")

    ## Listas das Instâncias de Retangulo e Quadrado
    listaDeRetangulos = []
    listaDeQuadrados = []

    ## Inicialização de 10 Retângulos e 10 Quadrados
    for i in range(1, 11):
        listaDeRetangulos.append(Retangulo(i+2*i, i+i))
        listaDeQuadrados.append(Quadrado(i))

    ## Imprime cada Retângulo com seus atributos
    print("Retângulos:\n")
    for i in range(1, 11):
        print("ret{:d} com altura {:d}, ".format(i, listaDeRetangulos[i-1].getAltura()) +
              "largura {:d}, ".format(listaDeRetangulos[i-1].getLargura()) +
              "área {:d} e perímetro {:d}".format(listaDeRetangulos[i-1].area(),
                                                  listaDeRetangulos[i-1].perimetro()))

    ## Imprime cada Quadrado com seus atributos
    print("\n\nQuadrados:\n")
    for i in range(1, 11):
        print("qua{:d} com lado {:d}, ".format(i, listaDeQuadrados[i-1].getLado()) +
              "área {:d} e perímetro {:d}".format(listaDeQuadrados[i-1].area(), 
                                                  listaDeQuadrados[i-1].perimetro()))

    ## Lista de Elementos do Retângulo
    elementosRet = []
    elementosRet.append(listaDeRetangulos[0].numeroLados())
    elementosRet.append(listaDeRetangulos[0].numeroVertices())
    elementosRet.append(listaDeRetangulos[0].angulosInternos())
    elementosRet.append(listaDeRetangulos[0].angulosExternos())
    elementosRet.append(listaDeRetangulos[0].numeroDiagonais())
    elementosRet.append(listaDeRetangulos[0].ehConvexo())

    ## Imprime o elemento seguido de seu valor específico para Retângulos
    print("\n\nOs elementos do Polígono Retângulo são:zn")
    for i in range(0, 6):
        print(Poligono.elementos[i] + ': ' + str(elementosRet[i]))

    
## Testes
alt1 = 2
larg1 = 3
lado1 = 4
r1 = Retangulo(alt1, larg1)
q1 = Quadrado(lado1)

## Testa o Método getAltura()
def testaGetAltura():
    print("Teste 1: getAltura()\n" +
          "A altura de r1 ({:d}) deve ser ".format(r1.getAltura()) +
          "igual a {:d}.".format(alt1))
    if r1.getAltura() == alt1:
        print("PASSOU!!\n\n")
    else:
        print("FALHOU!!\n\n")

## Testa o Método getLargura()
def testaGetLargura():
    print("Teste 2: getLargura()\n"+
          "A altura de r1 ({:d}) deve ser ".format(r1.getLargura())  +
          "igual a {:d}.".format(larg1))
    if r1.getLargura() == larg1:
        print("PASSOU!!\n\n")
    else:
        print("FALHOU!!\n\n")

## Testa o Método area()
def testaArea():
    print("Teste 3: area()\n" +
          "A área de r1 ({:d}) deve ser igual ao ".format(r1.area()) +
          "produto de {:d} com {:d}, ".format(alt1, larg1) +
          "que é {:d}.".format(alt1*larg1))
    if r1.area() == alt1*larg1:
        print("PASSOU!!\n\n")
    else:
        print("FALHOU!!\n\n")

## Testa o Método perimetro()
def testaPerimetro():
    print("Teste 4: perimetro()\n" +
          "O perímetro de r1 ({:d}) deve ser igual à ".format(r1.perimetro()) +
          "soma dos lados de r1, ou seja, {:d}.".format(2*(alt1+larg1)))
    if r1.perimetro() == 2*(alt1+larg1):
        print("PASSOU!!\n\n")
    else:
        print("FALHOU!!\n\n")

## Testa a Herança Simples
def testaHerancaSimples():
    print("Teste 5: Herança Simples\n" +
          "O método isinstance() com os parâmetros:\n" +
          "r1(objeto) e Poligono(interface) " +
          "precisa indicar 1 como booleano para True.")
    ## Testa se Retangulo é subclasse de Polígono
    if isinstance(r1, Poligono):
        print("PASSOU!!\n\n")
    else:
        print("FALHOU!!\n\n")

## Testa a Herança Múltipla
def testaHerancaMultipla():
    print("Teste 6: Herança Múltipla\n" +
          "O método isinstance() com os parâmetros:\n" +
          "r1(objeto), Poligono(interface) e r1(objeto), Retangulo(classe), \n" +
          "precisa indicar 1 como booleano para True.")
    ## Testa se a classe quadrado é subclasse de Poligono e Retangulo
    if isinstance(q1, Poligono) and (q1, Retangulo):
        print("PASSOU!!\n\n")
    else:
        print("FALHOU!!\n\n")

## Testa a Mutabilidade do Atributo da Classe
def testaAtributoClasse():
    print("Teste 7: Mutabilidade do Atributo da Classe\n" +
          "A classe Retangulo tem " +
          "{:d} instâncias ativas. \n" .format(Retangulo.contador) +
          "Se criarmos mais uma instância, o contador precisará " +
          "ser incrementado de 1.")
    aux = Retangulo.contador
    r2 = Retangulo(larg1, alt1)
    if Retangulo.contador == aux+1:
        print("PASSOU!!\n\n")
    else:
        print("FALHOU!!\n\n")

## Chamada para todos os Testes
def testes():
    print("\n\nT E S T E S\n")
    print("Retângulo r1\naltura: {:d}\n".format(alt1) +
          "largura: {:d}\n".format(larg1))
    print("Quadrado q1\nlado: {:d}\n".format(lado1))
    testaGetAltura()
    testaGetLargura()
    testaArea()
    testaPerimetro()
    testaHerancaSimples()
    testaHerancaMultipla()
    testaAtributoClasse()

main()
testes()
