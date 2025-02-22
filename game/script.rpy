# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define res = Character("???")
define m = Character("Mira")
define d = Character("Dean")
define v = Character("Vivienne")
define p = Character("Professor")
define f = Character("Finn")
define e = Character ("Elliot")

#Locations

image deans office box = "deans_office.png"
image ochem box = "ochem_lecture.png"


# The game starts here.

# DAY 1 --------------------------------------

# OPENING --------------------------------------

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

    m "...I don't know what else I expected."

    play sound "audio/sfx/SoundsCrate-Debris_Shuffle_1.mp3"

    res "Don't move. Your hands are tied."

    m "Was that reallyyy necessary?"

    res "I don't have much time, so let's get this over with."

    res "According to the laws of necromancy, I have full control over you as your resurrector."

    res "But I won't do anything right now. There's a three-day stalemate, you see."

    m "I don't see. I just woke up—do you think I understand any of this?"

    res "Listen. For the next 72 hours, we will walk the world as two separate people. One living and the other undead."

    res "But after time runs out, you're under my will forever."

    m "........Oh."

    res "See you in three days, Mira."

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

    jump deansoffice

# DEAN'S OFFICE --------------------------------------

label deansoffice:

    scene deans office
    with fade

    show deans_office
    with dissolve

    pause 2.0

    hide deans_office
    with dissolve

    play music "audio/BackgroundMusicDraft.mp3" volume 0.1

    show mira default at left
    with dissolve

    d "—and can I remind you, this school has one of the most competitive acceptance rates in the region." 
    
    d "Your professors may turn a blind eye to you skipping the occasional lecture, but missing important events like the annual masquerade ball will {i}not be tolerated {/i}."

    show mira sighing

    m "{i}( I just freed my wrists a few hours ago, cut me some slack. ){/i}"

    show mira default

    d "I expect to see you at every event in the future, understand?"
    
    d "If it troubles you so much to attend this academy, there are hundreds of other students lining up to take your place." 


    m "{i}( Is that a list of names for other students who missed the ball? Damn, she's going to be out of breath by the end of the day. ){/i}"

    d "Now, get out of my office."

    m "Yes, Dean."

    play sound "audio/sfx/soundscrate-walking-indoors.mp3"

    show mira default:
        moveoffright

    m "{i}My footsteps echo as I dodge the piles of paperwork and dirty mugs blocking the way to the exit.{/i}"

    scene blackscreen

    scene hallway
    with fade

    show mira default at left
    with dissolve

    m "Where was the Dean when one of her own students died? She's worried about the wrong balls…"

    show mira surprised

    m "Wait, that list."

    m "My resurrector must be one of the other students who missed the ball."

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

    d "Your professors may turn a blind eye to you skipping the occasional lecture, but missing important events like the annual masquerade ball will {i}not be tolerated {/i}."

    show mira sighing

    m "{i}( This spiel again?? ){/i}"

    show mira default

    m "{i}( What just happened…? It felt so easy, like taking a step backwards in a shifting landscape. ){/i}"


    d "I expect to see you at every school event in the future, understand?"

    d "If it troubles you so much to attend this academy, there are hundreds of other students lining up to be in your place." 

    play audio "audio/sfx/soundscrate-dropped-glass-1.mp3" volume 0.25
    play sound "audio/sfx/SoundsCrate-Wall_Break_1.mp3"

    show mira at center:
        moveright

    m "...!" 

    m "Oh sorry, I’ll pick that up—"

    show mira surprised

    d "Don’t touch my belongings and get {i}out of my office!{/i}" with vpunch

    show mira default

    m "Yes, Dean."

    show mira default:
        moveoffright

    m "{i}My footsteps echo as I sidestep what has become an avalanche of paperwork, shattered mugs, and scattered pens almost blocking the exit completely. {/i}" 
   
    m "{i}The list lies crumpled against my skirt. {/i}"

    jump tutorial

# TUTORIAL --------------------------------------

label tutorial:

    scene blackscreen
    with fade

    scene hallway
    with fade

    show mira default at left
    with dissolve

    m "I guess I shouldn’t be surprised. I’m a spirit — the temporal laws of the human world don’t apply to me anymore."

    m "But I can still feel time unspooling in the spirit world."

    m "Even when I travel back in time, the countdown keeps moving forward towards the third day." 

    $ hourglass = True
    $ day = 3
    $ remainingtime = 62

    "{i}Check the {color=#56768f}hourglass{/color} in the bottom left to view your remaining hours. {/i}"

    m "My mind was so clouded from the revival, I can barely remember the sound of my resurrector’s voice."

    m "I found a notebook lying on the gound earlier and created a profile for every student on the list."

    $ notebook = True

    "Click the {color=#56768f}notebook{/color} in the bottom right to access the character profiles."

    m "The sooner I find the resurrector, the sooner I can go back to being dead."

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
            $ remainingtime -=2
            jump V1

