from product_information_management import prompt_add_product, list_products, prompt_bought_product, prompt_delete_product
from storage import create_file

USER_CHOICE = """
Welcome to the shopping list app!
Enter:
- 'a' to add a new product
- 'l' to list all products
- 'b' to mark a product as bought
- 'd' to delete a product
- 'q' to quit
Your choice: """



def menu():
    """
    Show the main menu, get user choice and call the wanted function
    Stops only when user quits
    """
    create_file()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_product()
        elif user_input == 'l':
            list_products()
        elif user_input == 'b':
            prompt_bought_product()
        elif user_input == 'd':
            prompt_delete_product()

        user_input = input(USER_CHOICE)