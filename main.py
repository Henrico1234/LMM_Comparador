import warnings
import logging

# Suprimir warnings do transformers
warnings.filterwarnings("ignore", category=UserWarning, module="transformers")

# Suprimir logs do transformers (caso seja o caso)
logging.getLogger("transformers").setLevel(logging.ERROR)

# main.py
from factory import ChatGPT, OtherLLM
from commands import QueryLLMsCommand
from strategy import EnhancedEvaluationStrategy
from observer import ConsoleObserver

def main():


    llms = {
        "ChatGPT": ChatGPT(),
        "OutroLLM": OtherLLM()
    }

    # Criando o observador
    console_observer = ConsoleObserver()

    # Criando a estratégia e adicionando o observador
    strategy = EnhancedEvaluationStrategy()
    strategy.add_observer(console_observer)

    while True:
        print("\n=== Menu ===")
        print("1. Fazer uma pergunta")
        print("2. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            user_prompt = input("\nDigite sua pergunta: ")

            command = QueryLLMsCommand(llms, user_prompt)
            responses = command.execute()

            print("\nRespostas dos LLMs:")
            for name, response in responses.items():
                print(f"{name}: {response}")

            # Avaliando as respostas e notificando o observador
            result = strategy.evaluate(responses, user_prompt)


        elif choice == "2":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
