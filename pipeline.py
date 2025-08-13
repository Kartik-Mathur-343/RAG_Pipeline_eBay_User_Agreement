from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.core import StorageContext
from llama_index.core import Settings
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
from llama_index.core.text_splitter import SentenceSplitter
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import chromadb
import os

def main():
    parent = os.path.dirname(os.path.dirname(__file__))

    Settings.llm = LlamaCPP(
        model_path = os.path.join(os.path.dirname(__file__), "Llama-3.2-3B-Instruct-Q4_K_S.gguf"),
        temperature = 0.1
    )

    # Settings.text_splitter = SentenceSplitter(
    #     chunk_size = 512,
    #     chunk_overlap = 128
    # )

    Settings.embed_model = HuggingFaceEmbedding(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    document = SimpleDirectoryReader(
        input_dir=os.path.join(parent, "chunks")
    ).load_data()

    db = chromadb.PersistentClient(path="./chroma_db")

    chroma_collection = db.get_or_create_collection("quickstart")

    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)


    if os.path.exists("./chroma_db"):
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        index = VectorStoreIndex.from_documents(
            document, storage_context=storage_context
        )
    else:
        index = VectorStoreIndex.from_vector_store(
        vector_store,
    )
    query_engine = index.as_query_engine()
    return query_engine

