
import faiss
import numpy as np

dim = 8
index = faiss.IndexFlatL2(dim)

memory_store = []

def embed(text):
    vec = np.zeros(dim)
    for i, c in enumerate(text[:dim]):
        vec[i] = ord(c) % 10
    return vec.astype('float32')

def add_memory(text):
    v = embed(text)
    index.add(np.array([v]))
    memory_store.append(text)

def search_memory(query):
    if len(memory_store) == 0:
        return []
    v = embed(query)
    D, I = index.search(np.array([v]), k=2)
    return [memory_store[i] for i in I[0] if i < len(memory_store)]
