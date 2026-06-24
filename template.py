from abc import ABC, abstractmethod


class OrdenadaPalavras(ABC):

    def executar(self, palavras):

        self.vazio(palavras)
        palavras.sort(key=self.regra_ordenacao)

    def vazio(self, palavras):
        if not palavras:
            raise ValueError("Lista de palavras vazia.")

    @abstractmethod
    def regra_ordenacao(self, palavra):
        pass


class OrdenadaUltimaLetra(OrdenadaPalavras):

    def regra_ordenacao(self, palavra):
        #Ordena pela última letra e o critério de desempate é o restante da palavra 
        return (palavra[-1].lower(), palavra.lower())


# Teste da última letra 
palavras = [
    "ana",
    "beatriz",
    "mario",
    "anderson",
    "maria",
    "camile",
    "adilson"
]
ordenador = OrdenadaUltimaLetra()
ordenador.executar(palavras)
print(palavras)