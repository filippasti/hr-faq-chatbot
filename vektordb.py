from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from data_loader import lade_dokumente

def erstelle_datenbank():
    # 1. Chunks holen
    chunks = lade_dokumente()

    # 2. Embedding-Modell laden (wandelt Text in Vektoren)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # 3. FAISS-Datenbank aus den Chunks bauen
    db = FAISS.from_documents(chunks, embeddings)

    # 4. Datenbank auf der Festplatte speichern
    db.save_local("faiss_index")
    print("Datenbank erfolgreich erstellt und gespeichert!")

if __name__ == "__main__":
    erstelle_datenbank()