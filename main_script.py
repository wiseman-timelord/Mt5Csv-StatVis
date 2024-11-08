import json
import logging
from scripts.config import Config
from scripts.utility import Utility
from scripts.interface import start_webui

def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    try:
        # Load persistent settings
        with open('./data/persistence.json', 'r') as f:
            persistence_data = json.load(f)

        config = Config(persistence_data)
        utility = Utility(config)

        # Load and process data
        utility.load_and_process_data()

        # Start the WebUI
        start_webui(utility)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()