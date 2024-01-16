import requests

URL_SERVICE = " https://50186371-485b-43e4-9a8b-5286a8e70463.serverhub.praktikum-services.ru"
CREATE_ORDERS = "/api/v1/orders"

orders_body = {
    "firstName": "Варя",
    "lastName": "Куранина",
    "address": "Елочная 55",
    "metroStation": 15,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-02-12",
    "comment": "Привет, Варя",
    "color": [
        "BLACK"
    ]
}


# Создание заказа
def create_order(body):
    return requests.post(URL_SERVICE + CREATE_ORDERS,
                         json=body)


# Получение заказа по трекеру
def get_order(track_number):
    get_order_url = f"{URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response


# Куранина Екатерина, 12 когорта - Финальный проект. Инженер по тестированию плюс
# Автотест
def test_order():
    response = create_order(orders_body)
    track_number = response.json()["track"]
    order_response = get_order(track_number)
    assert order_response.status_code == 200, f"Error:{order_response.status_code}"
    order_data = order_response.json()
    print("Данные заказа:")
    print(order_data)
