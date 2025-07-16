# ---------------------------------------------------
# Import necessary modules and classes
# ---------------------------------------------------
import os                             # For accessing environment variables
from dotenv import load_dotenv        # For loading environment variables from a .env file
from agents import (
    Agent,
    Runner,
    OpenAIChatCompletionsModel,
    AsyncOpenAI,
    RunConfig
)                                     # Import core Agent SDK components

# ---------------------------------------------------
# Load API keys from the .env file
# ---------------------------------------------------
load_dotenv()                         # Load environment variables from .env into os.environ

# ---------------------------------------------------
# Retrieve the Gemini API key from environment
# ---------------------------------------------------
gemini_api_key = os.getenv("GEMINI_API_KEY")  # Get the Gemini API key

# ---------------------------------------------------
# If the key is missing, raise an exception
# ---------------------------------------------------
if not gemini_api_key:
    raise Exception("GEMINI_API_KEY is not set in .env file")

# ---------------------------------------------------
# Create an Async client to communicate with Gemini API
# ---------------------------------------------------
external_client = AsyncOpenAI(
    api_key=gemini_api_key,                                   # Your Gemini API key
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"  # Gemini-compatible OpenAI endpoint
)

# ---------------------------------------------------
# Define the model used for chat completions
# ---------------------------------------------------
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",    # Gemini 2.0 Flash model (adjust to your provider's model name)
    openai_client=external_client  # Use the Gemini-compatible OpenAI-style client
)

# ---------------------------------------------------
# Define the run configuration for the agent
# ---------------------------------------------------
config = RunConfig(
    model=model,                    # The LLM model used during agent execution
    model_provider=external_client, # The provider/client that executes model calls
    tracing_disabled=True           # Disable tracing/logging if not needed (set to False to enable)
)
