# DAY 3 --------------------------------------

# VIVIENNE 2 --------------------------------------
    
label V2:

    $ day = 3

    $ v2_done += 1

    scene courtyard
    with fade

    $ hide_menu()

    centered "{font=Marker Felt.ttf} {size=35} 7:00 am {/size} \n {size=40} Before School {/size} {/font}"

    $ show_menu()

    "Scene WIP"

    jump continue_three


label continue_three:

    $ remainingtime -= 1

    if sera_day1 == True:

        menu:

            "Meet with Finn after school":
                $ remainingtime -=3
                jump F2

            "Time travel":
                jump timetravel8

    else:

        menu:

            "Go talk to Elliot":
                $ remainingtime -= 0
                jump E2

            "Time travel":
                jump timetravel8


label timetravel8:

    menu:

        "Meet Vivienne (-26 hrs)":
            $ time_travel_jump("V1")

        "Meet Finn (-24 hrs)":
            $ time_travel_jump("F1")

        "Meet Serafina (-23 hrs)":
            $ time_travel_jump("S1")

        "Meet Aster (-21 hrs)":
            $ time_travel_jump("A1")

        "Meet Elliot (-19 hrs)":
            $ time_travel_jump("E1")

        "Do Elliot's tests (-5 hours)":
            $ time_travel_jump("E2")

        "Talk to Vivienne again (-1 hr)":
            $ time_travel_jump("V2")

        "Never mind":
            jump continue_three


# ELLIOT 2 --------------------------------------

label E2:

    $ e2_done += 1

    scene courtyard
    with fade

    $ hide_menu()

    centered "{font=Marker Felt.ttf} {size=35} 8:00 am {/size} \n {size=40} Before School {/size} {/font}"

    $ show_menu()

    show mira default at left

    e "Over here!"

    m "{i}I turn towards the voice.{/i}"

    m "{i}Elliot is waving at me from a distance, sheltered under a pair of tall trees that partially hide him from the students in the courtyard.{/i}"

    m "{i}As I walk over to him, I notice he’s set up a blanket on the grass with an assortment of objects scattered on top.{/i}"

    show elliot grin at right
    with dissolve

    e "I didn’t actually think you’d show up."

    m "I told you I would."

    show elliot default

    e "But you know, I figured it was mostly to get me to stop pestering you."

    m "I can leave again, if you’d like."

    show elliot at center:
        movecenter

    e "Absolutely not. Come here."

    show mira at center:
        movecenter

    show elliot at right:
        moveright

    m "{i}I let him take my wrist and drag me towards the blanket.{/i}"

    show mira surprised

    m "What’s all this?"

    show elliot grin

    e "Materials to help me test a couple of hypotheses."

    show mira default

    show elliot default

    e "We already know you exhibit a few signs that set you apart from living people."

    e "These include an inability to feel pain, a temperature drop in the air around you, and a lack of reflection in your eyes."

    e "The objects here will help us figure out how far the differences go."

    e "Go ahead, pick one."

    m "Any one?"

    e "Yep."

    m "What are you going to do with them?"

    e "You’ll find out when you pick one."

    e "Come on, I’ll get yelled at if I’m late to my first class."

    jump experiment

label experiment:
    $ choiceLeftToggle = True

    hide mira
    hide elliot
    with dissolve

    show experiment_screen

    menu:

            "Choose the wand":
                hide experiment_screen
                $ choiceLeftToggle = False
                jump wand

            "Choose the camera":
                hide experiment_screen
                $ choiceLeftToggle = False
                jump camera

            "Choose the switchblade":
                hide experiment_screen
                $ choiceLeftToggle = False
                jump knife

            "Choose the book":
                hide experiment_screen
                $ choiceLeftToggle = False
                jump book

label wand:
    
    $ test += 1
    
    show mira default at left

    show elliot grin at right

    e "Ooh, this one’s going to be fun."

    show elliot default

    e "Have you ever tried to do magick before?"

    m "What? Of course not."

    e "Usually, it’d take several weeks for you to master your first spell."

    e "However, it’s rumored that undead beings have a higher capacity for magick, likely due to their existence being rooted in a magickal process."

    e "Okay, repeat after me."

    show mira surprised

    m "What’s this going to do??"

    e "It’s just a simple light summoning spell, relax. It might not even work."

    show mira default

    e "{i}Ai lu jalai budi holi.{/i}"

    m "{i}Ai lu…jalai…budi holi?{/i}"

    ## get weezered lmao

    e "…"

    m "…"

    e "…"

    m "…"

    show elliot grin

    e "Oh my god."

    e "Hahahaahahaaa."

    m "{i}He doubles over, snorting from laughter.{/i}"

    show mira sighing

    m "What? You’re the one that said it’s a difficult process!"

    e "I can’t believe you actually fell for that."

    show mira default

    m "What?"

    e "Mira, that’s not how magick works."

    e "Wands don’t exist outside of fairytales. This is a really nice stick I found behind the senior dorms."

    m "………"

    show mira sighing

    m "Are you serious."

    m "{i}( Despite my tone, it’s hard to be annoyed in the face of Elliot’s massive grin. ){/i}"

    show mira default

    if test == 3:

        jump continue18

    else:

        show elliot smile

        e "Okay okay, I’m sorry. Pick another one."

        e "The others are all real tests, I promise."

        jump experiment


