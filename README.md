# RepBot discord Bot
Simple python bot to manually track user reputation on discord
and assign them roles automatically.

## Commands:

### Give reputation to user
```
+rep <discord user> (optional)<rep amount>
```

rep amount defaults to 1 if not provided.

### Remove reputation from user
```
+rep <discord user> (optional)<rep amount>
```

rep amount defaults to 1 if not provided.

### Show user reputation status
```
?rep <discord user>
```
Example Ouput:

`> ?rep @Soykaf`
```yaml
Rank: Good Customer
Reputation: 7
Discount: 15%
```

---

## Installation

you will need python version 3.10+ and this assumes you correctly setup your app on the discord side.

### 1. Download or clone this repo.
```
$ git clone git@github.com:S0yKaf/RepBot.git
```
### 2. Install dependencies.
```
$ python3 -m pip install -U -r requirements.txt
```
### 3. Create the config file.
```
$ cp config.py.example config.py
```
### 4. Setup your config file
```python
CSV_FILE = "rep_data.csv"
BOT_KEY = "YOUR BOT KEY"
ALLOWED_ROLES = ["Weeb"] # Roles allowed to interact with the bot

# Ranks are
# Rep required
# Rank Name
# Discount awarded (in percent)
RANKS = [
    [0, "First Timer", 0],
    [1, "Customer", 0],
    [5, "Good Customer", 15],
    [10, "Big Shot", 30]
]
```
### 5. Run the Bot!
```
$ python3 app.py
```