# VIVIENNE 1 --------------------------------------

label V1:

    show classroom
    with fade

    show ochem box
    with dissolve

    # change to astrophysics 

    pause 2.0

    hide ochem box
    with dissolve

    show mira sighing at left
    with dissolve

    m "{i}( I’m starting to remember why I always skip morning lectures. ){/i}"

    p "That’s all for today, class dismissed."

    show mira default at left

    show vivienne default at right
    with dissolve

    show mira default at left:
        moveright

    m "Did I miss anything important?"

    show vivienne surprised at right

    v "Wow, I almost forgot you were in this class."

    m "Me too."

    show vivienne default

    v "And no, everyone’s still too excited from last night. What’d you wear to the masquerade?"

    hide mira 
    hide vivienne 

    menu: 

        "I skipped":
            jump skipped

        "I got resurrected":
            jump resurrected

        "Just a shirt and slacks":
            jump shirtandslacks


label skipped:

    show mira default at center

    show vivienne default at right

    m "Oh, I skipped. Got yelled at by the Dean earlier."

    show vivienne frowning

    v "Definitely an experience, huh?"

    m "2/10. I don’t get why we’re required to go to these events."

    v  "It’s all for the school’s publicity. I’d rather hole up in my dorm and read."
    
    m "Did you?"
    
    v "Against my will, actually. I got sick with an awful cold."

    show vivienne frowning

    v "Can’t wait for my turn to be yelled at by the Dean."

    jump continue1

         
label resurrected:

    show mira default at center

    show vivienne default at right

    m "Nothing, I was busy being resurrected. How do I look for a dead girl?"

    show vivienne surprised

    v "..."

    m "..."

    show vivienne frowning

    v "Has anyone ever told you that they like your sense of humor?"

    m "Never."

    v "Right, that’s because they don't."

    m "...So what did you wear?"

    v "Oh, I couldn’t make it either. I got sick with an awful cold."

    show vivienne frowning

    v "Can’t wait to be yelled at by the Dean."

    jump continue1


label shirtandslacks:

    show mira default at center

    show vivienne default at right

    m "I threw on an old shirt and unearthed a pair of slacks. I don’t get why we’re required to go to these events."

    show vivienne frowning

    v  "It’s all for the school’s publicity. I’d rather hole up in my dorm and read."

    m "Did you?"

    v "Against my will, actually. I got sick with an awful cold."

    show vivienne frowning

    v "Can’t wait to be yelled at by the Dean."

    jump continue1


label continue1:
    
    hide mira 

    hide vivienne 

    menu:

        "You don't look sick":
            jump fine

        "I was literally resurrected":
            jump resurrected2

        "No sympathy for her daughter?" if vividaughter == True:
            jump daughter


label fine:

    show mira default at center

    show vivienne surprised at right

    m "You don’t look sick. Recover quickly?"

    show vivienne default

    v "...7 consecutive hours of sleep."

    m "Is that supposed to be a lot."

    show vivienne surprised

    v "What—how else do you think I recovered this fast?"

    show vivienne frowning

    v "But now the Dean will think I’m making up excuses, won’t she."

    m "You seem pretty caught up in astro, too."

    v "Not quite—I haven’t finished updating my notes, I’m still confused how parallax works, I lost one of my pens, and—"

    m "Just use another one?"

    show vivienne surprised

    v "What?"

    m "To write with."

    show vivienne frowning

    v "I can’t—all my notes are color-coded by historical relevance."

    m "..."

    jump continue2


label resurrected2:

    show mira sighing at center

    show vivienne surprised at right

    m "Yeah, I got resurrected from the dead and couldn’t use that as an excuse either."

    show mira default

    v "..."

    show vivienne frowning

    m "..."

    v "I’m sorry to hear that…?"

    m "Eh, I’ll get over it."

    m "Being yelled at, I mean. Not being dead."

    v "Whatever bit you're doing isn't as funny as you think."

    jump continue2


label daughter:

    show mira default at center

    show vivienne frowning at right

    m "Does she have no sympathy for her own daughter being sick?"

    show vivienne surprised

    v "..."

    show vivienne frowning

    v "I wish our relationship wasn’t such widespread news. How do you of all people know about it?"

    hide mira
    hide vivienne

    menu:

        "Finn mentioned it":
            $ finnsnitch = True
            jump finnsaid

        "Just campus rumors":
            jump rumors

        "Me of all people?":
            jump me


