import sys

def my_var() -> tuple[dict[str, str], dict[str, str]]:
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    return states, capital_cities


def get_state(city: str) -> None:
    states, capital_cities = my_var()
    keys = [key for key, val in capital_cities.items() if val == city]
    if len(keys) == 0:
        print("Unknown capital city")
        return
    abbr_state = keys[0]
    keys = [key for key, val in states.items() if val == abbr_state]
    print(keys[0])

def process_input() -> None:
    args = sys.argv
    if len(args) == 2:
        get_state(args[1])

if __name__ == "__main__":
    process_input()
