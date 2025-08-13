
This project's flow is as follows:
1. src.chunker.py reads the pdf of the training document and uses Sentence Aware Splitting to semantically split the document into almost 70 small, overlapping chunks, saving them to the chunks folder
2. src.pipeline.py defines the RAG pipeline as a portable function that will initialise the LLM, retrieve the chunks, embed them, index them, and finally save the resulting vectors locally to a chroma database. The function returns the resulting index as a query engine.
3. app.py contains the streamlit app which will run the function defined in src.pipeline.py using the cache resource decorator to ensure that the computationally expensive function is only run once and persists across reruns of the app.
----------------------------------------------------
Instructions:
1. upload AI Training document to ./data/ as a pdf.
2. Download the LLM Llama-3.2-3B-Instruct-Q4_K_S.gguf from https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF and save the model locally to ./src
3. run src.chunker.py to create the chunks folder (if it does not already exist).
4. Navigate to the project folder using the terminal
5. run the streamlit app by typing following line in the terminal

        streamlit run app.py

----------------------------------------------------
The LLM used in this project is LlaMA-3.2-3B-Instruct.
This model was chosen as it is a lightweight version of the open source LlaMA model, reducing the cost of computation ggg
----------------------------------------------------
The embedding model used is 
all-MiniLM-L6-v2, specialising in short chunks of text, ideal when dealing with the requirement to be specific when reviewing legal documents
----------------------------------------------------
GIF link showing chatbot streaming responses:  https://www.canva.com/design/DAGv8kPDINo/zQKERq586u3hbI-P7ztxhQ/watch?utm_content=DAGv8kPDINo&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hdb923b8434

