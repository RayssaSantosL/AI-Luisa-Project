# AI-Luisa-Project

---

## Documentação: Criação de uma IA com LangChain

### Introdução

Este documento descreve o processo de criação de uma Inteligência Artificial (IA) utilizando a biblioteca LangChain e o modelo GPT-4 da OpenAI. O exemplo fornecido implementa um assistente que responde perguntas baseando-se nas entradas fornecidas pelo usuário.

### Requisitos

- Python 3.7 ou superior
- Bibliotecas Python:
  - `langchain`
  - `openai`

### Passos para Configuração e Execução

#### 1. Instalação das Dependências

Para começar, instale as bibliotecas necessárias usando pip:

```bash
pip install langchain openai
```

#### 2. Configuração da Chave da API do OpenAI

Você precisará de uma chave da API do OpenAI para acessar o modelo GPT-4. Configure a chave da API como uma variável de ambiente ou diretamente no código:

```python
import os
os.environ["OPENAI_API_KEY"] = "sua-chave-api-aqui"
```

#### 3. Importação e Configuração do LangChain

Importe as bibliotecas necessárias e configure o modelo de linguagem da OpenAI:

```python
from langchain import OpenAI
from langchain.chains import SimpleChain
from langchain.prompts import PromptTemplate
from langchain.memory import SimpleMemory

# Configurar o modelo de linguagem da OpenAI
model = OpenAI(model_name="gpt-4")
```

#### 4. Criação de um Fluxo de Trabalho Simples

Crie um template de prompt e defina uma cadeia simples usando o modelo configurado:

```python
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
```

#### 5. Teste do Fluxo de Trabalho

Teste o fluxo de trabalho com uma pergunta para verificar se tudo está configurado corretamente:

```python
# Testar o fluxo de trabalho com uma pergunta
response = chain.run(input_text="Qual é a capital da França?")
print(response)
```

### Exemplo Completo

Abaixo está o código completo integrando todos os passos mencionados:

```python
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
```

### Personalização e Expansão

- **Customização do Prompt**: O `PromptTemplate` pode ser ajustado para melhor atender às suas necessidades específicas.
- **Funcionalidades Adicionais**: Integre a aplicação com outras APIs, bancos de dados, ou adicione manipulação de memória mais complexa.
- **Desenvolvimento e Deploy**: Transforme o script em uma aplicação web ou API usando frameworks como Flask ou FastAPI.

### Conclusão

Esta documentação fornece uma visão geral de como configurar e executar uma IA básica usando LangChain e GPT-4 da OpenAI. Para casos de uso mais avançados, considere explorar mais funcionalidades da biblioteca LangChain e ajustar o fluxo de trabalho conforme necessário.

---
