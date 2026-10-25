# 🎙️ Vocom — Voice-Powered E-commerce

**Vocom** is an e-commerce web application that explores voice-based product search through artificial intelligence. It combines a Vue.js frontend, a Flask backend, and Google's Gemini API to provide an alternative way to search for products using voice input.

The project explores how generative AI can make product discovery more intuitive and improve the shopping experience.

## ✨ Features

- 🛍️ **Product Catalog:** Browse and discover available products.
- 🎙️ **AI-Powered Voice Search:** Search for products using voice input, powered by the Google Gemini API.
- 🛒 **Shopping Cart:** Add products to the cart and manage selected items before checkout.
- 📦 **Order Management:** Place orders and manage the ordering process.
- ⭐ **Product Ratings:** Rate products and share feedback to help other customers make informed decisions.
- 🔗 **Frontend-Backend Integration:** Connect the Vue.js frontend to the Flask backend through API requests.

## 🏗️ Project Architecture

Vocom separates its frontend and backend into two main components.

| Component | Technology | Responsibility |
|---|---|---|
| Frontend | Vue.js | User interface, product browsing, shopping cart, ratings, and voice-search interaction |
| Backend | Python / Flask | Business logic, API endpoints, cart and order operations, and product-related requests |
| AI Integration | Google Gemini API | AI capabilities for voice-based product search |

## 🎯 Project Objectives

- Build a functional e-commerce web application.
- Provide an alternative to traditional text-based product search through voice interaction.
- Integrate generative AI into a practical web application.
- Implement core shopping features, including cart management, orders, and product ratings.
- Explore the integration of frontend technologies, backend APIs, and AI services in a single project.

## 🔮 Potential Future Improvements

- Improve voice-search accuracy and handling of ambiguous product requests.
- Add advanced product filters and sorting.
- Enhance the shopping experience with personalized product recommendations.
- Improve automated testing, error handling, and deployment configuration.

### Frontend — Vue.js

The frontend provides the user interface and the product-search experience. It communicates with the backend to process search requests.

### Backend — Flask

The backend handles application API requests and integrates with the Gemini API to support the voice-search functionality.

### AI Integration — Google Gemini

Gemini provides the AI capabilities used in the voice-search workflow. The integration aims to make product discovery more natural than relying exclusively on conventional text-based search.

## 🚀 Getting Started

### Prerequisites

Make sure the following tools are installed:

- Python
- Node.js and npm
- A Google Gemini API key

### 1. Clone the repository

```bash
git clone https://github.com/JoharyJonathan/vocom.git
cd vocom
```

### 2. Set up the backend

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Configure your Gemini API key using an environment variable or the configuration mechanism expected by the backend.

```env
GEMINI_API_KEY=your_gemini_api_key
```

> Use the exact environment variable name expected by the application. Never commit API keys or other secrets to GitHub.

Start the Flask application using the entry point configured in the `back/` directory.

### 3. Set up the frontend

Open a terminal in the frontend directory:

```bash
cd front
npm install
```

Start the development server using the script defined in `front/package.json`. For a typical Vue.js project using Vite, the command is:

```bash
npm run dev
```

Ensure that the frontend is configured to communicate with the correct Flask backend URL.

## 🔐 Configuration and Security

- Store the Gemini API key in an environment variable.
- Keep secret credentials out of version control.
- Configure the backend URL appropriately for local development and production.
- Ensure that API errors and unavailable services are handled gracefully.

## 🎯 Project Goals

Vocom explores the integration of AI into e-commerce, with a particular focus on making product search more accessible and intuitive through voice interaction.

The project brings together frontend development, backend API integration, and generative AI in a single web application.

## 👨‍💻 Author

**Johary Jonathan**

- GitHub: [@JoharyJonathan](https://github.com/JoharyJonathan)
- Repository: [JoharyJonathan/vocom](https://github.com/JoharyJonathan/vocom)

---

*An e-commerce project exploring voice-based product discovery with Vue.js, Flask, and Google Gemini.*