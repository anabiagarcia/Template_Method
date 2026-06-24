from abc import ABC, abstractmethod
from typing import Any

class OrdenadaPalavras(ABC):

    def executar(self, palavras: list[str]) -> None:

        self.vazio(palavras)
        palavras.sort(key=self.regra_ordenacao)

    def vazio(self, palavras: list[str]) -> None:
        if not palavras:
            raise ValueError("Lista de palavras vazia.")

    @abstractmethod
    def regra_ordenacao(self, palavra: str) -> Any:
        pass


class OrdenadaUltimaLetra(OrdenadaPalavras):

    def regra_ordenacao(self, palavra:str) -> tuple[str, str]:
        #Ordena pela última letra e o critério de desempate é o restante da palavra 
        return (palavra[-1].lower(), palavra.lower())

class OrdenadaTamanho(OrdenadaPalavras):
    
    def regra_ordenacao(self, palavra: str) -> tuple[int, str]:
        return (len(palavra), palavra.lower())


# Teste da última letra 
palavras_1 = [
    "ana",
    "beatriz",
    "mario",
    "anderson",
    "maria",
    "camile",
    "adilson"
]

palavras_2 = palavras_1.copy()

print("Ordenada pelo critério: Ordem alfabética da última letra")
ordenador = OrdenadaUltimaLetra()
ordenador.executar(palavras_1)
print(palavras_1)

print("Ordenada pelo critério: Tamanho do texto")
ordenador = OrdenadaTamanho()
ordenador.executar(palavras_2)
print(palavras_2)
