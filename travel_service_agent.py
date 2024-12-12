"""
Created on 12-Dec-2024

@author: Smart Travel Consultant Team
"""

def validate_input(input_data, required_fields):
    """
    Validates user input against the required fields.

    Args:
        input_data (dict): The user-provided data.
        required_fields (list): A list of required field names.

    Returns:
        tuple: (bool, list) - A boolean indicating if all fields are present, and a list of missing fields.
    """
    missing_fields = [field for field in required_fields if field not in input_data or not input_data[field]]
    return len(missing_fields) == 0, missing_fields

def format_response(message, details=None):
    """
    Formats a response message with additional details if provided.

    Args:
        message (str): The main response message.
        details (dict, optional): Additional details to include in the response.

    Returns:
        str: Formatted response.
    """
    if details:
        detail_lines = "\n".join([f"{key}: {value}" for key, value in details.items()])
        return f"{message}\n\nDetails:\n{detail_lines}"
    return message

def is_valid_country(country_name):
    """
    Checks if a given country name is valid. (Placeholder function for now.)

    Args:
        country_name (str): The name of the country to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    # Placeholder for actual validation logic, e.g., using an API or country list
    return isinstance(country_name, str) and len(country_name) > 0

def capitalize_words(sentence):
    """
    Capitalizes the first letter of each word in a sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        str: Capitalized sentence.
    """
    return " ".join(word.capitalize() for word in sentence.split())

# Example usage
if __name__ == "__main__":
    # Validate input
    input_data = {"destination_country": "France", "nationality": "Indian"}
    required_fields = ["destination_country", "nationality", "purpose_of_travel"]
    is_valid, missing = validate_input(input_data, required_fields)
    print(f"Input valid: {is_valid}, Missing fields: {missing}")

    # Format response
    message = "Here are the details you requested."
    details = {"Visa Type": "Business", "Processing Time": "5-7 days"}
    print(format_response(message, details))

    # Check country validity
    print(is_valid_country("Germany"))  # True

    # Capitalize words
    print(capitalize_words("hello world"))  # Hello World
