# AI Customer Support Agent with Memory

An intelligent customer support agent built with Streamlit, OpenAI GPT-4, and Mem0 for persistent memory across conversations.

## Features

- 🤖 **AI-Powered Support**: Uses OpenAI's GPT-4 for intelligent customer support responses
- 🧠 **Persistent Memory**: Leverages Mem0 with Qdrant for long-term memory storage
- 👤 **User-Specific Context**: Maintains separate conversation history per customer ID
- 📊 **Synthetic Data Generation**: Generate realistic customer profiles for testing
- 🔍 **Memory Search**: Search and retrieve relevant past interactions

## Requirements

- Python 3.8+
- Qdrant vector database (running on localhost:6333)
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Shriiii01/customer_support_agent.git
cd customer_support_agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start Qdrant (using Docker):
```bash
docker run -p 6333:6333 qdrant/qdrant
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run main.py
```

2. Enter your OpenAI API key in the app
3. Enter a customer ID to start chatting
4. Use the sidebar to generate synthetic data or view memory information

## Configuration

You can configure the application using environment variables:

- `QDRANT_HOST`: Qdrant host (default: localhost)
- `QDRANT_PORT`: Qdrant port (default: 6333)
- `OPENAI_MODEL`: OpenAI model to use (default: gpt-4)
- `OPENAI_TEMPERATURE`: Temperature for response generation (default: 0.7)
- `OPENAI_MAX_TOKENS`: Maximum tokens for responses (default: 500)
- `OPENAI_API_KEY`: Your OpenAI API key (can also be entered in the app)

## Project Structure

```
customer_support_agent/
├── main.py           # Main Streamlit application
├── config.py         # Configuration management
├── utils.py          # Utility functions
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details
