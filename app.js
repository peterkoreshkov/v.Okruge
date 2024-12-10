//  ЗАПУСК
let tg = window.Telegram.WebApp;
tg.expand();

//  В МЕНЮ ИЗ ВЫБОРА КАТЕГОРИЙ
to_menu_from_cats_but.addEventListener("click", () => {
    document.getElementById("choose_category_menu").style.display = "none";
    document.getElementById("main_menu").style.display = "block";
});

//  В МЕНЮ ИЗ ВЫБОРА ДАТЫ
to_menu_from_dates_but.addEventListener("click", () => {
    document.getElementById("choose_date_menu").style.display = "none";
    document.getElementById("main_menu").style.display = "block";
});

//  КНОПКА ИСКАТЬ МЕРОПРИЯТИЯ
search_events_but.addEventListener("click", () => {
    document.getElementById("main_menu").style.display = "none";
    document.getElementById("choose_category_menu").style.display = "block";
});

//   КНОПКА ВЫБОРА КАТЕГОРИИ ВСЕ

cat_all_but.addEventListener("click", () => {
    let chosen_category = document.getElementById("cat_all_but").value;

    document.getElementById("choose_category_menu").style.display = "none";
    document.getElementById("choose_date_menu").style.display = "block";
});

//   КНОПКА ВЫБОРА КАТЕГОРИИ БЕСПЛАТНЫЕ
cat_free_but.addEventListener("click", () => {
    document.getElementById("choose_category_menu").style.display = "none";
    document.getElementById("show_events_menu").style.display = "block";
});

//   КНОПКА ВЫБОРА КАТЕГОРИИ ДЕТСКИЕ
cat_kids_but.addEventListener("click", () => {
    document.getElementById("choose_category_menu").style.display = "none";
    document.getElementById("show_events_menu").style.display = "block";
});

//  КНОПКА ВЫБОРА КАТЕГОРИИ ВЫСТАВКИ
cat_exhib_but.addEventListener("click", () => {
    document.getElementById("choose_category_menu").style.display = "none";
    document.getElementById("show_events_menu").style.display = "block";
});

//  КНОПКА ВЫХОД
exit_but.addEventListener("click", () => {
    tg.close()
});