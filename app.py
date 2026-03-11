import gradio as gr
from agents.workflow import initialise_database, run_workflow

# initialize vector database
initialise_database()


def chat(query):

    answer, sentiment, docs = run_workflow(query)

    result = f"""
Answer:
{answer}

Sentiment:
{sentiment}

Sources:
{docs}"""

    return result


interface = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(label="Ask about latest news"),
    outputs=gr.Textbox(label="Analysis"),
    title="AI NEWS ANALYSIS Project"
)

interface.launch()