"""
Created on 12-Dec-2024

@author: Smart Travel Consultant Team
"""

import openai
from travel_tools import get_visa_info, get_hotel_info, get_city_info, get_event_info, get_flight_info
from travel_prompts import generate_visa_prompt, generate_hotel_prompt, generate_city_prompt, generate_event_prompt, generate_generic_prompt
from utils.config_reader import get_property
from utils.helpers import validate_input, format_response
from utils.logger import setup_logger

# Initialize logger
logger = setup_logger()

# Set OpenAI API key
openai.api_key = get_property("API_KEYS", "OPENAI_API_KEY")

def classify_query(user_query):
    """
    Classifies the user query into one of the predefined categories.

    Args:
        user_query (str): The user's query.

    Returns:
        str: The category of the query (e.g., 'visa', 'hotel', 'flight', 'event', 'city', or 'generic').
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Classify the user's query into one of the following categories: visa, hotel, flight, event, city, or generic."},
                {"role": "user", "content": user_query}
            ],
            max_tokens=10
        )
        category = response['choices'][0]['message']['content'].strip().lower()
        logger.info(f"Query classified as: {category}")
        return category
    except Exception as e:
        logger.error(f"Error classifying query: {e}")
        return "generic"

def handle_user_query(user_query, session_state):
    """
    Handles the user query by invoking the appropriate agent.

    Args:
        user_query (str): The user's query.
        session_state (dict): A dictionary to maintain the session state.

    Returns:
        str: The response to the user's query.
    """
    # Add query to session history
    session_state.setdefault("messages", []).append({"role": "user", "content": user_query})

    # Classify query
    category = classify_query(user_query)

    # Invoke appropriate agent
    if category == "visa":
        return handle_visa_query(user_query, session_state)
    elif category == "hotel":
        return handle_hotel_query(user_query, session_state)
    elif category == "flight":
        return handle_flight_query(user_query, session_state)
    elif category == "event":
        return handle_event_query(user_query, session_state)
    elif category == "city":
        return handle_city_query(user_query, session_state)
    else:
        return handle_generic_query(user_query, session_state)

def handle_visa_query(user_query, session_state):
    """
    Handles visa-related queries.
    """
    required_fields = ["destination_country", "nationality", "country_of_residence", "purpose_of_travel"]
    collected_data = session_state.get("collected_data", {})

    is_valid, missing_fields = validate_input(collected_data, required_fields)
    if not is_valid:
        missing_field = missing_fields[0]
        return f"Please provide your {missing_field.replace('_', ' ')}."

    prompt = generate_visa_prompt(
        nationality=collected_data.get("nationality"),
        destination=collected_data.get("destination_country"),
        residence=collected_data.get("country_of_residence"),
        purpose=collected_data.get("purpose_of_travel")
    )
    visa_info = get_visa_info(prompt)
    return format_response("Here are the visa requirements:", {"Details": visa_info})

def handle_hotel_query(user_query, session_state):
    """
    Handles hotel-related queries.
    """
    prompt = generate_hotel_prompt(user_query)
    hotel_info = get_hotel_info(prompt)
    return format_response("Here are the hotel options:", {"Details": hotel_info})

def handle_flight_query(user_query, session_state):
    """
    Handles flight-related queries.
    """
    prompt = generate_generic_prompt(user_query)
    flight_info = get_flight_info(prompt)
    return format_response("Here are the flight options:", {"Details": flight_info})

def handle_event_query(user_query, session_state):
    """
    Handles event-related queries.
    """
    prompt = generate_event_prompt(user_query)
    event_info = get_event_info(prompt)
    return format_response("Here are the event details:", {"Details": event_info})

def handle_city_query(user_query, session_state):
    """
    Handles city-related queries.
    """
    prompt = generate_city_prompt(user_query)
    city_info = get_city_info(prompt)
    return format_response("Here is the city information:", {"Details": city_info})

def handle_generic_query(user_query, session_state):
    """
    Handles generic travel-related queries.
    """
    prompt = generate_generic_prompt(user_query)
    generic_info = get_visa_info(prompt)
    return format_response("Here is the information:", {"Details": generic_info})

# Example usage
if __name__ == "__main__":
    session_state = {}
    user_query = "What are the visa requirements for Germany?"
    response = handle_user_query(user_query, session_state)
    print(response)
