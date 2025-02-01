# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define res = Character("???")
define m = Character("Mira")
define d = Character("Dean")
define v = Character("Vivienne")
define p = Character("Professor")
define f = Character("Finn")

#invisible counters
default flirtmeter = 0

define fade = Fade(0.5, 0.0, 0.5)
define fadehold = Fade(0.5, 1.0, 0.5)

image deans office box = "deans_office.png"
image ochem box = "ochem_lecture.png"

transform left:
    xalign 0.25 yalign 0.0

transform right:
    xalign 0.75 yalign 0.0

transform moveleft:
    xalign 0.75
    ease 0.4 xalign 0.5

transform moveright:
    xalign 0.25
    ease 0.4 xalign 0.5

transform moveoffleft:
    xalign 0.75
    ease 0.5 xalign -0.5

transform moveoffright:
    xalign 0.75
    ease 0.5 xalign 1.5

# The game starts here.

# DAY 1 --------------------------------------

# OPENING AND TUTORIAL --------------------------------------

label start:

    scene opening
    with fade

    play music "audio/BackgroundMusicDraft.mp3" volume 0.25

    play sound "audio/sfx/soundscrate-waves.mp3" volume 0.50

    pause 3.0

    res "Are you surprised to be alive again?"

    m "{i}( ...? ) {/i}"
    
    m "{i}( Waves...broken rocks against my skin...is this how I died? ) {/i}"

    res "It's been a week, if you were wondering. And so far, it seems like no one else has noticed you're gone."

    m "I don't know what else I expected."

    play sound "audio/sfx/SoundsCrate-Debris_Shuffle_1.mp3"

    res "Don't move. Your hands are tied."

    m "Was that reallyyy necessary?"

    res "I don't have much time, so let's get this over with."

    res "According to the laws of necromancy, I have full control over you as your resurrector."

    res "But I won't do anything right now. There's a five-day stalemate, you see."

    m "I don't see. I just woke up—do you think I understand any of this?"

    res "Listen. For the next 120 hours, we’ll walk the world as two separate people. One living and the other undead."

    res "But after time runs out, you're under my will forever."

    m "........Oh."

    res "See you in five days, Mira."

    play sound "audio/sfx/sand-walk.mp3" volume 2.75

    scene beach

    "..."

    m "{i}I remember falling, pieces of the cliffside raining from the sky, and a silence that surprised me with how much it sounded like resignation. {/i}"

    m "{i}And after that, the cold sting of ocean spray. {/i}"

    m "{i}...I just wanted to be dead. {/i}"

    stop music fadeout 3

    window hide

    show blackscreen
    with fadehold

    # TUTORIAL --------------------------------------

    scene deans office #Dean's Office
    with fade

    show deans_office
    with dissolve

    pause 2.0

    hide deans_office
    with dissolve

    play music "audio/BackgroundMusicDraft.mp3" volume 0.1

    show mira sighing at left
    with dissolve

    d "—and can I remind you, this school has one of the most competitive acceptance rates in the region." 
    
    d "Your professors may turn an occasional blind eye to you skipping the occasional lecture, but missing important events like the annual masquerade ball will {i}not be tolerated {/i}."

    m "{i}( I just freed my wrists a few hours ago, cut me some slack. ){/i}"

    d "I expect to see you at every event in the future, understand?"
    
    d "If it troubles you so much to attend this academy, there are hundreds of other students lining up to take your place." 

    show mira default at left

    m "{i}( Is that a list of names for other students who missed the ball? Damn, she's going to be out of breath by the end of the day. ){/i}"

    d "Now, get out of my office."

    m "Yes, Dean."

    play sound "audio/sfx/soundscrate-walking-indoors.mp3"

    m "{i}My footsteps echo as I dodge the piles of paperwork and dirty mugs blocking the way to the exit. {/i}"

    scene blackscreen

    scene hallway
    with fade

    show mira default at left
    with dissolve

    m "Where was the Dean when one of her own students died? She's worried about the wrong balls…"

    show mira surprised at left

    m "Wait, that list."

    m "My resurrector has to be one of the other students who missed the ball."

    hide mira default

    menu:
        "I wish there was a way to go back":
            play audio "audio/sfx/hourglass.mp3"
            play sound "audio/sfx/SOUNDSCRATE-Whoosh.mp3" volume 0.25

    scene blackscreen
    with fade

    scene deans office
    with fade

    show deans_office
    with dissolve

    pause 2.0

    hide deans_office
    with dissolve

    show mira default at left
    with dissolve

    d "—and can I remind you,  this school has one of the most competitive acceptance rates in the region."

    d "Your professors may turn an occasional blind eye to you skipping the occasional lecture, but missing important events like the annual masquerade ball will {i}not be tolerated {/i}."

    show mira sighing at left

    m "{i}( This spiel again?? ){/i}"

    show mira default at left

    m "{i}( What just happened…? It felt so easy, like taking a step backwards in a shifting landscape. ){/i}"


    d "I expect to see you at every school event in the future, understand?"

    d "If it troubles you so much to attend this academy, there are hundreds of other students lining up to be in your place." 

    play audio "audio/sfx/soundscrate-dropped-glass-1.mp3" volume 0.25
    play sound "audio/sfx/SoundsCrate-Wall_Break_1.mp3"

    d "..."

    m "...!"

    m "Oh sorry, I’ll pick that up—"

    show mira surprised at left

    d "Don’t touch my belongings and get {i}out of my office!{/i}" with vpunch

    show mira default at left

    m "Yes, Dean."

    m "{i}My footsteps echo as I sidestep what has become an avalanche of paperwork, shattered mugs, and scattered pens almost blocking the exit completely. {/i}" 
   
    m "{i}The list lies crumpled against my skirt. {/i}"

    scene blackscreen
    with fade

    scene hallway
    with fade

    show mira default at left
    with dissolve

    m "I guess I really shouldn’t be surprised. I’m a spirit — the laws of the human world don’t affect me."

    m "That said, I can still feel time unspooling in the spirit world. Even when I traveled back in time, the countdown didn't stop moving towards the fifth day." 

    $ hourglass = True

    "{i}Check the {color=#56768f}hourglass{/color} in the bottom left to view your remaining days. {/i}"

    #Remaining time should be 5 days 

    m "It's simultaneously so little time and so many hours I'm forced to be alive."

    m "My mind was so foggy from the revival, I can barely remember the sound of my resurrector’s voice."

    m "I found a notebook earlier and wrote a profile for every student who was on the list."

    $ notebook = True

    "Click the {color=#56768f}notebook{/color} in the bottom right to access the character profiles."

    m "The sooner I find the resurrector, the sooner this will all be over."

    show mira default at left

    m "Finn, Elliot…I recognize a few of these names…Vivienne?"

    show mira surprised at left

    m "I know where Vivienne is right now."

    show mira sighing at left

    m "..."

    m "This is going to be the first lecture I've gone to in weeks."

    hide mira sighing

    menu: 

        "Find Vivienne":

            jump V1

