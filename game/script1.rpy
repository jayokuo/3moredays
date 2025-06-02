# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define x = Character("???")
define r = Character("Resurrector")
define m = Character("Mira")
define d = Character("Dean")
define v = Character("Vivienne")
define p = Character("Professor")
define f = Character("Finn")
define e = Character ("Elliot")
define s = Character ("Serafina")
define a = Character ("Aster")


# The game starts here.

# DAY 1 --------------------------------------

# OPENING --------------------------------------

label start:

    scene beach
    with fade

    play music "audio/ost/opening.mp3" volume 0.25

    play sound "audio/sfx/waves.mp3" volume 0.50

    pause 3.0

    show resurrector

    x "Are you surprised to be alive again?"

    m "{i}( ...? ) {/i}"
    
    m "{i}( Waves...broken rocks against my skin...is this how I died? ) {/i}"

    x "It's been a week, if you were wondering. And so far, it seems like no one else has noticed you're gone."

    m "...I don't know what else I expected."

    play sound "audio/sfx/shuffle.mp3"

    x "Don't move. Your hands are tied."

    m "Was that reallyyy necessary?"

    x "I don't have much time, so let's get this over with."

    x "According to the laws of necromancy, I have full control over you as your resurrector."

    x "But I won't do anything right now. There's a three-day delay, you see."

    m "I don't see. I just woke up—do you think I understand any of this?"

    x "Listen. For the next 72 hours, we will walk the world as two separate people. One living and the other undead."

    x "But after time runs out, you're under my will forever."

    m "........Oh."

    x "See you in three days, Mira."

    play sound "audio/sfx/walk-sand.mp3" volume 2.75

    hide resurrector
    with dissolve

    "..."

    m "{i}I remember falling, pieces of the cliffside raining from the sky, and a silence that surprised me with how much it sounded like resignation. {/i}"

    m "{i}And after that, the cold sting of ocean spray. {/i}"

    m "{i}...I just wanted to be dead. {/i}"

    stop music fadeout 3

    window hide

    show image "ui/general/blackscreen.png"
    with fadehold

    jump deansoffice

# DEAN'S OFFICE --------------------------------------

label deansoffice:

    scene deans office
    with fade

    $ hide_menu()

    centered "{font=Marker Felt.ttf} {size=35} 8:00 am {/size} \n {size=40} Seacliff Academy - Dean's Office {/size} {/font}"

    $show_menu1()

    $ hourglass = True
    $ remainingtime = 64

    play music "audio/ost/bgm1.mp3" volume 0.25

    d "—and can I remind you, this school has one of the most competitive acceptance rates in the region." 
    
    d "Your professors may turn a blind eye to you skipping the occasional lecture, but missing important events like the annual masquerade ball will {i}not be tolerated {/i}."

    show mira sighing at left
    with dissolve

    m "{i}( I just freed my wrists a few hours ago, cut me some slack. ){/i}"

    show mira default

    d "I expect to see you at every event in the future, understand?"
    
    d "If it troubles you so much to attend this academy, there are hundreds of other students lining up to take your place." 

    m "{i}( Is that a list of names for other students who missed the ball? Damn, she's going to be out of breath by the end of the day. ){/i}"

    d "Now, get out of my office."

    m "Yes, Dean."

    play sound "audio/sfx/walk-indoors.mp3"

    show mira default:
        moveoffright

    m "{i}My footsteps echo as I dodge the piles of paperwork and dirty mugs blocking the way to the exit.{/i}"

    scene hallway
    with fade

    show mira default at left
    with dissolve

    m "Where was the Dean when one of her own students died? She's worried about the wrong balls…"

    show mira surprised

    m "Wait, that list."

    m "My resurrector must be one of the other students who missed the ball."

    hide mira
    with dissolve

    menu:
        "I wish there was a way to go back":
            play audio "audio/time travel/hourglass.mp3"
            play sound "audio/time travel/whoosh.mp3" volume 0.25

    scene blackscreen
    with fade

    scene deans office
    with fade

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

    play audio "audio/sfx/glass-drop.mp3" volume 0.25
    play sound "audio/sfx/wall-break.mp3"

    show mira at center:
        movecloseleft

    m "...!" 

    m "Oh sorry, I’ll pick that up—"

    show mira surprised

    d "Don’t touch my belongings and get {i}out of my office!{/i}" with vpunch

    show mira default

    m "Yes, Dean."

    play sound "audio/sfx/walk-indoors.mp3"

    show mira default:
        moveoffright

    m "{i}My footsteps echo as I sidestep what has become an avalanche of paperwork, shattered mugs, and scattered pens almost blocking the exit completely. {/i}" 
   
    m "{i}The list lies crumpled against my skirt. {/i}"

    $ remainingtime -= 1

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

    "{i}Click the {color=#56768f}hourglass{/color} in the bottom left to view your remaining hours.{/i}"

    m "My mind was so clouded from the revival, I can barely remember the sound of my resurrector’s voice."

    m "I found a notebook lying on the gound earlier and created a profile for every student on the list."

    $ notebook = True

    "{i}Click the {color=#56768f}notebook{/color} in the bottom right to access the character profiles. {/i}"

    m "The sooner I find the resurrector, the sooner I can go back to being dead."

    show mira default at left

    m "Finn, Elliot…I recognize a few of these names…Vivienne?"

    show mira surprised at left

    m "I know where Vivienne is right now."

    show mira sighing at left

    m "..."

    m "This is going to be the first lecture I've gone to in ages."

    hide mira
    with dissolve

    jump V1

