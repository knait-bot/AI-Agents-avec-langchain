from dotenv import load_dotenv
import re
import streamlit as st

from src.rag import answer_question, build_retriever

load_dotenv()

st.set_page_config(page_title="Chatbot RAG", page_icon="🤖", layout="wide")
st.title("🤖 Chatbot RAG avec LangChain")
st.write("Pose une question sur les documents `.txt` présents dans le dossier `data/`.")

try:
    retriever = build_retriever()
except Exception as e:
    st.error(f"Erreur lors de la construction du retriever : {e}")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Bonjour 👋 Pose-moi une question sur les documents du dossier data."
        }
    ]

if "user_memory" not in st.session_state:
    st.session_state.user_memory = {}

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Écris ta question ici...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    lower_prompt = prompt.lower()

    name_match = re.search(r"je m'appelle\s+([a-zA-ZÀ-ÿ'-]+)", prompt, re.IGNORECASE)
    age_match = re.search(r"j'ai\s+(\d+)\s+ans", prompt, re.IGNORECASE)

    if name_match:
        st.session_state.user_memory["name"] = name_match.group(1)

    if age_match:
        st.session_state.user_memory["age"] = age_match.group(1)

    with st.chat_message("user"):
        st.markdown(prompt)

    history = "\n".join(
        [
            f"{'Utilisateur' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}"
            for msg in st.session_state.messages
        ]
    )

    if ("âge" in lower_prompt or "age" in lower_prompt) and "age" in st.session_state.user_memory:
        response = f"Tu as {st.session_state.user_memory['age']} ans."
    elif ("nom" in lower_prompt or "m'appelle" in lower_prompt or "name" in lower_prompt) and "name" in st.session_state.user_memory:
        response = f"Tu t'appelles {st.session_state.user_memory['name']}."
    else:
        with st.chat_message("assistant"):
            with st.spinner("Je cherche la réponse..."):
                try:
                    response = answer_question(prompt, retriever, history)
                except Exception as e:
                    response = f"Erreur : {e}"
                st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.stop()

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})