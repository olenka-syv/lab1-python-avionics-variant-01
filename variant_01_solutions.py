"""
Лабораторна робота: Варіант 1
Студент: Сиваченко Олена
Група: EIP 30
"""

# Задача 1: Аналіз телеметрії орієнтації БПЛА (if/elif/else)
def check_orientation(roll: float = 23, pitch: float = 45) -> str:
    """
    Перевіряє кути крен (roll) та тангаж (pitch) БПЛА.
    Межі: |roll| <= 30, |pitch| <= 20.
    Повертає один із рядків:
    "Штатний політ", "Критичний крен", "Критичний тангаж", "Аварійний режим"
    """
    if abs(roll) <= 30 and abs(pitch) <= 20:
        return ("Штатний політ")
    elif abs(roll) <= 30 and abs(pitch) > 20:
        return ("Критичний тангаж")
    elif abs(roll) > 30 and abs(pitch) <= 20:
        return ("Критичний крен")
    else:
        return ("Аварійний режим")
print(check_orientation())

# Задача 2: Декодер стану сервоприводів (match-case)
def decode_servo_status(actuator_data: tuple = ("ABC", 3, 2000)) -> str:
    """
    Приймає кортеж (actuator_id, status_code, current_mA).
    Використовує match-case та вирази-вартові (if):
    - current_mA > 2000 -> "Перевантаження приводу {id}"
    - status_code == 0 -> "Привід {id} вимкнено"
    - штатний режим -> "Привід {id} працює штатно ({current_mA} мА)"
    - за замовчуванням -> "Невідомий формат даних"
    """
#Не знаю, як розбирати випадок коли current_mA > 2000 та status_code == 0. 
#На виконання обох умов не передбачено конкретної дії. 
#Тому розібрала окремо цей case.
#Чи є обмеження на тип даних у кортежі? Бо буде видавати помилку, якщо current_mA не буде числом. 
#Поки не придумала як відсіяти випадки коли це не число використовуючи лише match-case...
    match actuator_data:
        case (actuator_id, 0, current_mA) if current_mA > 2000:
            return f"Обидві умови порушено, не зрозуміло що робити!"
        case (actuator_id, status_code, current_mA) if current_mA > 2000:
            return f"Перевантаження приводу {actuator_id}"
        case (actuator_id, 0, current_mA):
            return f"Привід {actuator_id} вимкнено"
        case (actuator_id, status_code, current_mA) if current_mA <= 2000:
            return f"Привід {actuator_id} працює штатно ({current_mA} мА)"
        case _:
            return f"Невідомий формат даних"
print(decode_servo_status())

# Задача 3: Обробка буфера UART (while / else)
def parse_uart_buffer(buffer: list = [0xD2, 0xAB, 0x45]) -> str:
    """
    Послідовно вилучає перші елементи зі списку buffer за допомогою while,
    поки не зустріне заголовок 0xAA (повертає "Кадр знайдено").
    Якщо список спорожнів без виклику break -> повертає через else: "Заголовок відсутній"
    """
    result = "Заголовок відсутній"
    while len(buffer) > 0:
        if buffer[0] == 0xAA: 
            result = "Кадр знайдено"
            break
        else:
            del buffer[0]
    return (result)
print (parse_uart_buffer())

# Задача 4: Аналіз тиску двигуна (enumerate / range)
def check_engine_pressure(pressures: list = [100, 200, 300, 50]) -> list | str:
    """
    Перебирає список тисків за допомогою enumerate.
    Збирає кортежі (індекс, значення) для всіх тисків < 150 кПа.
    Якщо є аномалії -> повертає список кортежів [(idx, val), ...].
    Якщо тиск всюди в нормі -> повертає "Тиск у нормі".
    """
    problems = []
    for (index, value) in enumerate(pressures):
        if value < 150:
            problems.append((index, value))
    if len(problems) > 0:
        return (problems)
    else:
        return ("Тиск у нормі")
print(check_engine_pressure())
