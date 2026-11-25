from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config.settings import EMBEDDING_MODEL


def get_embedding_model():

    embeddings = GoogleGenerativeAIEmbeddings(

        model=EMBEDDING_MODEL

    )

    return embeddings