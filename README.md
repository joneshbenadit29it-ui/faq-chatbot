# 🤖 Smart FAQ Customer Support Chatbot

An interactive, AI-powered FAQ chatbot designed to handle customer support queries instantly. Built using **Python**, **NLP (Natural Language Processing)**, and **Streamlit**, this intelligent assistant processes user inputs, evaluates structural similarity against a predefined FAQ database, and provides context-aware answers in real-time.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-Green?style=for-the-badge)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

---

## 🚀 Key Features

* **Advanced Text Preprocessing:** Uses **NLTK** for automated lowercasing, tokenization, and intelligent removal of stop words/punctuation.
* **Vector Space Modeling:** Converts text queries into multi-dimensional coordinates using **TF-IDF Vectorization**.
* **Intent Matching:** Leverages **Cosine Similarity** to compute semantic proximity between customer inputs and the FAQ knowledge base.
* **Fallback Confidence Safeguard:** Includes a strict threshold mechanism. If a user's question scores below `0.2` confidence, the bot gracefully asks for clarification instead of guessing randomly.
* **Dynamic Chat UI:** Features a modern, sleek, web-based chat interface provided by **Streamlit**.

---

## 🛠️ Tech Stack & Core Libraries

* **Language:** Python 3
* **NLP Framework:** NLTK (Natural Language Toolkit)
* **Machine Learning Math:** Scikit-Learn (TF-IDF & Cosine Similarity)
* **User Interface:** Streamlit (Web-based interactive chat elements)

---

## 📦 Project Structure

```text
faq-chatbot/
│
├── app.py             # Main application logic & Streamlit UI code
├── .gitignore         # Prevents heavy metadata & local cache files from uploading
└── README.md          # Comprehensive documentation of the project
⚙️ Complete Step-by-Step Explanation & Setup
Here is exactly how the project is built and executed from scratch.

📋 Phase 1: Environment Setup
First, the workspace is prepared inside VS Code. We install the essential scientific and web libraries required for handling matrix mathematical operations and rendering a web viewport:

Bash
pip install nltk scikit-learn streamlit
🧠 Phase 2: Natural Language Preprocessing (NLP)
Computers do not read sentences like humans; they analyze structural statistics. The bot cleans raw user text through a pipeline before analyzing it:

Lowercasing: Converts all letters to lowercase to ensure uniformity (e.g., "Shipping" becomes "shipping").

Tokenization: Breaks strings down into individual word units called tokens.

Stop Words & Punctuation Filtering: Eliminates structural "noise" words like is, standard, the, a, do, you and symbols like ?, !, . so that only semantic high-value keywords remain.

📐 Phase 3: Mathematical Vectorization & Matching
Once clean text tokens are extracted, the system runs advanced matching calculations:

TF-IDF Vectorization: The words are converted into numerical frequency coordinates inside a multidimensional vector space model.

Cosine Similarity: The backend measures the exact angular proximity between the user's vector and the stored dataset matrices. The closest mathematical match is selected as the correct intent.

🛠️ Installation & Local Run
Get this project running on your local machine in just a few steps:

1. Clone the Repository
Bash
git clone [https://github.com/joneshbenadit29it-ui/faq-chatbot.git](https://github.com/joneshbenadit29it-ui/faq-chatbot.git)
cd faq-chatbot
2. Launch the Application
Start your Streamlit local web server:

Bash
streamlit run app.py
Your browser will automatically open up to http://localhost:8501 to display your brand-new interactive AI interface!

💡 System Workflow Architecture
Code snippet
graph TD
    A[User Inputs Query] --> B[NLP Preprocessing: Tokenize & Strip Stopwords]
    B --> C[TF-IDF Vectorization]
    C --> D[Calculate Cosine Similarity against FAQs]
    D --> E{Is Similarity > 0.2?}
    E -- Yes --> F[Display Closest FAQ Answer]
    E -- No --> G[Trigger Fallback: Request Clarification]
📬 Contact / Contributions
Contributions, issues, and feature requests are welcome! Feel free to fork this project and add your own modifications.

Developed with ❤️ using Python and Streamlit.
