python early:

    def update_hourglass():
        
        if store.remainingtime <= 24:
            store.day = 3

        elif store.remainingtime <= 48:
            store.day = 2

        elif store.remainingtime <= 72:
            store.day = 1

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

    # instead of:
    # jump label
    # use:
    # time_travel_jump("label")
    def time_travel_jump(location):
        renpy.sound.play("audio/time travel/hourglass.mp3", channel="audio")
        renpy.sound.play("audio/time travel/whoosh.mp3", channel="sound", relative_volume=0.25)
        
        # black screen
        renpy.scene()
        renpy.show("blackscreen")
        renpy.with_statement(fade)

        # new scene
        renpy.scene()
        renpy.jump(location)
        renpy.with_statement(fade)

    def skip_scene(location):
        renpy.show("blackscreen2") 
        renpy.show("confirm")
        ui.text("I've seen this all before.", xalign=0.5, yalign=0.447)
        ui.textbutton("Continue", clicked=xcontinue, xalign=0.42, yalign=0.538)
        ui.textbutton("Skip", clicked=Jump(location), xalign=0.58, yalign=0.538)
        ui.interact()

    def xcontinue():
        renpy.restart_interaction()
        renpy.hide("blackscreen2")
        renpy.hide("confirm")
        ui.clear()
        renpy.end_interaction("cleared")

