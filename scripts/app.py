import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

if "GEMINI_API_KEY" not in st.secrets:
    load_dotenv()
    secret_key_gemini = os.getenv("GEMINI_API_KEY")
else:
    secret_key_gemini = st.secrets["GEMINI_API_KEY"]  
    
if "OPENAI_API_KEY" not in st.secrets:
    load_dotenv()
    secret_key_openai = os.getenv("OPENAI_API_KEY")
else:
    secret_key_openai = st.secrets["OPENAI_API_KEY"]  

def iaOpenAi(prompt, **kwargs):
  client = OpenAI(api_key=secret_key_openai)
  max_tokens = kwargs.get('max_tokens', 500)
  temperature = kwargs.get('temperature', 0)
  
  resposta = client.chat.completions.create(
      model='gpt-4o',
      messages=[
          {'role':'user','content':prompt}
      ],
      n=1,
      max_tokens=max_tokens,
      temperature=temperature,
  )
  
  return resposta.choices[0].message.content

def iaGemini(prompt, **kwargs):
  client = OpenAI(api_key=secret_key_gemini, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
  max_tokens = kwargs.get('max_tokens', 500)
  temperature = kwargs.get('temperature', 0)
  
  resposta = client.chat.completions.create(
      model='gemini-1.5-flash',
      messages=[
          {'role':'user','content':prompt}
      ],
      n=1,
      max_tokens=max_tokens,
      temperature=temperature,
  )
  
  return resposta.choices[0].message.content


@st.dialog("Aqui está a sua receita! 🎉")
def response(json):
    st.subheader(json["titulo"])
    
    for ingrediente in json["ingredientes"]:
        st.markdown(ingrediente)
    
    st.markdown("**Modo de preparo:**")
    st.markdown(json["modo_de_preparo"])
    
    if st.button("Voltar"):
        st.rerun()

@st.dialog("Tivemos um problema! 😢")
def error(json):
    st.error(json["mensagem"])
    
    if st.button("Voltar"):
        st.rerun()

st.title("Olá! Eu sou um robô que gera receitas. 🫡")

ia = st.selectbox("Você tem preferência por uma IA?\n", ["OpenAI", "Gemini"])

if not ia:
  ia = "OpenAI"

ingredientes = st.text_input("Me dê os ingrediente que você tem na sua casa, por favor.\n")
tipo = st.selectbox("Que tipo de refeição é essa ?", ["Lanche", "Jantar", "Almoço", "Sobremesa", "Café da manhã", "Petisco", "Você decide"])

if not tipo:
  tipo = "Você decide"

culinaria = st.text_input("Você tem preferência por culinárias de alguma região, diga qual ?\n")

if not culinaria:
  culinaria = "brasileira"

tempo = st.selectbox("Você tem preferência por tempo de preparo ?", ["Rápido", "Médio", "Demorado", "Você decide"])

if not tempo:
  tempo = "Você decide"

complexidade = st.selectbox("Você tem preferência por complexidade de preparo ?", ["Fácil", "Médio", "Difícil", "Ta na mão de Deus"])

if not complexidade:
  complexidade = "Ta na mão de Deus"

porcoes = st.number_input("Quantas pessoas você quer servir ?\n", min_value = 1, value=1, step=1, format="%d")
restricoes = st.text_input("Você tem alguma restrição alimentar ? (Ex: Vegetariano, Vegano, Intolerante a lactose)\n")

if not restricoes:
  restricoes = "nenhuma"

if st.button("Gerar Receita"):  
  prompt = f"""Eu tenho os seguintes ingredientes: {ingredientes}. 
    Gostaria de uma receita de {tipo}, com a culinária de {culinaria} com tempo de preparo {tempo}, 
    complexidade {complexidade}, para {porcoes} pessoas, com as restrições alimentares de {restricoes}.

    Mas preciso que siga as seguintes regras:
        1 - Use apenas ingredientes que eu tenho em casa.
        2 - Siga a risca meus gostos e preferências.
        3 - Respeite meu tempo e complexidade de preparo.
        4 - Não use ingredientes que eu não gosto.
        5 - Não use ingredientes que eu não tenho em casa.
        6 - Siga as regras de restrição alimentar.
        
    Eu pretendo enviar essa receita para uma API, preciso que me de uma resposta como JSON seguindo a estrutura
        
        "titulo": "Nome da receita",
        "ingredientes": ["Lista de ingredientes"],
        "modo_de_preparo": "Modo de preparo",
        
    Atenção: Preciso que use exatamente o mesmo formato, com os mesmo nomes das keys.
    Atenção: Não esqueça de seguir as regras que eu te passei. """
    
  if tipo not in ["Você decide"]:
    prompt += f""" Atenção: Caso o o tipo da refeição não seja lanche nem almoço, janta, petisco, sobremesa, café da manhã ou coisas similiares ou até mesmo se eu não estiver pedindo pars você decidir, por favor, me retorne um json de erro e não gera a receita, o JSON de erro deve ter a seguinte estrutura.
    por favor, me retorne um json de erro e não gera a receita, o JSON de erro deve ter a seguinte estrutura. """  
  else: 
    prompt += f""" Você pode decidir o tipo da refeição"""  
  
  prompt += f"""
    Atenção: Verifique os dados como os ingredientes para que os seja algo viável e realmente possíveis para um alimento.
    exemplo: Se ele colocar algo como cimento, seja inválido e entre na mensagem de erro
    Atenção: Caso os igredientes não estejam de acordo com as restrições alimentares, seja inválido e entre na mensagem de erro
    Exemplo: Se ele colocar carne em uma restrição vegetariana, seja inválido e entre na mensagem de erro, ou coloque
    peixe e a restrição ser vegana ou vegetariana, seja inválido e entre na mensagem de erro
        
        "erro": true,
        "mensagem": "A entrada fornecida violou os requsitos do sistema" - Aqui você pode colocar a mensagem que achar melhor e quais entradas foram violadas.
        
    regra eu quero somente o json de resposta, não quero a receita em texto, por favor, me retorne apenas o JSON.
    e sem esse colocar na sua resposta o valor:
    ```json
        conteudo json
    ```
    Quero uma atenção especial na formatação do JSON, por favor, siga a risca o que eu pedi.
    Quero que não tenha esses caracteres de ``` e nem a palavra json, quero somente o conteúdo do JSON, sem a formatação."""
        
  with st.spinner("Aguarde um momento, estou gerando a receita para você. 🚀"):
    if ia == "OpenAI":
      resposta = iaOpenAi(prompt, max_tokens=500, temperature=0.5)
      dados = json.loads(resposta)
    else:
      resposta = iaGemini(prompt, max_tokens=500, temperature=0.5)  
      resposta = resposta.replace("```json", "").replace("```", "").strip()
      print(resposta)
      dados = json.loads(resposta)
        
    if dados.get("erro"):
      error(dados)
    else:
      response(dados)