label camera:

    $ test += 1
    
    show mira default at left

    show elliot default at right

    e "So I think I turn this knob here, then press the button…"

    e "Smile!"

    show elliot grin at center:
        movecenter

    show mira surprised

    m "Wait, what—"

    # sfx: flash

    m "!!"

    show elliot default

    e "Okay, now we just wait for the photo to develop. It should only take a few minutes."

    show mira default

    m "What was that for?"

    m "{i}( I can’t remember the last time anyone took my picture. ){/i}"

    e "Magickal elements are often hard to capture on camera, since the technology was developed without taking magick into consideration."

    show elliot curious

    e "Oh, it’s done. Let me see, let me see."

    e "Woaaah."

    show elliot default

    e "Mira, look at this."

    m "{i}I stare at the photo he holds up in front of me.{/i}"

    show mira surprised

    m "I look…indistinct."

    m "{i}It’s the only way I can describe it. The photo appears smudged and blurry where my body is, obscuring my features and the details of my uniform.{/i}"

    m "{i}I’m hit with the sudden certainty that if anyone had taken my photo while I was alive, they would have seen the same thing.{/i}"

    e "Here, take it."

    show mira default

    m "{i}He thrusts out the photo at me.{/i}"

    m "What?"

    show elliot grin

    e "As a keepsake. And a thank-you for doing this with me."

    m "Oh. You don’t want to keep it as evidence?"

    show elliot smile

    e "Usually I would, but you can have it this time."

    show mira smile

    m "{i}Quietly, I tuck the photo into my notebook.{/i}"

    if test == 3:

        jump continue18

    else:

        show elliot default

        e "Okay, let’s move on."

        jump experiment


label knife:

    $ test += 1

    show mira default at left

    show elliot default at right

    m "Who let you have a knife?"

    m "You shouldn't be trusted with sharp objects."

    show elliot frown

    e "I’m insulted."

    e "But here, you can hold onto it then."

    show elliot at center:
        movecenter

    m "…?"

    m "{i}He reaches out to me, the switchblade in his hand.{/i}"

    show mira surprised

    show elliot at center:
        movecloseleft2

    m "!!" with vpunch

    m "{i}In one smooth motion, Elliot has flicked open the knife and slashed it across my palm.{/i}"

    m "What was that for??"

    m "Just because I can’t feel pain—"

    show elliot default at center:
        movecenter

    e "Look. No blood."

    show mira default

    m "I stare down at the wound on my hand. Despite the torn skin, there’s no sign of bleeding at all."

    e "Do you have a pulse?"

    m "….I don’t know."

    m "{i}Hesitantly, I press my thumb against the inside of my wrist as if the gesture might damage my body.{/i}"

    m "……"

    show mira surprised

    m "There’s nothing."

    e "Hmm, makes sense. You’re not truly alive, after all."

    e "Does this mean necromancy only does the bare minimum to keep your body from decaying?"

    m "{i}I’m not listening to him. For the first time since I was resurrected, it fully registers that I will never be alive again.{/i}"

    m "{i}Did I waste it…..?{/i}"

    show elliot at center:
        movecloseleft3

    e "Hey."

    show mira default

    m "{i}I look up. Elliot has pressed my hand to the inside of his wrist.{/i}"

    e "{i}Underneath his freckled skin, I can feel the quiet, slightly erratic pulse of his heartbeat.{/i}"

    show elliot smile
    
    e "You can pretend it’s yours."

    m "…"

    m "{i}I look away, momentarily at a loss for words.{/i}"

    m "{i}In the end, I let myself stand still for a few moments, memorizing the rhythm of his heartbeat before pulling away.{/i}"

    if test == 3:

        jump continue_one

    else:

        m "What next?"

        show elliot default

        e "It’s up to you."

        jump experiment