# VIVIENNE 1 --------------------------------------

label V1:

    show classroom
    with fade

    show ochem box
    with dissolve

    pause 2.0

    hide ochem box
    with dissolve

    show mira sighing at left
    with dissolve

    m "( I’m starting to remember why I always skip morning lectures. )"

    p "That’s all for today, class dismissed."

    show mira default at left

    show vivienne default at right
    with dissolve

    show mira default at left:
        moveright

    m "Did I miss anything important?"

    show vivienne surprised at right

    v "Woah—I almost forgot you were in this class."

    m "Me too."

    show vivienne default

    v "And no you didn’t, everyone’s still excited from last night. What’d you wear to the masquerade?"

    hide mira 
    hide vivienne 

    menu: 

        "I skipped":
            jump skipped

        "I got resurrected":
            jump resurrected


label skipped:

    show mira default at center

    show vivienne default at right

    m "I skipped it and got yelled at by the Dean earlier."

    show vivienne frowning

    v "Unpleasant experience, right?"

    m "I don’t get why we’re required to go to these events."

    show vivienne default

    v  "It’s only for publicity; I’d rather hole up in my dorm and read."

    m "Is that what you did?"

    v "I mean yes, but not by choice."

    show vivienne frowning

    v "I was sick with an awful cold, but I’m sure the Dean is going to yell at me too."


    jump continue1

         
