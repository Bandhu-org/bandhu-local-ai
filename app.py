import streamlit as st
from rag_engine import get_context
from ollama_client import query_ollama

st.set_page_config(page_title="Bandhu Local AI", page_icon="🪵")

st.title("Bandhu — Copilote Local")
question = st.text_input("Pose une question à ton IA métier :")

if question:
    with st.spinner("Recherche en cours..."):
        context, sources = get_context(question)
        prompt = f"""Tu es un assistant métier local. 
Voici le contexte extrait des documents internes :\n\n{context}\n\n
Réponds à la question : {question}
        """
        response = query_ollama(prompt)

        st.markdown("### Réponse de l'IA :")
        st.write(response)

        st.markdown("#### Source(s) :")
        for src in sources:
            st.code(src.get("source", "inconnu"))