# VIVIENNE 1 --------------------------------------

label V1:

    if f1_done > 0:
        $ sera_day1 = True

    $ v1_done += 1

    scene classroom
    with fade

    $ hide_menu()

    centered "{font=Marker Felt.ttf} {size=35} 8:55 am {/size} \n {size=40} Astrophysics Lecture {/size} {/font}"

    $ show_menu()

    show mira sighing at left
    with dissolve

    if f1_done == 0:

        m "{i}( I’m starting to remember why I always skip morning classes. ){/i}"

    p "That’s all for today, class dismissed."

    show mira default at left

    show vivienne default at right
    with dissolve

    show mira default at center:
        movecenter 

    m "Did I miss anything important?"

    show vivienne surprised at right

    v "Wow, I almost forgot you were in this class."

    m "Me too."

    if f1_done == 0:

        show vivienne default

        v "And no, everyone’s still too excited from last night. What’d you wear to the masquerade?"

        hide mira 
        hide vivienne 
        with dissolve

        menu: 

            "I skipped":
                jump skipped

            "I got resurrected":
                jump resurrected

            "Just a shirt and slacks":
                jump shirtandslacks

    else:

        m "{i}I chat with Vivienne about the masquerade, only half-listening to the responses I’ve already heard once before.{/i}"

        v "Can’t wait to be yelled at by the Dean."

        jump continue1


label skipped:

    show mira default at center

    show vivienne default at right

    m "Oh, I skipped. Got yelled at by the Dean earlier."

    show vivienne frown

    v "Definitely an experience, huh?"

    m "2/10. I don’t get why we’re required to go to these events."

    v  "It’s all for the school’s publicity. I’d rather hole up in my dorm and read."
    
    m "Did you?"
    
    v "Against my will, actually. I got sick with an awful cold."

    show vivienne frown

    v "Can’t wait for my turn to be yelled at by the Dean."

    jump continue1

         
label resurrected:

    show mira default at center

    show vivienne default at right

    m "Nothing, I was busy being resurrected. How do I look for a dead girl?"

    show vivienne surprised

    v "..."

    m "..."

    show vivienne frown

    v "Has anyone ever told you that they like your sense of humor?"

    m "Never."

    v "Right, that’s because they don't."

    m "...So what did you wear?"

    v "Oh, I couldn’t make it either. I got sick with an awful cold."

    show vivienne frown

    v "Can’t wait to be yelled at by the Dean."

    jump continue1


