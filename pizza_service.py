# A simple welcome message for this pizza app

print("Welcome to Python Pizza!")

available_toppings = ['pepperoni', 'mushrooms', 'extra cheese']

for topping in available_toppings:
    print(topping)

customer_toppings = []

prompt = "\nPlease enter a topping to add:"
prompt += "\n(Enter 'quit' when you are finished) "

total_price = 10

# Dictionary for the key and value

topping_price = {
    'pepperoni': 2.00,
    'mushrooms': 1.50,
    'extra cheese': 1.00
}

while True:

    chose_topping = input(prompt)

    if chose_topping in available_toppings:
        print(f"Adding {chose_topping} to your pizza!")
        customer_toppings.append(chose_topping)
        total_price += topping_price[chose_topping]

    elif chose_topping == 'quit':
        break

    else:
        print("Sorry, we don't have that topping.")

print("\nYour final pizza will have: ")
for topping in customer_toppings:
    print(f"- {topping}")

print(f"The total price is ${total_price:.2f}")