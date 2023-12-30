from Configuration.Config import connection


class Model:

    def get(self, table):
        with connection().cursor() as cursor:
            select_all_rows = f"SELECT * FROM {table}"
            cursor.execute(select_all_rows)
            return cursor.fetchall()
        connection().close()

    def get1(self):
        with connection().cursor() as cursor:
            query = (f"SELECT motorboat.Name, catch.Date_O, catch.Weight "
                     f"FROM motorboat "
                     f"JOIN catch "
                     f"ON motorboat.ID_Motorboat = catch.ID_Motorboat")
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

    def get2(self):
        with connection().cursor() as cursor:
            query = (f"INSERT INTO commands (ID_Motorboat, ID_Fishermen, Job, Date_D, Date_E) "
                     f"VALUES ('2', '2', 'Капитан', '2023-04-05', '2023-07-05')")
            print("Запись добавлена.")
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

    def get3(self):
        with connection().cursor() as cursor:
            query = (f"SELECT catch.ID_Fishermen, MAX(catch.Weight) "
                     f"FROM catch "
                     f"WHERE catch.Date_O BETWEEN '2021-01-19' AND '2024-01-21'"
                     f"GROUP BY catch.ID_Fishermen")
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

    def get4(self):
        with connection().cursor() as cursor:
            query = (f"SELECT catch.ID_Fishermen, AVG(catch.Weight) "
                     f"FROM catch "
                     f"WHERE catch.Date_O BETWEEN '2021-01-19' AND '2024-01-21' "
                     f"GROUP BY catch.ID_Fishermen")
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

    def get5(self):
        with connection().cursor() as cursor:
            query = (f"INSERT INTO motorboat (ID_Motorboat, Name, Type, Vodoizmeschenie, Date_B) "
                     f"VALUES (15, 'Урал-2015', 'Моторный(Крупногабаритный)', '3004', '2015-04-10')")
            print("Запись добавлена.")
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

    def get6(self):
        with connection().cursor() as cursor:
            query = (f"SELECT catch.ID_Fishermen, catch.Weight "
                     f"FROM catch "
                     f"JOIN motorboat "
                     f"ON catch.ID_Motorboat = motorboat.ID_Motorboat "
                     f"WHERE motorboat.Name = 'Ледоход23' AND catch.Weight > (SELECT AVG(catch.Weight) FROM catch)")
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

    def get9(self):
        with connection().cursor() as cursor:
            query = (f"UPDATE motorboat "
                     f"SET Name  = 'Катер2011' , Type = 'Моторный(Малогабаритный)', Vodoizmeschenie = '1800.00', Date_B = '2011-03-12' "
                     f"WHERE ID_Motorboat = 1")
            print("Запись обновлена.")
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

    def get10(self):
        with connection().cursor() as cursor:
            query = (f"INSERT INTO motorboat (ID_Motorboat, Name, Type, Vodoizmeschenie, Date_B) "
                     f"VALUES (24, 'Катер999', 'Моторный', '593', '2022-05-10')")
            print("Запись добавлена.")
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

