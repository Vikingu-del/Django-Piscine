#!/usr/bin/env python3

class Intern:
    def __init__(self, name: str = "My name? I'm nobody, an intern, I have no name."):
            self.name = name
    def __str__(self) -> str:
        return self.name
    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."
    def work(self):
        raise Exception("I'm just an intern, I can't do that...")
    def make_coffee(self) -> Coffee:
        return self.Coffee()
    
    
def main():
    intern1 = Intern("Mark")
    intern2 = Intern()
    print("------- How the __str__ works for both of them----")
    print(intern1)
    print(intern2)
    print("------- Printing the name for both of them--------")
    print(intern1.name)
    print(intern2.name)
    print("------- Mark Making a coffe-----------------------")
    result = intern1.make_coffee()
    print(type(result))
    print(result)
    print("------- Intern2 working---------------------------")
    try:
        intern2.work()
    except Exception as e:
        print(e)

if __name__=='__main__':
     main()