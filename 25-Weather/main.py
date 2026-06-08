import pandas

_file_path = "weather_data.csv"


def read_csv(file_path):
    from csv import reader

    with open(file_path, "r") as file:
        data = list(reader(file))

    return data


def read_temperatures(file_path):
    data = read_csv(file_path)
    temperatures = [int(row[1]) for row in data[1:]]

    return temperatures


def average_temperature(temperatures):
    # from functools import reduce

    # return reduce(lambda acc, temp: acc + temp, temperatures.to_list(), 0) / len(temperatures)
    return sum(temperatures) / len(temperatures)


def max_temperature(temperatures):
    max_temp = temperatures[0]

    for temp in temperatures:
        if temp > max_temp:
            max_temp = temp

    return max_temp


def use_file(file_path):
    data = read_csv(_file_path)

    for line in data:
        print(line)

    temperatures = read_temperatures(_file_path)

    print(temperatures)
    print(f"Average temperature: {average_temperature(temperatures)}")


def pandas_read_csv(file_path):
    data = pandas.read_csv(file_path)

    return data


def pandas_read_temperatures(file_path):
    data = pandas_read_csv(file_path)
    temperatures = data["temp"]

    return temperatures


def pandas_average_temperature(temperatures):
    # pandas series has a built-in method to calculate the mean, so we can use that instead of converting to a list and
    # calculating the mean manually.
    return temperatures.mean()


def pandas_max_temperature(temperatures):
    return temperatures.max()


def pandas_day_temp_fahrenheit(data, day):
    day_temp = data[data.day == day].temp[0]

    return day_temp * 9 / 5 + 32


def use_pandas(file_path):
    data = pandas_read_csv(file_path)

    print(data)
    # print(data.to_records())
    # print(data.to_dict())
    # print(data.to_dict('records'))

    temperatures = pandas_read_temperatures(file_path)

    print(temperatures)
    print(f"Average temperature: {pandas_average_temperature(temperatures)}")

    max_temp = pandas_max_temperature(temperatures)

    print(f"Max temperature: {max_temp}")
    print(f"Day(s) with max temperature:\n{data[data['temp'] == max_temp]}")

    print(f"Monday's temperature in Fahrenheit: {pandas_day_temp_fahrenheit(data, 'Monday')}")


if __name__ == "__main__":
    use_file(_file_path)
    use_pandas(_file_path)
