import streamlit as st
import os
from groq import Groq
from knowledge_base import KnowledgeBase
from chat_handler import ChatHandler
from utils import initialize_session_state, display_chat_history

# Configure page
st.set_page_config(
    page_title="Aarogya Vatika - Customer Support",
    page_icon="🪷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
initialize_session_state()

# Initialize Groq client
@st.cache_resource
def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY", "gsk_default_key")
    return Groq(api_key=api_key)

# Initialize knowledge base
@st.cache_resource
def get_knowledge_base():
    return KnowledgeBase()

# Initialize chat handler
@st.cache_resource
def get_chat_handler():
    groq_client = get_groq_client()
    knowledge_base = get_knowledge_base()
    return ChatHandler(groq_client, knowledge_base)

def main():
    # Header
    st.title("🪷 Aarogya Vatika Customer Support")
    st.markdown("*Your Ayurvedic Wellness Companion*")
    
    # Sidebar with store information
    with st.sidebar:
        st.header("🌿 About Aarogya Vatika")
        st.markdown("""
        **Ayurvedic Wellness Redefined**
        
        • 45+ years of traditional healing wisdom
        • 50+ Pure Ayurvedic Products
        • Expert Doctor Guidance
        • 7,200+ Members Community
        
        **Contact Us:**
        📞 +91-9910474566
        📧 aumyanaturals@gmail.com
        📍 D-9, Sector-3, Noida, U.P. – 201301
        """)
        
        st.header("🛍️ Quick Links")
        st.markdown("""
        • [Shop Products](https://www.aarogyavatika.com/collections/all)
        • [Women's Health](https://www.aarogyavatika.com/collections/women-s-health)
        • [Gut Health](https://www.aarogyavatika.com/collections/gut-health)
        • [Immunity Boosters](https://www.aarogyavatika.com/collections/herbs-suppliments)
        • [Consultation](https://www.aarogyavatika.com/pages/consultation)
        """)
        
        if st.button("Clear Chat History"):
            st.session_state.chat_history = []
            st.rerun()
    
    # Main chat interface
    st.header("💬 Chat with our AI Assistant")
    
    # Display chat history
    display_chat_history()
    
    # Chat input
    chat_handler = get_chat_handler()
    
    # Sample questions
    st.subheader("🤔 Common Questions")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("What products do you offer?"):
            handle_sample_question("What products do you offer?", chat_handler)
    
    with col2:
        if st.button("Shipping and delivery info?"):
            handle_sample_question("What are your shipping and delivery policies?", chat_handler)
    
    with col3:
        if st.button("Return policy?"):
            handle_sample_question("What is your return and refund policy?", chat_handler)
    
    # Chat input
    user_input = st.chat_input("Ask me anything about Aarogya Vatika...")
    
    if user_input:
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Generate response
        with st.spinner("Thinking..."):
            response = chat_handler.generate_response(user_input, st.session_state.chat_history)
        
        # Add assistant response to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        
        # Rerun to update the display
        st.rerun()

def handle_sample_question(question, chat_handler):
    """Handle sample question clicks"""
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": question})
    
    # Generate response
    with st.spinner("Thinking..."):
        response = chat_handler.generate_response(question, st.session_state.chat_history)
    
    # Add assistant response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": response})
    
    # Rerun to update the display
    st.rerun()

if __name__ == "__main__":
    main()
