import json, datetime, pprint, aiogram, asyncio, re, locale
import fetch_database as fetch, markups as nav
from datetime import datetime, timedelta, date, time
from aiogram import Bot, types, Dispatcher, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.client.default import DefaultBotProperties

#from aiogram.utils import executor
#from aiogram.contrib.fsm_storage.memory import MemoryStorage

#--------------АРХИВ----------------------

#from geopy.distance import great_circle
#from aiogram.dispatcher import Dispatcher
#from aiogram.dispatcher import FSMContext

#original token
#TOKEN = '5574605767:AAE2Gs61nr-M5YxjRoOxbCu1HY2Eu7AWqb0'
#url_get_events1 = 'https://quintadb.ru/apps/czW6pcM8jlWPy3W5VcLCkm/dtypes/entity/dcOmkhWQPoW4XNcCkJdb9U.json?rest_api_key=cqiNPXW4vcKOkRW6eGB8od&fetch_all=true&per_page=1000'
#URL_GET_ORGS = 'https://quintadb.ru/apps/czW6pcM8jlWPy3W5VcLCkm/dtypes/entity/ddUfldGKrcrikNkCkxdCk4.json?rest_api_key=cqiNPXW4vcKOkRW6eGB8od&fetch_all=true&per_page=1000'
#KEY = '4o4gqatnkrvkd6l575nd62vjs'


#-------------------------------------------------------------
#-----------------------ЗАПУСК БОТА---------------------------

#ТОКЕН ОТ НАСТОЯЩЕГО КАНАЛА:
#TOKEN = '7608059262:AAGEE1CHS_5Usw0DXnFqwwq1wnrBJyz9rUI'

#Токен тестового бота Петя:
TOKEN = '8184756910:AAHrjvfgZChQWajy7VlpBt7hMIJQuRgSSfE'

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
router = Router()
locale.setlocale(locale.LC_ALL, '')



KEY = 'cqiNPXW4vcKOkRW6eGB8od'

CHANNEL_NAME = ' в.Округе | Псков - интересное рядом.'
BOT_NAME = 'в.Округе Псков | Афиша-бот'
BOT_NAME_SIMPLE = 'в.Округе Псков'
CITY_NAME = 'Псков'
CITY_NAME_pr_padezh = 'Пскове'
CHANNEL_LINK = "https://t.me/vokruge_pskov"
BOT_LINK = "https://t.me/vokruge_pskov_bot"
SUPPORT_LINK = "https://t.me/vOkruge_support_bot"
TELEGRAPH_LINK = "https://telegra.ph/Kak-najti-interesnoe-meropriyatie-11-17-2"
NOTSUB_MESSAGE = str('Дорогой пользователь, для получения возможности пользоваться функционалом, Вам необходимо подписаться на канал\n\n' + '<a href="' + CHANNEL_LINK + '">' + CHANNEL_NAME + '</a>' + '\n\nПодписавшись, вы откроете себе доступ к дополнительным обзорам и дайждестам мероприятий города.')
main_menu_text = str(f'Это бот <b>{BOT_NAME_SIMPLE}</b>\n\nЯ помогу вам найти мероприятия и события на ближайшую неделю.' + f'\n\n✨В моей базе информация из десятков источников с самыми интересными событиями города и области. Подборка мероприятий занимает несколько секунд.\n\n💸 Узнавайте о выгодных приобретениях в {CITY_NAME_pr_padezh} с нашей новой функцией "Акции и предложения"' + '\n\n<a href="' + CHANNEL_LINK + '">' + CHANNEL_NAME + '</a>'  + '\n\n📖 ' + '<a href="' + TELEGRAPH_LINK + '">' + "Что такое «в.Округе - интересное рядом»?" + '</a>')
WELCOME_PHOTO = "https://postimg.cc/HcS8cSPL"


print('Бот запущен')
with open("users_logs.txt", "a") as file_data_users:
    cur_time = datetime.now() + timedelta(hours=3)
    logtime = cur_time.strftime("%H:%M:%S")
    file_data_users.write('Бот запущен ' + datetime.now().strftime("%d.%m.%y %H:%M:%S") + '\n')
global user_settings_dict
events_day = 0
#user_pos = (55.75583156779735, 37.61764840796227)
#combined_message = str(' ')
#var_user_latitude_int = float(0.0)
#var_user_longitude_int = float(0.0)

url_get_events = 'https://quintadb.ru/apps/ddP8ovW7PhWRFcS8oVfgfN/dtypes/entity/dcGaNdKcnkaykiW5JdUurN.json?rest_api_key=areK7dQ8ngb4khW5xcTmoD&fetch_all=true&per_page=1000'
url_get_offers = "https://quintadb.ru/apps/ddP8ovW7PhWRFcS8oVfgfN/dtypes/entity/ddPutcICjcWRmFlGPLW5rr.json?rest_api_key=areK7dQ8ngb4khW5xcTmoD&amp;view="
# ПЕРЕМЕННЫЕ КЛЮЧЕЙ БАЗЫ ДАННЫХ МЕРОПРИЯТИЙ
event_name = 'cHW4tdPmjcaz3dRXhcR3eq'
event_ticketlink = 'bHW68ymmndkyo1WONdRczS'
event_mainlink = 'ddJmoemgvdSykgWPzSzCol'
event_start_time = 'b7W43dJ8npWPfLWR5mWQng'
event_end_time = 'adW4GCW5vfW4xdLumWWQ1E'
mod_check = 'dcTSoZiv1mW6mjcSoGCSk9'
event_price = 'aeW73dU8nhWPqLW6WvW4Tx'
event_type = 'bAEImNjmjoWPDrg0pcSmkv'
event_desc = 'bNWOxdHH1dJOoPW5ZdRmkJ'
event_age = 'c0WR1IWRrpcOk8WOBdKSkW'
event_category = 'ddNuKnW71pWPaUp8oQpmoh'
event_org = 'ddO8kQtdDcTjtcVGqCt8kq'
event_lat = 'bce8oTWQfbWRVcKSk0W5CE'
event_long = 'dcN8oLoCjoWRqonsBcSCos'
event_orglink = 'ddRSkgvc1fWQ8oD8o7WRHu'
event_pay_type = 'ciymodeKHcHkb2sSk7WQ8u'
event_add_type = 'cEyWtdMWzdWOjju3C_iSo3'
event_google = 'cuiSkhW5rid4o6W4KCCqfx'
event_set_google = 'bWW5xcHXrftk3cOCoJWRui'
event_yandex = "cipHhcHmnbW6HEWPBcQmoc"
event_set_yandex = "dcRCk2oxPcH4kuBmoIumks"
event_set_lat = 'dcTuRcO15bb4o4EeRcUCoy'
event_set_long = 'bsW71rWPzoWQGJzmkVWPWw'
event_phone = "bVzaxdUmnaWR5DW5ZcUmkr"
event_photo = 'cwgmoxoavcW6SJzehdV8o6'
paginate_end_photo_old = "https://static.tildacdn.com/tild3866-3732-4935-b261-636634306263/events_final.jpg"
paginate_end_photo = "https://i.postimg.cc/wTHRYDSc/events-final.jpg"
#---------- ПЕРЕМЕННЫЕ БАЗЫ ДАННЫХ АКЦИЙ--------------
offer_category = "amW6idW7revykGDCkbW5qv"
offer_desc = "crFfqzW7PfWRXNvWlcHLrz"
offer_startdate = "b0dmoFx8nfWQ3dV8o2WPHX"
offer_enddate = "avW5OrWQLfniomW6BcSv06"
offer_orgname = "coW4tcGmnkW6S-FsVdRcfz"
offer_location_google = "cXWOBcNCjgW6HMW4BdL8ka"
offer_location_yandex = "ddGYOjW6zcGQXbWQbWWPjF"
offer_link = "cAjmoDWPjlaz3dKK7dMmox"
offer_photo = "bYW7ddI8jfrRlcKYizWQWH_original"

# ЗАПИСЬ ЛОГОВ В ФАЙЛ
def file_log(logtext):
    with open("users_logs.txt", mode="a") as file_data_users:
        cur_time = datetime.now() + timedelta(hours=3)
        logtime = cur_time.strftime("%H:%M:%S")
        file_data_users.write(logtime + ' ' + logtext + '\n')

# УЧЕТ ПОЛЬЗОВАТЕЛЕЙ В ФАЙЛ
def file_users(username):
    users = open('users.txt', mode='r+', encoding='utf-8')
    readingfile = users.readlines()
    isinlist = 0
    for line in readingfile:
        if username+'\n' == line:
            isinlist = 1
            break
    if isinlist == 0:
        users.write(username + "\n")
    users.close()

# СОСТОЯНИЯ И НАСТРОЙКИ ПОЛЬЗОВАТЕЛЯ
class user_settings(StatesGroup):
    event_category = State()
    event_day = State()
    body = State()
    part = State()
    photos = State()
    events_counter = State()
    stats_counter = State()
    offers_category = State()
    offers_type = State()

# ФУНКЦИЯ ВЫЗОВА ВРЕМЕНИ СО СМЕЩЕНИЕМ
async def timeadjust():
    adjust_time = datetime.today() + timedelta(hours=3)
    final_date_str = adjust_time.strftime("%Y-%m-%d")
    final_date = datetime.strptime(final_date_str, "%Y-%m-%d")
    today = final_date.date()
    return today

@router.message(Command("start"))
async def start(message: Message, state = FSMContext):
    result = await bot.get_chat_member(chat_id='@vokruge_pskov', user_id=message.from_user.id)
    if result.status == 'left':
        print(str(message.from_user.username) + ' Статус:' + str(result.status)+ ' не подписан')
        await message.answer(NOTSUB_MESSAGE, reply_markup=await nav.subMenu(), disable_web_page_preview=True)
    else:
        await state.clear()
        print(str(message.from_user.username) + ' Статус:' + str(result.status) + ' приступил к работе')
        file_log(logtext=f'{str(message.from_user.username)} нажал команду /start')
        await bot.send_photo(message.from_user.id, photo=WELCOME_PHOTO, caption=f'{message.from_user.first_name}, привет!' + '\n' + '\n' +\
          f'Это бот <b>{BOT_NAME_SIMPLE}</b>\n\nЯ помогу вам найти мероприятия и события на ближайшую неделю.' +\
          f'\n\n✨В моей базе информация из десятков источников с самыми интересными событиями города и области.'+\
          'Подборка мероприятий занимает несколько секунд.'+f'\n\n💸 Узнавайте о выгодных приобретениях в '+\
          f'{CITY_NAME_pr_padezh} с нашей новой функцией "Акции и предложения"' + '\n\n📖 ' + '<a href="' +\
          TELEGRAPH_LINK + '">' + "Что такое «в.Округе - интересное рядом»?" + '</a>',reply_markup=await nav.mainMenu())

