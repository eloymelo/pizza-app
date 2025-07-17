import json

AVAILABLE_TOPPINGS = ['pepperoni', 'mushrooms', 'extra cheese']

TOPPING_PRICES = {
    'pepperoni': 2.00,
    'mushrooms': 1.50,
    'extra cheese': 1.00
}    

BASE_PRICE = 10.00

class Pizza():

    def __init__(self):
        self.toppings = []
        self.price = BASE_PRICE

    def to_dict(self):
        order_dict = {
            'toppings': self.toppings,
            'price': self.price
        }

        return order_dict

def display_menu():

    print("Welcome to Python Pizza!")
    print("\nHere is our menu:")

    for topping in AVAILABLE_TOPPINGS:
        print(topping)

def main():

    filename = 'pizza_order.json'

    try:
        with open(filename) as f:
            last_order = json.load(f)

    except FileNotFoundError:
        pass
    else:
        print("--- Welcome back! Here was your last order: ---")
        toppings = last_order['toppings']
        print("Toppings:")
        for topping in toppings:
            print(f"- {topping}")

        price = last_order['price']
        print(f"The total price was: ${price:.2f}")
    
    display_menu()
    the_finished_order = take_order()
    display_summary(the_finished_order)

    with open(filename, 'w') as f:
        order_details = the_finished_order.to_dict()

        json.dump(order_details, f)

    print("\nYour order has been saved!")


def take_order():

    current_order = Pizza()

    prompt = "\nPlease enter a topping to add:"
    prompt += "\n(Enter 'quit' when you are finished) "

    while True:

        chose_topping = input(prompt)

        if chose_topping in AVAILABLE_TOPPINGS:
            print(f"Adding {chose_topping} to your pizza!")
            current_order.toppings.append(chose_topping)
            current_order.price += TOPPING_PRICES[chose_topping]

        elif chose_topping == 'quit':
            break

        else:
            print("Sorry, we don't have that topping.")

    return current_order

def display_summary(pizza_order):
    
    print("\nYour final pizza will have:")
    for topping in pizza_order.toppings:
        print(f"- {topping}")

    print(f"The total price is ${pizza_order.price:.2f}")

if __name__ == "__main__":
    main()