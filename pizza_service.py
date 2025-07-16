AVAILABLE_TOPPINGS = ['pepperoni', 'mushrooms', 'extra cheese']

TOPPING_PRICES = {
    'pepperoni': 2.00,
    'mushrooms': 1.50,
    'extra cheese': 1.00
}    

def display_menu():

    print("Welcome to Python Pizza!")
    print("\nHere is our menu:")

    for topping in AVAILABLE_TOPPINGS:
        print(topping)

def main():
    
    display_menu()
    ordered_toppings, final_price = take_order()

    display_summary(ordered_toppings, final_price)

def take_order():

    customer_toppings = []

    prompt = "\nPlease enter a topping to add:"
    prompt += "\n(Enter 'quit' when you are finished) "

    total_price = 10

    while True:

        chose_topping = input(prompt)

        if chose_topping in AVAILABLE_TOPPINGS:
            print(f"Adding {chose_topping} to your pizza!")
            customer_toppings.append(chose_topping)
            total_price += TOPPING_PRICES[chose_topping]

        elif chose_topping == 'quit':
            break

        else:
            print("Sorry, we don't have that topping.")

    return customer_toppings, total_price

def display_summary(toppings, price):
    
    print("\nYour final pizza will have: ")
    for topping in toppings:
        print(f"- {topping}")

    print(f"The total price is ${price:.2f}")

if __name__ == "__main__":
    main()