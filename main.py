import requests

# URL API для получения случайного пользователя
url = 'https://randomuser.me/api/'


def get_random_user():
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        user = data['results'][0]['name']['first']  # Пример получения имени пользователя
        return user
    else:
        return 'Ошибка при получении случайного пользователя'


# Вызов функции для получения случайного пользователя
random_user = get_random_user()
print(random_user)
