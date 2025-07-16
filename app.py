# Import necessary classes and functions from your SDK and Python standard libraries
from agents import Agent, Runner, function_tool, RunContextWrapper
import asyncio
from connection import config      # Your SDK or app's custom configuration object
from dataclasses import dataclass  # To define structured data easily
import rich                        # For nicely formatted console output

# ---------------------------------------------------------
# Define a data structure to hold user info
# ---------------------------------------------------------

@dataclass
class UserInfo:
    name: str   # User's name (e.g. "Sohail")
    uid: int    # User's unique ID (e.g. 123456)

# ---------------------------------------------------------
# Define a tool that can be called by the agent
# ---------------------------------------------------------

@function_tool
async def fetch_user_age(wrapper: RunContextWrapper[UserInfo]) -> str:
    """
    This function-tool will be called by the agent whenever it needs
    to know the user's age. It receives a wrapper that contains the
    user's context data.

    The function returns a simple string with the user's name and a dummy age.
    """
    # Access user's name from the context object
    user_name = wrapper.context.name
    
    # Return a fixed response string
    return f'User "{user_name}" is 25 years old.'

# ---------------------------------------------------------
# Define the main asynchronous function
# ---------------------------------------------------------

async def main():
    # Create a user info object with example data
    user_info = UserInfo(name="Sohail", uid=123456)

    # Create an agent configured with:
    # - A name
    # - Instructions that tell it how to behave
    # - A list of tools it can use (in this case, fetch_user_age)
    agent = Agent[UserInfo](
        name="Assistant",
        instructions="Use fetch_user_age tool and always only say exactly what the tool returns.",
        tools=[fetch_user_age]
    )

    # Run the agent:
    # - starting_agent → the Agent object to start with
    # - input → the question being asked by the user
    # - context → the user's context object (UserInfo)
    # - run_config → any runtime settings (e.g. model, logging)
    result = await Runner.run(
        starting_agent=agent,
        input="What is the age of the user?",
        context=user_info,
        run_config=config
    )

    # Print the agent's final output nicely formatted
    rich.print(result.final_output)

# ---------------------------------------------------------
# Kick off the async main function when this script runs
# ---------------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())
