"""
Utility functions for the customer support agent.
"""
import logging
from datetime import datetime
from typing import Optional


def setup_logging(log_level: str = "INFO") -> None:
    """
    Set up logging configuration for the application.
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def validate_customer_id(customer_id: Optional[str]) -> bool:
    """
    Validate customer ID format.
    
    Args:
        customer_id: Customer ID to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not customer_id:
        return False
    if len(customer_id.strip()) == 0:
        return False
    return True


def format_timestamp(dt: datetime) -> str:
    """
    Format datetime to readable string.
    
    Args:
        dt: Datetime object to format
        
    Returns:
        Formatted timestamp string
    """
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def sanitize_user_input(text: str, max_length: int = 1000) -> str:
    """
    Sanitize user input to prevent issues.
    
    Args:
        text: Input text to sanitize
        max_length: Maximum allowed length
        
    Returns:
        Sanitized text
    """
    if not text:
        return ""
    text = text.strip()
    if len(text) > max_length:
        text = text[:max_length]
    return text
