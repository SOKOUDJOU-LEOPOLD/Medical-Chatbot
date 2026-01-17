# Medical Chatbot

A Retrieval-Augmented Generation (RAG) medical assistant powered by GPT-4o, LangChain, and Pinecone. Ask medical questions and get accurate, context-aware responses sourced from The Gale Encyclopedia of Medicine.

![Medical Chatbot Demo](chatbot-gif.gif)

## Features

- **RAG-Powered Responses**: Retrieves relevant medical information from a curated knowledge base before generating answers
- **GPT-4o Integration**: Leverages OpenAI's latest model for accurate, concise medical responses
- **Vector Search**: Uses Pinecone for fast similarity search across medical documents
- **Real-time Chat Interface**: Clean, responsive web UI built with Flask and Bootstrap
- **Source-Grounded Answers**: Responses are based on verified medical encyclopedia content

## Tech Stack

| Component | Technology |
|-----------|------------|
| LLM | OpenAI GPT-4o |
| Framework | LangChain |
| Vector Database | Pinecone |
| Embeddings | HuggingFace (all-MiniLM-L6-v2) |
| Backend | Flask |
| Frontend | Bootstrap 4, jQuery |
| Data Source | The Gale Encyclopedia of Medicine (3rd Edition) |

## Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   User Query    │────>│  Flask Server   │────>│   LangChain     │
└─────────────────┘     └─────────────────┘     └────────┬────────┘
                                                         │
                        ┌─────────────────┐              │
                        │    GPT-4o       │<─────────────┤
                        │   (Response)    │              │
                        └─────────────────┘              │
                                                         v
                        ┌─────────────────┐     ┌─────────────────┐
                        │    Pinecone     │<────│   Embeddings    │
                        │  (Vector DB)    │     │  (MiniLM-L6)    │
                        └─────────────────┘     └─────────────────┘
```

## Prerequisites

- Python 3.10+
- [Pinecone](https://www.pinecone.io/) account and API key
- [OpenAI](https://platform.openai.com/) API key

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Medical-Chatbot.git
   cd Medical-Chatbot
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root:
   ```env
   PINECONE_API_KEY=your_pinecone_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

5. **Index the medical data**

   Run this once to process the PDF and store embeddings in Pinecone:
   ```bash
   python store_index.py
   ```

## Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Open your browser**

   Navigate to `http://localhost:8080`

3. **Start chatting**

   Type your medical questions and receive AI-powered responses grounded in medical literature.

## Project Structure

```
Medical-Chatbot/
├── app.py                 # Flask application and chat endpoint
├── store_index.py         # Script to index PDF data into Pinecone
├── requirements.txt       # Python dependencies
├── setup.py               # Package configuration
├── .env                   # Environment variables (not tracked)
├── data/
│   └── *.pdf              # Medical reference documents
├── src/
│   ├── __init__.py
│   ├── helper.py          # PDF loading, text splitting, embeddings
│   └── prompt.py          # System prompt configuration
├── static/
│   └── chat.css           # Chat interface styles
├── templates/
│   └── chat.html          # Chat interface template
└── research/
    └── trials.ipynb       # Experimentation notebook
```

## Configuration

The chatbot behavior can be customized in `src/prompt.py`:

```python
system_prompt = (
    "You are a Medical assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)
```

## Disclaimer

This chatbot is for **educational and informational purposes only**. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a qualified healthcare provider with any questions regarding a medical condition.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Leopold Sokoudjou**
Email: leopoldgatsing@gmail.com

---

<p align="center">
  Built with LangChain and Pinecone
</p>
