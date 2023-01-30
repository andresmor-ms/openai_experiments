import os


def get_api_key():
    """
    Returns the OpenAI API key from the environment variable OPENAI_API_KEY.
    """
    return os.environ.get("OPENAI_API_KEY")
