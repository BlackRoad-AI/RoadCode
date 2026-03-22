"""RAG pipeline — retrieval-augmented generation with Qdrant + Ollama."""
from dataclasses import dataclass

@dataclass
class RAGConfig:
    qdrant_url: str = "http://192.168.4.49:6333"
    collection: str = "blackroad-knowledge"
    embed_model: str = "nomic-embed-text"
    llm_model: str = "llama3.2:3b"
    top_k: int = 5

class RAGPipeline:
    def __init__(self, config: RAGConfig | None = None):
        self.config = config or RAGConfig()

    async def query(self, question: str) -> str:
        # 1. Embed the question
        # 2. Search Qdrant for similar chunks
        # 3. Build context from top_k results
        # 4. Generate answer with LLM
        return f"RAG response for: {question}"
