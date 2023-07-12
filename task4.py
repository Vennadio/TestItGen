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
    
    #Сортировка по номеру
    def sort_by_number(autobus_list):
        routes = []
        with io.open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            if line.startswith("Номер маршрута"):
                route_number = line.split(": ")[1]
                routes.append(route_number)

        sorted_routes = sorted(routes, reverse=True)

        return sorted_routes

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



# Создание экземпляра класса Autobus
my_bus = Autobus("Минск", "Брест", "Маршрут №516", "2h 26min")

# Использование геттеров для получения значений полей
print(my_bus.get_begin_dir()) 
print(my_bus.get_end_dir()) 

info = my_bus.get_info()

print(info)

# Создание маршрутов
autopark = Autobus.create_autopark()

# Сохранение информации об автобусах в файл
Autobus.save_to_file(autopark, 'autobus_info.txt')


file_lines = Autobus.show_autopark('autobus_info.txt')

# Вывод информации на экран
for line in file_lines:
    print(line.strip())



# Чтение информации из файла
autopark = Autobus.read_from_file('autobus_info.txt')

# Ввод названия пункта пользователем
stop_name = input("Введите название пункта остановки: ")

# Поиск автобусов по пункту остановки
matching_autobuses = Autobus.search_by_stop(autopark, stop_name)

# Вывод информации об автобусах
if len(matching_autobuses) > 0:
    print(f"Автобусы, начинающиеся или заканчивающиеся в пункте '{stop_name}':")
    for autobus in matching_autobuses:
        info = autobus.get_info()
        print(info)
else:
    print(f"Нет информации об автобусах, начинающихся или заканчивающихся в пункте '{stop_name}'.")