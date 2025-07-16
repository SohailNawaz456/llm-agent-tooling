# ---------------------------------------------------------
# Import necessary classes
# ---------------------------------------------------------

from agents import Agent, Runner       # Import Agent class and Runner for execution
from connection import config          # Import your pre-configured RunConfig object
import asyncio                         # For running async Python code

# ---------------------------------------------------------
# Create an Agent object with instructions for behavior
# ---------------------------------------------------------

# NOTE:
# - Ye sirf ek LLM (Language Model) agent hai jo text instructions follow karta hai.
# - Humne agent ko yeh instructions di hain:
#   - User ka naam "Sohail" hai
#   - Hamesha polite raho (always polite)
#   - Har jawab mein "Sohail" ka naam lo (mention Sohail in every answer)

agent = Agent(
    name="PoliteAssistant",            # The agent's name (you can name it anything)
    instructions=(
        "User ka naam Sohail hai. "
        "Hamesha polite raho aur har jawab mein 'Sohail' ka naam lo."
    )
)

# ---------------------------------------------------------
# Define an asynchronous main function to run the agent
# ---------------------------------------------------------

async def main():
    # Run the agent's logic using Runner.run()
    # Parameters:
    # - starting_agent → Agent object created above
    # - input → The question you want to ask the agent
    # - run_config → Config object that contains model, credentials, etc.
    result = await Runner.run(
        starting_agent=agent,
        input="Who is the founder of Pakistan?",   # User's question
        run_config=config                          # LLM config (e.g. which model to use)
    )
    
    # Print the agent's final answer
    print(result.final_output)

# ---------------------------------------------------------
# Run the async main function
# ---------------------------------------------------------

# asyncio.run() is used to execute asynchronous code
asyncio.run(main())
