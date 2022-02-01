"""
Demo of logging module

Levels:
- Critical
- Error
- Warning
- Info
- Debug
"""
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(message)s",
    filename="logging_demo.log"
)

logging.warning("Program is for demo uses only")


def main():
    logging.info("Starting the program")
    retrieve_data()
    store_data()
    logging.info("Ending the program")


def retrieve_data():
    logging.info("Downloading data")
    data = [1, 2, 3]
    logging.debug(data)


def store_data():
    logging.info("Storing data")
    ...


if __name__ == "__main__":
    main()

