# observer.py
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, best_response: str, explanation: str) -> None:
        pass

class ConsoleObserver(Observer):
    def update(self, best_response: str, explanation: str) -> None:
        print("\n=== Atualização da Resposta ===")
        print(f"Melhor resposta escolhida: {best_response}")
        print(f"Explicação: {explanation}")
