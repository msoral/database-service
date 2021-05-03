import datetime


def get_last_month():
    today = datetime.datetime.today()
    last_month = today - datetime.timedelta(days=30)
    return last_month


def get_ticker_from_id():
    pass