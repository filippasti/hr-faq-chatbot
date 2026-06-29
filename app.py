import streamlit as st
from rag_chain import frage_stellen

# Seitenkonfiguration
st.set_page_config(
    page_title="HR FAQ Chatbot",
    page_icon="💬",
    layout="centered"
)

# Chat-Verlauf initialisieren
if "verlauf" not in st.session_state:
    st.session_state.verlauf = []

# Kopfbereich
st.title("💬 HR FAQ Chatbot")
st.caption("Stelle Fragen zu Urlaub, Homeoffice, Gehalt und mehr – beantwortet auf Basis interner HR-Dokumente.")
st.divider()

# Bisherigen Verlauf anzeigen
for nachricht in st.session_state.verlauf:
    with st.chat_message(nachricht["role"]):
        st.markdown(nachricht["content"])

# Eingabe
if frage := st.chat_input("Stelle eine Frage zu HR-Themen..."):
    # Frage anzeigen + speichern
    st.session_state.verlauf.append({"role": "user", "content": frage})
    with st.chat_message("user"):
        st.markdown(frage)

    # Antwort von Claude (RAG)
    with st.chat_message("assistant"):
        with st.spinner("Suche in den HR-Dokumenten..."):
            antwort = frage_stellen(frage)
            st.markdown(antwort)

    # Antwort speichern
    st.session_state.verlauf.append({"role": "assistant", "content": antwort})