
def parse_request(text):
    if not isinstance(text, str):
        raise ValueError("Request must be a string")

    if text.count("->") != 1:
        raise ValueError("Request must be in FROM->TO format")

    start, end = text.split("->")

    try:
        start = int(start.strip())
        end = int(end.strip())
    except ValueError:
        raise ValueError("Floor numbers must be integers")

    return start, end


def total_travel(floors_csv):
    if not isinstance(floors_csv, str) or not floors_csv.strip():
        raise ValueError("Floor list must be a non-empty string")

    try:
        floors = [int(f.strip()) for f in floors_csv.split(",")]
    except ValueError:
        raise ValueError("All floors must be valid integers")

    return sum(
        abs(floors[i + 1] - floors[i])
        for i in range(len(floors) - 1)
    )


def load_percent(text):
    if not isinstance(text, str):
        raise ValueError("Load input must be a string")

    if text.count(" of ") != 1:
        raise ValueError("Use the format X of Y")

    load, capacity = text.split(" of ")

    try:
        load = int(load.strip())
        capacity = int(capacity.strip())
    except ValueError:
        raise ValueError("Load and capacity must be integers")

    if load < 0:
        raise ValueError("Load cannot be negative")

    if capacity <= 0:
        raise ValueError("Capacity must be greater than zero")

    return load * 100 // capacity


def main():
    print("==== Running parse_request ====")
    user_input = input("Enter a request as FROM->TO (e.g. 5->9): ")
    try:
        result = parse_request(user_input)
        print("From and To:", result)
    except ValueError as e:
        print("Invalid request:", e)

    print("\n==== Running total_travel ====")
    user_input = input("Enter floors visited as CSV (e.g. 1,5,3,9): ")
    try:
        result = total_travel(user_input)
        print("Floors Travelled:", result)
    except ValueError as e:
        print("Invalid floor list:", e)

    print("\n==== Running load_percent ====")
    user_input = input("Enter load as 'X of Y' (e.g. 450 of 630): ")
    try:
        result = load_percent(user_input)
        print("Load Percent:", result)
    except ValueError as e:
        print("Invalid load:", e)


if __name__ == "__main__":
    main()
