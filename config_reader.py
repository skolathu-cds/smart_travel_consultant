"""
Created on 12-Dec-2024

@author: Smart Travel Consultant Team
"""

import configparser
import os

# Create a ConfigParser object
config = configparser.ConfigParser()

def load_config():
    """
    Loads the configuration file specified by the SMART_TRAVEL_CONFIG_PATH environment variable.
    """
    # Read the configuration file path from the environment variable
    config_file_path = os.getenv("SMART_TRAVEL_CONFIG_PATH")
    
    if not config_file_path:
        raise ValueError("Environment variable 'SMART_TRAVEL_CONFIG_PATH' is not set.")
    
    print(f"Config file path: {config_file_path}")
    
    # Read the properties file
    try:
        config.read(config_file_path)
        print("Configuration loaded successfully.")
    except Exception as e:
        print(f"Error loading configuration: {e}")
        raise

def get_property(section, key):
    """
    Retrieves the value of a property from the loaded configuration file.
    Args:
        section (str): The section in the configuration file.
        key (str): The key within the section.

    Returns:
        str: The value associated with the specified key.
    """
    try:
        return config[section][key]
    except KeyError as e:
        raise KeyError(f"Property not found: Section '{section}', Key '{key}'") from e

# Example usage
if __name__ == "__main__":
    try:
        load_config()
        openai_key = get_property("API_KEYS", "OPENAI_API_KEY")
        print(f"OpenAI API Key: {openai_key}")
    except Exception as e:
        print(f"Error: {e}")