#!/usr/bin/env python3

from beverages import HotBeverage
import random


class CoffeeMachine:
    def __init__(self, served=0):
        self.served = served

    class EmptyCup(HotBeverage):
        def __init__(self):
            super().__init__(
                price=0.90,
                name="empty cup",
                descript="An empty cup?! Gimme my money back!"
            )

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.served = 0
        print("Machine repaired!")

    def serve(self, beverage_class):
        if self.served >= 10:
            raise self.BrokenMachineException()
        self.served += 1
        if random.choice([True, False]):
            return self.EmptyCup()
        else:
            return beverage_class


def main():
    from beverages import Coffee, Tea, Chocolate, Cappucinno
    machine = CoffeeMachine()
    beverages = [Coffee(), Tea(), Chocolate(), Cappucinno()]
    for i in range(12):
        try:
            drink = machine.serve(beverages[0])
            print(f"Served: {drink.name}")
        except machine.BrokenMachineException as e:
            print(f"Error: {e}")
            machine.repair()
            print("Trying again...")
            drink = machine.serve(beverages[1])
            print(f"Served: {drink.name}")


if __name__ == "__main__":
    main()
