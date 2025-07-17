import streamlit as st
from typing import List, Dict

def initialize_session_state():
    """Initialize session state variables"""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    if 'user_info' not in st.session_state:
        st.session_state.user_info = {}

def display_chat_history():
    """Display chat history in the main interface"""
    if st.session_state.chat_history:
        # Create a container for chat messages
        chat_container = st.container()
        
        with chat_container:
            for i, message in enumerate(st.session_state.chat_history):
                if message["role"] == "user":
                    with st.chat_message("user", avatar="👤"):
                        st.write(message["content"])
                elif message["role"] == "assistant":
                    with st.chat_message("assistant", avatar="🪷"):
                        st.write(message["content"])
    else:
        # Welcome message with professional styling
        with st.chat_message("assistant", avatar="🪷"):
            st.markdown("""
            <div style="background: linear-gradient(135deg, #e8f5e8 0%, #f0f8ff 100%); padding: 20px; border-radius: 10px; border: 1px solid #2E8B57;">
                <h3 style="color: #2E8B57; margin: 0 0 15px 0;">🌿 Welcome to Aarogya Vatika!</h3>
                <p style="color: #555; margin: 10px 0;">I'm your AI assistant, here to help you with:</p>
                <ul style="color: #666; padding-left: 20px; margin: 15px 0;">
                    <li>🛍️ Product information and recommendations</li>
                    <li>🚚 Shipping and delivery details</li>
                    <li>🔄 Return and refund policies</li>
                    <li>🌱 Ayurvedic wellness guidance</li>
                    <li>ℹ️ General store information</li>
                </ul>
                <p style="color: #2E8B57; font-weight: bold; margin: 15px 0 0 0;">How can I assist you today?</p>
            </div>
            """, unsafe_allow_html=True)

def format_product_info(products: List[Dict]) -> str:
    """Format product information for display"""
    if not products:
        return "No products found."
    
    formatted_products = []
    for product in products[:5]:  # Limit to 5 products
        formatted_products.append(
            f"**{product['name']}**\n"
            f"Vendor: {product['vendor']}\n"
            f"Price: {product['price']}\n"
        )
    
    return "\n".join(formatted_products)

def get_wellness_recommendations(category: str) -> str:
    """Get wellness recommendations based on category"""
    recommendations = {
        "women's health": """
        🌸 **Women's Health Recommendations:**
        - Ashoka Capsules for menstrual health
        - Herbal supplements for hormonal balance
        - Consultation with our Ayurvedic doctors
        """,
        "gut health": """
        🌱 **Gut Health Recommendations:**
        - Digestive herbs and supplements
        - Probiotic-friendly Ayurvedic formulations
        - Personalized diet guidance
        """,
        "immunity": """
        🛡️ **Immunity Boosting Products:**
        - Ashwagandha capsules
        - Tulsi-based formulations
        - Immune-supporting herbal blends
        """,
        "diabetes": """
        🍃 **Diabetes Management:**
        - Bitter melon supplements
        - Cinnamon-based formulations
        - Blood sugar supporting herbs
        """
    }
    
    return recommendations.get(category.lower(), "Please contact our experts for personalized recommendations.")

def validate_user_input(user_input: str) -> bool:
    """Validate user input"""
    if not user_input or len(user_input.strip()) == 0:
        return False
    
    if len(user_input) > 500:
        return False
    
    return True

def get_contact_info() -> str:
    """Get formatted contact information"""
    return """
    📞 **Phone:** +91-9910474566
    📧 **Email:** aumyanaturals@gmail.com
    📍 **Address:** D-9, Sector-3, Noida, U.P. – 201301
    🌐 **Website:** www.aarogyavatika.com
    """

def format_shipping_info() -> str:
    """Format shipping information"""
    return """
    🚚 **Shipping Information:**
    • Processing Time: 1-2 days
    • Delivery Time: 3-10 days (depending on location)
    • Coverage: Ships across India
    • Free Shipping: Orders above ₹699
    • Shipping Charges: ₹79 (below ₹699), ₹50 COD charge
    • Tracking: Available via SMS/Email
    """

def format_return_policy() -> str:
    """Format return policy information"""
    return """
    🔄 **Return Policy:**
    
    Due to the perishable nature of Ayurvedic products, we generally don't accept returns except for:
    
    ✅ **Accepted Returns:**
    • Products damaged during shipping (report within 48 hours)
    • Incorrect items shipped
    
    💰 **Refund Process:**
    • Refunds processed to original payment method
    • Processing time: 7-10 business days
    
    📞 **Need Help?** Contact us at +91-9910474566
    """
