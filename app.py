from flask import Flask, render_template
from data import *

app = Flask(__name__)
tours_list = list(tours.items())

@app.route('/')
def main_page():
    '''
    Роут для вывода основной страницы со всеми турами

    tours_to_show - список, хроанящий в себе "id" первых 6 туров, с наибольшим значением "stars"

    :return: готовый шаблон с переданными аргументами

    '''

    tours_to_show = (sorted(tours, reverse=True, key=lambda k: tours[k]['stars']))[:6]
    # tours_list = list(tours.items())
    # print(sorted(tours_list, reverse=True, key=lambda x: x[1].get('price'))) Можно еще так - собирается сразу с id и телом тура
    # постарался использовать оба варианта в коде

    return render_template('index.html', subtitle=subtitle,description=description,
                           tours=tours, tours_id=tours_to_show, departures=departures)


@app.route('/from/<city>')
def direction_page(city):
    '''
    Роут для вывода страницы туров, город отправления которых = "city"

    tours_by_city - итоговый словарь всех туров, в которых город отправления = "city"
    prices - список, хранящий в себе все "price" из списка туров по городу
    nights - список, хранящий в себе все "nights" из списка туров по городу

    :return: готовый шаблон с переданными аргументами

    '''
    tours_by_city = {}
    prices = []
    nights = []
    for tour_id, tour in tours.items():
        if tour.get('departure') == city:
            tours_by_city[tour_id] = tour
            prices.append(tour.get('price'))
            nights.append(tour.get('nights'))

    return render_template('direction.html', tours=sorted(list(tours_by_city.items()),
                           reverse=True, key=lambda x: x[1].get('stars')),
                           prices=prices, nights=nights,
                           departures=departures, city=city)


@app.route('/tours/<int:tour_id>')
def tour_page(tour_id):
    '''
    Роут для вывода страницы с описанием тура

    :return: готовый шаблон с переданными аргументами

    '''
    return render_template('tours.html', tour=tours.get(tour_id),
                           departures=departures)


if __name__ == '__main__':
    app.run()
