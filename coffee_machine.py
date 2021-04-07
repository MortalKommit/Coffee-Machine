
class CoffeeMachine:
    def __init__(self, capacity, menu):
        self.capacity = {}
        contents = ("water", "milk", "coffee beans", "disposable cups", "money")
        for content, cap in zip(contents, capacity):
            self.capacity[content] = cap
        self.menu = menu

    def get_user_input(self):
        action = ''
        while action != 'exit':
            print("Write action (buy, fill, take, remaining, exit):")
            action = input()
            self.process_action(action)

    def process_action(self, action):
        if action == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            order = input()
            if order == 'back':
                return

            for key in self.capacity.keys():
                if key != "money":
                    if self.capacity[key] - self.menu[order][key] < 0:
                        print(f"Sorry, not enough {key}!")
                        break
            else:
                print("I have enough resources, making you a coffee!")

                # Add money
                self.capacity["money"] += self.menu[order]["money"]
                # Subtract the rest
                for key in self.capacity.keys():
                    if key != "money":
                        self.capacity[key] -= self.menu[order][key]

        elif action == "fill":
            print("Write how many ml of water do you want to add:")
            self.capacity["water"] += int(input())
            print("Write how many ml of milk do you want to add:")
            self.capacity["milk"] += int(input())
            print("Write how many grams of coffee beans do you want to add:")
            self.capacity["coffee beans"] += int(input())
            print("Write how many disposable cups do you want to add:")
            self.capacity["disposable cups"] += int(input())

        elif action == "take":
            print(f"I gave you ${self.capacity['money']}")
            self.capacity["money"] = 0

        elif action == "remaining":
            print("The coffee machine has:")
            for key, value in self.capacity.items():
                print(value, f"of {key}")


cafe_menu = {'1': {"water": 250, "milk": 0, "coffee beans": 16, "disposable cups": 1, "money": 4},
             '2': {"water": 350, "milk": 75, "coffee beans": 20, "disposable cups": 1, "money": 7},
             '3': {"water": 200, "milk": 100, "coffee beans": 12, "disposable cups": 1, "money": 6}
             }
caffe = CoffeeMachine((400,  540, 120,  9, 550), cafe_menu)
caffe.get_user_input()