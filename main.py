import logging
import logging.handlers
import os
import requests

from dotenv import load_dotenv
load_dotenv()

# Setup logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["WEATHERSTACK_KEY"]
except KeyError:
    SOME_SECRET = None
    logger.error("Weatherstack API key not found in environment variables!")
    # Optionally, you can exit here or handle as needed:
    # raise SystemExit("Missing API key")

if __name__ == "__main__":
    if SOME_SECRET:
        logger.info("Starting weather data fetch from Weatherstack")

        city = "Berlin"
        url = f"http://api.weatherstack.com/current?access_key={SOME_SECRET}&query={city}"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            if "current" in data:
                temperature = data["current"]["temperature"]  # Celsius
                weather_desc = data["current"]["weather_descriptions"][0] if data["current"]["weather_descriptions"] else "No description"
                logger.info(f"Weather in {city}: {temperature}°C, {weather_desc}")
            else:
                error_info = data.get("error", {})
                logger.error(f"API returned an error: {error_info.get('info', error_info)}")

        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")

    else:
        logger.error("No API key available. Exiting script.")