label shirtandslacks:

    show mira default at center

    show vivienne default at right

    m "I threw on an old shirt and unearthed a pair of slacks. I don’t get why we’re required to go to these events."

    show vivienne frown

    v  "It’s all for the school’s publicity. I’d rather hole up in my dorm and read."

    m "Did you?"

    v "Against my will, actually. I got sick with an awful cold."

    show vivienne frown

    v "Can’t wait to be yelled at by the Dean."

    jump continue1


label continue1:
    
    hide mira 
    hide vivienne 
    with dissolve

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

    show vivienne frown

    v "But now the Dean will think I’m making up excuses, won’t she."

    m "You seem pretty caught up in astro, too."

    v "Not quite—I haven’t finished updating my notes, I’m still confused how parallax works, I lost one of my pens, and—"

    m "Just use another one?"

    show vivienne surprised

    v "What?"

    m "To write with."

    show vivienne frown

    v "I can’t—all my notes are color-coded by historical relevance."

    m "..."

    jump continue2


label resurrected2:

    show mira sighing at center

    show vivienne surprised at right

    m "Yeah, I got resurrected from the dead and couldn’t use that as an excuse either."

    show mira default

    v "..."

    show vivienne frown

    m "..."

    v "I’m sorry to hear that…?"

    m "Eh, I’ll get over it."

    m "Being yelled at, I mean. Not being dead."

    v "Whatever bit you're doing isn't as funny as you think."

    jump continue2


label daughter:

    show mira default at center

    show vivienne frown at right

    m "Does she have no sympathy for her own daughter being sick?"

    show vivienne surprised

    v "..."

    show vivienne frown

    v "I wish our relationship wasn’t such widespread news. How do you of all people know about it?"

    hide mira
    hide vivienne
    with dissolve

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

    show vivienne frown at right

    m "Finn mentioned it to me offhandedly once."

    show vivienne default

    v "Did he also mention your pretty face?"

    show mira sighing

    m "Multiple times."

    v "He doesn’t mean it, you know. He says that to every girl who breathes."

    show mira default

    m "What a relief."

    jump continuetwo


label rumors:
    
    show mira default at center

    show vivienne frown at right

    m "It’s a remote campus. Rumors spread."

    show vivienne frown

    v "I suppose, though I could count on one hand how often I see you around campus."

    m "I’m standing in front of you right now."

    v "Yes, and I’m still not convinced it's not a sleep deprivation-induced hallucinatory effect."

    jump continueone


label me:

    show mira default at center

    show vivienne frown at right

    m "What do you mean, me of all people?"

    show vivienne frown

    v "I could count on one hand how often I see you around campus."

    m "I’m standing in front of you right now."

    v "Yes, and I’m still not convinced it's not a sleep deprivation-induced hallucinatory effect."

    jump continueone


label continueone:

    hide mira
    hide vivienne
    with dissolve

    menu: 

        "I thought you slept well last night?":
            jump lastnight

        "Say nothing":
            jump continuetwo


label lastnight:

    show mira default at center

    show vivienne frown at right

    m "I thought you got your 7 hours last night?"

    show vivienne surprised
 
    v "It stacks up."

    jump continue2


label continuetwo:

    show mira default at center

    show vivienne frown at right

    v "Anyways, no, the Dean only cares about appearances."

    v "...And the library’s 19th-century Impressionist paintings collection. So I'm still getting yelled at."

    jump continue2


