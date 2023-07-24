import io

class Autobus:
    def __init__(self, begin_dir, end_dir, number_trace, time_riding):
        self._begin_dir = begin_dir
        self._end_dir = end_dir
        self._number_trace = number_trace
        self._time_riding = time_riding

    # Геттеры для каждого поля
    def get_begin_dir(self):
        return self._begin_dir

    def get_end_dir(self):
        return self._end_dir

    def get_number_trace(self):
        return self._number_trace

    def get_time_riding(self):
        return self._time_riding

    # Сеттеры для каждого поля
    def set_begin_dir(self, new_begin_dir):
        self._begin_dir = new_begin_dir

    def set_end_dir(self, new_end_dir):
        self._end_dir = new_end_dir

    def set_number_trace(self, new_number_trace):
        self._number_trace = new_number_trace

    def set_time_riding(self, new_time_riding):
        self._time_riding = new_time_riding

    #Метод с общей информацией
    def get_info(self):
        return f'----------------------------------------\n'\
               f'Начальное направление: {self._begin_dir}\n' \
               f'Конечное направление: {self._end_dir}\n' \
               f'Номер маршрута: {self._number_trace}\n' \
               f'Время в пути: {self._time_riding}\n' \
               f'----------------------------------------\n'\

    def create_autopark():
        num_buses = int(input("Введите количество автобусов: "))
        autobus_list = []

        for i in range(num_buses):
            print(f"Ввод информации для автобуса {i+1}:")
            begin_dir = input("Введите начальное направление: ")
            end_dir = input("Введите конечное направление: ")
            number_trace = input("Введите номер маршрута: ")
            time_riding = input("Введите время в пути: ")

            autobus = Autobus(begin_dir, end_dir, number_trace, time_riding)
            autobus_list.append(autobus)

        return autobus_list

    def save_to_file(autopark, file_name):
        with io.open(file_name, 'w', encoding='utf-8') as file:
            for i, autobus in enumerate(autopark, start=1):
                file.write(f"Информация об автобусе {i}:\n")
                file.write(autobus.get_info())
                file.write("\n")

        print(f"Информация об автобусах сохранена в файл {file_name}.")

    def show_autopark(file_name):
        with io.open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return lines
    
    @staticmethod
    def sort_by_number_desc(autobus_list):
        sorted_autopark = sorted(autobus_list, key=lambda autobus: autobus.get_number_trace(), reverse=True)
        return sorted_autopark


    @staticmethod
    def read_from_file(file_name):
        autobus_list = []

        with io.open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        #Получаем и обрабатываем информацию из файла
        autobus_info = {}
        for line in lines:
            line = line.strip()
            if line.startswith("Информация об автобусе"):
                if autobus_info:
                    autobus = Autobus(
                        autobus_info['_begin_dir'],
                        autobus_info['_end_dir'],
                        autobus_info['_number_trace'],
                        autobus_info['_time_riding']
                    )
                    autobus_list.append(autobus)
                    autobus_info = {}
            elif line.startswith("Начальное направление"):
                autobus_info['_begin_dir'] = line.split(": ")[1]
            elif line.startswith("Конечное направление"):
                autobus_info['_end_dir'] = line.split(": ")[1]
            elif line.startswith("Номер маршрута"):
                autobus_info['_number_trace'] = line.split(": ")[1]
            elif line.startswith("Время в пути"):
                autobus_info['_time_riding'] = line.split(": ")[1]

        # Добаил последний автобус за эталон 
        if autobus_info:
            autobus = Autobus(
                autobus_info['_begin_dir'],
                autobus_info['_end_dir'],
                autobus_info['_number_trace'],
                autobus_info['_time_riding']
            )
            autobus_list.append(autobus)

        return autobus_list
    
    
    @staticmethod
    def search_by_stop(autopark, stop_name):
        matching_autobuses = []
        for autobus in autopark:
            if stop_name.lower() in autobus._begin_dir.lower() or stop_name.lower() in autobus._end_dir.lower():
                matching_autobuses.append(autobus)
        return matching_autobuses

#Решил создать методы вне класса
# Меню
def create_autopark_menu():
    autopark = Autobus.create_autopark()
    print("Автопарк успешно создан!")
    return autopark

# Меню для сохранения в файл
def save_to_file_menu(autopark):
    file_name = input("Введите имя файла для сохранения информации об автобусах: ")
    Autobus.save_to_file(autopark, file_name)

# Меню для отображения автопарка
def show_autopark_menu():
    file_name = input("Введите имя файла с информацией об автобусах: ")
    file_lines = Autobus.show_autopark(file_name)
    for line in file_lines:
        print(line.strip())

# Меню для чтения из файла
def read_from_file_menu():
    file_name = input("Введите имя файла для чтения информации об автобусах: ")
    autopark = Autobus.read_from_file(file_name)
    return autopark

# Меню по поиску имени остановки
def search_by_stop_menu(autopark):
    stop_name = input("Введите название пункта остановки: ")
    matching_autobuses = Autobus.search_by_stop(autopark, stop_name)
    if len(matching_autobuses) > 0:
        print(f"Автобусы, начинающиеся или заканчивающиеся в пункте '{stop_name}':")
        for autobus in matching_autobuses:
            print(autobus.get_info())
    else:
        print(f"Нет информации об автобусах, начинающихся или заканчивающихся по параметрам '{stop_name}'.")

# Меню для сортировки по номеру маршрута
def sort_by_number_menu(autopark):
    sorted_autopark = Autobus.sort_by_number_desc(autopark)
    print("Список автобусов, отсортированных по номеру маршрута (по убыванию):")
    for bus in sorted_autopark:
        print(bus.get_info())

# Главное меню
def main_menu():
    autopark = []
    while True:
        print("----------- Главное меню -----------")
        print("1. Создать автопарк")
        print("2. Сохранить информацию об автобусах в файл")
        print("3. Вывести информацию об автобусах из файла")
        print("4. Сортировать автобусы по номеру маршрута")
        print("5. Читать информацию об автобусах из файла")
        print("6. Поиск автобусов по пункту остановки")
        print("7. Выход")
        
        choice = input("Выберите действие (введите соответствующую цифру): ")
        
        if choice == "1":
            autopark = create_autopark_menu()
        elif choice == "2":
            if autopark:
                save_to_file_menu(autopark)
            else:
                print("Сначала нужно создать автопарк!")
        elif choice == "3":
            show_autopark_menu()
        elif choice == "4":
            if autopark:
                sort_by_number_menu(autopark)
            else:
                print("Сначала нужно создать автопарк!")
        elif choice == "5":
            autopark = read_from_file_menu()
        elif choice == "6":
            if autopark:
                search_by_stop_menu(autopark)
            else:
                print("Сначала нужно создать автопарк!")
        elif choice == "7":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, введите цифру от 1 до 7.")
            
if __name__ == "__main__":
    main_menu()
    