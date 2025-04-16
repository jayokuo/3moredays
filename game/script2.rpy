# DAY 2 --------------------------------------

$ day = 2

# SERAFINA 1 --------------------------------------

label S1:

    scene hallway
    with fade

    if v1_done > 1:

        $ hide_menu()

        centered "{font=Marker Felt.ttf} {size=35} 1:05 am {/size} \n {size=40} A Deserted Hallway {/size} {/font}"

        $ show_menu()

        show mira default at left
        with dissolve

        m "{i}( I know where to find Elliot this time around. ){/i}"

        m "{i}( But should I seek him out? I’m not sure I’ll learn any new information. ){/i}"

        show mira sighing

        m "{i}( Plus, I'll be interrogated all over again. ){/i}"

        show mira default

        # SFX: footsteps down a hallway

        m "{i}I’ll go look for one of the others—{/i}"

    else:

        $ hide_menu()

        centered "{font=Marker Felt.ttf} {size=35} 9:30 am {/size} \n {size=40} Before School {/size} {/font}"

        $ show_menu()

    show mira surprised

    show serafina

    m "!!" with hpunch

    m "{i}The girl leans in, pushing me back against the wall. Light from the window dances across the gloss smeared on her lips.{/i}"

    s "Play along."

    m "What??"

    s "Play {i}along.{/i}"

    m "{i}She twirls a strand of my hair around her finger in a lazy movement.{/i}"

    m "{i}I blink rapidly. She’s still there, her long eyelashes inches from my face.{/i}"

    m "{i}( What. Is happening. ){/i}"
