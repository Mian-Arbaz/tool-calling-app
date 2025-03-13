# AI Tool Calling App

## Overview
The AI Tool Calling App is a Streamlit-based application that leverages AI to perform two key functions:
1. **Calculator**: Evaluates mathematical expressions.
2. **Stock Price Checker**: Fetches real-time stock prices using the Polygon API.

This app utilizes **LangChain**, **Google Generative AI**, and **Streamlit** to create an interactive user experience.

## Features
- Perform **mathematical calculations** by entering expressions.
- Retrieve **real-time stock prices** using a stock symbol.
- User-friendly **web interface** built with Streamlit.
- Implements AI-powered responses using **LangChain** and **Google Generative AI**.

## Installation
### Prerequisites
- Python 3.8+
- A Google API Key for AI interactions
- A Polygon API Key for stock price retrieval

### Steps to Install
1. **Clone the Repository**
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. **Create and Activate a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set Up Environment Variables**
   - Create a `.env` file in the project root.
   - Add the following content:
     ```ini
     GOOGLE_API_KEY="your_google_api_key"
     ```
   - Replace `your_google_api_key` with your actual Google API Key.

## Usage
1. **Run the Application**
   ```sh
   streamlit run app.py
   ```
2. **Interact with the App**
   - Enter a mathematical expression (e.g., `2 + 3 * 4`).
   - Enter a stock symbol (e.g., `AAPL` for Apple Inc.).
   - Click **Search** to get the response.

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: Web application framework.
- **LangChain**: AI-powered tool calling.
- **Google Generative AI**: LLM for processing requests.
- **Polygon API**: Fetches stock prices.

## License
This project is licensed under the MIT License.

## Author
Developed by [Your Name].

## Acknowledgments
- [LangChain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [Google AI](https://ai.google/)
- [Polygon API](https://polygon.io/)

