import chromadb
from rag.embeddings import get_embeddings

client = chromadb.Client()
collection = client.create_collection("news")


def store_documents(texts):

    embeddings = get_embeddings(texts)

    for i, text in enumerate(texts):

        collection.add(
            ids=[str(i)],
            documents=[text],
            embeddings=[embeddings[i]]
        )