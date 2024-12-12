"""
Created on 12-Dec-2024

@author: Smart Travel Consultant Team
"""

def generate_visa_prompt(nationality, destination, residence, purpose):
    """
    Generates a specific prompt for Gemini API to fetch visa requirements.

    Args:
        nationality (str): User's nationality.
        destination (str): Destination country.
        residence (str): Country of residence.
        purpose (str): Purpose of travel (e.g., business, leisure).

    Returns:
        str: A formatted prompt for the visa query.
    """
    return (
        f"What are the visa requirements for a {nationality} citizen "
        f"residing in {residence}, visiting {destination} for {purpose}? "
        "Include visa application process, essential travel tips, and any mandatory documents. "
        "Provide URLs of official embassies or consulates for reference."
    )

def generate_hotel_prompt(user_query):
    """
    Generates a specific prompt for Gemini API to fetch hotel information.

    Args:
        user_query (str): User's query about hotels.

    Returns:
        str: A formatted prompt for the hotel query.
    """
    return f"Fetch hotel options based on the following user query: {user_query}. Include ratings, pricing, and proximity details."

def generate_flight_prompt(user_query):
    """
    Generates a specific prompt for flight-related queries.

    Args:
        user_query (str): User's query about flights.

    Returns:
        str: A formatted prompt for the flight query.
    """
    return f"Find flight options for the following request: {user_query}. Include airline names, pricing, and timings."

def generate_city_prompt(user_query):
    """
    Generates a specific prompt for Gemini API to fetch city or airport information.

    Args:
        user_query (str): User's query about city or airport information.

    Returns:
        str: A formatted prompt for the city query.
    """
    return f"Provide detailed city and airport information for the following query: {user_query}. Include transport options and tips."

def generate_event_prompt(user_query):
    """
    Generates a specific prompt for Gemini API to fetch event or conference information.

    Args:
        user_query (str): User's query about events or conferences.

    Returns:
        str: A formatted prompt for the event query.
    """
    return f"List events or conferences matching the following request: {user_query}. Include venue, timing, and registration links."

def generate_generic_prompt(user_query):
    """
    Generates a generic prompt for handling miscellaneous travel-related queries.

    Args:
        user_query (str): User's query about general travel information.

    Returns:
        str: A formatted prompt for the generic query.
    """
    return f"Answer the following travel-related question: {user_query}. Provide accurate and comprehensive details."

# Example usage
if __name__ == "__main__":
    # Test prompts
    print(generate_visa_prompt("Indian", "Germany", "India", "Business"))
    print(generate_hotel_prompt("Hotels near Eiffel Tower"))
    print(generate_flight_prompt("Flights from Delhi to Paris"))
    print(generate_city_prompt("Information about JFK Airport"))
    print(generate_event_prompt("Tech conferences in San Francisco"))
