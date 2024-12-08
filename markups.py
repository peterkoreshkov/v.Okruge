from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from datetime import datetime, timedelta, date, time
import locale
#from main import timeadjust
locale.setlocale(locale.LC_ALL, '')

async def timeadjust():
    adjust_time = datetime.today() + timedelta(hours=3)
    final_date_str = adjust_time.strftime("%Y-%m-%d")
    final_date = datetime.strptime(final_date_str, "%Y-%m-%d")
    today = final_date.date()
    return today

async def mainMenu():
    mainMenu = InlineKeyboardBuilder()
    mainMenu.button(text="Искать мероприятия", callback_data="show_events_sub")
    mainMenu.button(text="Акции и предложения", callback_data="offers")
    mainMenu.button(text="Статистика", callback_data="stats")
    mainMenu.button(text="Помощь", callback_data="show_help")
    mainMenu.button(text="Поделиться ботом", switch_inline_query="- бот-афиша в.Округе Псков")
    mainMenu.adjust(1,1,2,1)
    return mainMenu.as_markup()

async def subMenu():
    submenu = InlineKeyboardBuilder()
    submenu.button(text="Подписаться", url="https://t.me/vokruge_pskov")
    submenu.adjust(1)
    return submenu.as_markup()

async def mainMenu_inst():
    mainMenu_inst = InlineKeyboardBuilder()
    mainMenu_inst.button(text="Главное меню", callback_data="main_menu")
    mainMenu_inst.adjust(1)
    return mainMenu_inst.as_markup()

async def navMenu_category_choose():
    navMenu_category_choose = InlineKeyboardBuilder()
    navMenu_category_choose.button(text="Все", callback_data="Все")
    navMenu_category_choose.button(text="Бесплатные", callback_data="Бесплатные")
    #navMenu_category_choose.button(text="Образовательные", callback_data="Образовательные")
    #navMenu_category_choose.button(text="Музыкальные", callback_data="Музыкальные")
    #navMenu_category_choose.button(text="Культурные", callback_data="Культурные")
    #navMenu_category_choose.button(text="Развлекательные", callback_data="Развлекательные")
    navMenu_category_choose.button(text="Детские", callback_data="Детские")
    navMenu_category_choose.button(text='Выставки', callback_data="Выставки")
    navMenu_category_choose.button(text="Главное меню", callback_data="main_menu")
    navMenu_category_choose.adjust(2,2,1)
    return navMenu_category_choose.as_markup()

async def navMenu_events_choose():
    navMenu_events_choose = InlineKeyboardBuilder()
    navMenu_events_choose.button(text="Приступить к поиску", callback_data="catalogue")
    navMenu_events_choose.button(text="Главное меню", callback_data="main_menu")
    navMenu_events_choose.adjust(1,1)
    return navMenu_events_choose.as_markup()

