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


def process_input() -> None:
    states, capital_cities = my_var()
    args = sys.argv
    if len(args) == 2:
        expressions = sys.argv[1].split(',')
        low_states = {k.lower(): k for k in states.keys()}
        low_capitals = {v.lower(): v for v in capital_cities.values()}
        
        for expr in expressions:
            clean_name = " ".join(expr.split())
            if not clean_name:
                continue

            low_name = clean_name.lower()

            if low_name in low_states:
                state_original = low_states[low_name]
                abbr = states[state_original]
                cap_original = capital_cities[abbr]
                print(f"{cap_original} is the capital of {state_original}")

            elif low_name in low_capitals:
                cap_original = low_capitals[low_name]
                abbr = [k for k, v in capital_cities.items() if v == cap_original][0]
                state_original = [k for k, v in states.items() if v == abbr][0]
                print(f"{cap_original} is the capital of {state_original}")

            else:
                print(f"{clean_name} is neither a capital city nor a state")

if __name__ == "__main__":
    process_input()