@router.callback_query(F.data=="main_menu")
async def main_menu(callback: CallbackQuery, state: FSMContext):
    result = await bot.get_chat_member(chat_id='@vokruge_pskov', user_id=callback.from_user.id)
    if result.status == 'left':
       print(str(callback.from_user.username) + ' Статус:' + str(result.status) + ' не подписан')
       await callback.message.edit_text(NOTSUB_MESSAGE, reply_markup=await nav.subMenu(),
                              disable_web_page_preview=True)
    else:
        await state.clear()
        print(str(callback.from_user.username) + ' Статус:' + str(result.status) + ' Перешел в главное меню')
        print(str(callback.from_user.username) + ' Перешел в главное меню')
        file_log(logtext=f'{str(callback.from_user.username)} перешел в Главное меню')
        await callback.message.delete()
        await bot.send_photo(callback.from_user.id, photo=WELCOME_PHOTO, caption=main_menu_text, reply_markup=await nav.mainMenu())

@router.callback_query(F.data=="show_events_sub")
async def events_category(callback: CallbackQuery, state: FSMContext):
    print(f'{str(callback.from_user.username)} нажал "Искать мероприятия"')
    file_log(logtext=f'{str(callback.from_user.username)} нажал Искать мероприятия')
    await callback.message.delete()
    await callback.message.answer(f"<b>Выберите категорию мероприятий</b>\n\n<b>🗂 Категории:</b>\n\n<b>Все</b> - все мероприятия, кроме детских и выставок с возможностью выбора дня\n\n<b>🆓 Бесплатные</b> - все бесплатные мероприятия на неделю\n<b>🧒 Детские</b> - только детские и семейные мероприятия на неделю\n<b>🖼 Выставки</b> - проходящие сейчас выставки и экспозиции",\
               reply_markup = await nav.navMenu_category_choose())
    await state.set_state(user_settings.event_day)


#-------------------------------------------------------------
#---------------РЕЖИМ НАСТРОЕК КАТЕГОРИИ И ДНЯ----------------
#-------------------------------------------------------------


@router.callback_query(F.data=='Все')
async def events_day(callback: CallbackQuery, state: FSMContext):
    await state.update_data(event_category=callback.data)
    user_settings_dict = await state.get_data()
    if user_settings_dict['event_category'] == 'Все':
        print(f'{str(callback.from_user.username)} Выбрал категорию Все')
        file_log(logtext=f'{str(callback.from_user.username)} выбрал категорию Все')
        await callback.message.edit_text(f'<b>Вы выбрали категорию "Все мепроприятия"' +\
            "\n\nВыберите день:</b>\n\n<b>🔥️ Если вы ищите на сегодня:</b>\n\nОтображаться будут только те события, время окончания которых еще не наступило.\n\n<b>🔥 Успевайте бронировать места:</b>\nРегистрация на мероприятия, особенно бесплатные, часто очень быстро заканчивается. Рекомендуем просматривать афишу на пять-шесть дней вперед, ведь тогда шанс найти места на интересные события больше.", reply_markup = await nav.navMenu_day_choose())
        await state.set_state(user_settings.event_day)

#----------------------------ОКОНЧАНИЕ РЕЖИМА НАСТРОЕК ---------------------------------------------
#----------------------РЕЖИМ СБОРКИ СООБЩЕНИЯ В ВИДЕ КАТАЛОГА --------------------------------------