async def navMenu_day_choose():
    today = await timeadjust()
    button_day0 = ''
    button_day1 = ''
    button_day2 = ''
    button_day3 = ''
    button_day4 = ''
    button_day5 = ''
    button_day6 = ''
    if str(datetime.strftime(today, "%a.")) == 'Thu.':
        button_day0 = 'Чт.'
        button_day1 = 'Пт.'
        button_day2 = 'Сб.'
        button_day3 = 'Вс.'
        button_day4 = 'Пн.'
        button_day5 = 'Вт.'
        button_day6 = 'Ср.'
    if str(datetime.strftime(today, "%a.")) == 'Fri.':
        button_day6 = 'Чт.'
        button_day0 = 'Пт.'
        button_day1 = 'Сб.'
        button_day2 = 'Вс.'
        button_day3 = 'Пн.'
        button_day4 = 'Вт.'
        button_day5 = 'Ср.'
    if str(datetime.strftime(today, "%a.")) == 'Sat.':
        button_day5 = 'Чт.'
        button_day6 = 'Пт.'
        button_day0 = 'Сб.'
        button_day1 = 'Вс.'
        button_day2 = 'Пн.'
        button_day3 = 'Вт.'
        button_day4 = 'Ср.'
    if str(datetime.strftime(today, "%a.")) == 'Sun.':
        button_day4 = 'Чт.'
        button_day5 = 'Пт.'
        button_day6 = 'Сб.'
        button_day0 = 'Вс.'
        button_day1 = 'Пн.'
        button_day2 = 'Вт.'
        button_day3 = 'Ср.'
    if str(datetime.strftime(today, "%a.")) == 'Mon.':
        button_day3 = 'Чт.'
        button_day4 = 'Пт.'
        button_day5 = 'Сб.'
        button_day6 = 'Вс.'
        button_day0 = 'Пн.'
        button_day1 = 'Вт.'
        button_day2 = 'Ср.'
    if str(datetime.strftime(today, "%a.")) == 'Tue.':
        button_day2 = 'Чт.'
        button_day3 = 'Пт.'
        button_day4 = 'Сб.'
        button_day5 = 'Вс.'
        button_day6 = 'Пн.'
        button_day0 = 'Вт.'
        button_day1 = 'Ср.'
    if str(datetime.strftime(today, "%a.")) == 'Wed.':
        button_day1 = 'Чт.'
        button_day2 = 'Пт.'
        button_day3 = 'Сб.'
        button_day4 = 'Вс.'
        button_day5 = 'Пн.'
        button_day6 = 'Вт.'
        button_day0 = 'Ср.'
    navMenu_day_choose1 = InlineKeyboardBuilder()
    navMenu_day_choose1.button(text='Сегодня',
                                         callback_data=str(today + timedelta(days=0)))
    navMenu_day_choose1.button(text=str(datetime.strftime(today + timedelta(days=1), "%d.%m ") + str(button_day1)),
                               callback_data=str(today + timedelta(days=1)))
    navMenu_day_choose1.button(text=str(datetime.strftime(today + timedelta(days=4), "%d.%m ") + str(button_day4)),
                               callback_data=str(today + timedelta(days=4)))
    navMenu_day_choose1.button(text=str(datetime.strftime(today + timedelta(days=2), "%d.%m ") + str(button_day2)),
                               callback_data=str(today + timedelta(days=2)))
    navMenu_day_choose1.button(text=str(datetime.strftime(today + timedelta(days=5), "%d.%m ") + str(button_day5)),
                               callback_data=str(today + timedelta(days=5)))
    navMenu_day_choose1.button(text=str(datetime.strftime(today + timedelta(days=3), "%d.%m ") + str(button_day3)),
                               callback_data=str(today + timedelta(days=3)))
    navMenu_day_choose1.button(text=str(datetime.strftime(today + timedelta(days=6), "%d.%m ") + str(button_day6)),
                               callback_data=str(today + timedelta(days=6)))
    navMenu_day_choose1.button(text="Главное меню", callback_data="main_menu")
    navMenu_day_choose1.adjust(1,2,2,2,1)
    return navMenu_day_choose1.as_markup()

async def navMenu_events_catalogue_none():
    navMenu_events_catalogue_none = InlineKeyboardBuilder()
    navMenu_events_catalogue_none.button(text="Главное меню", callback_data="main_menu")
    navMenu_events_catalogue_none.adjust(1)
    return navMenu_events_catalogue_none.as_markup()

#-- КНОПКИ ПОКАЗА МЕРОПРИЯТИЙ КАТАЛОГОМ

def navMenu_events_catalogue():
    navMenu_events_catalogue = InlineKeyboardBuilder()
    navMenu_events_catalogue.button(text="Назад", callback_data="prev_events_catalogue")
    navMenu_events_catalogue.button(text="Вперед", callback_data="next_events_catalogue")
    navMenu_events_catalogue.button(text="Главное меню", callback_data="main_menu")
    navMenu_events_catalogue.adjust(2,1)
    return navMenu_events_catalogue.as_markup()

def navMenu_events_catalogue_nextstop():
    navMenu_events_catalogue_nextstop = InlineKeyboardBuilder()
    navMenu_events_catalogue_nextstop.button(text="Назад", callback_data="prev_events_catalogue")
    navMenu_events_catalogue_nextstop.button(text="Главное меню", callback_data="main_menu")
    navMenu_events_catalogue_nextstop.adjust(1,1)
    return navMenu_events_catalogue_nextstop.as_markup()

