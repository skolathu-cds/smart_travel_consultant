"""
Created on 12-Dec-2024

@author: Smart Travel Consultant Team
"""

import streamlit as st
import os
import secrets
from travel_service_agent import handle_user_query
from utils.logger import setup_logger

# Initialize logger
logger = setup_logger()

def main():
    """
    Streamlit app for AI Travel Advisor.
    """
    # Configure page
    st.set_page_config(
        page_title="AI Travel Advisor",
        page_icon="🌍",
        layout="wide"
    )

    # Sidebar
    with st.sidebar:
        st.title("AI Travel Advisor")
        st.markdown("""
        Your personal AI travel advisor to provide:
        - Visa requirements
        - Flight options
        - Hotel recommendations
        - City and airport information
        - Event and conference details
        """)

    # Initialize session state
    if "session_id" not in st.session_state:
        st.session_state.session_id = secrets.token_urlsafe(8)

    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = []

    # Display chat history
    st.title("AI Travel Advisor")
    st.markdown("Your personal AI Travel advisor to assist you on queries related to Visa requirements, Hotels, City & Airport information, flights and much more"
                "How can I assist you with your travel plans today?")

    for message in st.session_state.conversation_history:
        role = "user" if message["role"] == "user" else "assistant"
        with st.chat_message(role):
            st.markdown(message["content"])

    # User input
    user_query = st.chat_input("Enter your travel-related query...")

    if user_query:
        # Display user query
        with st.chat_message("user"):
            st.markdown(user_query)

        # Add to conversation history
        st.session_state.conversation_history.append({"role": "user", "content": user_query})

        # Handle the query
        with st.chat_message("assistant"):
            with st.spinner("Fetching response..."):
                try:
                    response = handle_user_query(user_query, st.session_state)
                except Exception as e:
                    logger.error(f"Error handling user query: {e}")
                    response = "I'm sorry, something went wrong while processing your query."

                st.markdown(response)

        # Add assistant response to conversation history
        st.session_state.conversation_history.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
