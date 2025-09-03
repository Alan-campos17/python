import time
import os
from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI


# Classe do cronômetro
class Cronometro:
    def __init__(self, segundos: int):
        self.segundos = segundos

    def iniciar(self):
        """Roda um cronômetro regressivo no terminal"""
        for s in range(self.segundos, 0, -1):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"⏳ Tempo restante: {s} segundos")
            time.sleep(1)
        print("🚨 Tempo esgotado!")


# Função que o LangChain vai usar
def cronometro_tool(segundos: int):
    c = Cronometro(segundos)
    c.iniciar()
    return "Cronômetro finalizado!"


if __name__ == "__main__":
    # Modelo da OpenAI via LangChain
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    # Registrar ferramenta
    tools = [
        Tool(
            name="Cronometro",
            func=cronometro_tool,
            description="Inicia um cronômetro regressivo em segundos"
        )
    ]

    # Criar agente
    agent = initialize_agent(
        tools,
        llm,
        agent="zero-shot-react-description",
        verbose=True
    )

    # Perguntar ao usuário
    segundos = int(input("Digite o tempo do cronômetro em segundos: "))
    agent.run(f"Inicie o cronômetro por {segundos} segundos")
