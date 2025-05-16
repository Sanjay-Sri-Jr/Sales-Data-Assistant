from flask import Flask,render_template,request
import streamlit as st
import pandas as pd
from langchain_ollama import OllamaLLM
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import re
app=Flask(__name__)
df=pd.read_excel("C:/Users/sanja/Downloads/supermarket_sales_data.xlsx")
llm = OllamaLLM(model="llama3.2")
agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=True,
    allow_dangerous_code=True,
    handle_parsing_errors=True)
@app.route('/')
def hello_world():
    return render_template('index.HTML')
@app.route('/home',methods=['POST'])
def h():
      
    user_query= request.form.get('user_query')
    if user_query:
        try:
            response = agent.run(user_query)
            return render_template('index.HTML', r=response)
        except Exception as e:
            return render_template('index.HTML', r=e)
    else:
        return render_template('index.HTML', r="Please enter a question.")
if __name__ == "__main__":
    app.run(debug=True)