label book:

    $ test += 1

    show mira default at left

    show elliot default at right

    e "Oh—that’s not part of the experiment."

    m "You’re the one who put it on the blanket."

    m "{i}I flip through a few pages. It’s old and heavy, likely something checked out of the Seacliff library.{/i}"

    m "{i}In a few places, someone—presumably Elliot—has scribbled notes in the margins.{/i}"

    m "“—”"

    e "It’s a book on necromancy."

    e "I found it in the library a few weeks ago. It’s pretty comprehensive, but the writing style’s kinda outdated."

    e "Go ahead and look through it if you want."

    m "{i}( Maybe there’s something in here that can help me. ){/i}"

    m "{i}( Section 2…Spells and Counterspells…page 249… ){/i}"

    show mira surprised

    m "{i}( Huh? ){/i}"

    show mira default

    m "Elliot."

    show elliot curious

    e "Hm? Did you find something interesting?"

    m "Was this page missing when you checked out the book?"

    show elliot default at center:
        movecenter

    e "Let me see."

    m "{i}He takes the book from me and runs his finger down the jagged edge of a page that’s been clearly ripped out.{/i}"

    e "I don’t think so. No, I wrote notes on the previous page here, see?"

    e "This was the first chapter I read when I checked out the book. I would’ve definitely noticed a missing page."

    m "{i}( That means either someone stole it, or he purposefully ripped it out to prevent me from reading it. ){/i}"

    m "{i}( Chapter 14: Common Necromancy Spells…){/i}"

    show mira surprised

    m "Elliot, did you leave the book unattended around other people at any point?"

    e "Yeah, I take the current book I’m reading everywhere I go."

    e "It could’ve been left on a desk while I went to the bathroom, or forgotten in a classroom for a few hours."

    e "Plus, I live with two roommates."

    show mira sighing

    m "{i}( …That’s completely unhelpful. ){/i}"

    e "One of them probably knocked it off my desk on accident and ripped the page."

    e "I don’t know why he couldn’t have just put it back in the book though."

    show mira default

    m "{i}( I'm sure it wasn't an accident. Whoever has the page right now used the spell on it to resurrect me. ){/i}"

    show elliot frown

    e "It’s not a big deal since I took notes on the chapter already, but I don't want to rack up more library fines."

    e "Whatever. I’ll ask them about it when I go back my dorm."

    if test == 3:

        jump continue_one

    else: 

        show elliot default

        e "Should we move on?"

        jump experiment


label continue_one:

    # sfx: bell

    show elliot default

    e "Oh—that's the 15-minute bell. I guess we’re out of time."

    show elliot grin

    e "Thanks for hanging out with me."

    m "I don’t know if this qualified as hanging out."

    m "Do you experiment on all your friends?"

    e "Only the undead ones."

    show elliot default

    e "How did you get resurrected, by the way?"

    m "Long story. I’ll tell you another time."

    m "{i}I watch as he begins to cram all the test objects into his backpack and roll up the blanket.{/i}"

    e "Okay, but I want all the details."

    show elliot grin

    e "See you later!"

    hide elliot 
    with dissolve

    m "{i}All this time, Elliot hasn’t tried to use my secret against me once.{/i}"

    m "{i}Is he waiting until the three-day deadline, or is he innocent after all?{/i}"

    m "{i}I realize I don’t really care.{/i}"

    m "{i}…….In the end, I just wanted someone to talk to.{/i}"

    hide mira
    with dissolve

    jump continue_two


label continue_two:
    
    $ remainingtime -=1

    if sera_day1 == True:
        
        menu:

            "Look for Vivienne at lunch":
                $ remainingtime -=3
                jump V2

            "Time travel":
                jump timetravel9

    else:

        jump notastorm


label timetravel9:

    if sera_day1 == True:    


        menu:

            "Meet Vivienne (-22 hrs)":
                $ time_travel_jump("V1")

            "Meet Finn (-20 hrs)":
                $ time_travel_jump("F1")

            "Meet Serafina (-19 hrs)":
                $ time_travel_jump("S1")

            "Meet Aster (-17 hrs)":
                $ time_travel_jump("A1")

            "Meet Elliot (-15 hrs)":
                $ time_travel_jump("E1")

            "Do Elliot's tests (-1 hr)":
                $ time_travel_jump("E2")

            "Never mind":
                jump continue_two

    else: 

        menu:

            "Meet Vivienne (-45 hrs)":
                $ time_travel_jump("V1")

            "Meet Finn (-43 hrs)":
                $ time_travel_jump("F1")

            "Meet Elliot (-38 hrs)":
                $ time_travel_jump("E1")

            "Meet Serafina (-24 hours)":
                $ time_travel_jump("S1")

            "Meet Aster (-19 hrs)":
                $ time_travel_jump("A1")

            "Study with Finn (-14 hours)":
                $ time_travel_jump("F2")

            "Break into Aster's dorm (-9 hrs)":
                $ time_travel_jump("SA2")

            "Talk to Vivienne again (-2 hrs)":
                $ time_travel_jump("V2")

            "Do Elliot's tests (-1 hr)":
                $ time_travel_jump("E2")

            "Never mind":
                jump continue_two


label notastorm:

    "GAME ENDS HERE. PROGRESSING WILL RETURN YOU TO THE START MENU."
