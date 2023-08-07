#upload a file to openAI API
import os
import pandas as pd
import matplotlib.pyplot as plt
from transformers import GPT2TokenizerFast
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain

def answer(query):
    os.environ["OPENAI_API_KEY"] = "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"


    # Advanced method - Split by chunk

    import textract
    doc = textract.process("./ReportTest.csv")

    # Step 2: Save to .txt and reopen (helps prevent issues)
    with open('knowledgebase.txt', 'w') as f:
        f.write(doc.decode('utf-8'))

    with open('knowledgebase.txt', 'r') as f:
        text = f.read()

    # Step 3: Create function to count tokens
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

    def count_tokens(text: str) -> int:
        return len(tokenizer.encode(text))

    # Step 4: Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size = 900,
        chunk_overlap  = 24,
        length_function = count_tokens,
    )

    chunks = text_splitter.create_documents([text])
    type(chunks[0]) 

    # Create a list of token counts
    token_counts = [count_tokens(chunk.page_content) for chunk in chunks]


    # Get embedding model
    embeddings = OpenAIEmbeddings()

    # Create vector database
    #def answer(query):
    db = FAISS.from_documents(chunks, embeddings)

    # Check similarity search is working
    #query = input("Enter Your Query: ")
    docs = db.similarity_search(query)
    docs[0]
    #answer(query)

    # Create QA chain to integrate similarity search with user queries (answer query from knowledge base)
    #def answer(query):
    chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")
    docs = db.similarity_search(query)

    data =chain.run(input_documents=docs, question=query)
    print(data)
    return data

