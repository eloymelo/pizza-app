# Python Pizza Service (Command-Line)

This project is a command-line pizza ordering application built with Python. It was created as part of a project-driven learning path to master core Python programming concepts, including functions, classes, data persistence with JSON, and error handling.

This repository contains the first phase of the project: the command-line interface (CLI) application. The next phase will involve rebuilding this application as a full web app using the Django framework.

## Current Features

* Greets the user and displays a menu of available toppings.
* Loads and displays the user's previous order upon startup, if one exists.
* Allows the user to add multiple toppings to their pizza in an interactive loop.
* Validates user input against the list of available toppings.
* Calculates the total price based on a base price and the cost of selected toppings.
* Displays a clean summary of the final order.
* Saves the completed order to a JSON file (`pizza_order.json`) for future use.

## How to Run

1.  Clone this repository to your local machine.
2.  Ensure you have Python installed.
3.  Navigate to the project directory in your terminal.
4.  Run the application with the following command:

    ```sh
    python3 pizza_service.py
    ```

## Technologies Used

* Python
* JSON