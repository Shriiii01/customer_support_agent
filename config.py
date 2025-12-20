"""
Configuration management for the customer support agent.
"""
import os
from typing import Dict, Any


def get_qdrant_config() -> Dict[str, Any]:
    """
    Get Qdrant configuration from environment variables or defaults.
    
    Returns:
        Dictionary containing Qdrant configuration
    """
    return {
        "vector_store": {
            "provider": "qdrant",
            "config": {
                "host": os.getenv("QDRANT_HOST", "localhost"),
                "port": int(os.getenv("QDRANT_PORT", "6333")),
            }
        },
    }


def get_openai_model() -> str:
    """
    Get OpenAI model name from environment variable or default.
    
    Returns:
        Model name string
    """
    return os.getenv("OPENAI_MODEL", "gpt-4")
