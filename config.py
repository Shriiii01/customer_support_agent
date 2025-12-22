"""
Configuration management for the customer support agent.

This module provides centralized configuration management with support for
environment variables and sensible defaults.
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


def get_temperature() -> float:
    """
    Get temperature setting for OpenAI API from environment variable or default.
    
    Returns:
        Temperature value (0.0 to 2.0)
    """
    return float(os.getenv("OPENAI_TEMPERATURE", "0.7"))


def get_max_tokens() -> int:
    """
    Get max tokens setting for OpenAI API from environment variable or default.
    
    Returns:
        Maximum number of tokens
    """
    return int(os.getenv("OPENAI_MAX_TOKENS", "500"))
