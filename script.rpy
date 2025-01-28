# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define res = Character("???")
define m = Character("Mira")
define d = Character("Dean")
define v = Character("Vivienne")
define p = Character("Professor")

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

# The game starts here.

# OPENING

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

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

    
    # DAY 1

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

            jump rightaway


label rightaway:

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

    hide mira default

    hide vivienne default

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


    jump firstContinue

         
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

    jump firstContinue


label firstContinue:
    
    hide mira default

    hide vivienne frowning

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


    jump secondContinue


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


    jump secondContinue


label secondContinue:

    show vivienne surprised at right

    v "Oh—I’m running late for my next lecture. See you next class?"

    show vivienne default

    m "No promises."

    show vivienne default:
        moveoffleft

    show mira surprised

    m "{i}She disappears in a swish of braids; one almost brushes my face. It smells like summer and worn books. {/i}"

    show mira default

    m "{i}I never noticed. {/i}"

    $ viv = True
    $ renpy.notify("The notebook has been updated.")

    hide vivienne default

    menu:

        "Find Vivienne later":
            jump later

label later:

    scene hallway
    with fade

    show mira default at left
    with dissolve

    show vivienne reading lookdown at right
    with dissolve

    m "Did you get yelled at yet?"

    show vivienne reading upset

    v "Couldn’t escape it—the Dean called me into her office after my second class."

    v "She was in a worse mood than usual too; it looked like someone knocked over her things earlier today."

    m "Must’ve been a nightmare to walk through the office."

    m "You look like you’re in a worse mood than usual too."

    v "I don’t get along with the Dean—it’s nothing half an hour of reading won’t fix."

    hide mira default

    hide vivienne reading upset

    menu:

        "Ask what she's reading":
            jump reading

        "Pry for more info":
            jump pry


label reading:

    show mira default at left

    show vivienne reading upset at right

    m "Anything interesting in there?"

    show vivienne reading excited at right:
        moveleft

    v "You wouldn’t believe how much. I just borrowed this from the library last week—{i}A Comprehensive History of Modern Alchemy. {/i}"

    m "...Alchemy?"

    v "Don’t look at me like that. I know alchemy is traditionally considered a dead field of study, but it’s the foundation of all modern magick."

    show mira default

    m "Which a lot of people also consider a dead field."

    m "{i} ( Then again, I was just resurrected less than a day ago. ) {/i}"

    v "It’s only dead if you don’t know where to look. The thing about alchemy is—all magick is essentially a form of transmutation."

    v "If we understood the details of alchemy better, we could unlock so many shortcuts that would solve the limitations and constraints we currently have in the field of magick."

    show mira surprised

    m "{i}( I’ve heard people talk about this problem before, but I’ve never seen someone suggestion the solution lies in a subject that’s infamous for having no practical uses. ) {/i}"

    show mira default

    m "It’s an interesting idea—at least you’re in the right place for it."

    v "Right? Seacliff is one of the only schools in the country that offer classes on alchemy."
    
    m "..."

    show vivienne reading lookdown
    
    v "..."

    m "{i} Vivienne’s attention has already wandered back to her book, my presence forgotten. {/i}"

    m "{i} I can't even be insulted. {/i}"

    m "{i} ...What does it feel like to believe in something so strongly? {/i}"

    $ vivupdate += 1
    $ renpy.notify("The notebook has been updated.")

    jump thirdContinue
    

label pry:

    show mira default at left

    show vivienne reading upset at right

    m "You say that like anyone gets along with her."

    v "If they do, I haven’t met them yet."

    m "Does she dislike you for a particular reason or something then?"

    v "No."
    
    m "..."

    v "I’m one in a sea of students she’s dissatisfied with."

    show vivienne reading lookdown

    v "..."

    m "{i}( She's intentionally ignoring me. ) {/i}"

    m "..."

    jump thirdContinue


label thirdContinue:
    
    m "{i}She smells like worn pages and summer again. {/i}"

    m "{i}Quietly, I lift my wrist to my nose. I expect saltwater or maybe the scent of decay, but there's neither. {/i}"
    
    m "{i} The dead smell like nothing. {/i}"


    scene to be continued
    with fade

    $ renpy.pause()

    jump fourthContinue

label fourthContinue:

    # WIp


    # This ends the game.
    return
