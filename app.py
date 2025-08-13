import streamlit as st
import time
from src.pipeline import main


st.title("AI Assistant")

st.subheader("currently using Llama-3.2-3B-Instruct-Q4_K_S.gguf and referencing almost 70 documents!")

if "messages" not in st.session_state:
    st.session_state.messages = []

@st.cache_resource
def init_query_engine():    
    return main()

query_engine = init_query_engine()

def gen_response(prompt):
    response = query_engine.query(prompt)

    st.sidebar.title("Source text")

    for i, node in enumerate(response.source_nodes):
        with st.sidebar.expander(f"Chunk {i+1}"):
            st.markdown(node.node.text)

    for char in str(response):
        yield char
        time.sleep(0.02)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append(
            {
                "role": "user", 
                "content": prompt
            }
         )
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.write_stream(gen_response(prompt))
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )