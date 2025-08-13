from llama_index.core.text_splitter import SentenceSplitter
from pypdf import PdfReader
import os

reader = PdfReader("./data/AI Training Document.pdf")

text = ''

for page in reader.pages:
    pg = page.extract_text()
    text += pg

splitter = SentenceSplitter(chunk_size=256, chunk_overlap=32)

chunks = splitter.split_text(text)

os.makedirs("chunks", exist_ok=True)

for i, chunk in enumerate(chunks):
    with open(f"chunks/chunk_{i+1}.txt", "w", encoding="utf-8") as f:
        f.write(chunk)
