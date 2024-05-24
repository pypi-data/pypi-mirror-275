---
# Blockmango API Wrapper

This Python package provides a convenient way to interact with the Blockmango API.

## Installation

You can install the package via pip:

```bash
pip install blockmango
```

## Usage

Import the package and create a `Clan` object using your user ID and access token:

```python
import blockmango
from blockmango import clan

clan = blockmango.Clan(user_id="your_id", access_token="your_token")
```

### Example Usage

```python
# Search for a clan by name
clans = clan.searchclan("Nasa")
print(clans)
```

Replace `your_id` and `your_token` with your actual Blockmango user ID and access token.

For more information on available methods and parameters, contact me on discord, darkk.py
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---
