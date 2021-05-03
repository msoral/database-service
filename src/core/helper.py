from sqlalchemy import and_


def fetch_ticker_from_id(asset_id: int) -> str:
    pass


def filter_with_date(db_object, query, start_date, end_date):
    if (start_date and end_date) is None:
        return query
    elif (start_date and end_date) is not None:
        return query.filter(
            and_(db_object.date >= start_date, db_object.date <= end_date)
        ).all()
    else:
        print("ERROR! Please use start_date and end_date together.")
