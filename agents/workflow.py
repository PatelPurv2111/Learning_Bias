from ingestion.collect_news import collect_news
from preprocessing.clean_text import clean_text
from rag.vector_store import store_documents
from rag.retriever import retrieve
from llm.gemini_llm import generate_answer
from ml.sentiment import analyze_sentiment


def initialise_database():

    df = collect_news()

    texts = []   # list for storing cleaned articles

    for article in df["content"]:

        cleaned = clean_text(article)

        texts.append(cleaned)   # append to list

    store_documents(texts)


def run_workflow(query):

    docs = retrieve(query, top_k=3)

    context = " ".join(docs)

    answer = generate_answer(query, context)

    sentiment = analyze_sentiment(answer)

    return answer, sentiment, docs