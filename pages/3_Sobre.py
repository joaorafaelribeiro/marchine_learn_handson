import streamlit as st

st.markdown('''
# Equipe:
            
* Alexandre Brasil
* Davi Lourenço
* João Rafael
* Nilmar Pereira
            
------
            ''')
st.markdown('''
        ## Sobre o Modelo:
   
        A base de dados **Employee** (*pycaret.datasets.get_data('employee')*) é uma versão fictícia de dados de recursos humanos e é frequentemente usado para fins educacionais e de demonstração. 
        Ele contém informações sobre funcionários, como salário, avaliações de desempenho, satisfação no trabalho, entre outros. 
        O modelo utilizado foi o **RandonForest** implementado na aulo do dia 16/11/2023 e pode ser acessado no link abaixo:
        
        https://colab.research.google.com/drive/1Y2XrDhGZoaHw1fB5Pl4WhQpVA14Myc6S?authuser=1
        
        ------
        ''')

st.markdown('''
        ## Sobre o Chat:
   
        Um assistente pessoal com instruções específicas para um problema de sua escolha. 
        Inclua opções ao usuário para controlar a criatividade da resposta, o tamanho da resposta e o estilo de escrita da resposta. 
        Adicione mais, ou outras, opções como widgets de interação com usuário se desejar.
        No uso do assistente, inclua um escape de moderação, isto é, caso o input do usuário violar as regras (você define), 
        uma resposta automática deve ser dada, ao invés de acionar a API de chat.
        Faça com o que o programa tenha uma opção para 'finalizar a conversa' e quando isso acontecer, 
        um conjunto de dados (pandas mesmo) deve ser alimentado com as seguintes informações: dia e horário da conversa, 
        tokens utilizados na conversa, custo estimado da conversa, histórico do dialogo.
        Além disso, gere um arquivo em PDF com o histórico da conversa e permita ao usuário baixar esse arquivo.

        
        
        ''')