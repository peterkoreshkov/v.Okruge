//  ЗАПУСК
let tg = window.Telegram.WebApp;

let search_events_but = document.getElementById("search_events_but")
let search_offers_but = document.getElementById("search_offers_but")
let show_stats_but = document.getElementById("show_stats_but")
let show_help_but = document.getElementById("show_help_but")
let exit_but = document.getElementById("exit_but")
let cat_all_but = document.getElementById("cat_all_but")
let cat_free_but = document.getElementById("cat_free_but")
let cat_kids_but = document.getElementById("cat_kids_but")
let cat_exhib_but = document.getElementById("cat_exhib_but")
let to_menu_from_cats_but = document.getElementById("to_menu_from_cats_but")
let days0_but = document.getElementById("days0_but")
let days1_but = document.getElementById("days1_but")
let days2_but = document.getElementById("days2_but")
let days3_but = document.getElementById("days3_but")
let days4_but = document.getElementById("days4_but")
let days5_but = document.getElementById("days5_but")
let days6_but = document.getElementById("days6_but")
let to_menu_from_dates_but = document.getElementById("to_menu_from_dates_but")
let confirm_events_but = document.getElementById("confirm_events_but")

let chosen_category = ""
tg.expand();


//  В МЕНЮ ИЗ ВЫБОРА КАТЕГОРИЙ
to_menu_from_cats_but.addEventListener("click", function(){
    document.getElementById("choose_category_menu").style.display = "none";
    document.getElementById("main_menu").style.display = "block";
});

//  В МЕНЮ ИЗ ВЫБОРА ДАТЫ
to_menu_from_dates_but.addEventListener("click", function(){
    document.getElementById("choose_date_menu").style.display = "none";
    document.getElementById("main_menu").style.display = "block";
});

//  КНОПКА ИСКАТЬ МЕРОПРИЯТИЯ
search_events_but.addEventListener("click", function(){
    document.getElementById("main_menu").style.display = "none";
    document.getElementById("choose_category_menu").style.display = "block";
});

//   КНОПКА ВЫБОРА КАТЕГОРИИ ВСЕ
cat_all_but.addEventListener("click", function(){
    chosen_category = document.getElementById("cat_all_but").value;
    chosen_date = "Неопределено"
    document.getElementById("choose_category_menu").style.display = "none";
    document.getElementById("choose_date_menu").style.display = "block";
});

//   КНОПКА ВЫБОРА КАТЕГОРИИ БЕСПЛАТНЫЕ
cat_free_but.addEventListener("click", function(){
    chosen_category = document.getElementById("cat_free_but").value;
    tg.sendData(chosen_category);
    document.getElementById("choose_category_menu").style.display = "none";
    document.getElementById("confirm_events_menu").style.display = "block";
});

//   КНОПКА ВЫБОРА КАТЕГОРИИ ДЕТСКИЕ
cat_kids_but.addEventListener("click", function(){
    chosen_category = document.getElementById("cat_kids_but").value;
    tg.sendData(chosen_category);
    document.getElementById("choose_category_menu").style.display = "none";
    document.getElementById("confirm_events_menu").style.display = "block";
});

//  КНОПКА ВЫБОРА КАТЕГОРИИ ВЫСТАВКИ
cat_exhib_but.addEventListener("click", function(){
    chosen_category = document.getElementById("cat_exhib_but").value;
    tg.sendData(chosen_category);
    document.getElementById("choose_category_menu").style.display = "none";
    document.getElementById("confirm_events_menu").style.display = "block";
});

//  КНОПКА ПРИСТУПИТЬ К ПОИСКУ
confirm_events_but.addEventListener("click", function(){
    document.getElementById("confirm_events_menu").style.display = "none";
    document.getElementById("show_events_menu").style.display = "block";
    let user_data = {
    "category": chosen_category,
    "date": chosen_date}
    Telegram.WebApp.sendData(JSON.stringify(user_data))
});

//  КНОПКА ВЫХОД
exit_but.addEventListener("click", function(){
    tg.close()
});

//let show_events_menu = document.getElementById("show_events_menu");
//let p = document.createElement("p");
//p.innerText = ${tg.initDataUnsafe.combined_message};
//show_events_menu.appendChild(p);