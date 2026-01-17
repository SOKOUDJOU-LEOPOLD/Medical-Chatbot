from dotenv import load_dotenv
import os
from src.helper import load_pdf_file, filter_to_minimal_docs, text_split, download_hugging_face_embeddings
from pinecone import Pinecone
from pinecone import ServerlessSpec 
from langchain_pinecone import PineconeVectorStore

load_dotenv()


PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
OPENAI_API_KEY=os.environ.get('OPENAI_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# load pdf containing data
extracted_data=load_pdf_file(data='data/')
# filter data
filter_data = filter_to_minimal_docs(extracted_data)
# divide into chunks
text_chunks=text_split(filter_data)
# call the embeddding that will convert chunk to vertor 
embeddings = download_hugging_face_embeddings()

# connect to pinecone using key
pinecone_api_key = PINECONE_API_KEY
pc = Pinecone(api_key=pinecone_api_key)


# specify the index that will contain our vector data
index_name = "medical-chatbot"  # change if desired

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )

# get the index
index = pc.Index(index_name)


docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings, 
)