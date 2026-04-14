
import faiss, numpy as np
DIM=16
index=faiss.IndexFlatL2(DIM)
store=[]

def embed(t):
    v=np.zeros(DIM)
    for i,c in enumerate(t[:DIM]):
        v[i]=ord(c)%50
    return v.astype('float32')

def add_memory(t):
    index.add(np.array([embed(t)]))
    store.append(t)

def search_memory(q,k=2):
    if not store: return []
    D,I=index.search(np.array([embed(q)]),k)
    return [store[i] for i in I[0] if i<len(store)]