label finnsaid:

    show mira default at center

    show vivienne frowning at right

    m "Finn mentioned it to me offhandedly once."

    show vivienne default

    v "Did he also mention your pretty face?"

    show mira sighing

    m "Multiple times."

    v "He doesn’t mean it, you know. He says it to every girl who breathes."

    show mira default

    m "What a relief."

    jump continuetwo


label rumors:
    
    show mira default at center

    show vivienne frowning at right

    m "It’s a remote campus. Rumors spread."

    show vivienne frowning

    v "I suppose, though I could count on one hand how often I see you around campus."

    m "I’m standing in front of you right now."

    v "Yes, and I’m still not convinced it's not a sleep deprivation-induced hallucinatory effect."

    jump continueone


label me:

    show mira default at center

    show vivienne frowning at right

    m "What do you mean, me of all people?"

    show vivienne frowning

    v "I could count on one hand how often I see you around campus."

    m "I’m standing in front of you right now."

    v "Yes, and I’m still not convinced it's not a sleep deprivation-induced hallucinatory effect."

    jump continueone


label continueone:

    hide mira
    hide vivienne

    menu: 

        "I thought you slept well last night?":
            jump lastnight

        "Say nothing":
            jump continuetwo


label lastnight:

    show mira default at center

    show vivienne frowning at right

    m "I thought you got your 7 hours last night?"

    show vivienne surprised
 
    v "It stacks up."

    jump continue2


label continuetwo:

    show mira default at center

    show vivienne frowning at right

    v "Anyways, no, the Dean only cares about appearances."

    v "...And the library’s 19th-century Impressionist paintings collection. So I'm still getting yelled at."

    jump continue2


label continue2:

    show mira default at center

    show vivienne surprised at right

    v "Oh—I’m running late for my next lecture. See you next class?"

    show vivienne default

    m "No promises."

    show vivienne default:
        moveoffleft

    show mira surprised

    if vividaughter == True:

        m "{i}Summer and worn books again, like I expected. {/i}"

        show mira default

        m "{i}Quietly, I raise a wrist to my nose. I expect the smell of decay or saltwater, but there's neither. {/i}"

        m "{i}The dead leave no scent. {/i}"

        hide vivienne default

        jump continue3

    else: 

        m "{i}She disappears in a swish of braids; one almost brushes my face. It smells like summer and worn books. {/i}"

        $ viv = True
        $ vupdate = 1
        $ renpy.notify("The notebook has been updated")

        m "{i}I never noticed. {/i}"

        hide vivienne default

        jump continue3


label continue3:

    hide mira

    menu:

        "Look for Elliot (WIP)":
            $ remainingtime -=1
            jump E1

        "Time travel":
            jump timetravel1


label timetravel1:

    menu:

        "Find Vivienne (-2 hrs)":
            $ remainingtime -=2
            jump V1

        "Never mind":
            jump continue3

# ELLIOT 1 --------------------------------------

label E1:

    show mira default at left 

    show elliot at right

    m "(Oh, finally I found him)"

    m "(It looks like he’s holding something… is that some kind of bug? It looks dead.)"

    m "(...)"

    m "Yeah that’s definitely a bug, and it’s definitely dead."

    e "You shouldn’t sneak up on someone you know. It’s pretty creepy"

    m "What?! How does he know I’m here?"

    m "I wasn’t- I just didn’t want to interrupt what you were doing"

    e "Nah, I’ve been getting better at this. Even with your intrusion I was able to stay focused"

    e "Ta da!"

    m "(Oh the insect in his palm! It’s starting to fly around!)"

    m "Wait, how did you—"

    e "Before we get to your question, how about you answer one of mine first?"

    m "Sure...?"

    show elliot at center:
        moveleft

    e "So how long have you been dead for?"

    m "?!"

    menu:
        "Lie":
            jump lie
        "Just admit you're dead":
            jump lie
label lie: 
    "(Insert more dialogue)"

    menu:

        "Find Finn":
            jump F1

# FINN 1 --------------------------------------

