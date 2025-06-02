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


    def skip_scene():
        renpy.show("blackscreen")
        renpy.show("confirm")
        renpy.text("test")


        
        # textbutton "I've seen this all before." xalign 0.5 yalign 0.445
        # textbutton "Continue" xalign 0.42 yalign 0.536
        # textbutton "Skip" xalign 0.58 yalign 0.536


