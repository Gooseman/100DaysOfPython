# file1 = ["3", "6", "5", "8", "33", "12", "7", "4", "72", "2", "42", "13"]
# file2 = ["3", "6", "13", "5", "7", "89", "12", "3", "33", "34", "1", "344", "42"]


def get_shared_numbers():
    file1 = open("file1.txt").readlines()
    file2 = open("file2.txt").readlines()

    # Use a set comprehension to find the unique numbers in file1 that are not in file2
    # shared_numbers = {int(num) for num in file1 if num in file2}
    shared_numbers = [int(num) for num in file1 if num in file2]

    print(shared_numbers)
    print(sorted(shared_numbers))


def get_fahrenheit():
    weather_c = {
        "Monday": 12,
        "Tuesday": 14,
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24,
    }
    weather_f = {day: ((temp * 9 / 5) + 32) for day, temp in weather_c.items()}

    print(weather_f)


def nato():
    import pandas

    nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
    dictionary = nato_dictionary(nato_data)

    print(dictionary)

    word = input("Enter a word: ").upper()

    # nato_word = [
    #     nato_data[nato_data.letter == letter.upper()].code.values[0] for letter in word
    # ]
    nato_word = [dictionary[letter] for letter in word]

    print(nato_word)


def nato_dictionary(nato_data):
    return {row.letter: row.code for (_, row) in nato_data.iterrows()}


if __name__ == "__main__":
    get_shared_numbers()
    get_fahrenheit()
    nato()