label continue2:

    show mira default at center

    show vivienne surprised at right

    v "Oh—I’m running late for a meeting. See you next class?"

    show vivienne default

    m "No promises."

    play sound "audio/sfx/walk-indoors.mp3" 

    # find sfx w quicker footsteps

    show vivienne default:
        moveoffleft

    show mira surprised

    if v1_done > 1:

        m "{i}Summer and worn books again, like I expected. {/i}"

        show mira default

        m "{i}Quietly, I raise a wrist to my nose. I expect the smell of decay or saltwater, but there's neither. {/i}"

        m "{i}The dead leave no scent. {/i}"

        hide vivienne

        jump continue3

    else: 

        $ vphoto = True
        $ vupdate = 1
        $ newinfoupdate = True

        m "{i}She disappears in a swish of braids; one almost brushes my face. It smells like summer and worn books. {/i}"

        m "{i}I never noticed. {/i}"

        # is it gay to notice the way your classmate smells 
        # when you're in the middle of a death or life situation

        jump continue3


label continue3:

    $ remainingtime -=1

    hide mira
    with dissolve

    if f1_done == 0:

        menu:

            "Look for Finn":

                $ findfinn = True
                $ remainingtime -= 2  
                jump F1

            "Look for Elliot":

                $ remainingtime -= 2
                jump F1

            "Time travel":
                jump timetravel1

    else:

        menu:

            "Look for Finn":

                $ findfinn = True
                jump sceneskip1

label timetravel1:

    menu:

        "Meet Vivienne (-1 hr)":
            $ time_travel_jump("V1")

        "Never mind":
            jump continue3


label sceneskip1:
    
    menu:

        "NOTE: this scene remains unchanged. Would you like to skip the scene? (I'LL REPLACE THIS W A POPUP DW)"

        "Yes":
            $ remainingtime -= 3
            jump S1

        "No":
            $ remainingtime -= 2
            jump F1


# FINN 1 --------------------------------------

label F1:

    $ f1_done += 1

    $ flirtmeter = 0

    scene hallway
    with fade

    $ hide_menu()

    centered "{font=Marker Felt.ttf} {size=35} 12:00 pm {/size} \n {size=40} Lunch Break {/size} {/font}"

    $ show_menu()

    show mira default at left
    with dissolve

    # SFX: crowd

    if findfinn == True:

        m "{i}Everyone seems to keep track of Finn's whereabouts except for me. {/i}"

    else:

        m "{i}I couldn't find anyone who knew Elliot. But on the other hand, there's not a single person who hasn't heard of Finn.{/i}"
        
    m "{i}I asked a passing student where he was and she immediately pointed me to the northern courtyard. {/i}"

    m "{i}Elbows and backpacks ram into my side as I make my way through the academy."

    m "{i}Lunch is always a hectic time, and the hallway is a sea of blue uniforms capped with white collars. {/i}"

    # girl who spends all her time staring at the ocean: 
    # getting a lot of ocean vibes from this

    scene courtyard 
    with fade

    show mira surprised at left
    with dissolve 

    m "{i}There he is—varsity jacket and all. Surrounded by a tide pool of chattering students. {/i}"

    # girl who spends all her time staring at the ocean, again: 
    # getting a lot of ocean vibes from this

    show mira default

    m "Finn. I need to talk to you. Finn? Finn."

    show mira sighing

    m "Please don’t make me push my way through that crowd. Maybe I resign myself to being an undead servant forever—"

    show mira surprised

    f "Watch out!"

    play sound "audio/sfx/thud.mp3" volume 3

    show mira bonk

    m "—!!" with hpunch

    play sound "audio/sfx/walk-outdoors-short.mp3" volume 1.5

    show finn concerned at right
    with dissolve

    show mira default

    f "Hey, you okay?"

    show finn default

    play audio [ "<silence 1.5>", "audio/sfx/thud.mp3" ] volume 1.5

    m "{i}He picks up the ball that slammed into the side of my head and tosses it back to a student who winces in apology. {/i}"

    m "Yeah, I can’t feel pain."

    show finn flirt

    f "That’s a relief—wouldn’t wanna damage that pretty face."

    hide mira
    hide finn
    with dissolve

    menu:

        "Pretend to flirt back":
            $ flirtmeter += 1
            jump flirt

        "Stare at him unimpressed":
            $ flirtmeter += 1
            jump unimpressed

        "Reject him outright":
            jump reject


