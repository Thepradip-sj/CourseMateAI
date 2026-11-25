from langchain_google_genai import ChatGoogleGenerativeAI

from core.vectorstore import get_retriever

from prompts.rag_prompt import RAG_PROMPT

from config.settings import LLM_MODEL


def get_llm():

    llm = ChatGoogleGenerativeAI(

        model=LLM_MODEL,

        temperature=0

    )

    return llm


def ask_question(question, collection_name):

    # Step 1: Get Retriever

    retriever = get_retriever(collection_name)

    # Step 2: Retrieve Relevant Documents

    relevant_docs = retriever.invoke(question)

    # Step 3: Prepare Context

    context = "\n\n".join(

        [doc.page_content for doc in relevant_docs]

    )

    # Step 4: Prepare Prompt

    final_prompt = RAG_PROMPT.invoke({

        "context": context,

        "question": question

    })

    # Step 5: Get LLM

    llm = get_llm()

    # Step 6: Generate Answer

    response = llm.invoke(final_prompt)

    # Step 7: Extract Sources

    sources = []

    for doc in relevant_docs:

        sources.append({

            "source": doc.metadata.get("source", "Unknown"),

            "page": doc.metadata.get("page", "Unknown")

        })

    return response.content, sources