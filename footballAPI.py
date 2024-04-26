from datetime import datetime, timedelta, timezone
import os

import requests
import pytz


api_tz = pytz.timezone("Europe/London")

local_tz = pytz.timezone("Europe/Moscow")


def get_current_datetime_on_api_server():
    london_time = datetime.now(tz=timezone.utc).astimezone(api_tz)
    return london_time


def to_local_datetime(start_date):
    dt = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S")
    return api_tz.localize(dt).astimezone(local_tz)


def get_matches():
    # this is a datetime object with the timezone used by our api
    current_server_time = get_current_datetime_on_api_server()

    # obtaining the next day as python date object
    tomorrow = current_server_time.date() + timedelta(days=1)
    today = current_server_time.date()
    yesterday = current_server_time.date() - timedelta(days=1)
    # setting our API key for auth
    headers = {
        "X-RapidAPI-Key": "3b37b78c84msha8e835899f37b8ap1d71ffjsn882b016592aa",
        "X-RapidAPI-Host": "football-prediction-api.p.rapidapi.com"
    }

    session = requests.Session()
    session.headers = headers

    # setting our query params
    params = {
        "iso_date": today.isoformat(), # python date object should be transformed to ISO format (YYYY-MM-DD)
        "federation": "UEFA",
        "market": "classic"
    }

    prediction_endpoint = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"
    response = session.get(prediction_endpoint, params=params)

    if response.ok:
        json = response.json()
        json["data"].sort(key=lambda p: p["start_date"])
        matches = []
        for match in json["data"]:
            # going to print tab separated start_time, home_team vs away team, prediction @ predicted odds.
            output = "{st}\t{ht} vs {at}\t{p} @ {odd}"

            local_start_time = to_local_datetime(match["start_date"])
            home_team = match["home_team"]
            away_team = match["away_team"]
            prediction = match["prediction"]

            if "odds" in match:
                prediction_odds = match["odds"].get(prediction, None)
            else:
                # user is not able to see odds as it's subscription plan does not support it.
                prediction_odds = None

            matches.append(output.format(st=local_start_time, ht=home_team, at=away_team, p=prediction, odd=prediction_odds))

        return matches
    else:
        print("Bad response from server, status-code: {}".format(response.status_code))
        print(response.content)