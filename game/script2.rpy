# DAY 2 --------------------------------------

$ day = 2

# SERAFINA 1 --------------------------------------

label S1:

    $ s1_done += 1

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

        $ remainingtime = 39

        $ hide_menu()

        centered "{font=Marker Felt.ttf} {size=35} 9:30 am {/size} \n {size=40} Before School {/size} {/font}"

        $ show_menu()

        
        show mira default at left
        with dissolve

        m "{i}As it turns out, I can sleep if I really want to.{/i}"

        m "{i}But my dreams are filled with scenes of my final days, over and over again. The cliffside that crumbled underneath my shoes is burned into my memory.{/i}"

        m "{i}I didn’t fall on purpose, you know. I just realized afterwards that I didn’t want to be alive again.{/i}"

        m "{i}I haven’t really narrowed down my list of suspects…and there’s still two others I haven't met.{/i}"

        m "..."


    show mira surprised at farleft:
        movefarleft

    show serafina behind mira:
        kabedon

    m "!!" with hpunch

    m "{i}The girl leans in, pushing me back against the wall. Light from the window dances across the gloss smeared on her lips.{/i}"

    x "Play along."

    m "What??"

    x "Just for a few minutes."

    m "{i}She twirls a strand of my hair around her finger in a lazy movement.{/i}"

    m "{i}( What. Is happening. ){/i}"

    hide mira
    hide serafina
    with dissolve

    menu: 

        "Do as she says":
            jump obey
            $ obey = True

        "Push her off":
            jump push
            $ push = True


label obey:

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

    show serafina behind mira:
        xalign 0.35
        movecenter

    m "{i}The girl takes a step back and dusts off her sleeve.{/i}"
    
    s "I’m Serafina, hi. Sorry for ambushing you out of nowhere."
    
    m "Mira. So.............what was that?"
    
    s "Ugh, I saw my ex in the hallway."

    jump continue10


label push:

    show mira surprised at farleft

    show serafina behind mira:
        xalign 0.35, movecenter
    
    m "Do I know you??" with vpunch
    
    s "What? No, I said to pretend—"
    
    s "Never mind. Sorry if I made you uncomfortable."

    show mira default
    
    m "I’m more offended you didn’t buy me dinner first."
    
    s "I wasn’t asking you out, I said to pretend!"
    
    m "{i}I look away briefly to the other students nearby. Most of them are busy, but a few cast curious glances our way.{/i}"

    m "{i}I catch the eyes of someone with mussed blonde hair that they’d evidently dyed themselves and turn my gaze back.{/i}"
    
    m "Can I get a name, then?"
    
    m "{i}The girl straightens her shirt, tugging out the wrinkles I’d left when I pushed her away.{/i}"
    
    s "I’m Serafina, hi. Sorry again for ambushing you."
    
    m "What was that about?"
    
    s "............Ugh, I saw my ex in the hallway."

    jump continue10


label continue10:

    show mira default at farleft

    show serafina at center
    
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

        "Ask her more about Aster":
            $ annoysera = True
            jump asterinfo

        "Offer to help her make Aster jealous":
            jump fakedate

        "Suggest a way to get back at Aster":
            jump revenge


label asterinfo:

    show mira default at farleft

    show serafina at center

    m "Aster’s your ex?"
    
    s "....Do you know them?"
    
    m "I was looking for them at the masquerade, but they didn’t turn up the entire night."
    
    s "Of course they would choose the one event I skipped on purpose to not even show up…!"
    
    s "I should’ve attended after all."
    
    m "Maybe they were also hoping to avoid you."
    
    s "No, Aster doesn’t give a shit."
    
    s "They wave to me whenever we run into each other and then walk off like they didn’t just ruin my entire day."
    
    s "......Are you interested in them? You should reconsider. Dating Aster is a nightmare."
    
    m "Sounds like it. I just need to ask them something. Do you know where they are?"
    
    s "Nope."
    
    m "..."
    
    m "Do you know which classes they have, or...."
    
    s "Look, I’m running late to my lecture. I’ve got better things to do than stand here and answer questions about my ex."
    
    s "See you around, Mira. I won’t pin you against the wall next time."

    show mira surprised

    hide serafina
    with dissolve
    
    m "{i}She’s gone before I can say anything else.{/i}"

    show mira sighing

    $ sphoto = True
    $ supdate = 1
    $ newinfoupdate = True
    
    m "{i}( Fuck. I didn't learn anything about her or Aster. ){/i]}"

    hide mira
    with dissolve

    jump continue12