async def navMenu_events_catalogue_prevstop():
    navMenu_events_catalogue_prevstop = InlineKeyboardBuilder()
    navMenu_events_catalogue_prevstop.button(text="Вперед", callback_data="next_events_catalogue")
    navMenu_events_catalogue_prevstop.button(text="Главное меню", callback_data="main_menu")
    navMenu_events_catalogue_prevstop.adjust(1,1)
    return navMenu_events_catalogue_prevstop.as_markup()


#-- КНОПКИ ПОКАЗА МЕРОПРИЯТИЙ КАРТОЧКАМИ
async def navMenu_events():
    navMenu_events = InlineKeyboardBuilder()
    navMenu_events.button(text="Назад", callback_data="prev_events")
    navMenu_events.button(text="Вперед", callback_data="next_events")
    navMenu_events.button(text="Главное меню", callback_data="main_menu")
    navMenu_events.adjust(2,1)
    return navMenu_events.as_markup()

async def navMenu_events_nextstop():
    navMenu_events_nextstop = InlineKeyboardBuilder()
    navMenu_events_nextstop.button(text="Назад", callback_data="prev_events")
    navMenu_events_nextstop.button(text="Главное меню", callback_data="main_menu")
    navMenu_events_nextstop.adjust(1,1)
    return navMenu_events_nextstop.as_markup()

async def navMenu_events_prevstop():
    navMenu_events_prevstop = InlineKeyboardBuilder()
    navMenu_events_prevstop.button(text="Вперед", callback_data="next_events")
    navMenu_events_prevstop.button(text="Главное меню", callback_data="main_menu")
    navMenu_events_prevstop.adjust(1,1)
    return navMenu_events_prevstop.as_markup()

#--- КАТЕГОРИИ АКЦИЙ
async def navMenu_offers_category_choose():
    navMenu_offers_category_choose = InlineKeyboardBuilder()
    navMenu_offers_category_choose.button(text="Все", callback_data="УсВсе")
    navMenu_offers_category_choose.button(text="Товары", callback_data="УсТовары")
    navMenu_offers_category_choose.button(text="Услуги", callback_data="УсУслуги")
    navMenu_offers_category_choose.button(text="Еда", callback_data="УсЕда")
    navMenu_offers_category_choose.button(text="Мероприятия", callback_data="УсМероприятия")
    navMenu_offers_category_choose.button(text="Главное меню", callback_data="main_menu")
    navMenu_offers_category_choose.adjust(1,2,2,1)
    return navMenu_offers_category_choose.as_markup()





