from groq import Groq
from knowledge_base import KnowledgeBase
from typing import List, Dict, Any
import json

class ChatHandler:
    def __init__(self, groq_client: Groq, knowledge_base: KnowledgeBase):
        self.groq_client = groq_client
        self.knowledge_base = knowledge_base
        self.system_prompt = self._create_system_prompt()
    
    def _create_system_prompt(self) -> str:
        """Create a comprehensive system prompt for the chatbot"""
        return """You are a helpful customer service assistant for Aarogya Vatika, an Ayurvedic wellness platform. You have access to comprehensive information about the company, products, services, and policies.

Key Information about Aarogya Vatika:
- 45+ years of traditional healing wisdom
- 50+ Pure Ayurvedic Products
- Expert Doctor Guidance available
- 7,200+ Members, 15,000+ Readers community
- Focus on personalized healing, sustainable products, and evidence-backed practices

Your Role:
1. Answer customer questions about products, services, shipping, returns, and general store information
2. Provide helpful, accurate, and friendly responses
3. Guide customers to relevant products or services
4. Maintain a professional yet warm tone that reflects the Ayurvedic wellness philosophy
5. If you don't have specific information, politely direct customers to contact customer service

Guidelines:
- Be concise but comprehensive
- Use emojis sparingly but appropriately
- Focus on natural, holistic wellness approaches
- Mention relevant product categories when appropriate
- Always provide contact information when customers need further assistance
- Respect the traditional Ayurvedic approach while making it accessible to modern customers

Contact Information:
- Phone: +91-9910474566
- Email: aumyanaturals@gmail.com
- Address: D-9, Sector-3, Noida, U.P. – 201301
- Website: www.aarogyavatika.com

Remember to be helpful, informative, and guide customers toward finding the right Ayurvedic solutions for their wellness needs.
"""
    
    def generate_response(self, user_query: str, chat_history: List[Dict[str, str]]) -> str:
        """Generate a response using Groq API with knowledge base context"""
        try:
            # Search knowledge base for relevant information
            relevant_info = self.knowledge_base.search_knowledge(user_query)
            
            # Check for FAQ response first
            faq_response = self.knowledge_base.get_faq_response(user_query)
            if faq_response:
                return faq_response
            
            # Create context from relevant information
            context = self._format_context(relevant_info)
            
            # Prepare messages for Groq API
            messages = [
                {"role": "system", "content": self.system_prompt + "\n\nRelevant Information:\n" + context}
            ]
            
            # Add recent chat history (last 6 messages for context)
            recent_history = chat_history[-6:] if len(chat_history) > 6 else chat_history
            for msg in recent_history:
                if msg["role"] in ["user", "assistant"]:
                    messages.append({"role": msg["role"], "content": msg["content"]})
            
            # Add current user query
            messages.append({"role": "user", "content": user_query})
            
            # Generate response using Groq
            response = self.groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                max_tokens=1024,
                temperature=0.3,
                stream=False
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"I apologize, but I'm having trouble processing your request right now. Please contact our customer service team at +91-9910474566 or aumyanaturals@gmail.com for immediate assistance. Error: {str(e)}"
    
    def _format_context(self, relevant_info: Dict[str, Any]) -> str:
        """Format relevant information into context for the AI"""
        if not relevant_info:
            return "No specific information found in knowledge base."
        
        context_parts = []
        
        if 'company_info' in relevant_info:
            info = relevant_info['company_info']
            context_parts.append(f"Company: {info['name']} - {info['tagline']}")
            context_parts.append(f"Legacy: {info['legacy']}")
            context_parts.append(f"Products: {info['products_count']}")
            context_parts.append(f"Community: {info['community']}")
            if 'contact' in info:
                contact = info['contact']
                context_parts.append(f"Contact: {contact['phone']}, {contact['email']}")
                context_parts.append(f"Address: {contact['address']}")
        
        if 'featured_products' in relevant_info:
            context_parts.append("Featured Products:")
            for product in relevant_info['featured_products'][:5]:  # Limit to first 5 products
                context_parts.append(f"- {product['name']} by {product['vendor']}: {product['price']}")
        
        if 'wellness_categories' in relevant_info:
            context_parts.append("Wellness Categories:")
            for category, description in relevant_info['wellness_categories'].items():
                context_parts.append(f"- {category.replace('_', ' ').title()}: {description}")
        
        if 'shipping_delivery' in relevant_info:
            shipping = relevant_info['shipping_delivery']
            context_parts.append("Shipping & Delivery:")
            context_parts.append(f"- Processing: {shipping['processing_time']}")
            context_parts.append(f"- Delivery: {shipping['delivery_time']}")
            context_parts.append(f"- Coverage: {shipping['coverage']}")
            context_parts.append(f"- Free shipping: {shipping['free_shipping']}")
            context_parts.append(f"- Charges: {shipping['shipping_charges']}")
        
        if 'payment_methods' in relevant_info:
            context_parts.append("Payment Methods: " + ", ".join(relevant_info['payment_methods']))
        
        if 'return_policy' in relevant_info:
            policy = relevant_info['return_policy']
            context_parts.append(f"Return Policy: {policy['general']}")
            context_parts.append("Exceptions: " + ", ".join(policy['exceptions']))
            context_parts.append(f"Refund Processing: {policy['refund_processing']}")
        
        if 'health_category' in relevant_info:
            for category, description in relevant_info['health_category'].items():
                context_parts.append(f"Health Category - {category.replace('_', ' ').title()}: {description}")
        
        if 'wellness_category' in relevant_info:
            for category, description in relevant_info['wellness_category'].items():
                context_parts.append(f"Wellness Category - {category.replace('_', ' ').title()}: {description}")
        
        return "\n".join(context_parts)