label fakedate:

    show mira default at farleft

    show serafina at center

    m "So you want to make your ex jealous?"
    
    s "I don’t want to make them jealous! I just...want Aster to see I don’t need them anymore."
    
    m "Mhm."
    
    m "Are you in the market for a fake girlfriend?"
    
    s "...What??"
    
    m "What it says on the label. I’ll pretend to date you, and you can pretend you’re in love with me now."

    if obey == True:
    
        m "Still no kissing though. Don’t take it personally."

    else:

        m "I don't do kissing though. Don’t take it personally."
    
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

    if obey == True:

        s "That was my line; it won't work on me."

    else: 

        s "That was supposed to be my line; it won't work on me."
    
    m "Fine, I’m bored and I like messing with people."

    s "......Okay, count me in."

    if aster_revenge == True:

        show mira:
            moveoffleft
            
        show serafina behind mira:
            moveoffleft

        $ sphoto = True
        $ supdate = 1
        $ newinfoupdate = True

        s "Tell me more about your idea."

        $ sphoto = True
        $ supdate = 1
        $ newinfoupdate = True


        jump continue11

    else:

        if sera_day1 == True:

            s "Are you free tomorrow night?"

        else: 

            s "Are you free  tonight?"
    
        m "Sure. What are we up to?"

        show mira:
            moveoffleft
            
        show serafina behind mira:
            moveoffleft

        $ sphoto = True
        $ supdate = 1
        $ newinfoupdate = True
    
        s "Revenge."

        jump continue12


label continue12:

    $ remainingtime -= 4

    menu:

        "Look for Aster":
            jump A1

        "Time travel":

            jump timetravel4


label timetravel4:

    if sera_day1 == True:    

        menu:

            "Find Vivienne (-2 hrs)":
                $ time_travel_jump("V1")

            "Meet Elliot (-1 hr)":
                $ time_travel_jump("E1")

            "Meet Finn (-1 hr)":
                $ time_travel_jump("F1")

            "Meet Serafina (-1 hr)":
                $ time_travel_jump("S1")

            "Never mind":
                jump continue12

    else: 

        menu:

            "Find Vivienne (-22 hrs)":
                $ time_travel_jump("V1")

            "Meet Elliot (-21 hr)":
                $ time_travel_jump("E1")

            "Meet Finn (-17 hr)":
                $ time_travel_jump("F1")

            "Meet Serafina (-1 hr)":
                $ time_travel_jump("S1")

            "Never mind":
                jump continue12

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


    show mira sighing at left
    with dissolve

    m "{i}( …………………Ugh. )"

    m "{i}( I can’t believe I was ambushed in the hallway by the professor and dragged into lab. ){/i}"

    m "{i}( In my defense, I forgot I had class in this area or I would’ve avoided it. ){/i}"

    show aster at right
    with dissolve

    x "Can I sit here? My lab partner’s gone today."

    show mira default

    m "{i}I look up. It’s the student who caught my eye in the hallway earlier.{/i}"

    m "I have no idea what experiment we’re even doing."

    x "Don’t worry, I got you."

    m "{i}They take the seat across from me and look down at the worksheet.Their hands move across the table confidently, measuring out fluids and powders.{/i}"

    x "So, are you Sera’s new girlfriend?"

    m "I’m trying to focus on the experiment."

    x "No you’re not, I’m doing all the work."

    show mira sighing

    m "{i}I sigh. They’re not exactly wrong on that.{/i}"

    show mira default

    a "I’m Aster, by the way. Nice to meet you."

    m "Mira."

    a "So Mira, what’s your relationship with Sera?"

    hide mira
    hide aster 
    with dissolve

    menu:

        "Why do you care?":
            jump care

        "We're friends":
            jump friends

        "We've been dating for a few days":
            jump dating

        "She's the love of my life":
            jump loml


label care:

    show mira default at left

    show aster at right
    
    m "Why do you care?"

    jump continue13


label friends:

    show mira default at left

    show aster at right

    m "We’re just friends. She’s not my type."

    a "Is that so? I see."

    if annoysera == True:

        m "I’m not sure she even likes me, to be honest."

        a "Why, what’d you do?"

        m "Just said the wrong thing at first and made her annoyed."

        a "Yeah, it’s easy to do that."

        a "You’ll learn how to do it less frequently over time."

        m "Anyways, why do you care who she dates now?"

    else: 

        m "Why are you asking in the first place? It’s none of your business who she dates now."

    jump continue13


label dating:

    show mira default at left

    show aster at right

    m "We’ve been dating for a few days now."

    a "Is that so? I see."

    m "Why do you care? It’s none of your business who she dates now."

    jump continue13


label loml:

    show mira default at left

    show aster at right

    m "She’s the love of my life."

    a "......You don’t sound very convinced about that."

    m "This is how I always sound."

    a "Right."

    m "Why are you asking in the first place? It’s none of your business who she dates now."

    jump continue13


label continue13:

    a "Just looking out for a friend."

    m "She didn’t make it sound like you two were friends."

    a "...No, but I’d like to be. "

    a "Did she tell you how we broke up?"

    m "No."

    a "( Insert backstory here )"

    "that's all we have for now, thanks for playing!!"



