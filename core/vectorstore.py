from langchain_chroma import Chroma

from core.embeddings import get_embedding_model

from config.settings import CHROMA_DIR


def get_vectorstore(collection_name):

    embeddings = get_embedding_model()

    vectorstore = Chroma(

        collection_name=collection_name,

        embedding_function=embeddings,

        persist_directory=CHROMA_DIR

    )

    return vectorstore


def store_documents(chunks, collection_name):

    vectorstore = get_vectorstore(collection_name)

    vectorstore.add_documents(chunks)

    return vectorstore


def get_retriever(collection_name):

    vectorstore = get_vectorstore(collection_name)

    retriever = vectorstore.as_retriever(

        search_type="mmr",

        search_kwargs={

            "k": 4,

            "fetch_k": 10,

            "lambda_mult": 0.5

        }

    )

    return retriever