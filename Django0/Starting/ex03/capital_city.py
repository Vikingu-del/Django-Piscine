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

def get_city(state: str) -> None:
    states, capital_cities = my_var()
    abbr = states.get(state)
    if abbr:
        print(capital_cities[abbr])
    else:
        print("Unknown state")

def process_input() -> None:
    args = sys.argv
    if len(args) == 2:
        get_city(args[1])

if __name__ == "__main__":
    process_input()
