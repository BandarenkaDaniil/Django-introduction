from railways import settings


def calculate_amount(route):
    total_ride_length = 0
    for item in route.items.all():
        total_ride_length += item.track.length

    return settings.COST_PER_KM * total_ride_length
