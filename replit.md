# Aarogya Vatika Customer Support Chatbot

## Overview

This is a Streamlit-based customer support chatbot for Aarogya Vatika, an Ayurvedic wellness platform. The application provides an AI-powered customer service interface that can answer questions about products, services, shipping, returns, and general store information. It leverages the Groq API for natural language processing and maintains a structured knowledge base about the company's offerings and policies.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

The application follows a modular architecture with clear separation of concerns:

- **Frontend**: Streamlit web interface with chat-based interaction
- **AI Integration**: Groq API for conversational AI responses
- **Knowledge Management**: Structured knowledge base with company information
- **Session Management**: Streamlit session state for chat history persistence

## Key Components

### 1. Main Application (`app.py`)
- **Purpose**: Entry point and UI orchestration
- **Features**: 
  - Streamlit page configuration and layout
  - Resource caching for performance optimization
  - Sidebar with company information
  - Main chat interface integration

### 2. Chat Handler (`chat_handler.py`)
- **Purpose**: Manages conversation flow and AI responses
- **Key Features**:
  - Groq API integration for natural language processing
  - System prompt configuration for Ayurvedic wellness context
  - Chat history management
  - Response generation with knowledge base context

### 3. Knowledge Base (`knowledge_base.py`)
- **Purpose**: Centralized information repository
- **Structure**:
  - Company information and contact details
  - Product categories and featured products
  - Philosophy and core values
  - Wellness categories and offerings
- **Data Format**: Structured dictionary with nested categories

### 4. Utilities (`utils.py`)
- **Purpose**: Helper functions and UI components
- **Functions**:
  - Session state initialization
  - Chat history display with avatars
  - Product information formatting
  - Welcome message display

## Data Flow

1. **User Input**: Customer enters query through Streamlit chat interface
2. **Context Retrieval**: Knowledge base searches for relevant information
3. **AI Processing**: Groq API generates contextual response using system prompt
4. **Response Display**: Formatted response shown in chat interface
5. **History Management**: Conversation stored in session state for continuity

## External Dependencies

### Required APIs
- **Groq API**: Natural language processing and response generation
  - API Key: `GROQ_API_KEY` environment variable
  - Default fallback: `gsk_default_key`

### Python Libraries
- `streamlit`: Web interface framework
- `groq`: Official Groq API client
- `os`: Environment variable management
- `json`: Data serialization
- `typing`: Type hints for better code maintainability

## Deployment Strategy

### Environment Setup
- Environment variables required: `GROQ_API_KEY`
- Python dependencies managed through standard requirements
- Streamlit configuration for page layout and branding

### Caching Strategy
- `@st.cache_resource` decorators for:
  - Groq client initialization
  - Knowledge base loading
  - Chat handler instantiation
- Improves performance by avoiding repeated resource creation

### Session Management
- Streamlit session state for:
  - Chat history persistence
  - User information storage
  - Cross-request data continuity

## Company Context

The application serves Aarogya Vatika, an Ayurvedic wellness platform with:
- 45+ years of traditional healing wisdom
- 50+ pure Ayurvedic products
- Expert doctor guidance
- 7,200+ members and 15,000+ readers community
- Focus on personalized healing and sustainable products

The chatbot is designed to maintain the company's holistic wellness philosophy while providing modern, accessible customer service.