import os
from dotenv import load_dotenv

env = os.getenv("TEST_ENV", "dev")
load_dotenv(f".env.{env}")

BASE_URL=os.getenv("BASE_URL").lower()
EMAIL=os.getenv("EMAIL").lower()
PASSWORD=os.getenv("PASSWORD")
BROWSER=os.getenv("BROWSER").lower()
HEADLESS=os.getenv("HEADLESS", "true").lower() == "true"
if BROWSER not in ["chrome", "firefox", "edge"]:
    raise ValueError(f"Invalid BROWSER value: {BROWSER}. Must be 'chrome', 'firefox', or 'edge'.")