label flirt:
        
        show mira smile at left

        show mira at center:
            movecenter

        show finn flirt at right

        m "What, the one in your mirror?"

        show finn default

        f "Hahaa. Finn, by the way."

        m "Mira. And I know who you are; I see your face all over the school’s newsletters."

        f "Surely I have more redeeming qualities than my test scores?"

        jump continue7


label unimpressed:

    show mira default at left

    show finn flirt at right

    m "..."

    f  "..."

    m "Did you think that was going to work, or..."

    show finn default

    f "Just telling it like it is. Finn, by the way."

    m "Mira. And I know who you are; I see your face all over the school’s newsletters."

    f "Surely I have more redeeming qualities than my test scores?"

    jump continue7


label reject:

    show mira sighing at left

    show finn flirt at right

    m "Should’ve taken one for the team then."

    m "Actually, the school would be heartbroken if they lost you. Who else would they put on the front page of their newsletters?"

    show finn pensive

    f "Surely I have more redeeming qualities than my test scores?"

    jump continue7


label continue7:

    hide mira
    hide finn
    with dissolve

    menu: 

        "I think so" if flirtmeter >= 1:
            $ flirtmeter += 1
            jump think

        "Everyone else thinks so":
            $ flirtmeter += 1
            jump everyone

        "That's your most attractive trait":
            jump attractive


label think:

    show mira smile at left

    show finn default at right

    m "Of course. I don’t collect those newsletters to read them, you know."

    show finn default

    f "Do you cut out the pictures of me?"

    m "Yeah. I have a shrine and everything."

    show finn concerned

    f "Oh, wow. I was going to keep flirting back, but that suddenly made it weird."

    show mira default

    show finn default

    m "I wouldn’t be surprised if someone actually had a shrine."

    m "Do you know how many students were devastated when they couldn’t find you at the masquerade?"

    jump flirtcheck


label everyone:

    show mira default at left

    show finn default at right

    m "Everyone else definitely seems to think so."

    m "How do you stand being surrounded by so many people all the time?"

    f "I could ask the opposite of you."

    m "Do you know how many students were devastated when they couldn’t find you at the masquerade?"

    jump flirtcheck


label attractive:

    $ intelligence = True

    show mira default at left

    show finn default at right

    m "Nope, that’s your most attractive trait."

    if flirtmeter == 1: 

        m "Don’t underestimate the appeal of intelligence."

    show finn pensive

    f "What are you, a university recruiter?"

    if flirtmeter == 1:

        jump flirtcheck

    m "I’d be two years early."

    m "Though if anyone was going to graduate high school in half the amount of time, it would definitely be you."

    f "If that’s all—"

    show mira surprised

    m "No, wait—your redeeming quality is actually your ability to help me catch up on last week’s chemistry lectures. Please? I’m so close to failing the class."

    jump continue8


label flirtcheck:

    if intelligence == True:

        show mira default at left

        show finn pensive at right

        m "I can't be the only one who thinks so."

        m "Do you know how many students were devastated when they couldn’t find you at the masquerade?"

    if flirtmeter >= 1:

        jump devastated


label devastated:

    show mira default at left

    show finn pensive at right

    f "Ah—I was sick."

    m "..."

    f "..."

    show finn concerned

    f "...What?"

    show mira sighing

    m "Was there an outbreak of the Black Plague last week? You couldn’t think of a better excuse than Vivienne?"

    show finn default

    f "Oh, Vivi might be telling the truth. Have you seen how little that girl sleeps?"

    $ newinfoupdate = True

    f "It’s like she thinks she’s got something to prove because she’s the {color=#56768f}daughter of our Dean.{/color}"

    $ vividaughter = True
    $ vupdate = 2

    show mira default

    m "So what’s the real reason you were gone?"

    show finn flirt

    f "You’re getting ahead of yourself—I don’t tell my secrets to people who think I have no redeeming qualities."

    show mira sighing

    m "Your redeeming quality is your ability to help me catch up on last week’s chemistry lectures. Please? I’m so close to failing the class."

    jump continue8
    

