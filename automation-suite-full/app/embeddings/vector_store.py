import faiss
import numpy as np
from app.core.config import settings


class VectorStore:
    def __init__(self, dim: int = 384):
        self.index = faiss.IndexFlatL2(dim)
        self.ids: list[int] = []

    def add(self, record_id: int, vector):
        arr = np.array([vector], dtype="float32")
        self.index.add(arr)
        self.ids.append(record_id)

    def save(self):
        faiss.write_index(self.index, settings.vector_index_path)
        np.save(settings.vector_meta_path, np.array(self.ids, dtype=np.int64))