label resurrected:

    show mira default at center

    show vivienne default at right

    m "Nothing, I was busy being resurrected. Do I look good for a dead girl?"

    show vivienne frowning

    v "..."

    m "..."

    v "Has anyone ever told you that you have a good sense of humor?"

    m "Never."

    v "That's because you don't."

    m "So what did you wear?"

    show vivienne default

    v "Oh, I wasn’t there either."

    show vivienne frowning

    v " I was sick with an awful cold, but I’m sure the Dean is going to yell at me later."

    jump continue1


label continue1:
    
    hide mira 

    hide vivienne 

    menu:

        "You look fine":
            jump fine

        "Mood, I was literally resurrected":
            jump resurrected2


label fine:

    show mira default at center

    show vivienne frowning at right

    m "You look like you’ve already recovered."

    show vivienne default

    v "I slept the whole night through, so I’m feeling better."

    show vivienne frowning

    v "But now the Dean’s going to say I look fine too, isn’t she?"

    m "You seem pretty caught up in this class too."

    show vivienne frowning

    v "Oh I’m not—I read over the textbook this morning, but I haven’t finished updating all my notes—"
    v "—there’s a concept from last week’s lecture I’m confused on, I lost the pen I usually write with, and—"
   
    m "Is that an issue?"

    show vivienne surprised

    v "What?"

    show vivienne frowning

    m "Don’t you have more than one pen."

    v "I mean yeah, but now the color of the ink won’t match."

    m "..."

    show vivienne default

    v "All that aside, you’re doing pretty well yourself for someone I never see in lecture."

    m "Maybe the trick is using multiple pens."

    m "{i}( So many hours of studying wasted just to end up dead. ) {/i}"

    jump continue2


label resurrected2:

    show mira sighing at center

    show vivienne frowning at right

    m "Yeah, I got resurrected from the dead and couldn’t use that as an excuse either."

    show mira default

    show vivienne frowning

    v "..."

    m "..."

    v "I’m sorry to hear that…?"

    m "Eh, I’ll get over it."

    m "Being yelled at, I mean. Not being dead."

    v "You’re really leaning into this bit, huh?"

    jump continue2


label continue2:

    show vivienne surprised at right

    v "Oh—I’m running late for my next lecture. See you next class?"

    show vivienne default

    m "No promises."

    show vivienne default:
        moveoffleft

    show mira surprised

    m "{i}She disappears in a swish of braids; one almost brushes my face. It smells like summer and worn books. {/i}"

    $ viv = True
    $ renpy.notify("The notebook has been updated")

    show mira default

    m "{i}I never noticed. {/i}"

    hide vivienne default

    jump continue3


label continue3:

    hide mira
    hide vivienne

    menu:

        "Look for Finn (there is a timeskip here that you will ignore for the sake of the playtest)":
            jump F1

        "Time travel":
            jump timetravel1


label timetravel1:

    menu:

        "Find Vivienne":
            jump V1

        "Never mind":
            jump continue3

# FINN 1 --------------------------------------SS

label F1:


    scene hallway
    with fade

    show mira default at left
    with dissolve

    # SFX: crowd

    m "{i}( How does half the school seem to know where he is? I asked a passing student and they immediately pointed me this way. ){/i}"

    m "{i}( Elbows and backpacks ram into my side as I make my way through the school. It’s the end of the day; the hallway is a sea of blue uniforms capped with white collars. ){/i}"

    scene courtyard 
    with fade

    show mira surprised at left
    with dissolve 

    m "{i}( There he is—surrounded by a tide pool of chattering students. ){/i}"

    show mira default at left

    m "Finn. I need to talk to you. Finn? Finn."

    m "Please don’t make me push my way through that crowd. Maybe I resign myself to being an undead servant forever—"

    show mira surprised at left

    f "Watch out!"

    #SFX: thud

    # show mira bonk at left

    m "—!!" with hpunch

    # make this effect last longer

    show finn at right

    # show finn concerned at right

    f "Hey, you okay?"

    m "{i}( He picks up the ball that slammed into the side of my head and tosses it back to a student who winces in apology. ){/i}"

    show mira default at left

    m "Yeah, I can’t feel pain."

    # show finn flirting at right

    f "That’s a relief—wouldn’t wanna damage that pretty face."

    hide mira
    hide finn

    menu:

        "Pretend to flirt back":
            $ flirtmeter += 1
            jump flirt

        "Tell him off":
            jump telloff


