# openrouter-selector

LLM connection using OpenRouter with a single library.

## Installation

To install the `openrouter-selector` library, use pip:

```bash
pip install openrouter-selector
```

## Usage

Here is a basic example of how to use the `openrouter-selector` library:

```python
from openrouter_selector import Selector

llm = Selector(model_name="your_model_name", openai_api_key="your_api_key")

# If the API key is defined in the .env file, you can omit the openai_api_key parameter
llm = Selector(model_name="your_model_name")
```
