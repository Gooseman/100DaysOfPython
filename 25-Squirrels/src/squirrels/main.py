import pandas


def read_raw_data():
    return pandas.read_csv(
        "2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260608.csv"
    )


def get_squirrel_counts():
    squirrel_data = read_raw_data()
    by_fur_colour = squirrel_data.groupby("Primary Fur Color")
    return (
        by_fur_colour.size()
        .reset_index(name="Count")
        # .set_index("Primary Fur Color")["Count"]
    )


def save_squirrel_counts(counts):
    # print(f"saving counts: {counts}")
    # print(f"counts type: {type(counts)}")
    counts.to_csv("squirrel_counts.csv")


if __name__ == "__main__":
    squirrel_counts = get_squirrel_counts()
    # print(squirrel_counts)
    # save_squirrel_counts(squirrel_counts.to_frame())
    save_squirrel_counts(squirrel_counts)
