import requests
import datetime as dt


def highest_price_function():
    end_time = dt.datetime.today()
    start_time = end_time - dt.timedelta(days=7)
    end_datetime = end_time.strftime("%Y-%m-%dT23:00Z")
    start_datetime = start_time.strftime("%Y-%m-%dT00:00Z")

    api_url = "https://dashboard.elering.ee/api/nps/price"
    raw_data = requests.get(
        url = api_url,
        params={"start":start_datetime, "end":end_datetime}
    ).json()

    max_price = {'price': 0, 'place': '', 'time': ''}
    for country in ['ee', 'lv', 'lt']:
        country_data = raw_data['data'][country]
        for d in country_data:
            if d['price'] > max_price['price']:
                max_price['price'] = d['price']
                max_price['place'] = country
                max_datetime = dt.datetime.fromtimestamp(d['timestamp'])
                max_hour = max_datetime.strftime("%Y-%m-%d %H:00")
                max_price['time'] = max_hour
    return max_price
