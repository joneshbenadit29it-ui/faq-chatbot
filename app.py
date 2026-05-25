import string
import nltk
import streamlit as st
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- STEP 1: DOWNLOAD NLP ESSENTIALS ---
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("punkt_tab")  # Ensuring compatibility with newer NLTK versions

# --- STEP 2: DEFINE THE FAQ DATA ---
faq_data = [
    {
        "question": "What is your return policy?",
        "answer": "You can return any product within 30 days of purchase for a full refund. Items must be in original condition.",
    },
    {
        "question": "How long does shipping take?",
        "answer": "Standard shipping takes 3-5 business days. Express shipping takes 1-2 business days.",
    },
    {
        "question": "Do you ship internationally?",
        "answer": "Yes, we ship to over 50 countries worldwide. Shipping fees and delivery times vary by destination.",
    },
    {
        "question": "How can I track my order?",
        "answer": "Once your order ships, we will email you a tracking link. You can also track it from your account dashboard.",
    },
    {
        "question": "What payment methods do you accept?",
        "answer": "We accept all major credit cards (Visa, MasterCard, Amex), PayPal, and Apple Pay.",
    },
]

# Extract just the questions for our NLP model to analyze
faq_questions = [faq["question"] for faq in faq_data]


# --- STEP 3: TEXT PREPROCESSING FUNCTION ---
def preprocess_text(text):
    # 1. Lowercase the text
    text = text.lower()
    # 2. Tokenize into individual words
    tokens = word_tokenize(text)
    # 3. Remove punctuation and stop words (like 'is', 'the', 'a')
    stop_words = set(stopwords.words("english"))
    cleaned_tokens = [
        word
        for word in tokens
        if word not in stop_words and word not in string.punctuation
    ]
    # Rejoin tokens back into a single clean string
    return " ".join(cleaned_tokens)


# Preprocess all FAQ questions
cleaned_faqs = [preprocess_text(q) for q in faq_questions]


# --- STEP 4: CHATBOT RESPONSE LOGIC ---
def get_bot_response(user_query):
    # Preprocess the user's input
    cleaned_user_query = preprocess_text(user_query)

    # Combine user query with FAQ questions for vectorization
    all_documents = cleaned_faqs + [cleaned_user_query]

    # Convert text to TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_documents)

    # Calculate cosine similarity between the user query (last item) and all FAQs
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])[0]

    # Find the index of the highest similarity score
    best_match_idx = similarity_scores.argmax()
    highest_score = similarity_scores[best_match_idx]

    # Confidence Threshold: If the match is too low, say "I don't understand"
    if highest_score < 0.2:
        return "I'm sorry, I couldn't find a good match for your question. Could you please rephrase it?"

    # Return the corresponding answer
    return faq_data[best_match_idx]["answer"]


# --- STEP 5: STREAMLIT CHAT UI ---
st.set_page_config(page_title="E-Commerce FAQ Bot", page_icon="🤖")
st.title("🤖 FAQ Customer Support Chatbot")
st.write("Ask me anything about shipping, returns, tracking, or payments!")

# Initialize chat history in Streamlit session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! How can I help you today?"}
    ]

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input field
if user_input := st.chat_input("Type your question here..."):
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get bot response using our NLP logic
    bot_reply = get_bot_response(user_input)

    # Display bot response
    with st.chat_message("assistant"):
        st.write(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})