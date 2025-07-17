# Pizzeria - Command-Line App

This is the command-line version of the Pizzeria project, an application built with Python to practice core programming concepts. It allows a user to order a pizza with multiple toppings and calculates the final price.

This repository contains the first phase of the project: the command-line interface (CLI) application. The next phase will involve rebuilding this application as a full web app using the Django framework.

## Current Features

* Displays a menu of available toppings.
* Loads and displays the user's previous order upon startup, if one exists.
* Allows the user to add multiple toppings to their pizza in an interactive loop.
* Validates user input against the list of available toppings.
* Calculates the total price based on a base price and the cost of selected toppings.
* Displays a clean summary of the final order.
* Saves the completed order to a JSON file for future use.

## How to Run

1.  Clone this repository to your local machine.
2.  Ensure you have Python installed.
3.  Navigate to the project directory in your terminal.
4.  Run the application with the following command:

    ```sh
    python3 pizzeria.py
    ```

## Technologies Used

* Python
* JSON