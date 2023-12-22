import streamlit as st
import pandas as pd
from pycaret.datasets import get_data
from pycaret.regression import load_model, predict_model

dados = get_data('employee')

st.set_page_config(page_title='Modelo de predição para RH', page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)


st.markdown('''
        # Modelo
        
        ### Prever se o colaborador esta disposto a deixar o quatro de funcionários da empresa.
            
            ''')

c1, c2 = st.columns(2, gap='large')

with c1:
    satisfaction_level = st.slider(
        label='Nível de Satisfação',
        max_value=1.,
        min_value=0.,
        value=.63,
        step=.01)
    last_evaluation = st.slider(
        label='Avaliações de Desempenho',
        value=.71,
        min_value=.36,
        max_value=1.,
        step=.01)
    number_project = st.slider(
        label='Quatidade de Projetos',
        value=3,
        min_value=2,
        max_value=7,
        step=1)
    time_spend_company = st.slider(
        label='Tempo de Empresa (Anos)',
        value=3,
        min_value=2,
        max_value=10,
        step=1)
with c2:
    average_montly_hours = st.number_input(
        label='Horas Trabalhadas (Média Mensal)',
        value=200,
        min_value=96,
        max_value=310,
        step=1)
    department = st.selectbox(label='Departamento', options=dados['department'].unique())
    salary = st.selectbox(label='Salário', options=dados['salary'].unique())
    Work_accident = st.checkbox(label='Acidente de Trabalho')
    promotion_last_5years = st.checkbox(label='Promovido (Últimos 5 Anos)')

#b1, b2 = st.columns(2, gap='large')

#with b1:
confirm = st.button(label='Gerar Previsão',type='primary',use_container_width=True)
#with b2:
#    reset = st.button(label='Limpar',type='secondary',use_container_width=True)

if confirm:
    modelo = load_model('randoforest-employee')
    previsao = predict_model(modelo, data = pd.DataFrame({
        'satisfaction_level' : [satisfaction_level],
        'last_evaluation' : [last_evaluation],
        'number_project' : [number_project],
        'time_spend_company' : [time_spend_company],
        'average_montly_hours': [average_montly_hours],
        'department': [department],
        'salary': [salary],
        'Work_accident': [Work_accident],
        'promotion_last_5years': [promotion_last_5years]
    }))
    valor = round(previsao.loc[0,'prediction_label'], 2)
    st.markdown(f''' 
        --------------------
        ### Resultado: 
        O modelo previu que o funcionário **{'DEIXARÁ a' if valor else 'PERMANECERÁ na'}** Empresa.
    ''')