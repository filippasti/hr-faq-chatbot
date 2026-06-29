# HR FAQ Chatbot (RAG)

Ein KI-Chatbot, der Fragen zu internen HR-Themen beantwortet – nicht aus allgemeinem 
Wissen, sondern auf Basis echter HR-Dokumente. Das Projekt nutzt **RAG 
(Retrieval-Augmented Generation)**, um Mitarbeiterfragen wie "Wie viele Urlaubstage 
habe ich?" oder "Wie viel Homeoffice ist erlaubt?" präzise und dokumentenbasiert 
zu beantworten.

## Wie es funktioniert

Das System arbeitet in vier Schritten:

1. **Einlesen & Chunking** – HR-Dokumente werden geladen und in kleine Textabschnitte zerteilt
2. **Embeddings** – jeder Abschnitt wird mit sentence-transformers in einen Vektor umgewandelt
3. **Retrieval** – zu einer Frage werden die passendsten Abschnitte aus der FAISS-Vektordatenbank gesucht
4. **Generation** – Claude formuliert die Antwort ausschließlich auf Basis der gefundenen Abschnitte

Dadurch antwortet der Bot faktenbasiert und gibt ehrlich zu, wenn eine Information 
nicht in den Dokumenten steht – statt zu halluzinieren.

## Features

- Beantwortet HR-Fragen zu Urlaub, Homeoffice, Gehalt, Krankmeldung, Elternzeit, Weiterbildung u.v.m.
- Dokumentenbasierte Antworten (kein Halluzinieren)
- Chat-Oberfläche mit Gesprächsverlauf (Streamlit)
- Lokale, kostenlose Embeddings (kein zusätzlicher API-Key nötig)

## Projektstruktur

| Datei | Funktion |
|-------|----------|
| `data_loader.py` | Lädt HR-Dokumente und zerteilt sie in Chunks |
| `vektordb.py` | Erstellt die FAISS-Vektordatenbank aus den Chunks |
| `rag_chain.py` | Retrieval + Generation: findet passende Abschnitte und lässt Claude antworten |
| `app.py` | Streamlit-Weboberfläche (Chat) |

## Was ich dabei gelernt habe

- Wie RAG technisch funktioniert: Chunking, Embeddings, Vektorsuche, kontextbasierte Generierung
- Eine Vektordatenbank (FAISS) aufbauen, speichern und abfragen
- Text mit sentence-transformers in Vektoren umwandeln (lokal, ohne API)
- Ein Projekt sauber modular in mehrere Dateien aufteilen (Separation of Concerns)
- Prompts so gestalten, dass das LLM nur auf Basis bereitgestellter Dokumente antwortet

## Tech Stack

- Python 3.13
- LangChain (Document Loading, Text Splitting, FAISS-Integration)
- FAISS (Vektordatenbank)
- sentence-transformers (Embeddings, Modell: all-MiniLM-L6-v2)
- Anthropic Claude API (claude-sonnet-4-6)
- Streamlit (Weboberfläche)

## Setup

1. Repository klonen
2. Virtuelle Umgebung erstellen: `python3 -m venv venv`
3. Aktivieren: `source venv/bin/activate`
4. Abhängigkeiten installieren: `pip install -r requirements.txt`
5. `.env` Datei erstellen mit: `ANTHROPIC_API_KEY=dein-key`
6. Vektordatenbank erstellen: `python vektordb.py`
7. App starten: `streamlit run app.py`

## Hinweis

Dies ist ein Lernprojekt, entstanden im Rahmen meiner Vorbereitung auf ein Praktikum 
im Bereich HR-IT. Es demonstriert den praktischen Einsatz von RAG zur Automatisierung 
von HR-Auskünften. Die verwendeten HR-Dokumente sind fiktiv.