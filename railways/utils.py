import logging

from railways import constants


def calculate_route_cost(route):
    total_ride_length = 0

    for item in route.items.all():
        total_ride_length += item.track.length

    return constants.COST_PER_KM * total_ride_length


def get_logger(
        name='railways_logger',
        filename='logs/logs.log',
        logging_level=logging.INFO
):
    logger = logging.getLogger(name)
    logger.setLevel(logging_level)

    log_file_handler = logging.FileHandler(filename)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    log_file_handler.setFormatter(formatter)

    logger.addHandler(log_file_handler)

    return logger