label flirt:
        
        # show mira smiling at center:

        show mira default at center:
            moveright


        show finn at right

        # show finn flirting at right

        m "What, the one in your mirror?"

        # show finn default at right

        f "Hahaa. Finn, by the way."

        show mira default at center

        m "I know who you are, Mr. Top Student at Seacliff."

        # show finn pensive at right

        f "Ugh, surely I have more redeeming qualities?"

        jump continue4


label telloff:

        show mira sighing at center

        show finn at right

        # show finn flirting at right

        m "Should’ve taken one for the team then, Mr. Top Student."

        # show finn pensive at right

        f "Ugh, surely I have more redeeming qualities than my grades?"

        jump continue4


label continue4:

    hide mira
    hide finn

    if flirtmeter > 0:

        menu: 

            "Plenty more, according to everyone else":

                jump more

            "That's your most attractive trait":

                jump most

    else:

        menu:

            "That's your most attractive trait":

                jump most


label more:

    show mira default at center

    show finn at right

    # show finn pensive at right

    m "Everyone else seems to think so. Do you know how many students were devastated when they couldn’t find you at the masquerade?"

    f "Ah—I was sick."

    m "..."

    f "..."

    # show finn concerned at right

    f "...What?"

    show mira sighing at center

    m "Was there an outbreak of the Black Plague last week? You couldn’t think of a better excuse than Vivienne?"

    # show finn default at right

    f "Oh, Vivi might be telling the truth. Have you seen how little that girl sleeps?"

    f "It’s like she thinks she’s got something to prove because she’s the daughter of the Dean."

    show mira default at center

    m "{i}( ...What? ){/i}"

    m "So what’s the real reason you were gone?"

   # show finn flirting at right

    f "You’re getting ahead of yourself—I don’t tell my secrets to people who think I have no redeeming qualities."

    show mira sighing at center

    m "Your redeeming quality is your ability to help me catch up on last week’s chemistry lectures. Please? I’m so close to failing the class."

    jump continue5
    

label most:

    show mira default at center

    show finn at right

    # show finn pensive at right

    m "No, that’s definitely your most attractive trait. Don’t drown in the admissions letters that flood your dorm room next year."

    # show finn frowning at right

    f "Don’t concern yourself with my grades."

    m "...Okay."

    m "Your redeeming quality is actually your ability to help me catch up on last week’s chemistry lectures. Please? I’m so close to failing the class."

    jump continue5


label continue5:

    show mira default at center

    show finn at right

    # show finn pensive at right

    f "..."

    m "{i}( There’s a moment of silence as I watch the synapses go off in his head, trying to decide how much he wants to uphold his reputation as the boy who does anything and everything. ){/i}"

    # show finn default at right

    f "Day after tomorrow, physical sciences lecture hall at lunch break. It’s the only time I’m free."

    m "See you there. Thanks, Finn."

    # show finn flirting at right

    f "Only because you’re pretty."

    hide finn 
    with dissolve

    $ finn = True
    $ renpy.notify("The notebook has been updated (not actually yet)")

    m "{i}( Oh. I never told him my name. ){/i}"

    # here we need to change what info the notebook fills in depending on which dialogue options you chose

    jump continue6


label continue6:

    hide mira
    hide finn

    menu:

        "Go back to the dorms and sleep.":
            jump sleep

        "Time travel":
            jump timetravel2


label sleep:
    
    show mira default at center

    m "{i}( Oh right, I don’t need sleep anymore. ){/i}"

    show mira sighing

    m "{i}( I’ll go wander the hallways wailing like the ghost I’m supposed to be until someone finds a way to put me to rest permanently. ){/i}"

    jump continue7


label timetravel2:
    
    menu:

        "Find Vivienne (this will have consequences that I haven't implemented yet)":
            jump V1

        "Look for Finn":
            jump F1

        "Never mind":
            jump sixthcontinue


label continue7:

    scene end of day 1

    $ renpy.pause()

# This ends the game.

return
