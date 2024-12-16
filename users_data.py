# users_data.py
import streamlit as st

users = st.secrets["users"]

import streamlit as st

# Ajustando a forma de acessar os usuários
def get_users():
    # Carregar os dados dos usuários a partir dos segredos
    users = st.secrets["users"]

    # Verificar como os dados estão estruturados (opcional, para debug)
    print(users)  # Verifique isso no log para entender a estrutura exata

    user_dict = {}

    # Iterar sobre cada usuário e seus dados no TOML
    for user_key in users:
        # A lista de tabelas de usuários dentro de cada chave, geralmente com um único item
        user_info = users[user_key][0]  # Acessar o primeiro (e único) item da lista

        user_dict[user_key] = {
            "password": user_info["password"],
            "permissions": user_info["permissions"]
        }

    return user_dict



def save_user(username, password, permissions):
    users[username] = {"password": password, "permissions": permissions}