label F1:

    scene hallway
    with fade

    show mira default at left
    with dissolve

    # SFX: crowd

    m "{i}( How does half the school seem to know where he is? I asked a passing student and they immediately pointed me this way. ){/i}"

    m "{i} Elbows and backpacks ram into my side as I make my way through the school."
    m "{i} It’s the end of the day; the hallway is a sea of blue uniforms capped with white collars. {/i}"

    scene courtyard 
    with fade

    show mira surprised at left
    with dissolve 

    m "{i}( There he is—surrounded by a tide pool of chattering students. ){/i}"

    show mira default

    m "Finn. I need to talk to you. Finn? Finn."

    show mira sighing

    m "Please don’t make me push my way through that crowd. Maybe I resign myself to being an undead servant forever—"

    show mira surprised

    f "Watch out!"

    #SFX: thud

    show mira bonk

    m "—!!" with hpunch

    show finn concerned at right

    show mira default

    f "Hey, you okay?"

    show finn default

    m "{i}( He picks up the ball that slammed into the side of my head and tosses it back to a student who winces in apology. ){/i}"

    m "Yeah, I can’t feel pain."

    show finn flirt

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
        
        show mira smile at center:
            moveright

        show finn flirt at right

        m "What, the one in your mirror?"

        show finn default

        f "Hahaa. Finn, by the way."

        show mira default

        m "I know who you are, Mr. Top Student at Seacliff."

        show finn pensive

        f "Ugh, surely I have more redeeming qualities?"

        jump continue4


label telloff:

        show mira sighing at center:
            moveright

        show finn flirt at right

        m "Should’ve taken one for the team then, Mr. Top Student."

        show finn pensive

        f "Ugh, surely I have more redeeming qualities than my grades?"

        jump continue4


label continue4:

    hide mira
    hide finn

    menu: 

        "According to everyone else" if flirtmeter > 0:

            jump more

        "That's your most attractive trait":

            jump most


label more:

    show mira smile at center

    show finn pensive at right

    m "Everyone else seems to think so. Do you know how many students were devastated when they couldn’t find you at the masquerade?"

    show mira default

    f "Ah—I was sick."

    m "..."

    f "..."

    show finn concerned

    f "...What?"

    show finn pensive

    show mira sighing

    m "Was there an outbreak of the Black Plague last week? You couldn’t think of a better excuse than Vivienne?"

    f "Oh, Vivi might be telling the truth. Have you seen how little that girl sleeps?"

    f "It’s like she thinks she’s got something to prove because she’s the daughter of our Dean."

    $ vividaughter = True

    show mira default

    m "So what’s the real reason you were gone?"

    show finn flirt

    f "You’re getting ahead of yourself—I don’t tell my secrets to people who think I have no redeeming qualities."

    show mira sighing

    m "Your redeeming quality is your ability to help me catch up on last week’s chemistry lectures. Please? I’m so close to failing the class."

    jump continue5
    

label most:

    show mira default at center

    show finn pensive at right

    m "No, that’s definitely your most attractive trait. Don’t drown in the admissions letters that flood your dorm room next year."

    show finn frown

    f "Don’t concern yourself with my grades."

    m "...Okay."

    show mira sighing

    m "Your most attractive trait is actually your ability to help me catch up on last week’s chemistry lectures. Please? I’m so close to failing the class."

    jump continue5


label continue5:

    show mira default at center

    show finn pensive at right

    f "..."

    m "{i}( There’s a moment of silence as I watch the synapses go off in his head, trying to decide how much he wants to uphold his reputation as the boy who does anything and everything. ){/i}"

    show finn default

    f "Tomorrow, physical sciences lecture hall at lunch break. It’s the only time I’m free."

    show mira smile

    m "See you there. Thanks, Finn."

    show finn flirt

    f "Only because you’re pretty."

    hide finn 
    with dissolve

    $ fin = True
    
    if vividaughter == True: 
        $ fupdate = 2

    else:
        $ fupdate = 1

    $ renpy.notify("The notebook has been updated")

    show mira default

    m "{i}( Oh. I never told him my name. ){/i}"

    # here we need to change what info the notebook fills in depending on which dialogue options you chose

    jump continue6


label continue6:

    hide mira
    hide finn

    menu:

        "Go back to the dorms and sleep.":
            $ remainingtime -=1
            jump sleep

        "Time travel":
            jump timetravel2


label sleep:
    
    show mira default

    m "{i}( Oh right, I don’t need sleep anymore. ){/i}"

    show mira sighing

    m "{i}( I’ll go wander the hallways wailing like the ghost I’m supposed to be until someone finds a way to put me to rest permanently. ){/i}"

    jump continue7


label timetravel2:
    
    menu:

        "Find Vivienne (-8 hrs)":
            $ remainingtime -=8
            jump V1

        "Look for Finn (-1 hr)":
            $ remainingtime -=1
            jump F1

        "Never mind":
            jump continue6


label continue7:

    scene end of day 1

    $ renpy.pause()

# This ends the game.

return
