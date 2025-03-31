# Global configuration for file paths, model checkpoints, etc.
class Config:
    DOC_PATH = "data/raw/"
    EMBEDDINGS_PATH = "data/processed/embeddings.pkl"
    LAYOUT_MODEL = "microsoft/layoutlmv3-base"
    RAG_MODEL = "google/flan-t5-base"
    DEVICE = "cuda"  # or "cpu"
