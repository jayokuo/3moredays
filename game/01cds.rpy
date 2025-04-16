python early:

    def hide_menu():
        store.notebook = False
        store.quick_menu = False
        store.hourglass = False
        renpy.show("locationbox")

    def show_menu():
        store.notebook = True
        store.quick_menu = True
        store.hourglass = True
        renpy.hide("locationbox")

    def hide_menu1():
        store.notebook = False
        store.quick_menu = False
        store.hourglass = False

    def show_menu1():
        store.quick_menu = True
        renpy.hide("locationbox")