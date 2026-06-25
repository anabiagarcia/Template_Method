from abc import ABC, abstractmethod
from typing import Any

class OrdenaPalavras(ABC):

    def executar(self, palavras: list[str]) -> None:

        self.vazio(palavras)
        palavras.sort(key=self.regra_ordenacao)

    def vazio(self, palavras: list[str]) -> None:
        if not palavras:
            raise ValueError("Lista de palavras vazia.")

    @abstractmethod
    def regra_ordenacao(self, palavra: str) -> Any:
        pass

class OrdenaAlfabetica(OrdenaPalavras):

    def regra_ordenacao(self, palavra: str) -> tuple[str, str]:
        # Ordena em ordem alfabética, em caso de empate, usa a palavra inteira.
        return (palavra[0].lower(), palavra.lower())

class OrdenaUltimaLetra(OrdenaPalavras):

    def regra_ordenacao(self, palavra: str) -> tuple[str, str]:
        # Ordena pela última letra, em caso de empate, usa a palavra inteira.
        return (palavra[-1].lower(), palavra.lower())

class OrdenaTamanho(OrdenaPalavras):

    def regra_ordenacao(self, palavra: str) -> tuple[int, str]:
        # Ordena pelo tamanho da palavra, em caso de empate, usa a palavra inteira.
        return (len(palavra), palavra.lower())


# Exemplos de uso
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
palavras_3 = palavras_1.copy()

print("Ordenada pelo critério: Ordem alfabética")
ordenador = OrdenaAlfabetica()
ordenador.executar(palavras_1)
print(palavras_1)

print("Ordenada pelo critério: Ordem alfabética da última letra")
ordenador = OrdenaUltimaLetra()
ordenador.executar(palavras_2)
print(palavras_2)

print("Ordenada pelo critério: Tamanho do texto")
ordenador = OrdenaTamanho()
ordenador.executar(palavras_3)
print(palavras_3)