label continue8:

    show mira default at left

    show finn pensive at right

    f "..."

    m "{i}There’s a moment of silence as I watch the synapses go off in his head, trying to decide how much he wants to uphold his reputation as the boy who does anything and everything. {/i}"

    show finn default

    f "Tomorrow, physical sciences lecture hall at lunch break. It’s the only time I’m free."

    $ fphoto = True
    
    if vividaughter == True: 
        $ fupdate = 2

    else:
        $ fupdate = 1

    $ newinfoupdate = True

    show mira smile

    m "See you there. Thanks, Finn."

    show finn flirt

    f "Only because you’re pretty."

    play sound "audio/sfx/walk-outdoors.mp3"

    hide finn 
    with dissolve

    m "{i}I watch as he's swallowed up by the crowd again.{/i}"

    jump continue9


label continue9:

    $ remainingtime -=1

    hide mira
    with dissolve

    if sera_day1 == True:
        jump S1

    else:

        if findfinn == True:

            menu:

                "Look for Elliot":

                    $ remainingtime -= 4
                    jump E1

                "Time travel":
                    jump timetravel2
        else:

            menu:

                "Look for Elliot again":
                    $ remainingtime -= 4
                    jump E1

                "Time travel":
                    jump timetravel2


label timetravel2:
    
    menu:

        "Meet Vivienne (-3 hrs)":
            $ time_travel_jump("V1")

        "Meet Finn (-1 hr)":
            $ time_travel_jump("F1")

        "Never mind":
            jump continue9


# ELLIOT 1 --------------------------------------

label E1:

    $ e1_done += 1

    scene hallway
    with fade

    $ hide_menu()

    centered "{font=Marker Felt.ttf} {size=35} 5:00 pm {/size} \n {size=40} After School {/size} {/font}"

    $ show_menu()

    show mira default at left
    with dissolve

    m "{i}I've spent the entire day looking for Elliot, but he's nowhere to be found.{/i}"

    m "{i}Even the few students who did know him couldn’t tell me where he was.{/i}"

    show mira sighing

    m "{i}Does this person have no friends…?{/i}"

    show resurrector thought at right
    with dissolve

    r "{i}( It's been a week, if you were wondering. And so far, no one else has noticed you're gone. ){/i}"

    hide resurrector

    m "{i}Shut up.{/i}"

    scene classroom
    with dissolve

    show mira default at left
    with dissolve

    m "...?"

    m "{i}Is that a dead beetle on the desk?{/i}"

    m "{i}Wish that were me.{/i}"

    show elliot smile at right, flip
    with dissolve

    # figure out how to fade in without disappearing dialogue box

    x "~~"

    m "{i}With agonizing slowness, the beetle rolls over and raises itself on its spindly legs. It flaps its wings, once. {/i}"

    show mira surprised

    m "{i}( !! ) {/i}"

    m "{i}( Necromancy. ) {/i}"

    show elliot default

    x "You shouldn’t spy on people, you know. It’s rude."

    m "—!!"

    show mira default

    m "...I didn’t want to interrupt what you were doing."

    show elliot smile

    x "Come on, little one."

    m "{i}He scoops the beetle into his hands. It flaps its wings again in irritation and sets off flying around the classroom. {/i}"

    show elliot default at right, reflip

    e "Elliot. Nice to meet you."

    show mira surprised

    m "I—You—Why are you resurrecting dead beetles for fun??"

    e "Hang on; before we get to that, how about you answer a question of my own?"

    show mira default 

    show elliot smile at closeleft behind mira:
        movecloseleft

    m "...?"

    show elliot default

    e "How long have you been dead?"

    show mira surprised

    m "—!!"

    m "{i}( Fuck. ) {/i}"

    hide mira
    hide elliot
    with dissolve

    menu:

        "Feign confusion":
            jump confusion

        "Deliberately misinterpret the question":
            jump misinterpret

        "Confess the truth":
            jump truth


