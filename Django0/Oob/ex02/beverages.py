#!/usr/bin/env python3

class HotBeverage:
    def __init__(
            self,
            price=0.30,
            name="hot beverage",
            descript="Just some hot water in a cup."
    ):
        self.price = price
        self.name = name
        self.descript = descript

    def description(self) -> str:
        return self.descript

    def __str__(self) -> str:
        return f"""name : {self.name}
price : {self.price:.2f}
description : {self.description()}"""


class Coffee(HotBeverage):
    def __init__(self):
        super().__init__(
            price=0.40, 
            name="coffee",
            descript="A coffee, to stay awake."
        )

    def __str__(self):
        return f"Coffee:\n{super().__str__()}"


class Tea(HotBeverage):
    def __init__(self):
        super().__init__(
            name="tea",
            descript="Just some hot water in a cup."
        )

    def __str__(self):
        return f"Tea:\n{super().__str__()}"


class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__(
            price=0.50,
            name="chocolate",
            descript="Chocolate, sweet chocolate..."
        )

    def __str__(self):
        return f"Chocolate:\n{super().__str__()}"


class Cappucinno(HotBeverage):
    def __init__(self):
        super().__init__(
            price=0.45,
            name="cappuccino",
            descript="Un po' di Italia nella sua tazza!"
        )

    def __str__(self):
        return f"Cappucinno:\n{super().__str__()}"


def main():
    beverages = [Coffee(), Tea(), Chocolate(), Cappucinno()]
    for bev in beverages:
        print(bev, "\n")


if __name__ == '__main__':
    main()
