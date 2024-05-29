def calculate_weekly_hours(daily_hours):
    """
    Calculate total weekly hours based on daily hours.
    Assumes a 5-day work week.

    :param daily_hours: Number of hours worked per day
    :return: Total weekly hours
    """
    return daily_hours * 5


def calculate_monthly_hours(weekly_hours):
    """
    Calculate total monthly hours based on weekly hours.
    Assumes a 4-week month.

    :param weekly_hours: Number of hours worked per week
    :return: Total monthly hours
    """
    return weekly_hours * 4