label confusion:
    
    show mira default at left

    show elliot default at closeleft

    m "What are you talking about??"

    m "Most girls don’t take being told they resemble a rotting corpse as a compliment, you know."

    jump stabbystab


label misinterpret:

    show mira default at left

    show elliot default at closeleft

    m "Inside? About 15 years or so, now."

    m "The anniversary of my depression was just last week, actually."

    jump stabbystab


label stabbystab:

    e "..."

    show elliot stab 

    m "!!"

    m "{i}( I look down. He’s stabbed a pen into the side of my arm. ){/}"

    m "...Ow?"

    show elliot grin

    e "Can’t feel pain, huh?"

    show mira sighing

    e "I knew it. You {i}are{/i} dead."

    jump continue4


label truth:

    show mira sighing at left

    show elliot default at closeleft

    m "Less than a day."

    show elliot curious

    e "{i}Fascinating{/i}."

    jump continue4


label continue4:

    show mira default

    show elliot 

    m "{i}My hand is tight around his wrist before I realize what has happened. {/i}"

    m "Don’t tell {i}anyone. {/i}"

    show elliot default

    e "Relax, relax. Why would I do that? They’d be all over you in an instant."

    show mira sighing

    m "You’re all over me right now."

    show elliot smile at right:
        moveright

    e "Whoops."

    show mira default

    m "How did you know?"

    show elliot default

    e "Classic signs of a resurrected being. Colder air around you, inability to feel pain."

    m "{i}( So that’s how he knew I was watching him—I’m like a walking air conditioner. ) {/i}"

    m "{i}( I wonder if Vivienne or anyone else noticed.) {/i}"

    e "But what gave it away was your eyes. I couldn’t get a good look at them the last time I saw you, but now it’s obvious."

    e "They don’t reflect light at any angle."

    show mira surprised

    m "{i}( What? I can’t remember having ever talked to Elliot before this. ) {/i}"

    show mira default

    m "When...exactly did you see me?"

    e "The night of the masquerade."

    e "I was alone in the dorms because the spell I used to unwrinkle my shirt accidentally burnt a hole in my bedsheets, so I went out into the hallway to get some water."

    e "I saw you enter the building and make your way up the stairs."

    m "{i}( I did go back to the dorms after I managed to untie myself…it’s a plausible alibi. ) {/i}"

    m "{i}( But it’s also possible that he resurrected me and then went straight back, not expecting to see me come in a few hours later. ) {/i}"

    hide mira
    hide elliot
    with dissolve

    menu:

        "Ask if he saw anything else that night":
            jump whatelse

        "Question his absence further":
            jump absence

        "Tell him to use an iron like everyone else":
            jump iron


label whatelse:
    
    show mira default at left

    show elliot default at right

    m "Did you happen to see anything else that night?"

    e "There were these two girls making out in the West Hall."

    show mira sighing

    m "...Anything unusual."

    e "One of them started choking the other one halfway through."

    m "..."

    m "I’m going to take that as a no."

    show mira default

    e "If you mean anything magickal, no. I was in the dorms all night cleaning up the side effects of my spells."

    show elliot curious at center:
        movecenter

    e "Wait, why?"

    show elliot at closeleft:
        movecloseleft

    e "Did something happen?"

    show mira surprised

    m "Woah."

    show mira default

    show elliot default at right:
        moveright

    e "Sorry, sorry. I’ve been told I’m not great with personal boundaries."

    show mira sighing

    m "Why would anyone tell you that?"

    show mira default

    show elliot curious

    e "Did it have something to do with how you became undead?"

    e "Speaking of, what else can you do as a dead person? Do you need to eat or sleep? Can you die again, or are you effectively invincible now?"

    jump continue5


