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

def display_menu():

    print("Welcome to Python Pizza!")
    print("\nHere is our menu:")

    for topping in AVAILABLE_TOPPINGS:
        print(topping)

def main():
    
    display_menu()
    the_finished_order = take_order()
    display_summary(the_finished_order)

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