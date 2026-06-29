from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import anthropic
from dotenv import load_dotenv
import os

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def lade_datenbank():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )
    return db

def frage_stellen(frage):
    # 1. Datenbank laden
    db = lade_datenbank()

    # 2. RETRIEVAL: die 3 passendsten Chunks zur Frage finden
    treffer = db.similarity_search(frage, k=3)

    # 3. Die gefundenen Texte zu einem Kontext zusammenfügen
    kontext = "\n\n".join([chunk.page_content for chunk in treffer])

    # 4. GENERATION: Claude antwortet basierend auf dem Kontext
    prompt = f"""Du bist ein HR-Assistent. Beantworte die Frage des Mitarbeiters 
ausschließlich auf Basis der folgenden HR-Dokumente. Wenn die Information nicht 
in den Dokumenten steht, sage das ehrlich.

HR-DOKUMENTE:
{kontext}

FRAGE: {frage}"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text


if __name__ == "__main__":
    antwort = frage_stellen("Wie viele Urlaubstage habe ich?")
    print(antwort)