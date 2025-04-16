# DAY 2 --------------------------------------

$ day = 2

# SERAFINA 1 --------------------------------------

label S1:

    scene hallway
    with fade

    if sera_day1 == True:

        $ hide_menu()

        centered "{font=Marker Felt.ttf} {size=35} 1:05 pm {/size} \n {size=40} A Deserted Hallway {/size} {/font}"

        $ show_menu()

        show mira default at left
        with dissolve

        m "{i}( I know where to find Elliot this time around. But should I seek him out? I’m not sure I’d learn any new information. ){/i}"

        show mira sighing

        m "{i}( Plus, I'd be interrogated all over again. ){/i}"

        # SFX: footsteps down a hallway

        m "{i}I’ll go look for one of the others—{/i}"

    else:

        $ hide_menu()

        centered "{font=Marker Felt.ttf} {size=35} 9:30 am {/size} \n {size=40} Before School {/size} {/font}"

        $ show_menu()

        # placeholder dialogue 
        
        show mira default at left
        with dissolve

        m "{i}( Should I hunt down Vivienne or Elliot again? ){/i}"

        m "{i}( I'm supposed to see Finn after school... ){/i}"

        m "{i}( And there's still two more suspects I haven't met yet. ){/i}"

        m "..."

    show mira surprised at farleft:
        movefarleft

    show serafina behind mira:
        kabedon

    m "!!" with hpunch

    m "{i}The girl leans in, pushing me back against the wall. Light from the window dances across the gloss smeared on her lips.{/i}"

    x "Play along."

    m "What??"

    x "{i}Play along.{/i}"

    m "{i}She twirls a strand of my hair around her finger in a lazy movement.{/i}"

    m "{i}( What. Is happening. ){/i}"

    hide mira
    hide serafina
    with dissolve

    menu: 

        "Flirt back":
            jump flirtback

        "{s}Stare at her{/s}":
            jump stare

        "{s}Push her off{/s}":
            jump push

label flirtback:

    show mira smile at farleft

    show serafina behind mira:
        xalign 0.35

    m "Missed me already?"

    x "I can’t help it; it’s your fault for being so cute."

    show mira default

    m "{i}It takes an immense effort for me not to vomit on the spot.{/i}"

    m "Thanks, you have...dark eyes. And I’m drowning in them. I’m almost dead, actually."

    x "God, you’re so bad at this."

    m "{i}I look away briefly to the other students nearby. Most of them are busy, but a few cast bored glances our way.{/i}"

    m "{i}I catch the eyes of someone with mussed blonde hair that they’d evidently dyed themselves and turn my gaze back.{/i}"
    
    m "I don’t do kissing, by the way."
    
    x "What? Of course not, I don’t even know you."
    
    m "Oh, can we finally stop pretending now?"

    jump continue10


label continue10:

    show mira default at farleft

    show serafina behind mira:
        xalign 0.35
        movecenter

    m "{i}The girl takes a step back and dusts off her sleeve.{/i}"
    
    s "I’m Serafina, hi. Sorry for ambushing you out of nowhere."
    
    m ".............So, what was that?"
    
    s "Ugh, I saw my ex in the hallway."
    
    m "..."
    
    show mira sighing

    m "Are you serious."
    
    s "I panicked, okay!"
    
    m "You couldn’t have just ignored them instead of pinning me against the wall?"
    
    s "Yeah, but then Aster would think ‘look at her, pretending she doesn't see me’ with that stupid smug expression on their face."
    
    s "It's like they don’t know how badly it makes other people want to punch them."

    show mira default
    
    m "!!"
    
    m "{i}( I didn’t realize my last two suspects knew each other. ){/i}"
    
    m "{i}( Maybe this will be easier than I thought. ){/i}"

    hide mira
    hide serafina
    with dissolve

    menu:

        "{s}Ask her more about Aster{/s}":
            jump asterinfo

        "Offer to help her make Aster jealous":
            jump fakedate

        "Suggest a way to get back at Aster":
            jump revenge

label asterinfo:

    "more text"

label fakedate:

    show mira default at farleft

    show serafina at center

    m "So you want to make your ex jealous?"
    
    s "I don’t want to make them jealous! I just…want Aster to see I don’t need them anymore."
    
    m "Mhm."
    
    m "Are you in the market for a fake girlfriend?"
    
    s "...What??"
    
    m "What it says on the label. I’ll pretend to date you, and you can pretend you’re in love with me now."
    
    m "Still no kissing though. Don’t take it personally."
    
    s "..."
    
    s "Why are you offering to help me? What’s in it for you?"

    jump continue11

label revenge:

    $ aster_revenge = True

    show mira default at farleft

    show serafina at center

    m "That’s so annoying."
    
    s "I know, right??"

    s "You don’t know how many times I had to drag them out of social situations right before someone grabbed them by the shirt."
    
    s "Looking back, I can’t believe we used to laugh about it together."
    
    m "What? You’re the one who had to bail them out every time."
    
    s "Exactly, and they never even thanked me!"
    
    m "So, do you want to get back at your ex?"
    
    s "...What are you suggesting?"

    show mira smile
    
    m "Revenge."
    
    s "..."
    
    s "Why are you offering to help me? You don’t even know Aster."

    jump continue11


label continue11:

    show mira default

    m "Maybe I think you’re cute."

    s "That was my line; it won't work on me."
    
    m "Fine, I’m bored and I like messing with people."

    s "......Okay, count me in."

    if aster_revenge == True:

        show mira:
            moveoffleft
            
        show serafina behind mira:
            moveoffleft

        s "Tell me more about your idea."

        "{color=#56768f}{i}( Pretend the notebook has been updated. ){/i}{/color}"

        jump A1

    else:

        if sera_day1 == True:

            s "Are you free tomorrow night?"

        else: 

            s "Are you free  tonight?"
    
        m "Sure. What are we doing?"

        show mira:
            moveoffleft
            
        show serafina behind mira:
            moveoffleft
    
        s "Revenge."

        "{color=#56768f}{i}( Pretend the notebook has been updated. ){/i}{/color}"

        jump A1

label A1:

    scene classroom
    with fade

    if sera_day1 == True:

        $ hide_menu()

        centered "{font=Marker Felt.ttf} {size=35} 5:00 pm {/size} \n {size=40} After School {/size} {/font}"

        $ show_menu()

    else:

        $ hide_menu()

        centered "{font=Marker Felt.ttf} {size=35} 1:00 pm {/size} \n {size=40} Chemistry Lab {/size} {/font}"

        $ show_menu()

    "that's all we have for now, thanks for playing!!"



