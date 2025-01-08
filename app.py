from dotenv import load_dotenv
import requests
import os
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
import streamlit as st 

#Load environment variable from .env file
load_dotenv()

#Accessing environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

@tool
def calculator(expression: str) -> float:
    """
    Evaluate a mathematical expression and return the result.

    Parameters:
    expression (str): A string containing the mathematical expression to evaluate.

    Returns:
    float: The result of the evaluated expression.

    Examples:
    >>> evaluate_expression("2 + 3 * 4")
    14.0
    >>> evaluate_expression("(10 / 2) + 8")
    13.0

    Note:
    - This function uses Python's `eval()` to calculate the result.
    - Ensure the input is sanitized to avoid malicious code execution.
    """
    try:
        # Evaluate the expression safely
        result = eval(expression, {"__builtins__": {}})
        return float(result)
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return None
tools = [calculator]

@tool
def get_stock_price(symbol: str) -> str:
    """Fetches the current stock price of a company based on its stock symbol using the Polygon API.

    Args:
        symbol (str): The stock symbol of the company (e.g., 'AAPL' for Apple, 'GOOGL' for Google).

    Returns:
        str: A message containing the current stock price of the company.

    Raises:
        HTTPError: If the HTTP request to the stock API fails (e.g., 404 or 500 status).
        RequestException: If there is an issue with the request itself (e.g., connection error).
        Exception: For any other unexpected errors during the execution of the function.

    """
    api_key = "cBI8VUvn5zsXWp6UvpqbeYQJmiH5QHf_"  # Replace this with your actual secret API key from Polygon
    url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/prev"  # Polygon endpoint for previous close price

    try:
        # Send a GET request with the API key
        response = requests.get(url, params={'apiKey': api_key})
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)

        # Assuming the data contains 'close' in the response for the last closing price
        data = response.json()
        price = data.get('results', [{}])[0].get('c')  # 'c' is the closing price

        if price:
            return f"Tool used: get_stock_price\n get_stock_price tool is used to find The current price of {symbol} is ${price}"
        else:
            return f"Error: Could not retrieve stock data for {symbol}.\nTool used: get_stock_price"

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}\nTool used: get_stock_price"
    except requests.exceptions.RequestException as req_err:
        return f"Request error occurred: {req_err}\nTool used: get_stock_price"
    except Exception as err:
        return f"An unexpected error occurred: {err}\nTool used: get_stock_price"




tools = [calculator,get_stock_price]
 

llm = ChatGoogleGenerativeAI(model= "gemini-2.0-flash-exp", api_key=GOOGLE_API_KEY)

agent = initialize_agent(tools, llm , agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)


# Front End
st.set_page_config(page_title="AI Tool Calling", page_icon="⚙️", layout="wide")

# Custom CSS for styling
st.markdown(
    """<style>
    body {
        background-color: #f5f7fa;
    }
    .stButton>button {
        color: white;
        background-color: #4CAF50;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
    }
    .stContainer {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>""",
    unsafe_allow_html=True
)

st.title("🤖 Tool Helper")
st.write("Hi there! Enjoy exploring this AI-powered tool.")

# Layout with two columns
col1, col2 = st.columns(2)

with col1:
    st.header("🔠 Enter Your Query")
    user_input = st.text_input('How can I assist you today?', placeholder="Type a query like 'Calculate 2+2' or 'Stock price of AAPL'")

    if st.button("Search"):
        if user_input:
            try:
                with st.spinner("Processing your request..."):
                    # Pass the query to the agent
                    response = agent.run(user_input)
                st.success(f"Response: {response}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.error("Please enter a query before hitting the button.")

# Sidebar for guidance and warnings
st.sidebar.title("🔧 Tool Info")
st.sidebar.info("This tool supports simple calculations and stock price queries. Use the examples for inspiration!")
st.sidebar.warning("⚠️ Ensure your input is clear and valid.")

# Expander for Additional Information
with st.expander("🔍 Guidance"):
    st.markdown("""
    This tool is designed to help you with **simple calculations** and provide **stock price insights**.  
    Simply enter your query below, click the **Search** button, and get the answers you need!  
    Feel free to ask anything, and we'll assist you promptly!
    """)
