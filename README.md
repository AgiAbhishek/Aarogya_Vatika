# 🪷 Aarogya Vatika Customer Support Chatbot

A professional AI-powered customer support chatbot for Aarogya Vatika, an Ayurvedic wellness platform with 45+ years of traditional healing wisdom. Built with Streamlit and powered by Groq API for intelligent customer service.

## 🌟 Features

- **AI-Powered Responses**: Utilizes Groq's Llama 3.3 70B model for intelligent, contextual responses
- **Comprehensive Knowledge Base**: Detailed information about products, services, policies, and wellness guidance
- **Professional Interface**: Clean, responsive design with Aarogya Vatika branding
- **Real-time Chat**: Interactive chat interface with session management
- **Common Questions**: Quick access buttons for frequently asked questions
- **Multi-category Support**: Handles inquiries about products, shipping, returns, and wellness guidance

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip package manager
- Git (optional)

### Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd aarogya-vatika-chatbot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit groq python-dotenv
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py --server.port 5000
   ```

6. **Access the chatbot**
   
   Open your browser and go to: `http://localhost:5000`

## 📁 Project Structure

```
aarogya-vatika-chatbot/
├── app.py                      # Main Streamlit application
├── chat_handler.py             # AI chat logic and response generation
├── knowledge_base.py           # Knowledge base management and search
├── utils.py                    # Utility functions and UI helpers
├── .env                        # Environment variables (create this)
├── README.md                   # This file               
├── .streamlit/
│   └── config.toml             # Streamlit configuration
├── attached_assets/
│   ├── logo_1752783306177.jpeg # Aarogya Vatika logo
│   ├── logo_1752783780690.jpeg # Alternative logo
│   ├── content-1752783297992.md # Website content
│   └── Knowledge Base Aarogya Vatika_1752783313076.pdf # Knowledge base PDF
├── pyproject.toml              # Python project configuration
└── uv.lock                     # Dependency lock file
```

## 🔧 Configuration

### Streamlit Configuration (`.streamlit/config.toml`)

```toml
[server]
headless = true
address = "0.0.0.0"
port = 5000

[theme]
primaryColor = "#2E8B57"
backgroundColor = "#F0F8FF"
secondaryBackgroundColor = "#E6F3FF"
textColor = "#1E3A8A"
```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Your Groq API key for AI responses | Yes |

## 🏗️ Architecture

### Core Components

1. **Main Application (`app.py`)**
   - Streamlit UI configuration and layout
   - Chat interface orchestration
   - Session state management
   - Professional styling and branding

2. **Chat Handler (`chat_handler.py`)**
   - Groq API integration
   - Context-aware response generation
   - Chat history management
   - System prompt configuration

3. **Knowledge Base (`knowledge_base.py`)**
   - Structured data storage
   - Intelligent search functionality
   - FAQ response handling
   - Product and service information

4. **Utilities (`utils.py`)**
   - Session state initialization
   - Chat message display
   - UI helper functions
   - Data formatting utilities

### Data Flow

1. User input → Chat Handler
2. Knowledge Base search → Relevant context
3. Groq API → AI response generation
4. Response display → Updated chat history

## 🎨 UI Features

- **Professional Header**: Gradient background with company branding
- **Sidebar Information**: Company details, contact info, and quick links
- **Welcome Message**: Styled introduction with service categories
- **Common Questions**: Interactive buttons for quick queries
- **Clean Chat Interface**: Professional chat bubbles with avatars
- **Responsive Design**: Works on desktop and mobile devices

## 🔍 Knowledge Base Categories

- **Company Information**: About Aarogya Vatika, philosophy, and history
- **Products**: 50+ Ayurvedic products with pricing and vendors
- **Wellness Categories**: Women's health, gut health, immunity, diabetes management
- **Shipping & Delivery**: Processing times, costs, and policies
- **Returns & Refunds**: Policy details and procedures
- **Contact Information**: Phone, email, and address details

## 🚢 Deployment

### Local Development
```bash
streamlit run app.py --server.port 5000
```

### Production Deployment
The application is configured for deployment on platforms like:
- Heroku
- AWS EC2
- Google Cloud Platform
- Any platform supporting Python web applications

## 🛠️ Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named 'groq'**
   ```bash
   pip install groq
   ```

2. **GROQ_API_KEY environment variable not set**
   - Ensure `.env` file exists with your API key
   - Install python-dotenv: `pip install python-dotenv`
   - Add `load_dotenv()` to the top of app.py

3. **Port already in use**
   ```bash
   streamlit run app.py --server.port 8501
   ```

## 📞 Support

For questions or support regarding this chatbot:

- **Email**: aumyanaturals@gmail.com
- **Phone**: +91-9910474566
- **Website**: [www.aarogyavatika.com](https://www.aarogyavatika.com)
