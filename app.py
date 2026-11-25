import streamlit as st

import os

from core.document_processor import (
    load_pdf,
    split_documents
)

from core.vectorstore import store_documents

from core.rag_pipeline import ask_question

from utils.helpers import (
    create_collection_name,
    get_file_hash,
    safe_filename
)

from config.settings import UPLOAD_DIR


# -------------------------------
# PAGE CONFIGURATION
# -------------------------------

st.set_page_config(

    page_title="CourseMate AI",

    page_icon="📚",

    layout="wide"

)


st.title("📚 CourseMate AI")

st.write(

    "Your personal AI-powered learning assistant. "

    "Upload your study materials and start learning!"

)


st.divider()


# -------------------------------
# SESSION STATE
# -------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


if "collection_name" not in st.session_state:

    st.session_state.collection_name = None


if "indexed_hashes" not in st.session_state:

    st.session_state.indexed_hashes = set()


# -------------------------------
# SIDEBAR
# -------------------------------

st.sidebar.title("Course Settings")


course_name = st.sidebar.text_input(

    "Enter Course Name",

    placeholder="e.g. Machine Learning"

)


uploaded_files = st.sidebar.file_uploader(

    "Upload Study Materials",

    type=["pdf"],

    accept_multiple_files=True

)


if course_name:

    collection_name = create_collection_name(course_name)

    st.session_state.collection_name = collection_name


# -------------------------------
# DOCUMENT PROCESSING
# -------------------------------

if st.sidebar.button("Process Documents"):

    if not course_name:

        st.sidebar.error("Please enter a course name.")

    elif not uploaded_files:

        st.sidebar.error("Please upload PDF files.")

    else:

        collection_name = create_collection_name(course_name)

        course_dir = os.path.join(

            UPLOAD_DIR,

            collection_name

        )

        os.makedirs(course_dir, exist_ok=True)

        processed_count = 0

        with st.spinner("Processing your study materials..."):

            for uploaded_file in uploaded_files:

                file_bytes = uploaded_file.getvalue()

                file_hash = get_file_hash(file_bytes)

                if file_hash in st.session_state.indexed_hashes:

                    continue

                filename = safe_filename(uploaded_file.name)

                file_path = os.path.join(

                    course_dir,

                    filename

                )

                with open(file_path, "wb") as f:

                    f.write(file_bytes)


                # Load PDF

                documents = load_pdf(file_path)


                # Add metadata

                for doc in documents:

                    doc.metadata["source"] = filename


                # Split documents

                chunks = split_documents(documents)


                # Store embeddings

                if chunks:

                    store_documents(

                        chunks,

                        collection_name

                    )

                    processed_count += 1

                    st.session_state.indexed_hashes.add(file_hash)


        st.session_state.collection_name = collection_name

        st.session_state.messages = []

        st.success(

            f"Successfully processed {processed_count} new document(s)!"

        )


# -------------------------------
# CHAT INTERFACE
# -------------------------------

st.subheader("💬 Ask CourseMate AI")


# Display previous messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


query = st.chat_input(

    "Ask anything from your course materials..."

)


if query:

    if not st.session_state.collection_name:

        st.warning("Please process your study materials first.")

    else:

        # Display user message

        st.session_state.messages.append({

            "role": "user",

            "content": query

        })

        with st.chat_message("user"):

            st.markdown(query)


        # Generate AI response

        with st.chat_message("assistant"):

            with st.spinner("CourseMate is thinking..."):

                try:

                    answer, sources = ask_question(

                        query,

                        st.session_state.collection_name

                    )

                    st.markdown(answer)


                    # Display sources

                    with st.expander("📖 View Sources"):

                        for source in sources:

                            st.write(

                                f"**Document:** {source['source']}"

                            )

                            page = source["page"]

                            st.write(

                                f"**Page:** {page + 1 if isinstance(page, int) else page}"

                            )

                            st.divider()


                    st.session_state.messages.append({

                        "role": "assistant",

                        "content": answer

                    })


                except Exception as e:

                    st.error(f"Something went wrong: {e}")