import os
from langchain import OpenAI
from langchain.chains import SimpleChain
from langchain.prompts import PromptTemplate
from langchain.memory import SimpleMemory

# Configurar a chave da API do OpenAI
os.environ["OPENAI_API_KEY"] = "sua-chave-api-aqui"

# Configurar o modelo de linguagem da OpenAI
model = OpenAI(model_name="gpt-4")

# Defina um template de prompt
prompt_template = PromptTemplate(
    input_variables=["input_text"],
    template="Você é um assistente que responde perguntas. Pergunta: {input_text}"
)

# Criar memória simples
memory = SimpleMemory()

# Definir uma cadeia simples usando o modelo, o prompt e a memória
chain = SimpleChain(
    prompt_template=prompt_template,
    llm=model,
    memory=memory,
    verbose=True
)

# Testar o fluxo de trabalho com uma pergunta
response = chain.run(input_text="Qual é a capital da França?")
print(response)
