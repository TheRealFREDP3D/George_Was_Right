# George-was-Right - Environment Variables and Security

## Keep API keys secure in `.env` file

* Store API keys in a separate `.env` file.
* Use environment variables to access API keys.
* Avoid hardcoding API keys in code.
* Use secrets management tools to manage API keys.
  * [python-dotenv](https://python-dotenv.readthedocs.io/en/latest/)

---

## python-dotenv

### .env file

```sh
# .env file
OPENAI_API_KEY=sk-...
SERPAPI_API_KEY=...
```

---

### Python Code

```python
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access API keys using environment variables 
# Examples
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
```
