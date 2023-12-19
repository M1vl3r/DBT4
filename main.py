import mysql.connector

# Функция для выполнения SQL-запроса
def execute_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

# Функция для подключения к базе данных
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='fishing_company',
            user='root',
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Основная функция
def main():
    # Подключаемся к базе данных
    connection = connect_to_database()

    if not connection:
        print("Не удалось подключиться к базе данных.")
        return

    try:
        # Запрос номера задания
        task_number = int(input("Введите номер задания (1-11): "))

        # Выполнение соответствующего SQL-запроса
        if task_number == 1:
            query = "SELECT BoatName, TripDate, TotalCatch FROM FishingTrips;"
            result = execute_query(connection, query)
            print("Результат запроса:")
            print(result)
        elif task_number == 2:
            # Добавление выхода катера в море
            query = "INSERT INTO FishingTrips (BoatID, TripDate, Captain, Crew) VALUES (1, '2022-01-01', 'Капитан', 'Боцман, Рыбак1, Рыбак2');"
            execute_query(connection, query)
            print("Выход катера в море добавлен успешно.")
        elif task_number == 3:
            # Для указанного интервала дат вывести для каждого сорта рыбы список катеров с наибольшим уловом
            query = "SELECT FishType, BoatName, MAX(TotalCatch) AS MaxCatch FROM FishingTrips WHERE TripDate BETWEEN '2022-01-01' AND '2022-12-31' GROUP BY FishType;"
            result = execute_query(connection, query)
            print("Результат запроса:")
            print(result)
        elif task_number == 4:
            # Для указанного интервала дат вывести список банок с указанием среднего улова за этот период
            query = "SELECT BankName, AVG(TotalCatch) AS AvgCatch FROM FishingTrips WHERE TripDate BETWEEN '2022-01-01' AND '2022-12-31' GROUP BY BankName;"
            result = execute_query(connection, query)
            print("Результат запроса:")
            print(result)
        elif task_number == 5:
            # Добавление новой банки
            query = "INSERT INTO FishingBanks (BankName, Location) VALUES ('Новая банка', 'Новое место');"
            execute_query(connection, query)
            print("Новая банка добавлена успешно.")
        elif task_number == 6:
            # Для заданной банки вывести список катеров, которые получили улов выше среднего
            query = "SELECT BoatName, TotalCatch FROM FishingTrips WHERE BankID = 1 AND TotalCatch > (SELECT AVG(TotalCatch) FROM FishingTrips WHERE BankID = 1);"
            result = execute_query(connection, query)
            print("Результат запроса:")
            print(result)
        elif task_number == 7:
            # Вывести список сортов рыбы и для каждого сорта список рейсов с указанием даты выхода и возвращения, количества улова
            query = "SELECT FishType, BoatName, TripDate, ReturnDate, TotalCatch FROM FishingTrips;"
            result = execute_query(connection, query)
            print("Результат запроса:")
            print(result)
        elif task_number == 8:
            # Добавление данных о сорте и количестве пойманной рыбы для выбранного рейса и банки
            query = "INSERT INTO FishCatches (TripID, FishType, CatchAmount) VALUES (1, 'Треска', 50);"
            execute_query(connection, query)
            print("Данные о пойманной рыбе добавлены успешно.")
        elif task_number == 9:
            # Изменение характеристик выбранного катера
            query = "UPDATE Boats SET BoatLength = 25 WHERE BoatID = 1;"
            execute_query(connection, query)
            print("Характеристики катера изменены успешно.")
        elif task_number == 10:
            # Добавление нового катера
            query = "INSERT INTO Boats (BoatName, BoatType, BoatLength) VALUES ('Новый катер', 'Тип', 20);"
            execute_query(connection, query)
            print("Новый катер добавлен успешно.")
        elif task_number == 11:
            # Для указанного сорта рыбы и банки вывести список рейсов с указанием количества пойманной рыбы
            query = "SELECT BoatName, TripDate, ReturnDate, CatchAmount FROM FishingTrips JOIN FishCatches USING (TripID) WHERE FishType = 'Треска' AND BankID = 1;"
            result = execute_query(connection, query)
            print("Результат запроса:")
            print(result)
        else:
            print("Некорректный номер задания. Введите число от 1 до 11.")
    finally:
        # Закрываем соединение с базой данных
        connection.close()

if __name__ == "__main__":
    main()