@router.callback_query(user_settings.event_day)
async def show_events(callback: CallbackQuery, state: FSMContext):
    user_settings_dict = await state.get_data()
    try:
        if user_settings_dict['event_category'] == 'Все':
            await state.update_data(event_day=callback.data)
            print(f'{str(callback.from_user.username)} выбрал день {callback.data}')
    except:
        await state.update_data(event_category=callback.data)
        user_settings_dict = await state.get_data()
        print(f'{str(callback.from_user.username)} Выбрал категорию {user_settings_dict["event_category"]}')
        file_log(logtext=f'{str(callback.from_user.username)} выбрал категорию {user_settings_dict["event_category"]}')
        await state.update_data(event_day='Неопределено')
    print(str(callback.from_user.username) + ' запросил поиск по каталогу')
    file_log(logtext=f'{str(callback.from_user.username)} начал поиск в категории {user_settings_dict["event_category"]}')
    await callback.message.edit_text('⏳Подбираем мероприятия для вас...\nПожалуйста, подождите', reply_markup=await nav.mainMenu_inst())
    global events_day, event_day, list_fin, events_sorted
    list_fin = 0
    events_fin = []
    combined_message = ''
    now = (datetime.now() + timedelta(hours=3))
    events_check = fetch.events_catalogue_fetch(url_get_events)
    user_settings_dict = await state.get_data()
    if user_settings_dict['event_category'] == 'Выставки':
        for i in range(len(events_check)):
            if events_check[i]['values'][mod_check] != 'Не проверено':
                events_fin.append(events_check[i])
        events_sorted = sorted(events_fin, key=lambda x: datetime.strptime(x['values'][event_end_time], "%d.%m.%y %H:%M:%S"))
    if user_settings_dict['event_category'] != 'Выставки':
        for i in range(len(events_check)):
            if events_check[i]['values'][mod_check] != 'Не проверено':
                events_fin.append(events_check[i])
        events_sorted = sorted(events_fin,key=lambda x: datetime.strptime(x['values'][event_start_time], "%d.%m.%y %H:%M:%S"))

    if user_settings_dict['event_category'] != 'Выставки':
        #if user_settings_dict['event_day'] != 'Неопределено':
            combined_message = str('Список найденных мероприятий в категории ' + user_settings_dict['event_category'] + '\n' +'\n')
    #if user_settings_dict['event_day'] == 'Неопределено':
    if user_settings_dict['event_category'] == 'Выставки':
        combined_message = str('Список найденных выставок в базе:' + '\n' +'\n')
        # ------------------------ ВЫВОД СПИСКА МЕРОПРИЯТИЙ НА ТЕКУЩИЙ ДЕНЬ С ОТСЕЧЕНИЕМ ПРОЙДЕННЫХ
    today = await timeadjust()
    if str(user_settings_dict['event_day']) != "Неопределено":

        if str(today) == str(user_settings_dict['event_day']):
            event_day = today + timedelta(days=0)
        elif str(today + timedelta(days=1)) == str(user_settings_dict['event_day']):
            event_day = today + timedelta(days=1)
        elif str(today + timedelta(days=2)) == str(user_settings_dict['event_day']):
            event_day = today + timedelta(days=2)
        elif str(today + timedelta(days=3)) == str(user_settings_dict['event_day']):
            event_day = today + timedelta(days=3)
        elif str(today + timedelta(days=4)) == str(user_settings_dict['event_day']):
            event_day = today + timedelta(days=4)
        elif str(today + timedelta(days=5)) == str(user_settings_dict['event_day']):
            event_day = today + timedelta(days=5)
        elif str(today + timedelta(days=6)) == str(user_settings_dict['event_day']):
            event_day = today + timedelta(days=6)
        elif str(today + timedelta(days=7)) == str(user_settings_dict['event_day']):
            event_day = today + timedelta(days=7)
    else:
        event_day = today
    counter_temp = 0
    await state.update_data(events_counter=0)
    for session in events_sorted:
        counter_temp += 1
        session_starttime = datetime.strptime(session['values'][event_start_time], "%d.%m.%y %H:%M:%S")
        session_endtime = datetime.strptime(session['values'][event_end_time], "%d.%m.%y %H:%M:%S")
        session_start = datetime.strptime(session['values'][event_start_time], "%d.%m.%y %H:%M:%S")
        session_end = datetime.strptime(session['values'][event_end_time], "%d.%m.%y %H:%M:%S")
        session_end_date = datetime(session_end.year, session_end.month, session_end.day)
        curr_date = datetime(now.year, now.month, now.day)
        global events_count
        # ------------------------------ ВЫВОД МЕРОПРИЯТИЙ ТОЛЬКО НА СЕГОДНЯ
        if session['values'][event_phone] != 'Отсутствует':
            phone_number = '\n☎️ Телефон: '+session['values'][event_phone]
        else:
            phone_number = ''

        if user_settings_dict['event_category'] != 'Бесплатные':  # ВСЕ КАТЕГОРИИ КРОМЕ БЕСПЛАТНЫХ
            if datetime.fromisoformat(event_day.strftime("%Y-%m-%d")) == datetime.fromisoformat(
                    session_starttime.strftime("%Y-%m-%d")):
                if now.date() == event_day:
                    if session_end.time() > now.time() and session_end.date() == now.date() or session_end.date() != now.date():
                        if session['values'][event_add_type] == 'Основной адрес':
                            google_url = (session['values'][event_yandex])
                        else:
                            google_url = (session['values'][event_set_yandex])
                        if str(session['values'][event_category]) == user_settings_dict['event_category'] or \
                                user_settings_dict['event_category'] == 'Все':
                            if str(session['values'][event_category]) != 'Выставки':
                                    if str(session['values'][event_category]) != 'Детские':
                                        if str(session['values'][event_pay_type]) != 'Свободный вход':
                                            if str(session['values'][event_pay_type]) == 'Платно':
                                                if session["values"][event_price] == '0':
                                                    combined_message += str(
                                                        f'<a href="' + session["values"][event_mainlink] + f'">' +
                                                        session['values'][event_name] + f'</a>' + '\n' +
                                                        session["values"][
                                                            event_type] + ' ' + session['values'][
                                                            event_age] + ' ' + '\n' + '🗓 ' + str(
                                                            session_starttime.strftime("%d.%m")) + ' ' + str(
                                                            session_starttime.strftime("%H:%M")) + ' - ' + str(
                                                            session_endtime.strftime(
                                                                "%H:%M")) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                        session["values"][event_ticketlink] + f'">' +
                                                        f'Платно' + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                        session["values"][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                                else:
                                                    combined_message += str(
                                                        f'<a href="' + session["values"][event_mainlink] + f'">' +
                                                        session['values'][event_name] + f'</a>' + '\n' + session["values"][
                                                            event_type] + ' ' + session['values'][
                                                            event_age] + ' ' + '\n' + '🗓 ' + str(
                                                            session_starttime.strftime("%d.%m")) + ' ' + str(
                                                            session_starttime.strftime("%H:%M")) + ' - ' + str(
                                                            session_endtime.strftime(
                                                                "%H:%M")) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                        session["values"][event_ticketlink] + f'">' +
                                                        f'От {session["values"][event_price]}р' + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                        session["values"][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                            else:
                                                combined_message += str(
                                                    f'<a href="' + session["values"][event_mainlink] + f'">' +
                                                    session['values'][event_name] + f'</a>' + '\n' + session["values"][
                                                        event_type] + ' ' + session['values'][
                                                        event_age] + ' ' + '\n' + '🗓 ' + str(
                                                        session_starttime.strftime("%d.%m")) + ' ' + str(
                                                        session_starttime.strftime("%H:%M")) + ' - ' + str(
                                                        session_endtime.strftime(
                                                            "%H:%M")) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                    session["values"][event_ticketlink] + f'">' +
                                                    session["values"][
                                                        event_pay_type] + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                    session["values"][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                            counter_data = await state.get_data()
                                            await state.update_data(events_counter=int(counter_data['events_counter'])+1)
                                            counter_data = await state.get_data()
                                        else:
                                            combined_message += str(
                                                f'<a href="' + session["values"][event_mainlink] + f'">' +
                                                session["values"][event_name] + f'</a>' + '\n' + session["values"][
                                                    event_type] + ' ' + session["values"][event_age] + ' ' + '\n' +
                                                '🗓 ' + str(session_starttime.strftime("%d.%m")) + ' ' + str(
                                                    session_starttime.strftime("%H:%M")) + ' - ' + str(
                                                    session_endtime.strftime("%H:%M")) + '\n' + '🎟' + ' ' +
                                                session["values"][
                                                    event_pay_type] + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                session["values"][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                            counter_data = await state.get_data()
                                            await state.update_data(events_counter=int(counter_data['events_counter']) + 1)
                                            counter_data = await state.get_data()
                                        if counter_data['events_counter'] == 5:
                                            combined_message += '🔹'
                                            await state.update_data(events_counter=0)
                                    # if user_settings_dict['event_category'] == 'Детские':
                                    #     if str(session['values'][event_pay_type]) != 'Свободный вход':
                                    #         if str(session['values'][event_pay_type]) == 'Платно':
                                    #             if session["values"][event_price] == '0':
                                    #                 combined_message += str(
                                    #                     f'<a href="' + session["values"][event_mainlink] + f'">' +
                                    #                     session['values'][event_name] + f'</a>' + '\n' +
                                    #                     session['values'][
                                    #                         event_type] + ' ' + session['values'][
                                    #                         event_age] + ' ' + '\n' + '🗓 ' + str(
                                    #                         session_starttime.strftime('%d.%m')) + ' ' + str(
                                    #                         session_starttime.strftime('%H:%M')) + ' - ' + str(
                                    #                         session_endtime.strftime(
                                    #                             '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                    #                     session['values'][event_ticketlink] + f'">' +
                                    #                     f'Платно' + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                    #                     session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                    #             else:
                                    #                 combined_message += str(
                                    #                     f'<a href="' + session["values"][event_mainlink] + f'">' +
                                    #                     session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                    #                         event_type] + ' ' + session['values'][
                                    #                         event_age] + ' ' + '\n' + '🗓 ' + str(
                                    #                         session_starttime.strftime('%d.%m')) + ' ' + str(
                                    #                         session_starttime.strftime('%H:%M')) + ' - ' + str(
                                    #                         session_endtime.strftime(
                                    #                             '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                    #                     session['values'][event_ticketlink] + f'">' +
                                    #                     f'От {session["values"][event_price]}р' + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                    #                     session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                    #         else:
                                    #             combined_message += str(
                                    #                 f'<a href="' + session["values"][event_mainlink] + f'">' +
                                    #                 session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                    #                     event_type] + ' ' + session['values'][
                                    #                     event_age] + ' ' + '\n' + '🗓 ' + str(
                                    #                     session_starttime.strftime('%d.%m')) + ' ' + str(
                                    #                     session_starttime.strftime('%H:%M')) + ' - ' + str(
                                    #                     session_endtime.strftime(
                                    #                         '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                    #                 session['values'][event_ticketlink] + f'">' +
                                    #                 session['values'][
                                    #                     event_pay_type] + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                    #                 session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                    #         counter_data = await state.get_data()
                                    #         await state.update_data(events_counter=int(counter_data['events_counter']) + 1)
                                    #         counter_data = await state.get_data()
                                    #     else:
                                    #         combined_message += str(
                                    #             f'<a href="' + session['values'][event_mainlink] + f'">' +
                                    #             session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                    #                 event_type] + ' ' + session['values'][event_age] + ' ' + '\n' +
                                    #             '🗓 ' + str(session_starttime.strftime('%d.%m')) + ' ' + str(
                                    #                 session_starttime.strftime('%H:%M')) + ' - ' + str(
                                    #                 session_endtime.strftime('%H:%M')) + '\n' + '🎟' + ' ' +
                                    #             session['values'][
                                    #                 event_pay_type] + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                    #             session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                    #         counter_data = await state.get_data()
                                    #         await state.update_data(events_counter=int(counter_data['events_counter']) + 1)
                                    #         counter_data = await state.get_data()
                                    #     if counter_data['events_counter'] == 5:
                                    #         combined_message += '🔹'
                                    #         await state.update_data(events_counter=0)
        if user_settings_dict['event_category'] == 'Бесплатные':
            if datetime.fromisoformat(event_day.strftime("%Y-%m-%d")) == datetime.fromisoformat(
                    session_starttime.strftime("%Y-%m-%d")):
                if now.date() == event_day:
                    if session_end.time() > now.time():
                        if session['values'][event_add_type] == 'Основной адрес':
                            google_url = (session['values'][event_yandex])
                        else:
                            google_url = (session['values'][event_set_yandex])
                        if str(session['values'][event_pay_type]) != 'Платно':
                            if str(session['values'][event_category]) != 'Выставки':
                                if str(session['values'][event_category]) != 'Многодневные':
                                    if str(session['values'][event_category]) != 'Детские':
                                        if str(session['values'][event_pay_type]) != 'Свободный вход':
                                            if str(session['values'][event_pay_type]) == 'Платно':
                                                if session["values"][event_price] == '0':
                                                    combined_message += str(
                                                        f'<a href="' + session['values'][event_mainlink] + f'">' +
                                                        session['values'][event_name] + f'</a>' + '\n' +
                                                        session['values'][
                                                            event_type] + ' ' + session['values'][
                                                            event_age] + ' ' + '\n' + '🗓 ' + str(
                                                            session_starttime.strftime('%d.%m')) + ' ' + str(
                                                            session_starttime.strftime('%H:%M')) + ' - ' + str(
                                                            session_endtime.strftime(
                                                                '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                        session['values'][event_ticketlink] + f'">' +
                                                        f'Платно' + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                        session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                                else:
                                                    combined_message += str(
                                                        f'<a href="' + session['values'][event_mainlink] + f'">' +
                                                        session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                                            event_type] + ' ' + session['values'][
                                                            event_age] + ' ' + '\n' + '🗓 ' + str(
                                                            session_starttime.strftime('%d.%m')) + ' ' + str(
                                                            session_starttime.strftime('%H:%M')) + ' - ' + str(
                                                            session_endtime.strftime(
                                                                '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                        session['values'][event_ticketlink] + f'">' +
                                                        f'От {session["values"][event_price]}р' + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                        session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                            else:
                                                combined_message += str(
                                                    f'<a href="' + session['values'][event_mainlink] + f'">' +
                                                    session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                                        event_type] + ' ' + session['values'][
                                                        event_age] + ' ' + '\n' + '🗓 ' + str(
                                                        session_starttime.strftime('%d.%m')) + ' ' + str(
                                                        session_starttime.strftime('%H:%M')) + ' - ' + str(
                                                        session_endtime.strftime(
                                                            '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                    session['values'][event_ticketlink] + f'">' +
                                                    session['values'][
                                                        event_pay_type] + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                    session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                            counter_data = await state.get_data()
                                            await state.update_data(events_counter=int(counter_data['events_counter']) + 1)
                                            counter_data = await state.get_data()
                                        else:
                                            combined_message += str(
                                                f'<a href="' + session['values'][event_mainlink] + f'">' +
                                                session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                                    event_type] + ' ' + session['values'][event_age] + ' ' + '\n' +
                                                '🗓 ' + str(session_starttime.strftime('%d.%m')) + ' ' + str(
                                                    session_starttime.strftime('%H:%M')) + ' - ' + str(
                                                    session_endtime.strftime('%H:%M')) + '\n' + '🎟' + ' ' +
                                                session['values'][
                                                    event_pay_type] + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                            counter_data = await state.get_data()
                                            await state.update_data(events_counter=int(counter_data['events_counter']) + 1)
                                            counter_data = await state.get_data()
                                        if counter_data['events_counter'] == 5:
                                            combined_message += '🔹'
                                            await state.update_data(events_counter=0)
                                    if user_settings_dict['event_category'] == 'Детские':
                                        if str(session['values'][event_pay_type]) != 'Свободный вход':
                                            if str(session['values'][event_pay_type]) == 'Платно':
                                                if session["values"][event_price] == '0':
                                                    combined_message += str(
                                                        f'<a href="' + session['values'][event_mainlink] + f'">' +
                                                        session['values'][event_name] + f'</a>' + '\n' +
                                                        session['values'][
                                                            event_type] + ' ' + session['values'][
                                                            event_age] + ' ' + '\n' + '🗓 ' + str(
                                                            session_starttime.strftime('%d.%m')) + ' ' + str(
                                                            session_starttime.strftime('%H:%M')) + ' - ' + str(
                                                            session_endtime.strftime(
                                                                '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                        session['values'][event_ticketlink] + f'">' +
                                                        f'Платно' + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                        session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                                else:
                                                    combined_message += str(
                                                        f'<a href="' + session['values'][event_mainlink] + f'">' +
                                                        session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                                            event_type] + ' ' + session['values'][
                                                            event_age] + ' ' + '\n' + '🗓 ' + str(
                                                            session_starttime.strftime('%d.%m')) + ' ' + str(
                                                            session_starttime.strftime('%H:%M')) + ' - ' + str(
                                                            session_endtime.strftime(
                                                                '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                        session['values'][event_ticketlink] + f'">' +
                                                        f'От {session["values"][event_price]}р' + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                        session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                            else:
                                                combined_message += str(
                                                    f'<a href="' + session['values'][event_mainlink] + f'">' +
                                                    session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                                        event_type] + ' ' + session['values'][
                                                        event_age] + ' ' + '\n' + '🗓 ' + str(
                                                        session_starttime.strftime('%d.%m')) + ' ' + str(
                                                        session_starttime.strftime('%H:%M')) + ' - ' + str(
                                                        session_endtime.strftime(
                                                            '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                    session['values'][event_ticketlink] + f'">' +
                                                    session['values'][
                                                        event_pay_type] + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                    session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                            counter_data = await state.get_data()
                                            await state.update_data(events_counter=int(counter_data['events_counter']) + 1)
                                            counter_data = await state.get_data()
                                        else:
                                            combined_message += str(
                                                f'<a href="' + session['values'][event_mainlink] + f'">' +
                                                session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                                    event_type] + ' ' + session['values'][event_age] + ' ' + '\n' +
                                                '🗓 ' + str(session_starttime.strftime('%d.%m')) + ' ' + str(
                                                    session_starttime.strftime('%H:%M')) + ' - ' + str(
                                                    session_endtime.strftime('%H:%M')) + '\n' + '🎟' + ' ' +
                                                session['values'][
                                                    event_pay_type] + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                            counter_data = await state.get_data()
                                            await state.update_data(events_counter=int(counter_data['events_counter']) + 1)
                                            counter_data = await state.get_data()
                                        if counter_data['events_counter'] == 5:
                                            combined_message += '🔹'
                                            await state.update_data(events_counter=0)

        # ------------------------------ ВЫВОД МЕРОПРИЯТИЙ НА ЛЮБОЙ ДЕНЬ
        if now.date() != event_day:
            if user_settings_dict['event_category'] != 'Бесплатные':  # ТОЛЬКО ПЛАТНЫЕ
                if datetime.fromisoformat(event_day.strftime("%Y-%m-%d")) == datetime.fromisoformat(
                        session_starttime.strftime("%Y-%m-%d")):
                    if session['values'][event_add_type] == 'Основной адрес':
                        google_url = (session['values'][event_yandex])
                    else:
                        google_url = (session['values'][event_set_yandex])
                    if str(session['values'][event_category]) == user_settings_dict['event_category'] or \
                            user_settings_dict['event_category'] == 'Все':  # СООТВЕТСТВИЕ КАТЕГОРИИ ИЛИ ВСЕ
                        if str(session['values'][event_category]) != 'Выставки':  # НЕ ВЫСТАВКИ
                                if str(session['values'][event_category]) != 'Детские':  # НЕ ДЕТСКИЕ
                                    if str(session['values'][event_pay_type]) != 'Свободный вход':
                                        if str(session['values'][event_pay_type]) == 'Платно':
                                            if session["values"][event_price] == '0':
                                                combined_message += str(
                                                    f'<a href="' + session['values'][event_mainlink] + f'">' +
                                                    session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                                        event_type] + ' ' + session['values'][
                                                        event_age] + ' ' + '\n' + '🗓 ' + str(
                                                        session_starttime.strftime('%d.%m')) + ' ' + str(
                                                        session_starttime.strftime('%H:%M')) + ' - ' + str(
                                                        session_endtime.strftime(
                                                            '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                    session['values'][event_ticketlink] + f'">' +
                                                    f'Платно' + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                    session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                            else:
                                                combined_message += str(
                                                    f'<a href="' + session['values'][event_mainlink] + f'">' +
                                                    session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                                        event_type] + ' ' + session['values'][
                                                        event_age] + ' ' + '\n' + '🗓 ' + str(
                                                        session_starttime.strftime('%d.%m')) + ' ' + str(
                                                        session_starttime.strftime('%H:%M')) + ' - ' + str(
                                                        session_endtime.strftime(
                                                            '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                    session['values'][event_ticketlink] + f'">' +
                                                    f'От {session["values"][event_price]}р' + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                    session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                        else:
                                            combined_message += str(
                                                f'<a href="' + session['values'][event_mainlink] + f'">' +
                                                session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                                    event_type] + ' ' + session['values'][
                                                    event_age] + ' ' + '\n' + '🗓 ' + str(
                                                    session_starttime.strftime('%d.%m')) + ' ' + str(
                                                    session_starttime.strftime('%H:%M')) + ' - ' + str(
                                                    session_endtime.strftime(
                                                        '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                session['values'][event_ticketlink] + f'">' +
                                                session['values'][
                                                    event_pay_type] + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                        counter_data = await state.get_data()
                                        await state.update_data(events_counter=int(counter_data['events_counter']) + 1)
                                        counter_data = await state.get_data()
                                    else:
                                        combined_message += str(
                                            f'<a href="' + session['values'][event_mainlink] + f'">' +
                                            session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                                event_type] + ' ' + session['values'][event_age] + ' ' + '\n' +
                                            '🗓 ' + str(session_starttime.strftime('%d.%m')) + ' ' + str(
                                                session_starttime.strftime('%H:%M')) + ' - ' + str(
                                                session_endtime.strftime('%H:%M')) + '\n' + '🎟' + ' ' +
                                            session['values'][
                                                event_pay_type] + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                            session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                        counter_data = await state.get_data()
                                        await state.update_data(events_counter=int(counter_data['events_counter'])+1)
                                        counter_data = await state.get_data()
                                    if counter_data['events_counter'] == 5:
                                        combined_message += '🔹'
                                        await state.update_data(events_counter=0)
                                # if user_settings_dict['event_category'] == 'Детские':
                                #     if str(session['values'][event_pay_type]) != 'Свободный вход':
                                #         if str(session['values'][event_pay_type]) == 'Платно':
                                #             if session["values"][event_price] == '0':
                                #                 combined_message += str(
                                #                     f'<a href="' + session['values'][event_mainlink] + f'">' +
                                #                     session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                #                         event_type] + ' ' + session['values'][
                                #                         event_age] + ' ' + '\n' + '🗓 ' + str(
                                #                         session_starttime.strftime('%d.%m')) + ' ' + str(
                                #                         session_starttime.strftime('%H:%M')) + ' - ' + str(
                                #                         session_endtime.strftime(
                                #                             '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                #                     session['values'][event_ticketlink] + f'">' +
                                #                     f'Платно' + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                #                     session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                #             else:
                                #                 combined_message += str(
                                #                     f'<a href="' + session['values'][event_mainlink] + f'">' +
                                #                     session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                #                         event_type] + ' ' + session['values'][
                                #                         event_age] + ' ' + '\n' + '🗓 ' + str(
                                #                         session_starttime.strftime('%d.%m')) + ' ' + str(
                                #                         session_starttime.strftime('%H:%M')) + ' - ' + str(
                                #                         session_endtime.strftime(
                                #                             '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                #                     session['values'][event_ticketlink] + f'">' +
                                #                     f'От {session["values"][event_price]}р' + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                #                     session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                #         else:
                                #             combined_message += str(
                                #                 f'<a href="' + session['values'][event_mainlink] + f'">' +
                                #                 session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                #                     event_type] + ' ' + session['values'][
                                #                     event_age] + ' ' + '\n' + '🗓 ' + str(
                                #                     session_starttime.strftime('%d.%m')) + ' ' + str(
                                #                     session_starttime.strftime('%H:%M')) + ' - ' + str(
                                #                     session_endtime.strftime(
                                #                         '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                #                 session['values'][event_ticketlink] + f'">' +
                                #                 session['values'][
                                #                     event_pay_type] + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                #                 session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                #         counter_data = await state.get_data()
                                #         await state.update_data(events_counter=int(counter_data['events_counter']) + 1)
                                #         counter_data = await state.get_data()
                                #     else:
                                #         combined_message += str(
                                #             f'<a href="' + session['values'][event_mainlink] + f'">' +
                                #             session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                #                 event_type] + ' ' + session['values'][event_age] + ' ' + '\n' +
                                #             '🗓 ' + str(session_starttime.strftime('%d.%m')) + ' ' + str(
                                #                 session_starttime.strftime('%H:%M')) + ' - ' + str(
                                #                 session_endtime.strftime('%H:%M')) + '\n' + '🎟' + ' ' +
                                #             session['values'][
                                #                 event_pay_type] + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                #             session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                #         counter_data = await state.get_data()
                                #         await state.update_data(events_counter=int(counter_data['events_counter']) + 1)
                                #         counter_data = await state.get_data()
                                #     if counter_data['events_counter'] == 5:
                                #         combined_message += '🔹'
                                #         await state.update_data(events_counter=0)
            else:  # ТОЛЬКО БЕСПЛАТНЫЕ
                if datetime.fromisoformat(event_day.strftime("%Y-%m-%d")) == datetime.fromisoformat(
                        session_starttime.strftime("%Y-%m-%d")):
                    if session['values'][event_add_type] == 'Основной адрес':
                        google_url = (session['values'][event_yandex])
                    else:
                        google_url = (session['values'][event_set_yandex])
                    if str(session['values'][event_pay_type]) != 'Платно':  # ВСЕ БЕСПЛАТНЫЕ
                        if str(session['values'][event_category]) != 'Выставки':  # НЕ ВЫСТАВКИ
                            if str(session['values'][event_category]) != 'Многодневные':
                                if str(session['values'][event_category]) != 'Детские':  # НЕ ДЕТСКИЕ
                                    if str(session['values'][event_pay_type]) != 'Свободный вход':
                                        if str(session['values'][event_pay_type]) == 'Платно':
                                            if session["values"][event_price] == '0':
                                                combined_message += str(
                                                    f'<a href="' + session['values'][event_mainlink] + f'">' +
                                                    session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                                        event_type] + ' ' + session['values'][
                                                        event_age] + ' ' + '\n' + '🗓 ' + str(
                                                        session_starttime.strftime('%d.%m')) + ' ' + str(
                                                        session_starttime.strftime('%H:%M')) + ' - ' + str(
                                                        session_endtime.strftime(
                                                            '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                    session['values'][event_ticketlink] + f'">' +
                                                    f'Платно' + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                    session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                            else:
                                                combined_message += str(
                                                    f'<a href="' + session['values'][event_mainlink] + f'">' +
                                                    session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                                        event_type] + ' ' + session['values'][
                                                        event_age] + ' ' + '\n' + '🗓 ' + str(
                                                        session_starttime.strftime('%d.%m')) + ' ' + str(
                                                        session_starttime.strftime('%H:%M')) + ' - ' + str(
                                                        session_endtime.strftime(
                                                            '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                    session['values'][event_ticketlink] + f'">' +
                                                    f'От {session["values"][event_price]}р' + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                    session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                        else:
                                            combined_message += str(
                                                f'<a href="' + session['values'][event_mainlink] + f'">' +
                                                session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                                    event_type] + ' ' + session['values'][
                                                    event_age] + ' ' + '\n' + '🗓 ' + str(
                                                    session_starttime.strftime('%d.%m')) + ' ' + str(
                                                    session_starttime.strftime('%H:%M')) + ' - ' + str(
                                                    session_endtime.strftime(
                                                        '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                session['values'][event_ticketlink] + f'">' +
                                                session['values'][
                                                    event_pay_type] + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                        counter_data = await state.get_data()
                                        await state.update_data(events_counter=int(counter_data['events_counter']) + 1)
                                        counter_data = await state.get_data()
                                    else:
                                        combined_message += str(
                                            f'<a href="' + session['values'][event_mainlink] + f'">' +
                                            session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                                event_type] + ' ' + session['values'][event_age] + ' ' + '\n' +
                                            '🗓 ' + str(session_starttime.strftime('%d.%m')) + ' ' + str(
                                                session_starttime.strftime('%H:%M')) + ' - ' + str(
                                                session_endtime.strftime('%H:%M')) + '\n' + '🎟' + ' ' +
                                            session['values'][
                                                event_pay_type] + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                            session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                        counter_data = await state.get_data()
                                        await state.update_data(events_counter=int(counter_data['events_counter']) + 1)
                                        counter_data = await state.get_data()
                                    if counter_data['events_counter'] == 5:
                                        combined_message += '🔹'
                                        await state.update_data(events_counter=0)
                                if user_settings_dict['event_category'] == 'Детские':
                                    if str(session['values'][event_pay_type]) != 'Свободный вход':
                                        if str(session['values'][event_pay_type]) == 'Платно':
                                            if session["values"][event_price] == '0':
                                                combined_message += str(
                                                    f'<a href="' + session['values'][event_mainlink] + f'">' +
                                                    session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                                        event_type] + ' ' + session['values'][
                                                        event_age] + ' ' + '\n' + '🗓 ' + str(
                                                        session_starttime.strftime('%d.%m')) + ' ' + str(
                                                        session_starttime.strftime('%H:%M')) + ' - ' + str(
                                                        session_endtime.strftime(
                                                            '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                    session['values'][event_ticketlink] + f'">' +
                                                    f'Платно' + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                    session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                            else:
                                                combined_message += str(
                                                    f'<a href="' + session['values'][event_mainlink] + f'">' +
                                                    session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                                        event_type] + ' ' + session['values'][
                                                        event_age] + ' ' + '\n' + '🗓 ' + str(
                                                        session_starttime.strftime('%d.%m')) + ' ' + str(
                                                        session_starttime.strftime('%H:%M')) + ' - ' + str(
                                                        session_endtime.strftime(
                                                            '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                    session['values'][event_ticketlink] + f'">' +
                                                    f'От {session["values"][event_price]}р' + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                    session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                        else:
                                            combined_message += str(
                                                f'<a href="' + session['values'][event_mainlink] + f'">' +
                                                session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                                    event_type] + ' ' + session['values'][
                                                    event_age] + ' ' + '\n' + '🗓 ' + str(
                                                    session_starttime.strftime('%d.%m')) + ' ' + str(
                                                    session_starttime.strftime('%H:%M')) + ' - ' + str(
                                                    session_endtime.strftime(
                                                        '%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                session['values'][event_ticketlink] + f'">' +
                                                session['values'][
                                                    event_pay_type] + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                        counter_data = await state.get_data()
                                        await state.update_data(events_counter=int(counter_data['events_counter']) + 1)
                                        counter_data = await state.get_data()
                                    else:
                                        combined_message += str(
                                            f'<a href="' + session['values'][event_mainlink] + f'">' +
                                            session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                                event_type] + ' ' + session['values'][event_age] + ' ' + '\n' +
                                            '🗓 ' + str(session_starttime.strftime('%d.%m')) + ' ' + str(
                                                session_starttime.strftime('%H:%M')) + ' - ' + str(
                                                session_endtime.strftime('%H:%M')) + '\n' + '🎟' + ' ' +
                                            session['values'][
                                                event_pay_type] + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                            session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                        counter_data = await state.get_data()
                                        await state.update_data(events_counter=int(counter_data['events_counter']) + 1)
                                        counter_data = await state.get_data()
                                    if counter_data['events_counter'] == 5:
                                        combined_message += '🔹'
                                        await state.update_data(events_counter=0)

        # ------------------- ВЫВОД ТОЛЬКО ВЫСТАВОК

        if user_settings_dict['event_category'] == 'Выставки':
            if session_end_date >= curr_date:
                if session['values'][event_add_type] == 'Основной адрес':
                    google_url = (session['values'][event_yandex])
                else:
                    google_url = (session['values'][event_set_yandex])
                # ---- ФИЛЬТР КАТЕГОРИИ
                if str(session['values'][event_category]) == 'Выставки':
                    if str(session['values'][event_pay_type]) != 'Свободный вход':
                        if str(session['values'][event_pay_type]) == 'Платно':
                            if session["values"][event_price] == '0':
                                combined_message += str(f'<a href="' +
                                                        session['values'][event_mainlink] + f'">' +
                                                        session['values'][event_name] + f'</a>' + '\n' +
                                                        session['values'][event_type] + ' ' + session['values'][
                                                            event_age] + ' ' + '\n' + '🗓 ' + 'До ' + str(
                                    session_endtime.strftime('%d.%m.%y')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                        session['values'][event_ticketlink] + f'">' +
                                                        f'Платно' + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                        session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                            else:
                                combined_message += str(f'<a href="' +
                                                        session['values'][event_mainlink] + f'">' +
                                                        session['values'][event_name] + f'</a>' + '\n' +
                                                        session['values'][event_type] + ' ' + session['values'][
                                                            event_age] + ' ' + '\n' + '🗓 ' + 'До ' + str(
                                    session_endtime.strftime('%d.%m.%y')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                        session['values'][event_ticketlink] + f'">' +
                                                        f'От {session["values"][event_price]}р' + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                        session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                        else:
                            combined_message += str(f'<a href="' +
                                                    session['values'][event_mainlink] + f'">' +
                                                    session['values'][event_name] + f'</a>' + '\n' +
                                                    session['values'][event_type] + ' ' + session['values'][
                                                        event_age] + ' ' + '\n' + '🗓 ' + 'До ' + str(
                                session_endtime.strftime('%d.%m.%y')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                                    session['values'][event_ticketlink] + f'">' +
                                                    session['values'][
                                                        event_pay_type] + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                    session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                        counter_data = await state.get_data()
                        await state.update_data(events_counter=int(counter_data['events_counter']) + 1)
                        counter_data = await state.get_data()
                    else:
                        combined_message += str(f'<a href="' +
                                                session['values'][event_mainlink] + f'">' +
                                                session['values'][event_name] + f'</a>' + '\n' +
                                                session['values'][event_type] + ' ' + session['values'][
                                                    event_age] + ' ' + '\n' + '🗓 ' + ' До ' + str(
                            session_endtime.strftime('%d.%m.%y')) + '\n' + '🎟' + ' ' + session['values'][
                                                    event_pay_type] + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                        counter_data = await state.get_data()
                        await state.update_data(events_counter=int(counter_data['events_counter']) + 1)
                        counter_data = await state.get_data()
                    if counter_data['events_counter'] == 5:
                        combined_message += '🔹'
                        await state.update_data(events_counter=0)

        #--------- ТОЛЬКО ДЕТСКИЕ NEW
        if user_settings_dict['event_category'] == 'Детские':
                    if session_end.time() > now.time() and session_end.date() == now.date() or session_end.date() > now.date():
                        if session['values'][event_add_type] == 'Основной адрес':
                            google_url = (session['values'][event_yandex])
                        else:
                            google_url = (session['values'][event_set_yandex])
                        weekday = session_starttime.strftime('%a.')
                        if weekday == 'Mon.':
                            weekday = 'Пн.'
                        elif weekday == 'Tue.':
                            weekday = 'Вт.'
                        elif weekday == 'Wed.':
                            weekday = 'Ср.'
                        elif weekday == 'Thu.':
                            weekday = 'Чт.'
                        elif weekday == 'Fri.':
                            weekday = 'Пт.'
                        elif weekday == 'Sat.':
                            weekday = 'Сб.'
                        elif weekday == 'Sun.':
                            weekday = 'Вс.'
                        # ---- ФИЛЬТР КАТЕГОРИИ
                        if str(session['values'][event_category]) == 'Детские':
                            if str(session['values'][event_pay_type]) != 'Свободный вход':
                                if str(session['values'][event_pay_type]) == 'Платно':
                                    if session["values"][event_price] == '0':
                                        combined_message += str(f'<a href="' +
                                                                session['values'][event_mainlink] + f'">' +
                                                                session['values'][event_name] + f'</a>' + '\n' +
                                                                session['values'][event_type] + ' ' + session['values'][
                                                                    event_age] + ' ' + '\n' + '🗓 ' + str(
                                            session_starttime.strftime('%d.%m ') + weekday + session_starttime.strftime(' %H:%M')) + ' - ' + session_endtime.strftime('%H:%M') + '\n' + '🎟' + ' ' + f'<a href="' +
                                                                session['values'][event_ticketlink] + f'">' +
                                                                f'Платно' + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                                session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                    else:
                                        combined_message += str(f'<a href="' +
                                                                session['values'][event_mainlink] + f'">' +
                                                                session['values'][event_name] + f'</a>' + '\n' +
                                                                session['values'][event_type] + ' ' + session['values'][
                                                                    event_age] + ' ' + '\n' + '🗓 ' + str(
                                            session_starttime.strftime('%d.%m ') + weekday + session_starttime.strftime(' %H:%M')) + ' - ' + session_endtime.strftime('%H:%M') + '\n' + '🎟' + ' ' + f'<a href="' +
                                                                session['values'][event_ticketlink] + f'">' +
                                                                f'От {session["values"][event_price]}р' + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                                session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                else:
                                    combined_message += str(f'<a href="' +
                                                            session['values'][event_mainlink] + f'">' +
                                                            session['values'][event_name] + f'</a>' + '\n' +
                                                            session['values'][event_type] + ' ' + session['values'][
                                                                event_age] + ' ' + '\n' + '🗓 ' + str(
                                        session_starttime.strftime('%d.%m ') + weekday + session_starttime.strftime(
                                            ' %H:%M')) + ' - ' + session_endtime.strftime('%H:%M') + '\n' + '🎟' + ' ' + f'<a href="' +
                                                            session['values'][event_ticketlink] + f'">' +
                                                            session['values'][
                                                                event_pay_type] + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                            session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                counter_data = await state.get_data()
                                await state.update_data(events_counter=int(counter_data['events_counter']) + 1)
                                counter_data = await state.get_data()
                            else:
                                combined_message += str(f'<a href="' +
                                                        session['values'][event_mainlink] + f'">' +
                                                        session['values'][event_name] + f'</a>' + '\n' +
                                                        session['values'][event_type] + ' ' + session['values'][
                                                            event_age] + ' ' + '\n' + '🗓 ' + str(
                                    session_starttime.strftime('%d.%m ') + weekday + session_starttime.strftime(
                                        ' %H:%M')) + ' - ' + session_endtime.strftime('%H:%M') + '\n' + '🎟' + ' ' + session['values'][
                                                            event_pay_type] + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                        session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                                counter_data = await state.get_data()
                                await state.update_data(events_counter=int(counter_data['events_counter']) + 1)
                                counter_data = await state.get_data()
                            if counter_data['events_counter'] == 5:
                                combined_message += '🔹'
                                await state.update_data(events_counter=0)

        # ---------- ТОЛЬКО БЕСПЛАТНЫЕ NEW
        if user_settings_dict['event_category'] == 'Бесплатные' and str(session['values'][event_category]) != 'Выставки':
            if session_end.time() > now.time() and session_end.date() == now.date() or session_end.date() > now.date():
                if session['values'][event_add_type] == 'Основной адрес':
                    google_url = (session['values'][event_yandex])
                else:
                    google_url = (session['values'][event_set_yandex])
                weekday = session_starttime.strftime('%a.')
                if weekday == 'Mon.':
                    weekday = 'Пн.'
                elif weekday == 'Tue.':
                    weekday = 'Вт.'
                elif weekday == 'Wed.':
                    weekday = 'Ср.'
                elif weekday == 'Thu.':
                    weekday = 'Чт.'
                elif weekday == 'Fri.':
                    weekday = 'Пт.'
                elif weekday == 'Sat.':
                    weekday = 'Сб.'
                elif weekday == 'Sun.':
                    weekday = 'Вс.'
                # ---- ФИЛЬТР КАТЕГОРИИ
                if str(session['values'][event_pay_type]) != 'Платно':
                    if str(session['values'][event_pay_type]) != 'Свободный вход':
                        combined_message += str(f'<a href="' +
                                                    session['values'][event_mainlink] + f'">' +
                                                    session['values'][event_name] + f'</a>' + '\n' +
                                                    session['values'][event_type] + ' ' + session['values'][
                                                        event_age] + ' ' + '\n' + '🗓 ' + str(
                                session_starttime.strftime('%d.%m ') + weekday + session_starttime.strftime(' %H:%M')) + ' - ' + session_endtime.strftime('%H:%M') + '\n' + '🎟' + ' ' + f'<a href="' +
                                                    session['values'][event_ticketlink] + f'">' +
                                                    session['values'][
                                                        event_pay_type] + f'</a>' + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                    session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                        counter_data = await state.get_data()
                        await state.update_data(events_counter=int(counter_data['events_counter']) + 1)
                        counter_data = await state.get_data()
                    else:
                        combined_message += str(f'<a href="' +
                                                session['values'][event_mainlink] + f'">' +
                                                session['values'][event_name] + f'</a>' + '\n' +
                                                session['values'][event_type] + ' ' + session['values'][
                                                    event_age] + ' ' + '\n' + '🗓 ' + str(
                            session_starttime.strftime('%d.%m ') + weekday + session_starttime.strftime(' %H:%M')) + ' - ' + session_endtime.strftime('%H:%M') + '\n' + '🎟' + ' ' + session['values'][
                                                    event_pay_type] + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                                session['values'][event_org] + f'</a>' + phone_number + '\n' + '\n')
                        counter_data = await state.get_data()
                        await state.update_data(events_counter=int(counter_data['events_counter']) + 1)
                        counter_data = await state.get_data()
                    if counter_data['events_counter'] == 5:
                        combined_message += '🔹'
                        await state.update_data(events_counter=0)



        # ----------------------- ФИНАЛ СБОРКИ СООБЩЕНИЯ В ВИДЕ КАТАЛОГА
    await state.set_state(user_settings.part)
    await state.update_data(part=0)
    if combined_message.count('🔹') != 0:
        list_fin = 1
        await state.update_data(body=combined_message.split('🔹'))
        events_dict = await state.get_data()
        events_list = events_dict['body']
        for i in range(len(events_list)):
            events_list[i] = '\n\n' + events_list[i] + '📖Страница ' + str(i + 1) + ' из ' + str(len(events_list)) + '\n' + 'Сгенерировано ' + '<a href="' + BOT_LINK +'">' + BOT_NAME_SIMPLE + f'</a>'
            if i == len(events_list)-1:
                events_list[i] = events_list[i] + '\n\n✅Вывод списка мероприятий с учетом ваших критериев завершен. Помните, что при поиске на текущую дату - все мероприятия, которые уже закончились отображаться не будут.\n\n🔄Для нового запроса перейдите в "Главное меню"'
        if len(events_list) != 1:
            await callback.message.edit_text(events_list[0], parse_mode=ParseMode.HTML, disable_web_page_preview=True, reply_markup=await nav.navMenu_events_catalogue_prevstop())

    if combined_message.count('🔹') == 0:
        combined_message += 'Сгенерировано ' + '<a href="' + BOT_LINK +'">' + BOT_NAME_SIMPLE + f'</a>' + '\n\nДля нового запроса перейдите в "Главное меню"'
        await callback.message.delete()
        await bot.send_photo(callback.from_user.id,
                                 photo=paginate_end_photo,
                                 caption=combined_message,  parse_mode=ParseMode.HTML,
                                 reply_markup=await nav.navMenu_events_catalogue_none())
# --------------------------ОКОНЧАНИЕ РЕЖИМА СБОРКИ СООБЩЕНИЯ В ВИДЕ КАТАЛОГА-------------------

# ---------------------------------------- ВЫВОД КАТАЛОГА НА ЭКРАН ----------------------------------------------
#---БЛОК НАВИГАЦИИ ПРИ ВЫВОДЕ МЕРОПРИЯТИЙ - КАТАЛОГ

@router.callback_query(F.data == 'next_events_catalogue')
async def show_events_next(callback: CallbackQuery, state: FSMContext):
    events_info = await state.get_data()
    await state.update_data(part=int(events_info['part'])+1)
    events_info = await state.get_data()
    print(f'{str(callback.from_user.username)} нажал Вперед и перешел на страницу'+\
          f'{int(events_info["part"])+1}/{len(events_info["body"])}')
    if int(events_info['part']) < len(events_info['body'])-1:
        await callback.message.edit_text((events_info['body'])[events_info['part']], parse_mode=ParseMode.HTML, disable_web_page_preview=True, reply_markup=nav.navMenu_events_catalogue())
    if int(events_info['part']) == len(events_info['body'])-1:
        await callback.message.delete()
        await bot.send_photo(callback.from_user.id, photo=paginate_end_photo, caption=(events_info['body'])[events_info['part']], parse_mode=ParseMode.HTML, reply_markup=nav.navMenu_events_catalogue_nextstop())

@router.callback_query(F.data == 'prev_events_catalogue')
async def show_events_prev(callback: CallbackQuery, state: FSMContext):
     events_info = await state.get_data()
     await state.update_data(part=int(events_info['part']) - 1)
     events_info = await state.get_data()
     print(f'{str(callback.from_user.username)} нажал Назад и перешел на страницу {int(events_info["part"]) + 1}/{len(events_info["body"])}')
     if int(events_info['part']) > 0:
         await callback.message.delete()
         await callback.message.answer(f'{(events_info["body"])[events_info["part"]]}', parse_mode=ParseMode.HTML, disable_web_page_preview=True, reply_markup=nav.navMenu_events_catalogue())
     if int(events_info['part']) == 0:
         await bot.delete_message(callback.from_user.id, callback.message.message_id)
         await callback.message.answer(f'{(events_info["body"])[events_info["part"]]}', parse_mode=ParseMode.HTML, disable_web_page_preview=True, reply_markup=await nav.navMenu_events_catalogue_prevstop())
#---------------------------------- ОКОНЧАНИЕ ВЫВОДА КАТАЛОГА НА ЭКРАН -----------------------------------------------------
# -------------------------------СБОРКА КАРТОЧЕК РЕКОМЕНДОВАННЫХ МЕРОПРИЯТИЙ------------------------------------------

@router.callback_query(F.data=="recommended")
async def show_events_cards(callback: CallbackQuery, state: FSMContext):
    print(f'{str(callback.from_user.username)} нажал Наши рекомендации')
    file_log(
        logtext=f'{str(callback.from_user.username)} нажал Наши рекомендации')
    events_fin = []
    combined_message = ''
    photo_combined = ''
    now = datetime.now()
    events_check = fetch.events_catalogue_fetch(url_get_events)
    for i in range(len(events_check)):
        if events_check[i]['values'][mod_check] != 'Не проверено':
            events_fin.append(events_check[i])
    events_sorted = sorted(events_fin, key=lambda x: datetime.strptime(x['values'][event_start_time], "%d.%m.%y %H:%M:%S"))
    for session in events_sorted:
        session_starttime = datetime.strptime(session['values'][event_start_time], "%d.%m.%y %H:%M:%S")
        session_endtime = datetime.strptime(session['values'][event_end_time], "%d.%m.%y %H:%M:%S")
        session_start = datetime.strptime(session['values'][event_start_time], "%d.%m.%y %H:%M:%S")
        session_end = datetime.strptime(session['values'][event_end_time], "%d.%m.%y %H:%M:%S")
        session_end_date = datetime(session_end.year, session_end.month, session_end.day)
        curr_date = datetime(now.year, now.month, now.day)
        await state.update_data(events_counter=0)

        if session['values'][event_photo] != None:
            if session['values'][event_price] != '0':
                price = (' от ' + str(session['values'][event_price]) + '₽')
            else:
                price = ('')
            temp_photo = session['values'][event_photo]
            id = session['id']
            session['values'][event_photo] = 'https://quintadb.ru/images/data/cwgmoxoavcW6SJzehdV8o6/' + str(
                id) + '/' + str(
                temp_photo)
            if session['values'][event_desc] == None:
                session['values'][event_desc] = 'Организатор не предоставил описание мероприятия.\n'
            if session['values'][event_add_type] == 'Основной адрес':
                events_lat = (session['values'][event_lat])
                events_long = (session['values'][event_long])
                google_url = (session['values'][event_yandex])
            else:
                events_lat = (session['values'][event_set_lat])
                events_long = (session['values'][event_set_long])
                google_url = (session['values'][event_set_yandex])
            if session['values'][event_category] == 'Многодневные':
                if str(session['values'][event_pay_type]) != 'Свободный вход':

                    photo_combined += session['values'][event_photo]
                    combined_message += str('\n' + session['values'][event_desc] + '\n' + '\n' + f'<a href="' +
                                            session['values'][event_mainlink] + f'">' +
                                            session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                                event_type] + ' ' + session['values'][
                                                event_age] + ' ' + '\n' + '🗓 Многодневное: ' + str(
                        session_starttime.strftime('%d.%m')) + ' - ' + str(
                        session_endtime.strftime('%d.%m')) + '\n' + '🎟' + ' ' + f'<a href="' +
                                            session['values'][event_ticketlink] + f'">' +
                                            session['values'][event_pay_type] + f'</a>' + str(
                        price) + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' + session['values'][
                                                event_org] + f'</a>' + '\n' + '\n')
                    counter_data = await state.get_data()
                    await state.update_data(events_counter = counter_data['events_counter']+1)
                    counter_data = await state.get_data()

                else:
                    photo_combined += session['values'][event_photo]
                    combined_message += str('\n' + session['values'][event_desc] + '\n' + '\n' + f'<a href="' +
                                            session['values'][event_mainlink] + f'">' +
                                            session['values'][event_name] + f'</a>' + '\n' + session['values'][
                                                event_type] + ' ' + session['values'][
                                                event_age] + ' ' + '\n' + '🗓 ' + str(
                        session_starttime.strftime('%d.%m')) + ' ' + str(
                        session_starttime.strftime('%H:%M')) + ' - ' + str(
                        session_endtime.strftime('%H:%M')) + '\n' + '🎟' + ' ' + session['values'][
                                                event_pay_type] + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                                            session['values'][event_org] + f'</a>' + '\n' + '\n')
                    counter_data = await state.get_data()
                    await state.update_data(events_counter=counter_data['events_counter'] + 1)
                    counter_data = await state.get_data()
                if counter_data['events_counter'] == 1:
                    combined_message += ('🔹')
                    photo_combined += ('🔹')
                    await state.update_data(events_counter = 0)
            if session['values'][event_category] != 'Многодневные':
                if str(session['values'][event_pay_type]) != 'Свободный вход':
                    photo_combined += session['values'][event_photo]
                    combined_message += str(
                        '\n' + session['values'][event_desc] + '\n' + '\n' + f'<a href="' +
                        session['values'][event_mainlink] + f'">' +
                        session['values'][event_name] + f'</a>' + '\n' + session['values'][event_type] + ' ' +
                        session['values'][event_age] + ' ' + '\n' + '🗓 ' + str(
                            session_starttime.strftime('%d.%m')) + ' ' + str(
                            session_starttime.strftime('%H:%M')) + ' - ' + str(
                            session_endtime.strftime('%H:%M')) + '\n' + '🎟' + ' ' + f'<a href="' +
                        session['values'][event_ticketlink] + f'">' +
                        session['values'][event_pay_type] + f'</a>' + str(
                            price) + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' + session['values'][
                            event_org] + f'</a>' + '\n' + '\n')
                    counter_data = await state.get_data()
                    await state.update_data(events_counter=counter_data['events_counter'] + 1)
                    counter_data = await state.get_data()
                else:
                    photo_combined += session['values'][event_photo]
                    combined_message += str(
                        '\n' + session['values'][event_desc] + '\n' + '\n' + f'<a href="' +
                        session['values'][event_mainlink] + f'">' +
                        session['values'][event_name] + f'</a>' + '\n' + session['values'][event_type] + ' ' +
                        session['values'][event_age] + ' ' + '\n' + '🗓 ' + str(
                            session_starttime.strftime('%d.%m')) + ' ' + str(
                            session_starttime.strftime('%H:%M')) + ' - ' + str(
                            session_endtime.strftime('%H:%M')) + '\n' + '🎟' + ' ' + session['values'][
                            event_pay_type] + '\n' + '📍 ' + f'<a href ="' + google_url + f'">' +
                        session['values'][event_org] + f'</a>' + '\n' + '\n')
                    counter_data = await state.get_data()
                    await state.update_data(events_counter=counter_data['events_counter'] + 1)
                    counter_data = await state.get_data()
                if counter_data['events_counter'] == 1:
                    combined_message += ('🔹')
                    photo_combined += ('🔹')
                    await state.update_data(events_counter=0)
    combined_message += (
            '\n' + 'Вывод рекомендованных мероприятий завершен.\n\nВсю афишу мероприятий на неделю можно посмотреть с помощью кнопки "Искать мероприятия" в главном меню.\n' + '\n' + 'Хотите присоединиться к нашей базе и публиковать свои мероприятия? - пишите ' + '<a href="'+SUPPORT_LINK+ '">' + 'в поддержку.' + f'</a>')
    events_dictionary = combined_message.split('🔹')
    photo_dictionary = photo_combined.split('🔹')
    for i in range(len(photo_dictionary)-1):
        events_dictionary[i] = '\n\n' + events_dictionary[i] + 'Мероприятие ' + str(i + 1) + ' из ' + str(
                len(events_dictionary) - 1) + '\n\n' + 'Сгенерировано ' + '<a href="' + BOT_LINK +'">' + BOT_NAME_SIMPLE + f'</a>'
    await state.update_data(body=events_dictionary)
    await state.update_data(part=0)
    await state.update_data(photos=photo_dictionary)
    rec_data = await state.get_data()
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_photo(callback.from_user.id, photo=str(rec_data['photos'][0]), caption=(rec_data['body'])[0],
                         parse_mode=ParseMode.HTML, reply_markup=await nav.navMenu_events_prevstop())
    # ОКОНЧАНИЕ БЛОКА СБОРКИ МЕРОПРИЯТИЙ КАРТОЧКАМИ


#############################################################################################--- ОКОНЧАНИЯ БЛОКОВ СБОРКИ СООБЩЕНИЙ

# -- БЛОК НАВИГАЦИИ ПРИ ВЫВОДЕ МЕРОПРИЯТИЙ - КАРТОЧКА

@router.callback_query(F.data == 'next_events')
async def show_events_next(callback: CallbackQuery, state: FSMContext):
    rec_data = await state.get_data()
    await state.update_data(part=rec_data['part']+1)
    rec_data = await state.get_data()
    print(f'{str(callback.from_user.username)} нажал Вперед и перешел на страницу {int(rec_data["part"]) + 1}/{len(rec_data["body"])-1}')
    if rec_data['part'] < len(rec_data['body']) - 1:
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await bot.send_photo(callback.from_user.id, photo=str((rec_data['photos'])[rec_data['part']]),
                             caption=rec_data['body'][rec_data['part']], parse_mode=ParseMode.HTML,
                             reply_markup=await nav.navMenu_events())
    if rec_data['part'] == len(rec_data['body']) - 1:
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await bot.send_photo(callback.from_user.id,
                             photo=paginate_end_photo,
                             caption=rec_data['body'][rec_data['part']], parse_mode=ParseMode.HTML,
                             reply_markup=await nav.navMenu_events_nextstop())

@router.callback_query(F.data == 'prev_events')
async def show_events_prev(callback: CallbackQuery, state: FSMContext):
    rec_data = await state.get_data()
    await state.update_data(part=rec_data['part'] - 1)
    rec_data = await state.get_data()
    print(f'{str(callback.from_user.username)} нажал Назад и перешел на страницу {int(rec_data["part"]) + 1}/{len(rec_data["body"])-1}')
    if rec_data['part'] > 0:
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await bot.send_photo(callback.from_user.id, photo=str((rec_data['photos'])[rec_data['part']]),
                             caption=rec_data['body'][rec_data['part']], parse_mode=ParseMode.HTML,
                             reply_markup=await nav.navMenu_events())
    if rec_data['part'] == 0:
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await bot.send_photo(callback.from_user.id, photo=str((rec_data['photos'])[rec_data['part']]),
                             caption=rec_data['body'][rec_data['part']], parse_mode=ParseMode.HTML,
                             reply_markup=await nav.navMenu_events_prevstop())

# -- КАТЕГОРИИ АКЦИЙ И ПРЕДЛОЖЕНИЙ

@router.callback_query(F.data == 'offers')
async def offers_category(callback: CallbackQuery, state: FSMContext):
    print(f'{str(callback.from_user.username)} нажал Акции и предложения')
    file_log(logtext=f'{str(callback.from_user.username)} нажал Акции и предложения')
    await state.set_state(user_settings.offers_category)
    await callback.message.delete()
    await callback.message.answer(f'<b>Выберите категорию акций и предложений\n\n🗂 Категории :\n\nВсе</b> - показывает все скидки, акции и предложения\n\n'\
            '<b>📦 Товары</b> - акции на приобретение товаров\n<b>💸 Услуги </b> - акции на различные услуги\n<b>🍔 Еда </b> - акции на покупку еды и продуктов\n<b>🔥 Мероприятия</b> - акции на посещение мероприятий'\
            , reply_markup=await nav.navMenu_offers_category_choose(), parse_mode=ParseMode.HTML)
#
@router.callback_query(user_settings.offers_category)
async def show_offers(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text('⏳Подбираем акции и предложения для вас...\nПожалуйста, подождите', reply_markup=await nav.mainMenu_inst())
    await state.update_data(offers_category=callback.data[2:])
    userdata = await state.get_data()
    print(f'{str(callback.from_user.username)} выбрал категорию {userdata["offers_category"]}')
    file_log(logtext=f'{str(callback.from_user.username)} выбрал категорию {userdata["offers_category"]}')
    offers_list_temp = []
    combined_message = ''
    combined_photos = ''
    offer_counter_temp = 0
    now = (datetime.now() + timedelta(hours=3))
    offers_check = fetch.offers_catalogue_fetch(url_get_offers)
    if userdata["offers_category"] == 'Все':
        for i in range(len(offers_check)):
            offers_list_temp.append(offers_check[i])
        offers_sorted = sorted(offers_list_temp,
                                key=lambda x: datetime.strptime(x['values'][offer_startdate], "%d.%m.%y %H:%M:%S"))
    else:
        for i in range(len(offers_check)):
            if offers_check[i]["values"][offer_category] == userdata["offers_category"]:
                offers_list_temp.append(offers_check[i])
        offers_sorted = sorted(offers_list_temp,
                                key=lambda x: datetime.strptime(x['values'][offer_startdate], "%d.%m.%y %H:%M:%S"))
    for offer in offers_sorted:
        offer_counter_temp += 1
        offer_start_date = datetime.strptime(offer["values"][offer_startdate], "%d.%m.%y %H:%M:%S")
        offer_end_date = datetime.strptime(offer["values"][offer_enddate], "%d.%m.%y %H:%M:%S")
        id = offer['id']
        photo_link = 'https://quintadb.ru/images/data/bYW7ddI8jfrRlcKYizWQWH/' + str(
            id) + '/' + str(
            offer["values"][offer_photo])
        if offer_end_date.date() >= now.date():
            if offer_start_date.date() >= now.date() and offer_start_date.date()==offer_start_date.date():
                combined_message += str(f'{offer["values"][offer_desc]}\n\n📅 Только {offer_end_date.strftime("%d.%m")}\n📍 ' \
                                        + '<a href="' + offer["values"][offer_location_yandex] + '">' + offer["values"][
                                            offer_orgname] + '</a>\nℹ️ ' \
                                        + '<a href="' + offer["values"][offer_link] + '">Подробная информация</a>🔹')
            elif offer_start_date.date() > now.date():
                combined_message += str(f'{offer["values"][offer_desc]}\n\n📅 С {offer_start_date.strftime("%d.%m")} по {offer_end_date.strftime("%d.%m")}\n📍 '\
                    + '<a href="' + offer["values"][offer_location_yandex] + '">' + offer["values"][offer_orgname] + '</a>\nℹ️ '\
                    + '<a href="' + offer["values"][offer_link] + '">Подробная информация</a>🔹')
            elif offer_start_date.date() <= now.date():
                combined_message += str(f'{offer["values"][offer_desc]}\n\n📅 До {offer_end_date.strftime("%d.%m")}\n📍 ' \
                                    + '<a href="' + offer["values"][offer_location_yandex] + '">' + offer["values"][
                                        offer_orgname] + '</a>\nℹ️ ' \
                                    + '<a href="' + offer["values"][offer_link] + '">Подробная информация</a>🔹')
        combined_photos += str(f'{photo_link}🔹')
    combined_message += str('Вывод акций и предложений завершен.\n\nПросмотреть другую категорию можно с помощью кнопки "Акции и предложения" в главном меню, а афишу мероприятий на неделю можно - с помощью кнопки "Искать мероприятия".\n\nХотите присоединиться к нашей базе и добавлять свои предложения и акции? - пишите ' + '<a href="' + SUPPORT_LINK + '">' + 'в поддержку.' + f'</a>')
    offers_list = combined_message.split('🔹')
    offers_photos_list = combined_photos.split('🔹')
    for i in range(len(offers_list)-1):
        offers_list[i] = offers_list[i] + '\n\nПредложение ' + str(i + 1) + ' из ' + str(
                len(offers_list) - 1) + '\n' + 'Сгенерировано ' + '<a href="' + BOT_LINK +'">' + BOT_NAME_SIMPLE + f'</a>'
    await state.update_data(body=offers_list)
    await state.update_data(part=0)
    await state.update_data(photos=offers_photos_list)
    userdata = await state.get_data()
    print(offer_counter_temp)
    if offer_counter_temp != 0:
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await bot.send_photo(callback.from_user.id, photo=str(userdata["photos"][0]), caption=(userdata['body'])[0],
                             parse_mode=ParseMode.HTML, reply_markup=await nav.navMenu_events_prevstop())
    else:
        await bot.send_photo(callback.from_user.id,
                             photo=paginate_end_photo,
                             caption=('К сожалению, на данный момент в базе нет акций или предложений выбранной категории.\n\nПросмотреть другие категории можно с помощью кнопки "Акции и предложения" в главном меню, а афишу мероприятий на неделю можно - с помощью кнопки "Искать мероприятия".\n\nХотите присоединиться к нашей базе и добавлять свои предложения и акции? - пишите ' + '<a href="' + SUPPORT_LINK + '">' + 'в поддержку.' + f'</a>'), parse_mode=ParseMode.HTML,
                             reply_markup=await nav.navMenu_events_catalogue_none())


@router.callback_query(F.data == 'next_events')
async def show_events_offers(callback: CallbackQuery, state: FSMContext):
    userdata = await state.get_data()
    await state.update_data(part=userdata['part'] + 1)
    userdata = await state.get_data()
    print(
        f'{str(callback.from_user.username)} нажал Вперед и перешел на страницу {int(userdata["part"]) + 1}/{len(userdata["body"]) - 1}')
    if userdata['part'] < len(userdata['body']) - 1:
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await bot.send_photo(callback.from_user.id, photo=str((userdata['photos'])[userdata['part']]),
                                 caption=userdata['body'][userdata['part']], parse_mode=ParseMode.HTML,
                                 reply_markup=await nav.navMenu_events())
    if userdata['part'] == len(userdata['body']) - 1:
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await bot.send_photo(callback.from_user.id,
                                 photo=paginate_end_photo,
                                 caption=userdata['body'][userdata['part']], parse_mode=ParseMode.HTML,
                                 reply_markup=await nav.navMenu_events_nextstop())

@router.callback_query(F.data == 'prev_events')
async def show_prev_offers(callback: CallbackQuery, state: FSMContext):
    userdata = await state.get_data()
    await state.update_data(part=userdata['part'] - 1)
    userdata = await state.get_data()
    print(
        f'{str(callback.from_user.username)} нажал Назад и перешел на страницу {int(userdata["part"]) + 1}/{len(userdata["body"]) - 1}')
    if userdata['part'] > 0:
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await bot.send_photo(callback.from_user.id, photo=str((userdata['photos'])[userdata['part']]),
                                 caption=userdata['body'][userdata['part']], parse_mode=ParseMode.HTML,
                                 reply_markup=await nav.navMenu_events())
    if userdata['part'] == 0:
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await bot.send_photo(callback.from_user.id, photo=str((userdata['photos'])[userdata['part']]),
                                 caption=userdata['body'][userdata['part']], parse_mode=ParseMode.HTML,
                                 reply_markup=await nav.navMenu_events_prevstop())


    '''
    offers_list = []
    combined_message = ''
    photo_combined = ''
    offers_check = fetch.offers_catalogue_fetch(url_get_offers)
    for i in range(len(offers_check)):
        if offers_check[i]['values'][mod_check] != 'Не проверено':
            offers_list.append(offers_check[i])
    offers_sorted = sorted(offers_list,
                           key=lambda x: datetime.strptime(x['values'][offers_end_time], "%d.%m.%y %H:%M:%S"))
'''

# -- БЛОК ВЫВОД ИНСТРУКЦИИ НА ЭКРАН

@router.callback_query(F.data=="show_help")
async def showhelp(callback: CallbackQuery):
    print(f'{str(callback.from_user.username)} нажал Помощь')
    await callback.message.delete()
    await callback.message.answer('Спасибо за интерес к нашему сервису.' + '\n' + '\n' + '<a href="' + BOT_LINK +'">' + BOT_NAME + '</a>' + ' - показывает мероприятия города ' + CITY_NAME + ' на ближайшую'
                              + ' неделю.' + '\n' + '\n'+ f'<b>Как пользоваться ботом:</b>' + '\n' + '\n' + '1️⃣  Перейти в "Главное меню"' + '\n' + '2️⃣  Нажать "Искать мероприятия"' + '\n' + '3️⃣  Выбрать категорию' + '\n4️⃣  Выбрать день\n'
                                 + '\n' + '🔸Наш телеграм-канал:' + '<a href="' + CHANNEL_LINK + '">' + CHANNEL_NAME + '</a>' + '\n\nСведения о мероприятиях в нашем боте взяты с сайтов организаторов или представлены ими.\n\nАдминистрация бота не несет ответственности за предоставленный материал, а также за действия организатора и/или иных лиц, действующих от его имени и по его поручению, либо от своего имени, но по поручению организатора, в том числе в связи с реализацией такими лицами билетов, а равно за организацию, проведение и содержание мероприятия. ' + '\n\nНужна помощь, или у вас вопрос по сотрудничеству? - '+ '<a href="'+SUPPORT_LINK+'">' + 'пишите сюда.' + '</a>', parse_mode='html', disable_web_page_preview = True, reply_markup=await nav.mainMenu_inst())

# -- ВЫВОД СТАТИСТИКИ

@router.callback_query(F.data=="stats")
async def stats(callback: CallbackQuery, state: FSMContext):
    print(f'{str(callback.from_user.username)} нажал Статистика')
    global mon, tue, wed, thu, fri, sat, sun
    total = 0
    mon = 0
    tue = 0
    wed = 0
    thu = 0
    fri = 0
    sat = 0
    sun = 0
    stats = fetch.events_catalogue_fetch(url_get_events)
    for session in stats:
        if session['values'][mod_check] != 'Не проверено':
            total = total + 1
            session_start = datetime.strptime(session['values'][event_start_time], "%d.%m.%y %H:%M:%S")
            weekday_strp_temp = session_start
            weekday_strf_temp = datetime.strftime(weekday_strp_temp, "%a.")
            if str(weekday_strf_temp) == 'Mon.':
                mon = mon + 1
            if str(weekday_strf_temp) == 'Tue.':
                tue = tue + 1
            if str(weekday_strf_temp) == 'Wed.':
                wed = wed + 1
            if str(weekday_strf_temp) == 'Thu.':
                thu = thu + 1
            if str(weekday_strf_temp) == 'Fri.':
                fri = fri + 1
            if str(weekday_strf_temp) == 'Sat.':
                sat = sat + 1
            if str(weekday_strf_temp) == 'Sun.':
                sun = sun + 1
    await state.update_data(stats_counter = {'tot': total, 'mon': mon, 'tue': tue, 'wed': wed, 'thu': thu, 'fri': fri, 'sat': sat, 'sun': sun})
    stats_data = await state.get_data()
    await callback.message.delete()
    await callback.message.answer(f'<b>Количество мероприятий в нашей базе:</b>\n\nВсего мероприятий: {stats_data["stats_counter"]["tot"]}\n\nИз них:\nПонедельник: {stats_data["stats_counter"]["mon"]}\nВторник: {stats_data["stats_counter"]["tue"]}\nСреда: {stats_data["stats_counter"]["wed"]}\nЧетверг: {stats_data["stats_counter"]["thu"]}\nПятница: {stats_data["stats_counter"]["fri"]}\nСуббота: {stats_data["stats_counter"]["sat"]}\nВоскресенье: {stats_data["stats_counter"]["sun"]}\n\nНаш телеграм канал с полезной информацией по мероприятиям в '+CITY_NAME_pr_padezh+f':' + '<a href="' + CHANNEL_LINK + '">' + CHANNEL_NAME + '</a>' +'\n\nДля перезапуска бота нажмите "Главное меню"'
                                     , parse_mode=ParseMode.HTML, disable_web_page_preview = True, reply_markup=await nav.mainMenu_inst())



# ПОЛУЧЕНИЕ ОБНОВЛЕНИЙ
async def get_updates():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
asyncio.run(get_updates())