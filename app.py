from flask import Flask, render_template, request, jsonify,url_for

app = Flask(__name__)

tours_db = {
    "1": {
        "name": " Novotel Beijing Peace",
        "description": "Расположен в центре Пекина, в районе Ванфуцзин. Отель находится в пешей доступности от площади Тяньаньмэнь и Запретного города, очень близко к Храму неба, Цзиншани, Бэйхаю, Хоухаю, старому городу и торговым центрам. Храм Ламы, Имперский колледж, Стадион Трудящихся и Санлитун.",
        "price": 15000,
        "duration": 14,
        "direction": "Пекин",
        "img": "img1.jpg"
    },
    "2": {
        "name": " Renaissance Shanghai Yu Garden Hotel",
        "description": "Большой центральный район: магазины на Нанкинской улице, набережная Вайтань и музеи на Народной площади.",
        "price": 10000,
        "duration": 10,
        "direction": "Шанхай",
        "img": "img2.jpg"
    },
    "3": {
        "name": " Guangzhou Huangpu·Caleals Apartment·Pazhou Exhibition",
        "description": "Находится в 1,6 км от телебашни Гуанчжоу. Отель находится в 5 км от музея Гуандун и в 6 км от торгового центра TaiKoo Hui.",
        "price": 12000,
        "duration": 12,
        "direction": "Гуанчжоу",
        "img": "img3.jpg"
    },
    "4": {
        "name": " Hilton Beijing Wangfujing",
        "description": "Культурный центр с дворцовым комплексом ""Запретный город"", площадью Тяньаньмэнь и храмом XVII века.",
        "price": 14000,
        "duration": 10,
        "direction": "Пекин",
        "img": "img4.jpg"
    },
    "5": {
        "name": " Fairmont Beijing Hotel",
        "description": "Большой район: рынки, где можно купить одежду, изделия ручной работы и цветы, и парк Чаоян с искусственным пляжем.",
        "price": 17000,
        "duration": 7,
        "direction": "Пекин",
        "img": "img5.jpg"
    },
    "6": {
        "name": " Radisson Blu Hotel Shanghai New World",
        "description": "Расположен напротив Народной площади, Шанхайского художественного музея, Шанхайского большого театра и торгового района «Восточная Нанкинская улица».",
        "price": 15000,
        "duration": 14,
        "direction": "Шанхай",
        "img": "img6.jpg"
    },
    "7": {
        "name": " The Langham, Shanghai, Xintiandi",
        "description": "Hасположен в торгово-развлекательном районе Синьтяньди в Шанхае, рядом с торговой улицей Хуайхай, в окружении различных модных клубов, роскошных ресторанов интернациональной кухни и дизайнерских бутиков.",
        "price": 15000,
        "duration": 14,
        "direction": "Шанхай",
        "img": "img7.jpg"
    },
    "8": {
        "name": " Hilton Guangzhou Tianhe",
        "description": "Расположение для прогулок, посещения ресторанов и осмотра достопримечательностей",
        "price": 15000,
        "duration": 14,
        "direction": "Гуанчжоу",
        "img": "img8.jpg"
    },
    "9": {
        "name": " Sofitel Guangzhou Sunrich",
        "description": "Расположение для прогулок, посещения ресторанов и осмотра достопримечательностей",
        "price": 15000,
        "duration": 14,
        "direction": "Гуанчжоу",
        "img": "img9.jpg"
    },
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        direction = request.form['direction']
        tours = []
        for tour_id, tour in tours_db.items():
            if tour['direction'] == direction:
                tour['id'] = tour_id
                tours.append(tour)
        return render_template('direction.html', tours=tours, direction=direction)
    else:
        return render_template('search.html')

@app.route('/tour/<tour_id>')
def tour(tour_id):
    tour = tours_db.get(tour_id)
    if tour:
        return render_template('tour.html', tour=tour)
    else:
        return jsonify({'error': 'Тур не найден'})

if __name__ == '__main__':
    app.run(debug=True)