'''
#-- КНОПКИ ПОКАЗА ОРГАНИЗАТОРОВ (НЕ ТРОГАЛ)


navMenu_orgs = InlineKeyboardMarkup(row_width=2)
#next_page = InlineKeyboardButton(text="Вперед", callback_data="next_orgs")
#prev_page = InlineKeyboardButton(text="Назад", callback_data="prev_orgs")
back_to_list = InlineKeyboardButton(text="Вернуться к списку", callback_data="show_orgs_list")
leave_org_list = InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
navMenu_orgs.insert(back_to_list)
navMenu_orgs.insert(leave_org_list)

navMenu_orgs_nextstop = InlineKeyboardMarkup(row_width=1)
prev_page = InlineKeyboardButton(text="Назад", callback_data="prev_orgs")
leave_org_list = InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
navMenu_orgs_nextstop.insert(prev_page)
navMenu_orgs_nextstop.insert(leave_org_list)

navMenu_orgs_prevstop = InlineKeyboardMarkup(row_width=1)
next_page = InlineKeyboardButton(text="Вперед", callback_data="next_orgs")
leave_org_list = InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
navMenu_orgs_prevstop.insert(next_page)
navMenu_orgs_prevstop.insert(leave_org_list)


#-- КНОПКИ МЕНЮ ВЫБОРА ВАРИАНТА ОТОБРАЖЕНИЯ МЕРОПРИЯТИЙ БЕЗ ГЕОЛОКАЦИИ           (ИЗМЕНИЛ)

navMenu_events_choose = InlineKeyboardMarkup(row_width=1)
catalogue = InlineKeyboardButton(text="Приступить к поиску", callback_data="catalogue")
leave_events_list = InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
navMenu_events_choose.insert(catalogue)

navMenu_events_choose.insert(leave_events_list)



!!!!!!!!!!!!!!!ДАЛЕЕ ВСЕ ПЕРЕДЕЛАЛ ИЛИ НЕ НУЖНО!!!!!!!!!!!!!!!!!

navMenu_events_catalogue_prevstop = InlineKeyboardMarkup(row_width=1)            
next_events_catalogue_page = InlineKeyboardButton(text="Вперед", callback_data="next_events_catalogue")
leave_events_catalogue_list = InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
navMenu_events_catalogue_prevstop.insert(next_events_catalogue_page)
navMenu_events_catalogue_prevstop.insert(leave_events_catalogue_list)

navMenu_events_catalogue_none = InlineKeyboardMarkup(row_width=1)
leave_events_catalogue_list = InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
navMenu_events_catalogue_none.insert(leave_events_catalogue_list)



#-- КНОПКИ МЕНЮ НАСТРОЙКИ КАТЕГОРИИ (ПЕРЕДЕЛАЛ)

НОВЫЕ

navMenu_category_choose = InlineKeyboardMarkup(row_width=2)
navMenu_category_all = InlineKeyboardButton(text="Все", callback_data="Все")
navMenu_category_free = InlineKeyboardButton(text="Бесплатные", callback_data="Бесплатные")
navMenu_category_edu = InlineKeyboardButton(text="Образовательные", callback_data="Образовательные")
navMenu_category_mus = InlineKeyboardButton(text="Музыкальные", callback_data="Музыкальные")
navMenu_category_clt = InlineKeyboardButton(text="Культурные", callback_data="Культурные")
navMenu_category_ent = InlineKeyboardButton(text="Развлекательные", callback_data="Развлекательные")
navMenu_category_kid = InlineKeyboardButton(text="Детские", callback_data="Детские")
navMenu_category_ehb = InlineKeyboardButton(text='Выставки', callback_data="Выставки")
#navMenu_category_multi = InlineKeyboardButton(text='Многодневные', callback_data="Многодневные")
leave_events_list = InlineKeyboardButton(text="Главное меню", callback_data="main_menu")

navMenu_category_choose.insert(navMenu_category_all)
navMenu_category_choose.insert(navMenu_category_free)
navMenu_category_choose.insert(navMenu_category_edu)
navMenu_category_choose.insert(navMenu_category_mus)
navMenu_category_choose.insert(navMenu_category_clt)
navMenu_category_choose.insert(navMenu_category_ent)
navMenu_category_choose.insert(navMenu_category_kid)
navMenu_category_choose.insert(navMenu_category_ehb)
#navMenu_category_choose.insert(navMenu_category_multi)
navMenu_category_choose.row(leave_events_list)

СТАРЫЕ

# navMenu_category_choose = InlineKeyboardMarkup(row_width=2)
# navMenu_category_all = InlineKeyboardButton(text="Все", callback_data="Все")
# navMenu_category_free = InlineKeyboardButton(text="Бесплатные", callback_data="Бесплатные")
# navMenu_category_exc = InlineKeyboardButton(text="Экскурсионные", callback_data="Экскурсионные")
# navMenu_category_edu = InlineKeyboardButton(text="Образовательные", callback_data="Образовательные")
# navMenu_category_mus = InlineKeyboardButton(text="Музыкальные", callback_data="Музыкальные")
# navMenu_category_clt = InlineKeyboardButton(text="Культурные", callback_data="Культурные")
# navMenu_category_kid = InlineKeyboardButton(text="Детские", callback_data="Детские")
# navMenu_category_gas = InlineKeyboardButton(text="🍔Гастрономические", callback_data="Гастрономические")
# navMenu_category_ent = InlineKeyboardButton(text="Развлекательные", callback_data="Развлекательные")
# navMenu_category_spec = InlineKeyboardButton(text="Специальные", callback_data="Специальные")
# navMenu_category_ehb = InlineKeyboardButton(text='Выставки', callback_data="Выставки")
# navMenu_category_multi = InlineKeyboardButton(text='Многодневные', callback_data="Многодневные")
# navMenu_category_sport = InlineKeyboardButton(text='Спортивные', callback_data="Спортивные")
# navMenu_category_bus = InlineKeyboardButton(text='Деловые', callback_data="Деловые")
# leave_events_list = InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
#
# navMenu_category_choose.insert(navMenu_category_all)
# navMenu_category_choose.insert(navMenu_category_free)
# navMenu_category_choose.insert(navMenu_category_exc)
# navMenu_category_choose.insert(navMenu_category_edu)
# navMenu_category_choose.insert(navMenu_category_mus)
# navMenu_category_choose.insert(navMenu_category_clt)
# navMenu_category_choose.insert(navMenu_category_kid)
# navMenu_category_choose.insert(navMenu_category_gas)
# navMenu_category_choose.insert(navMenu_category_ent)
# navMenu_category_choose.insert(navMenu_category_spec)
# navMenu_category_choose.insert(navMenu_category_sport)
# navMenu_category_choose.insert(navMenu_category_bus)
# navMenu_category_choose.insert(navMenu_category_ehb)
# navMenu_category_choose.insert(navMenu_category_multi)
# navMenu_category_choose.row(leave_events_list)

#--- КНОПКИ МЕНЮ НАСТРОЙКИ ДНЯ (ИЗМЕНИЛ)

today = date.today()
navMenu_day_choose = InlineKeyboardMarkup(row_width=2)
navMenu_day_1 = InlineKeyboardButton(text=str(datetime.strftime(today + timedelta(days=0), "%d.%m %a.")), callback_data=str(today + timedelta(days=0)))
navMenu_day_2 = InlineKeyboardButton(text=str(datetime.strftime(today + timedelta(days=1), "%d.%m %a.")), callback_data=str(today + timedelta(days=1)))
navMenu_day_3 = InlineKeyboardButton(text=str(datetime.strftime(today + timedelta(days=2), "%d.%m %a.")), callback_data=str(today + timedelta(days=2)))
navMenu_day_4 = InlineKeyboardButton(text=str(datetime.strftime(today + timedelta(days=3), "%d.%m %a.")), callback_data=str(today + timedelta(days=3)))
navMenu_day_5 = InlineKeyboardButton(text=str(datetime.strftime(today + timedelta(days=4), "%d.%m %a.")), callback_data=str(today + timedelta(days=4)))
navMenu_day_6 = InlineKeyboardButton(text=str(datetime.strftime(today + timedelta(days=5), "%d.%m %a.")), callback_data=str(today + timedelta(days=5)))
navMenu_day_7 = InlineKeyboardButton(text=str(datetime.strftime(today + timedelta(days=6), "%d.%m %a.")), callback_data=str(today + timedelta(days=6)))
leave_events_list = InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
navMenu_day_choose.insert(navMenu_day_1)
navMenu_day_choose.insert(navMenu_day_4)
navMenu_day_choose.insert(navMenu_day_2)
navMenu_day_choose.insert(navMenu_day_5)
navMenu_day_choose.insert(navMenu_day_3)
navMenu_day_choose.insert(navMenu_day_6)
navMenu_day_choose.insert(navMenu_day_7)
navMenu_day_choose.row(leave_events_list)


#--- КНОПКИ МЕНЮ НАСТРОЙКИ РАДИУСА

navMenu_radius_choose = InlineKeyboardMarkup(row_width=2)
navMenu_radius_1 = InlineKeyboardButton(text='1 км', callback_data="1")
navMenu_radius_2 = InlineKeyboardButton(text='2 км', callback_data="2")
navMenu_radius_3 = InlineKeyboardButton(text='5 км', callback_data="5")
navMenu_radius_4 = InlineKeyboardButton(text='10 км', callback_data="10")
navMenu_radius_5 = InlineKeyboardButton(text='Без геолокации', callback_data="0")
leave_events_list = InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
navMenu_radius_choose.insert(navMenu_radius_1)
navMenu_radius_choose.insert(navMenu_radius_2)
navMenu_radius_choose.insert(navMenu_radius_3)
navMenu_radius_choose.insert(navMenu_radius_4)
navMenu_radius_choose.row(navMenu_radius_5)
navMenu_radius_choose.row(leave_events_list)

#-- КНОПКИ МЕНЮ ВЫБОРА ОРГАНИЗАТОРОВ

navMenu_orgs_choose = InlineKeyboardMarkup(row_width=1)
navMenu_orgs_1 = InlineKeyboardButton(text="Антикафе", callback_data="Антикафе")
navMenu_orgs_2 = InlineKeyboardButton(text="Арт-пространства", callback_data="Арт-центр")
navMenu_orgs_3 = InlineKeyboardButton(text="Библиотеки", callback_data="Библиотека")
navMenu_orgs_4 = InlineKeyboardButton(text="Бары и пабы", callback_data="Бар или паб")
navMenu_orgs_5 = InlineKeyboardButton(text="Дома творчества и культуры", callback_data="ДК и ДТ")
navMenu_orgs_6 = InlineKeyboardButton(text="Галереи", callback_data="Галерея")
navMenu_orgs_7 = InlineKeyboardButton(text="Концертные площадки", callback_data="Концертная площадка")
navMenu_orgs_8 = InlineKeyboardButton(text="Кинотеатры", callback_data="Кинотеатр")
navMenu_orgs_9 = InlineKeyboardButton(text="Клубы", callback_data="Клуб")
navMenu_orgs_10 = InlineKeyboardButton(text="Лектории", callback_data="Лекторий")
navMenu_orgs_11 = InlineKeyboardButton(text='Магазины', callback_data="Магазин")
navMenu_orgs_12 = InlineKeyboardButton(text='Музеи', callback_data="Музей")
navMenu_orgs_13 = InlineKeyboardButton(text='Организаторы экскурсий', callback_data="Организатор экскурсий")
navMenu_orgs_14 = InlineKeyboardButton(text='Организаторы концертов', callback_data="Организатор концертов")
navMenu_orgs_15 = InlineKeyboardButton(text='Парки', callback_data="Парк")
navMenu_orgs_16 = InlineKeyboardButton(text='Разное', callback_data="Разное")
navMenu_orgs_17 = InlineKeyboardButton(text='Рестораны и кафе', callback_data="Ресторан или кафе")
navMenu_orgs_18 = InlineKeyboardButton(text='Студии', callback_data="Студия")
navMenu_orgs_19 = InlineKeyboardButton(text='Фудкорты', callback_data="Фудкорт")
navMenu_orgs_20 = InlineKeyboardButton(text='Театры', callback_data="Театр")
navMenu_orgs_21 = InlineKeyboardButton(text='Частные организаторы', callback_data="Частный организатор")
navMenu_orgs_22 = InlineKeyboardButton(text='Школы', callback_data="Школа")
leave_events_list = InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
navMenu_orgs_choose.insert(navMenu_orgs_1)
navMenu_orgs_choose.insert(navMenu_orgs_2)
navMenu_orgs_choose.insert(navMenu_orgs_3)
navMenu_orgs_choose.insert(navMenu_orgs_4)
navMenu_orgs_choose.insert(navMenu_orgs_5)
navMenu_orgs_choose.insert(navMenu_orgs_6)
navMenu_orgs_choose.insert(navMenu_orgs_7)
navMenu_orgs_choose.insert(navMenu_orgs_8)
navMenu_orgs_choose.insert(navMenu_orgs_9)
navMenu_orgs_choose.insert(navMenu_orgs_10)
navMenu_orgs_choose.insert(navMenu_orgs_11)
navMenu_orgs_choose.insert(navMenu_orgs_12)
navMenu_orgs_choose.insert(navMenu_orgs_13)
navMenu_orgs_choose.insert(navMenu_orgs_14)
navMenu_orgs_choose.insert(navMenu_orgs_15)
navMenu_orgs_choose.insert(navMenu_orgs_16)
navMenu_orgs_choose.insert(navMenu_orgs_17)
navMenu_orgs_choose.insert(navMenu_orgs_18)
navMenu_orgs_choose.insert(navMenu_orgs_19)
navMenu_orgs_choose.insert(navMenu_orgs_20)
navMenu_orgs_choose.insert(navMenu_orgs_21)
navMenu_orgs_choose.insert(navMenu_orgs_22)
navMenu_orgs_choose.row(leave_events_list)
'''