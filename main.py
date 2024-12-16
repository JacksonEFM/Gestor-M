import streamlit as st
from users_data import get_users
from config import config_page
from logistica import logistica_page
from pos_vendas import pos_vendas_page
from comercial import comercial_page
from pre_vendas import pre_vendas_page


# Inicializar dados dos usuários
users = get_users()  # Agora `get_users()` retorna um dicionário com os usuários

# Garantir inicialização de variáveis na sessão
def initialize_session():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if "username" not in st.session_state:
        st.session_state["username"] = ""
    if "permissions" not in st.session_state:
        st.session_state["permissions"] = []
    if "keep_logged" not in st.session_state:
        st.session_state["keep_logged"] = False

initialize_session()

def main():
    st.set_page_config(page_title="Moderna Tecnologia",  layout="wide")


    # Função para exibir a página inicial de login
    def login():
        st.title("Login")
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        keep_logged = st.checkbox("Manter conectado")
        login_button = st.button("Login")

        if login_button:
            if username in users and users[username]["password"] == password:
                st.session_state["authenticated"] = True
                st.session_state["username"] = username
                st.session_state["permissions"] = users[username]["permissions"]
                st.session_state["keep_logged"] = keep_logged
                st.rerun()
            else:
                st.error("Usuário ou senha inválidos!")

    # Lógica de autenticação
    if not st.session_state["authenticated"]:
        if st.session_state["keep_logged"] and st.session_state["username"]:
            # Restaurar sessão se "keep_logged" estiver ativo
            st.session_state["authenticated"] = True
        else:
            login()
    else:
        # Sistema de navegação com base em permissões
        st.sidebar.title(f"Bem-vindo, {st.session_state['username']}!")
        pages = {
            "Config": config_page,
            "Logistica": logistica_page,
            "Pós Vendas": pos_vendas_page,
            "Comercial": comercial_page,
            "Pré Vendas": pre_vendas_page
        }

        # Exibir apenas as páginas permitidas ao usuário
        available_pages = {
            name: func for name, func in pages.items() if name in st.session_state["permissions"]
        }

        selected_page = st.sidebar.radio("Navegar", list(available_pages.keys()))

        if st.sidebar.button("Sair"):
            st.session_state["authenticated"] = False
            st.session_state["username"] = ""
            st.session_state["permissions"] = []
            st.session_state["keep_logged"] = False
            st.rerun()

        # Verificar se a página selecionada está disponível
        if selected_page in available_pages:
            available_pages[selected_page]()
        else:
            st.error("A página selecionada não está disponível.")

if __name__ == "__main__":
    main()
