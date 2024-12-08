# Получение всех мероприятий по API из базы данных

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json, datetime, pprint, aiogram, requests


def events_catalogue_fetch(url_get_events):
    events_database = []
    for api_page in range(100):
        api_page = api_page + 1
        fetch_events = requests.get(url_get_events + '&page=' + str(api_page))
        events_database_temp = fetch_events.json()
        events_database = events_database + events_database_temp['records']
        if events_database_temp['records'] == []:
            break
    return events_database

def offers_catalogue_fetch(url_get_offers):
    offers_database = []
    for api_page in range(100):
        api_page = api_page + 1
        fetch_offers = requests.get(url_get_offers + '&page=' + str(api_page))
        offers_database_temp = fetch_offers.json()
        offers_database = offers_database + offers_database_temp['records']
        if offers_database_temp['records'] == []:
            break
    return offers_database
