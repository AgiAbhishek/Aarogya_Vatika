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
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        st.error("GROQ_API_KEY environment variable is not set. Please add your API key to continue.")
        st.stop()
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
    # Header with professional styling
    st.markdown("""
    <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); border-radius: 10px; margin-bottom: 30px;">
        <h1 style="color: #2E8B57; font-size: 2.5em; margin: 0;">🪷 Aarogya Vatika Customer Support</h1>
        <p style="color: #666; font-size: 1.2em; margin: 10px 0 0 0; font-style: italic;">Your Ayurvedic Wellness Companion</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar with store information
    with st.sidebar:
        # Logo section
        try:
            st.image("attached_assets/logo_1752783306177.jpeg", width=200)
        except:
            try:
                st.image("attached_assets/logo_1752783780690.jpeg", width=200)
            except:
                st.header("🪷 Aarogya Vatika")
        
        st.markdown("---")
        
        st.header("🌿 About Aarogya Vatika")
        st.markdown("""
        **Ayurvedic Wellness Redefined**
        
        - 45+ years of traditional healing wisdom
        - 50+ Pure Ayurvedic Products  
        - Expert Doctor Guidance
        - 7,200+ Members Community
        """)
        
        st.markdown("---")
        
        st.header("📞 Contact Information")
        st.markdown("""
        **Phone:** +91-9910474566  
        **Email:** aumyanaturals@gmail.com  
        **Address:** D-9, Sector-3, Noida, U.P. – 201301  
        **Website:** [www.aarogyavatika.com](https://www.aarogyavatika.com)
        """)
        
        st.markdown("---")
        
        st.header("🛍️ Quick Links")
        st.markdown("""
        - [Shop Products](https://www.aarogyavatika.com/collections/all)
        - [Women's Health](https://www.aarogyavatika.com/collections/women-s-health)
        - [Gut Health](https://www.aarogyavatika.com/collections/gut-health)
        - [Immunity Boosters](https://www.aarogyavatika.com/collections/herbs-suppliments)
        - [Consultation](https://www.aarogyavatika.com/pages/consultation)
        """)
        
        st.markdown("---")
        
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()
    
    # Main chat interface
    st.markdown("""
    <div style="background: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #2E8B57; margin-bottom: 20px;">
        <h3 style="color: #2E8B57; margin: 0 0 10px 0;">💬 Chat with our AI Assistant</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Display chat history
    display_chat_history()
    
    # Chat input
    chat_handler = get_chat_handler()
    
    # Chat input with professional styling
    st.markdown("""
    <div style="margin-top: 30px; margin-bottom: 15px;">
        <hr style="border: 1px solid #e0e0e0; margin: 20px 0;">
    </div>
    """, unsafe_allow_html=True)
    
    # Show common questions only if there's no chat history
    if not st.session_state.chat_history:
        # Sample questions with improved styling - positioned before chat input
        st.markdown("""
        <div style="background: #f0f8ff; padding: 15px; border-radius: 8px; margin: 20px 0;">
            <h4 style="color: #2E8B57; margin: 0 0 15px 0;">🤔 Common Questions</h4>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🛍️ What products do you offer?", use_container_width=True):
                handle_sample_question("What products do you offer?", chat_handler)
        
        with col2:
            if st.button("🚚 Shipping and delivery info?", use_container_width=True):
                handle_sample_question("What are your shipping and delivery policies?", chat_handler)
        
        with col3:
            if st.button("🔄 Return policy?", use_container_width=True):
                handle_sample_question("What is your return and refund policy?", chat_handler)
    
    user_input = st.chat_input("💬 Ask me anything about Aarogya Vatika...")
    
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
