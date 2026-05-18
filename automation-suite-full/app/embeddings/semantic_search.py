import numpy as np

from app.embeddings.encoder import encode


def search(store, query: str, k: int = 5) -> list[int]:
    q = np.array([encode([query])[0]], dtype="float32")
    _, idx = store.index.search(q, k)
    return [store.ids[i] for i in idx[0] if i >= 0 and i < len(store.ids)]
