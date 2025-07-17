import os
import json
from typing import Dict, List, Any

class KnowledgeBase:
    def __init__(self):
        self.knowledge_data = self._load_knowledge_base()
    
    def _load_knowledge_base(self) -> Dict[str, Any]:
        """Load and structure the knowledge base from the provided documents"""
        return {
            "company_info": {
                "name": "Aarogya Vatika",
                "tagline": "Ayurvedic Wellness Redefined",
                "legacy": "45+ years of traditional healing wisdom",
                "products_count": "50+ Pure Ayurvedic Products",
                "community": "7,200+ Members, 15,000+ Readers",
                "website": "www.aarogyavatika.com",
                "contact": {
                    "company": "Aumya Naturals LLP",
                    "address": "D-9, Sector-3, Noida, U.P. – 201301",
                    "phone": "+91-9910474566",
                    "email": "aumyanaturals@gmail.com"
                }
            },
            "philosophy": {
                "core_values": [
                    "Personalized healing",
                    "Sustainable and pure products",
                    "Evidence-backed practices",
                    "Holistic care that addresses mind, body, and spirit"
                ],
                "approach": "Blends ancient Ayurvedic traditions with modern wellness support"
            },
            "key_offerings": [
                "50+ Pure Ayurvedic Products – Carefully sourced, natural, and curated",
                "Expert Doctor Guidance – Personalized health consultations available",
                "Educational Content – Science-backed articles on key wellness topics",
                "Community Support – 7,200+ members, 15,000+ readers"
            ],
            "wellness_categories": {
                "womens_health": "Hormonal balance, menstrual care",
                "gut_health": "Digestion and microbiome-friendly support",
                "immunity_boosters": "Herbs like Ashwagandha, Tulsi, etc.",
                "diabetes_management": "Herbal support (e.g., bitter melon, cinnamon)"
            },
            "featured_products": [
                {
                    "name": "Neem Capsule",
                    "vendor": "Garry N Sun Organics",
                    "price": "From Rs. 282.00"
                },
                {
                    "name": "Ashoka Capsule",
                    "vendor": "Garry N Sun Organics",
                    "price": "From Rs. 290.00"
                },
                {
                    "name": "Moringa Capsule",
                    "vendor": "Garry N Sun Organics",
                    "price": "From Rs. 289.00"
                },
                {
                    "name": "Ultra Lite Chamomile Moisturiser",
                    "vendor": "Vatsa Padam",
                    "price": "Rs. 850.00"
                },
                {
                    "name": "Pure Himalayan Shilajit",
                    "vendor": "Garry N Sun Organics",
                    "price": "Rs. 1,999.00"
                }
            ],
            "shipping_delivery": {
                "processing_time": "1–2 days order processing",
                "delivery_time": "3–10 days delivery depending on location",
                "coverage": "Ships across India",
                "tracking": "Tracking via SMS/email",
                "free_shipping": "Free shipping over ₹699",
                "shipping_charges": "Flat ₹79 below ₹699, ₹50 COD charge",
                "multi_vendor": "Allows multi-vendor shipments"
            },
            "payment_methods": [
                "Credit/Debit Cards",
                "UPI Payments",
                "Net Banking",
                "Digital Wallets"
            ],
            "return_policy": {
                "general": "Due to the perishable nature of Ayurvedic products, we generally do not accept returns except for:",
                "exceptions": [
                    "Products damaged during shipping (must report within 48 hours of delivery)",
                    "Incorrect items shipped"
                ],
                "refund_processing": "Refunds will be processed to the original payment method within 7-10 business days"
            },
            "privacy_security": [
                "Data collected: Name, contact info, order details, usage stats",
                "No data sold or shared without consent",
                "SSL encryption for all transactions",
                "Rights to access, correct, or delete user data available"
            ],
            "featured_articles": [
                "Irregular Menstrual Cycles & Ayurveda",
                "Ayurvedic Fertility Guide",
                "Beyond Normal Period Pain",
                "Urinary Discomfort: Ayurvedic Perspective",
                "Pelvic Inflammatory Disease & Ayurveda"
            ],
            "testimonials": [
                "Transformed my space with Ayurvedic herbs—delivered pristine! – Emily R., Designer",
                "Peace Lily brought calm to my creative process. – Sarah T., Writer"
            ],
            "health_categories": {
                "heart_harmony": "Heart health support",
                "kidney_care": "Kidney health and detox",
                "skin_care": "Natural skincare solutions",
                "bone_joint": "Bone and joint support",
                "breathe_easy": "Respiratory health",
                "liver_care": "Liver detox and care",
                "digestive_care": "Gut health and digestion",
                "mood_stress": "Mental wellness and stress management"
            }
        }
    
    def search_knowledge(self, query: str) -> Dict[str, Any]:
        """Search the knowledge base for relevant information"""
        query_lower = query.lower()
        relevant_info = {}
        
        # Search for company information
        if any(word in query_lower for word in ['company', 'about', 'aarogya', 'vatika']):
            relevant_info['company_info'] = self.knowledge_data['company_info']
        
        # Search for product information
        if any(word in query_lower for word in ['product', 'buy', 'shop', 'price', 'cost']):
            relevant_info['featured_products'] = self.knowledge_data['featured_products']
            relevant_info['wellness_categories'] = self.knowledge_data['wellness_categories']
        
        # Search for shipping information
        if any(word in query_lower for word in ['shipping', 'delivery', 'order', 'dispatch']):
            relevant_info['shipping_delivery'] = self.knowledge_data['shipping_delivery']
        
        # Search for payment information
        if any(word in query_lower for word in ['payment', 'pay', 'method']):
            relevant_info['payment_methods'] = self.knowledge_data['payment_methods']
        
        # Search for return/refund information
        if any(word in query_lower for word in ['return', 'refund', 'exchange']):
            relevant_info['return_policy'] = self.knowledge_data['return_policy']
        
        # Search for contact information
        if any(word in query_lower for word in ['contact', 'phone', 'email', 'address']):
            relevant_info['contact'] = self.knowledge_data['company_info']['contact']
        
        # Search for health categories
        for category, description in self.knowledge_data['health_categories'].items():
            if any(word in query_lower for word in category.split('_')):
                relevant_info['health_category'] = {category: description}
        
        # Search for wellness categories
        for category, description in self.knowledge_data['wellness_categories'].items():
            if any(word in query_lower for word in category.split('_')):
                relevant_info['wellness_category'] = {category: description}
        
        return relevant_info
    
    def get_all_data(self) -> Dict[str, Any]:
        """Get all knowledge base data"""
        return self.knowledge_data
    
    def get_faq_response(self, query: str) -> str:
        """Get specific FAQ responses"""
        query_lower = query.lower()
        
        if 'shipping' in query_lower and 'time' in query_lower:
            return "Orders are processed within 1-2 days, and delivery takes 3-10 days depending on your location. We ship across India with tracking via SMS/email."
        
        elif 'free shipping' in query_lower:
            return "We offer free shipping on orders above ₹699. For orders below ₹699, there's a flat shipping charge of ₹79, and ₹50 for COD."
        
        elif 'return' in query_lower or 'refund' in query_lower:
            return "Due to the perishable nature of Ayurvedic products, we generally don't accept returns except for damaged products (report within 48 hours) or incorrect items shipped. Refunds are processed within 7-10 business days."
        
        elif 'payment' in query_lower:
            return "We accept Credit/Debit Cards, UPI Payments, Net Banking, and Digital Wallets. All transactions are secured with SSL encryption."
        
        elif 'consultation' in query_lower:
            return "We offer personalized health consultations with expert Ayurvedic doctors. You can book a consultation through our website."
        
        return None
