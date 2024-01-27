def count_older_than(year, data):
    count = 0
    for line in data:
        parts = line.split()
        birth_year = int(parts[-1].split('.')[2])
        if birth_year < year:
            count += 1
    return count

def filter_by_year_range(start_year, end_year, data):
    result = []
    for line in data:
        parts = line.split()
        birth_year = int(parts[-1].split('.')[2])
        if start_year <= birth_year <= end_year:
            result.append((parts[0], parts[1], parts[2], birth_year))
    return result

try:
    with open("Perepis.txt", "r") as file:
        data = file.readlines()

    older_than_1978 = count_older_than(1978, data)
    print("Число жителей, родившихся до 1978 года:", older_than_1978)

    start_year = int(input("Введите начальный год диапазона: "))
    end_year = int(input("Введите конечный год диапазона: "))

    filtered_data = filter_by_year_range(start_year, end_year, data)
    print(f"Данные людей, родившихся с {start_year} по {end_year} год:")
    if (len(filtered_data)==0):
        print("Людей в этом диапозоне не найдено.")
    for person in filtered_data:
        print(f"{person[0]} {person[1]} {person[2]} - {person[3]} год")

except FileNotFoundError:
    print("Файл Perepis.txt не найден.")
except ValueError:
    print("Ошибка ввода данных. Пожалуйста, введите года адекватно.")
