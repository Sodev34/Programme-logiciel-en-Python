from controllers.menu import MenuController
from views.menu import MenuViews


def main():
    MenuViews().title()
    MenuController().menu_start()


if __name__ == "__main__":
    main()