label absence:

    show mira default at left

    show elliot default at right

    m "You missed the masquerade because you got a small hole in your sheets?"

    e "Well no, I accidentally created an oil spill across the floor earlier and set a bird loose down the hallway."

    m "...How."

    e "Transmutation spells are hard, okay! I needed some hair grease and a few feathers for my mask last minute."

    e "On paper the equations worked perfectly fine, but in practice..."

    show mira sighing

    m "{i}( There’s no way someone can be this bad at something, even if it’s an under-studied subject. ) {/i}"

    e "Anyway, what else can you do as a dead person? Do you need to eat or sleep? Can you die again, or are you effectively invincible now?"

    jump continue5


label iron:

    show mira default at left

    show elliot default at right

    m "Have you tried just using an iron like everyone else?"

    e "If you saw a building with a stairway and a slide, would you take the stairway?"

    show mira sighing

    m "If the slide had a wildfire at the end of it, yes."

    e "You’re too boring. Plus, I don’t own an iron."

    show mira default

    m "Why do you not—"

    show mira surprised

    m "Actually, I’ve never touched an iron in my life."

    show mira default

    e "Anyway, what else can you do as a dead person? Do you need to eat or sleep? Can you die again, or are you effectively invincible now?"

    jump continue5


label continue5:

    show mira sighing

    m "I’m not your personal lab rat."

    e "When am I going to get another chance to study the effects of necromancy so directly? Can I do a few tests with you sometime?"

    e "Nothing dangerous, I promise."

    m "The hole in your bedsheets begs to differ."

    m "{i}The rest of my protest dies on my tongue, however. I need to find out if Elliot was the one who resurrected me as some sort of experiment. {/i}"

    show mira default

    m "Fine—only a few. And the second I see any fire, I’m walking out."

    show elliot grin

    e "I thought you just said you wouldn’t be my personal lab rat—"

    m "I change my mind, actually."

    show elliot default

    e "Waiit, I was kidding. Meet me tomorrow at 8. Oh, what’s your name?"

    m "Mira. Fine, sure."

    e "Okay, I should get going before they kick me out for doing magick in the classroom again."

    e "See you tomorrow, Mira!"

    play sound "audio/sfx/walk-indoors.mp3"

    show elliot at right, flip:
        moveoffright

    $ ephoto = True
    $ eupdate = 1
    $ newinfoupdate = True

    m "{i}( So it's no longer a secret. Someone else knows I'm dead now. ){/i}"

    m "{i}( But somehow, the fact of it doesn’t feel like a threat. ){/i}"

    show mira surprised

    m "{i}( It’s almost...a relief? ){/i}"

    show mira default

    m "{i}Somewhere during our conversation, the beetle has landed back on the desk. I watch for any further signs of movement, but its body is still.{/i}"

    m "{i}It’s dead once more.{/i}"

    # haha what if the bug foreshadowed her fate that'd be crazy

    jump continue6


label continue6:

    $ remainingtime -=1

    hide mira
    with dissolve

    menu:

        "Go back to the dorms and sleep":
            jump sleep1

        "Time travel":
            jump timetravel3


label timetravel3:

    menu:

        "Meet Vivienne (-2 hrs)":
            $ time_travel_jump("V1")

        "Meet Elliot (-1 hr)":
            $ time_travel_jump("E1")

        "Never mind":
            jump continue6


label sleep1:
    
    scene blackscreen
    with fade

    $ hide_menu1()

    centered "{color=#fffcf4}Oh right, I don’t need sleep anymore.{/color}"

    centered "{color=#fffcf4}I’ll go wander the hallways wailing like the ghost I’m supposed to be until someone finds a way to put me to rest permanently.{/color}"

    centered "{font=Marker Felt.ttf} {size=40} {color=#fffcf4} End of Day 1 {/size} \n {size=35} {color=#fffcf4} [remainingtime] hours remaining {/color} {/size} {/font}"

    # FIX WITH A STRING !!!

    if sera_day1 == True:
        $ remainingtime -= 14
        jump E2

    else:
        $ remainingtime -= 14
        jump S1


# $ renpy.pause()

# This ends the game.

return
