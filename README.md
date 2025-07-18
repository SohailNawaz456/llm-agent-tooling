# Agentic AI SDK Demo

This repository contains Python examples demonstrating how to build intelligent agents using the Agentic AI SDK. It integrates with Gemini or OpenAI-compatible APIs and shows how to:

✅ Build simple agents that follow custom instructions  
✅ Call tools (functions) to fetch dynamic data  
✅ Handle agent contexts and configurations  
✅ Run asynchronous agent workflows in Python

---

## Features

- Simple polite assistant agent example
- Tool calling with user context
- Support for Gemini API via OpenAI-compatible endpoints
- Easy integration with environment variables using `.env`

---

## Requirements

- Python 3.10+
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- Gemini API key or OpenAI API key

---

## How to Run

1. Clone the repo:

    ```bash
    git clone https://github.com/yourusername/agentic-ai-sdk-demo.git
    cd agentic-ai-sdk-demo
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file and add your API key:

    ```
    GEMINI_API_KEY=your_api_key_here
    ```

4. Run the example:

    ```bash
    uv run app.py
    ```

---

## Example Output

User "Sohail" is 25 years old.


Or from the polite assistant:

Sohail, the founder of Pakistan is Muhammad Ali Jinnah. I hope this helps, Sohail!


---

## Author

📝 **SOHAIL NAWAZ**

---

## License

MIT License

