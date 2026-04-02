from __future__ import annotations

from pathlib import Path

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import DATA_DIR, settings


def load_documents(data_dir: Path = DATA_DIR):
    docs = []
    for path in sorted(data_dir.glob("*.txt")):
        loader = TextLoader(str(path), encoding="utf-8")
        docs.extend(loader.load())
    return docs


def build_retriever(data_dir: Path = DATA_DIR):
    docs = load_documents(data_dir)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=100,
    )
    splits = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings(
        model=settings.embedding_model,
        api_key=settings.openai_api_key,
    )

    vectorstore = FAISS.from_documents(splits, embeddings)
    return vectorstore.as_retriever(search_kwargs={"k": 3})


def answer_question(question: str, retriever, history: str = "") -> str:
    llm = ChatOpenAI(
        model=settings.openai_model,
        temperature=settings.temperature,
        api_key=settings.openai_api_key,
    )

    docs = retriever.get_relevant_documents(question)
    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
Tu es un assistant utile.

Tu peux utiliser :
1. l'historique de conversation
2. les documents récupérés

Si la réponse est dans l'historique, utilise-la.
Sinon, utilise les documents.
Si l'information n'existe ni dans l'historique ni dans les documents, dis clairement que tu ne sais pas.

Historique :
{history}

Documents :
{context}

Question :
{question}

Réponse :
"""

    response = llm.invoke(prompt)
    return response.content