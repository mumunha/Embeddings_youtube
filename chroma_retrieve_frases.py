import chromadb


chroma_client = chromadb.Client()
chroma_client = chromadb.PersistentClient(path="db")
collection = chroma_client.get_or_create_collection(name="english")


    
results = collection.query(
    query_texts="crypto", 
    n_results=2
)
print(results)
