from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def lade_dokumente():
    # 1. Alle .txt Dateien aus dem Ordner laden
    loader = DirectoryLoader(
        "dokumente",
        glob="*.txt",
        loader_cls=TextLoader
    )
    dokumente = loader.load()

    # 2. In Chunks zerteilen
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(dokumente)

    return chunks

