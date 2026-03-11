from rag.vector_store import collection
from rag.embeddings import get_embeddings

def retrieve(query, top_k=5):
    query_embedding=get_embeddings([query])[0]
    results=collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    return results["documents"][0]