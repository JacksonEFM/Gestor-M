import streamlit as st
from users_data import get_users, save_user
# admin.py

def admin_page():
    st.title("Administração de Permissões")

    users = get_users()
    usernames = list(users.keys())

    selected_user = st.selectbox("Selecione um usuário", usernames)

    if selected_user:
        st.subheader(f"Permissões de {selected_user}")

        permission_options = ["Config", "Logistica", "Pós Vendas", "Comercial", "Pré Vendas", "Admin"]
        current_permissions = users[selected_user].get("permissions", [])

        # Garantir que os valores padrão estejam na lista de opções
        filtered_permissions = [perm for perm in current_permissions if perm in permission_options]

        selected_permissions = st.multiselect(
            "Permissões disponíveis",
            options=permission_options,
            default=filtered_permissions
        )

        if st.button("Salvar Permissões"):
            # Preservar a senha atual
            password = users[selected_user]["password"]
            # Salvar as permissões do usuário
            save_user(selected_user, password, selected_permissions)
            st.success("Permissões atualizadas com sucesso!")
