# DAY 2 --------------------------------------

$ day = 2


# SERAFINA 1 --------------------------------------

label S1:

    $ s1_done += 1

    scene hallway
    with fade

    if sera_day1 == True:

        $ hide_menu()

        centered "{font=Marker Felt.ttf} {size=35} 12:30 pm {/size} \n {size=40} A Deserted Hallway {/size} {/font}"

        $ show_menu()

        show mira default at left
        with dissolve

        m "{i}What now? I guess I'll look for one of the others—{/i}"

        # SFX: footsteps down a hallway

    else:

        $ remainingtime = 40

        $ hide_menu()

        centered "{font=Marker Felt.ttf} {size=35} 8:30 am {/size} \n {size=40} Before School {/size} {/font}"

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

    show serafina kabedon fierce behind mira:
        kabedon

    m "!!" with hpunch

    m "{i}The girl leans in, pushing me back against the wall. Light from the window dances across the gloss smeared on her lips.{/i}"

    x "Play along."

    m "What??"

    x "Just for a few minutes."

    show serafina flirt

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

    show serafina default behind mira:
        xalign 0.35

    m "Missed me already?"

    x "I can’t help it; it’s your fault for being so cute."

    show mira default

    m "{i}It takes an immense effort for me not to vomit on the spot.{/i}"

    m "Thanks, you have...dark eyes. And I’m drowning in them. I’m almost dead, actually."

    show serafina sigh

    x "God, you’re so bad at this."

    m "{i}I look away briefly to the other students nearby. Most of them are busy, but a few cast bored glances our way.{/i}"

    m "{i}I catch the eyes of someone with mussed blonde hair that they’d evidently dyed themselves and turn my gaze back.{/i}"
    
    m "I don’t do kissing, by the way."

    # show serafina surprised
    
    x "What? Of course not, I don’t even know you."
    
    m "Oh, can we finally stop pretending now?"

    show serafina behind mira:
        xalign 0.35
        movecenter

    m "{i}The girl takes a step back and dusts off her sleeve.{/i}"

    show serafina default
    
    s "I’m Serafina, hi. Sorry for ambushing you out of nowhere."
    
    m "Mira. So.............what was that?"

    show serafina sigh
    
    s "Ugh, I saw my ex in the hallway."

    jump continue10


label push:

    show mira surprised at farleft

    show serafina behind mira:
        xalign 0.35, movecenter

    # surprised
    
    m "Do I know you??" with vpunch

    show serafina fierce
    
    s "What? No, I said to pretend—"

    show serafina sigh
    
    s "Never mind. Sorry if I made you uncomfortable."

    show mira default
    
    m "I’m more offended you didn’t buy me dinner first."

    show serafina fierce
    
    s "I wasn’t asking you out, I said to pretend!"
    
    m "{i}I look away briefly to the other students nearby. Most of them are busy, but a few cast curious glances our way.{/i}"

    m "{i}I catch the eyes of someone with mussed blonde hair that they’d evidently dyed themselves and turn my gaze back.{/i}"
    
    m "Can I get a name, then?"

    show serafina default
    
    m "{i}The girl straightens her shirt, tugging out the wrinkles I’d left when I pushed her away.{/i}"
    
    s "I’m Serafina, hi. Sorry again for ambushing you."
    
    m "What was that about?"

    show serafina sigh
    
    s "............Ugh, I saw my ex in the hallway."

    jump continue10


label continue10:

    show mira default at farleft

    show serafina sigh at center
    
    m "..."
    
    show mira sighing

    m "Are you serious."

    show serafina fierce
    
    s "I panicked, okay!"
    
    m "You couldn’t have just ignored them instead of pinning me against the wall?"

    show serafina mad
    
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

    show serafina fierce at center

    m "Aster’s your ex?"
    
    s "....Do you know them?"
    
    m "I was looking for them at the masquerade, but they didn’t turn up the entire night."

    show serafina mad
    
    s "Of course they would choose the one event I skipped on purpose to not even show up…!"

    show serafina fierce
    
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

    show serafina default at center

    m "So you want to make your ex jealous?"
    
    s "I don’t want to make them jealous! I just...want Aster to see I don’t need them anymore."
    
    m "Mhm."
    
    m "Are you in the market for a fake girlfriend?"
    
    s "...What??"

    # show sera surprised
    
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

    show serafina default at center

    m "That’s so annoying."

    show serafina mad
    
    s "I know, right??"

    s "You don’t know how many times I had to drag them out of social situations right before someone grabbed them by the shirt."

    show serafina fierce
    
    s "Looking back, I can’t believe we used to laugh about it together."
    
    m "What? You’re the one who had to bail them out every time."

    show serafina mad
    
    s "Exactly, and they never even thanked me!"
    
    m "So, do you want to get back at your ex?"

    show serafina fierce

    # show serafina surprised
    
    s "...What are you suggesting?"

    show mira smile
    
    m "Revenge."
    
    s "..."
    
    s "Why are you offering to help me? You don’t even know Aster."

    jump continue11


label continue11:

    show mira default

    m "Maybe I think you’re cute."

    show serafina default

    if obey == True:

        s "That was my line; it won't work on me."

    else: 

        s "That was supposed to be my line; it won't work on me."
    
    m "Fine, I’m bored and I like messing with people."

    $ sphoto = True
    $ supdate = 1
    $ newinfoupdate = True

    s "......Okay, count me in."

    if aster_revenge == True:

        show mira:
            moveoffleft
            
        show serafina behind mira:
            moveoffleft

        s "Tell me more about your idea."

        jump continue12

    else:

        if sera_day1 == True:

            s "Are you free tomorrow night?"

        else: 

            s "Are you free  tonight?"
    
        m "Sure. What are we up to?"

        show mira:
            moveoffleft
            
        show serafina default behind mira:
            moveoffleft
    
        s "Revenge."

        jump continue12


label continue12:

    $ remainingtime -=1

    menu:

        "Look for Aster":

            if sera_day1 == True:
                $ remainingtime -= 1

            else: 
                $ remainingtime -= 4
            jump A1

        "Time travel":

            jump timetravel4


label timetravel4:

    if sera_day1 == True:    

        menu:

            "Meet Vivienne (-4 hrs)":
                $ time_travel_jump("V1")

            "Meet Finn (-2 hrs)":
                $ time_travel_jump("F1")

            "Meet Serafina (-1 hr)":
                $ time_travel_jump("S1")

            "Never mind":
                jump continue12

    else: 

        menu:

            "Meet Vivienne (-21 hrs)":
                $ time_travel_jump("V1")

            "Meet Finn (-19 hrs)":
                $ time_travel_jump("F1")

            "Meet Elliot (-14 hrs)":
                $ time_travel_jump("E1")

            "Meet Serafina (-1 hr)":
                $ time_travel_jump("S1")

            "Never mind":
                jump continue12


# ASTER 1 --------------------------------------

label A1:

    $ a1_done += 1

    scene classroom
    with fade

    if sera_day1 == True:

        $ hide_menu()

        centered "{font=Marker Felt.ttf} {size=35} 3:00 pm {/size} \n {size=40} Chemistry Lab {/size} {/font}"

        $ show_menu()

    else:

        $ hide_menu()

        centered "{font=Marker Felt.ttf} {size=35} 1:00 pm {/size} \n {size=40} Chemistry Lab {/size} {/font}"

        $ show_menu()


    show mira sighing at left
    with dissolve

    m "{i}( …………………Ugh. )"

    m "{i}( I can’t believe I was ambushed in the hallway by the professor and dragged into lab. ){/i}"

    m "{i}( In my defense, I forgot I had class in this area, or else I would’ve avoided it. ){/i}"

    show aster at right
    with dissolve

    x "Can I sit here? My lab partner’s gone for the day."

    show mira default

    m "{i}Oh. It’s the student who caught my eye in the hallway earlier.{/i}"

    m "I have no idea what experiment we’re even doing."

    x "Don’t worry, I got you."

    m "{i}They take the seat across from me and look down at the worksheet{/i}."

    m "{i}I watch as their hands move confidently across the table, measuring out fluids and powders.{/i}"

    x "So, are you Sera’s new girlfriend?"

    m ".....What?"

    m "I'm trying to focus on an experiment here."

    x "No you're not, I’m doing all the work."

    show mira sighing

    m "{i}I sigh. They’re not exactly wrong.{/i}"

    show mira default

    a "I’m Aster, by the way."

    m "Mira."

    a "So Mira, what’s your relationship with Sera?"

    hide mira
    hide aster 
    with dissolve

    menu:

        "We're friends":
            jump friends

        "We've been dating for a few days":
            jump dating

        "She's the love of my life":
            jump loml
        
        "Why do you care?":
            jump care


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

    a "So she did mention our relationship."

    jump continue13


label dating:

    show mira default at left

    show aster at right

    m "We’ve been dating for a few days now."

    a "Is that so? I see."

    m "Why do you care? It’s none of your business who she dates now."

    a "So she did mention our relationship."

    jump continue13


label loml:

    show mira default at left

    show aster at right

    m "She’s the love of my life."

    a "......You don’t sound very convinced about that."

    m "This is how I always sound."

    a "Right."

    m "Why are you asking in the first place? It’s none of your business who she dates now."

    a "So she did mention our relationship."

    jump continue13


label care:

    show mira default at left

    show aster at right
    
    m "Why do you care? It's none of your business."

    jump continue13


label continue13:

    a "I'm just looking out for a friend."

    m "She didn’t make it sound like you two were friends."

    a "...No, but I’d like to be. "

    a "Did Sera tell you how we broke up?"

    m "No."

    a "In the beginning, things were amazing."

    a "I know Sera probably didn’t make it sound that way, but we were spending almost all our time together between classes."

    a "We’d go to parties just to ignore everyone else and talk to each other for hours."

    m "The beaker’s about to overflow."

    a "What—? Oh whoops, help me pour some back."

    a "The thing about Sera is, she looks out for so many people."

    a "She might come off as assertive, but it doesn’t take a lot for her to see you as a friend." 

    a "There were times she’d get annoyed at me for acting inconsiderate, but for me, no one else in the room was worth talking to except her."

    m "..."

    a "The fight that ended it all was a few days before the masquerade."

    a "Some poor boy had tried to invite Sera as his date by declaring he would tailor his suit to match the color of her eyes."

    a "She turned him down of course, said she had a partner and also wasn’t interested in men. I laughed and told him he would have to show up naked."
    
    a "Immediately after he left, she dragged me under an archway and asked if I ever knew how to shut up."

    a "It wasn’t the specific comment that had upset her, I could tell. It was a continuation of all our other fights."

    a "But I had a question of my own."

    a "I asked her why she cared more about a guy who was hitting on her—and every other stranger in existence—over me."

    a "We ended up yelling at each other and causing a minor scene."

    m "No way."

    a "She told me she wanted to end the relationship, and at this point, I’d seen it coming for so long that I didn’t have to think before agreeing."

    a "Needless to say, we didn’t go to the masquerade together."

    m "{i}He picks up a bottle of powder and starts measuring it out, finished with the story.{/i}"

    m "........"

    m "It definitely sounds like—"

    hide mira
    hide aster
    with dissolve

    menu:

        "She didn't prioritize you":
            jump prioritize

        "You were unnecessarily difficult":
            jump difficult

        "You two just weren't compatible":
            jump compatible


label prioritize:

    show mira default at farleft

    show aster at right

    m "Plus, the other guy probably said the same thing to a blue-eyed girl three hours later."

    a "Maybe that’s the case. But maybe—"

    a "This is the extent of her affection towards a single person. "

    a "Can I really fault her for that?"

    m "..."

    m "Who did you end up going to the masquerade with?"

    jump continue14


label difficult:

    show mira default at farleft

    show aster at right
    
    m "Would it kill you to be more polite?"

    a "I’m severely allergic to it, actually."

    a "Rashes all down my arms. Hives swelling across my face. It’s not a pretty sight."

    a "I look much better like this."

    m "....."

    m "So who did you end up going to the masquerade with?"

    jump continue14


label compatible:

    show mira default at farleft

    show aster at right
    
    a "I don’t believe in compatibility."

    a "No one cares about it until they're in a relationship."

    a "Then they make up star signs and personality types to try and feel some sense of control over their fundamental personalities."

    a "Who worries about being compatible with their friends?"

    m "I wouldn’t know."

    m "Who did you end up going to the masquerade with?"

    jump continue14


label continue14:

    a "No one. I didn’t go."

    m "Why not?"

    $ newinfoupdate = True

    $ aupdate = 1

    a "Turns out the boy from earlier wanted revenge. He waited until I was alone in the hallway and pulled out a knife."

    $ newinfoupdate = False

    show mira surprised

    m "?!"

    m "And you didn’t use your injuries to get out of class as well?"

    a "Alright, caught. I never saw him again after that, actually."

    show mira default

    m "{i}( .......What’s wrong with this person? ){/i}"

    a "You should’ve seen your face, though."

    m "So what really happened?"

    $ newinfoupdate = True

    $ aupdate = 2

    a "Sera threatened to tell the Dean I was the one who flooded the biology lab last year if I went."

    $ newinfoupdate = False

    m "Sera didn’t go to the masquerade either."

    a "Oh, she didn’t?"

    a "But she was looking forward so much to dressing up."

    m "Maybe she would’ve gone if you’d told her you weren’t going to be there."

    $ newinfoupdate = True

    $ aupdate = 3

    a "It’s not like I planned on it—I didn’t know an aggressive crow was going to fly through my window and tear my dress shirt to pieces."

    $ newinfoupdate = False

    show mira sighing

    m "………"

    a "Or maybe it was a raven."

    m "Could you—"

    show mira default

    p "Everyone, you should now be on the final steps of the experiment. Please remember to wash all the beakers once you’re done and place them on the drying rack next to the sink."

    a "Shoot, you’ve been distracting me."

    show mira surprised

    m "Me???"

    show mira default

    a "Yes, you. We’re done with the beakers; could you wash them while I calculate the final results of the experiment?"

    m "Could you give me a straight answer first?"

    a "Ah, ah—we only have five minutes left. This is a team effort, remember?"

    show mira sighing

    m "......."

    m "{i}I scowl at the back of their head as they start writing on the worksheet and move to pick up the beakers.{/i}"

    a "Thanks, Mira. You know how to wash beakers, right?"

    m "You were more likeable when you were just doing our work and not saying anything."

    a "Eh, I’m sure you’ll figure it out. Don’t die~"

    $ aphoto = True
    $ aupdate = 4
    $ newinfoupdate = True

    show mira default

    hide aster
    with dissolve

    m "{i}I leave Aster at the table and make my way over to the crowded sink.{/i}"

    m "{i}I’m never coming to this lab again.{/i}"

    jump continue15


label continue15:

    $ remainingtime -=1

    hide mira
    with dissolve

    if sera_day1 == True:
        
        menu:

            "Look for Elliot":
                $ remainingtime -=1
                jump E1

            "Time travel":
                jump timetravel5

    else:

        menu:

            "Meet with Finn after school":
                $ remainingtime -=3
                jump F2

            "Time travel":
                jump timetravel5


label timetravel5:

    if sera_day1 == True:    

        menu:

            "Meet Vivienne (-6 hrs)":
                $ time_travel_jump("V1")

            "Meet Finn (-4 hrs)":
                $ time_travel_jump("F1")

            "Meet Serafina (-3 hrs)":
                $ time_travel_jump("S1")

            "Meet Aster (-2 hrs)":
                $ time_travel_jump("A1")

            "Never mind":
                jump continue12

    else: 

        menu:

            "Meet Vivienne (-27 hrs)":
                $ time_travel_jump("V1")

            "Meet Finn (-25 hrs)":
                $ time_travel_jump("F1")

            "Meet Elliot (-20 hrs)":
                $ time_travel_jump("E1")

            "Meet Serafina (-6 hours)":
                $ time_travel_jump("S1")

            "Meet Aster (-1 hr)":
                $ time_travel_jump("A1")

            "Never mind":
                jump continue12


label F2:

    $ f2_done += 1

    scene classroom
    with fade

    $ hide_menu()

    centered "{font=Marker Felt.ttf} {size=35} 4:55 pm {/size} \n {size=40} Physical Sciences Lecture Hall {/size} {/font}"

    $ show_menu()

    show finn default at right

    f "You’re early."

    show mira default at left
    with dissolve

    m "So are you."

    f "I’m always early."

    show finn flirt

    f "Looking forward to seeing me that much?"

    show mira sighing

    m "I’m looking forward to passing this class and not having to graduate a year late."

    show finn default

    f "As you should be."

    show mira default

    m "{i}He pulls out a chair and gestures for me to sit before taking the opposite seat. A variety of notebooks and worksheets are spread out across the table.{/i}"

    m "{i}Unlike Vivienne’s post-it-covered notebooks, Finn’s notes are simple and practical, written in dark ink.{/i}"

    f "So, what exactly are you having trouble with?"

    m "Here."

    m "{i}I open my own notebook and flip to last week’s lecture notes.{/i}"

    show mira sighing

    m "Could you explain this to me like you’re not a 50 year old man with a PhD?"

    show mira default

    m "{i}To Finn’s credit, he’s a good tutor. He breaks down the concepts easily and guides me through an example problem with precise taps of his pen against the paper.{/i}"

    m "{i}Even though I didn’t come here to learn, I find myself memorizing the knowledge anyways.{/i}"

    m "{i}But I’m having trouble fully concentrating, given the fact that none of this will matter in about [remainingtime] hours.{/i}"

    m "What was the real reason you missed the dance?"

    show finn concerned

    f "What?"

    f "Have you been listening to anything I've said in the past five minutes?"

    m "I was listening. I just wondered if I’d redeemed myself yet."

    show finn default

    f "Absolutely not. Maybe when you can finish a problem set without my help."

    show mira sighing
    
    m "{i}( Ugh. I don’t have time for this. ){/i}"

    show finn concerned

    show mira default at center:
        movecenter

    f "Hey—what are you doing?"

    m "I need another piece of scrap paper."

    f "Don’t just grab my binder like that! I’ll get one for you."

    show mira at left:
        moveleft

    m "{i}He pulls my hand away and digs around in the binder.{/i}"

    show finn frown

    m "{i}Something’s wrong. Finn’s voice is tense, the usual charismatic confidence hidden under a layer of panic.{/i}"

    show mira surprised

    m "Oww..."
    
    show finn concerned

    f "Did I hurt you?"

    f "I’m sorry, I didn’t mean to—"

    show mira default at center:
        bindergrab

    f "!!" with hpunch

    m "{i}I grab his wrist as he reaches for me and toss the binder open. Papers spill out across the desk.{/i}"

    f "Don’t—!"

    m "{i}As Finn scans the mess desperately, I follow his frantic gaze and snatch up the page it lands on.{/i}"

    m "{i}For a moment I’m disappointed; it’s just exam notes.{/i}"

    m "{i}Then I notice the neat columns of writing, numbers followed by sentences or letters from A to D, all the way down.{/i}"

    m "Ohhh."

    show finn pensive

    f "…………..."

    f "Look, I’ll help you pass the rest of your classes, whatever you want. Just don’t tell anyone, please."

    hide mira
    hide finn
    with dissolve

    menu:

        "Why are you cheating?":
            jump why

        "How long have you been doing this?":
            jump how

        "Who else knows?":
            jump whoknows


label why:

    show mira default at left
    show finn pensive at right

    m "Why are you cheating on your exams? You’re clearly intelligent."

    m "Isn’t it more effort to constantly lie than to just study and be content with above-average grades?"

    jump continue16


label how:

    show mira default at left
    show finn pensive at right

    m "How long have you been doing this?"

    m "Don’t tell me every time my professors used your work as an example, it was all copied."

    jump continue16


label whoknows:

    show mira default at left
    show finn pensive at right

    m "Who else knows you’ve been cheating on your exams?"

    m "Am I the first person to find out?"

    jump continue16


label continue16:

    f "It’s not what you think. I didn’t cheat my way to the top; that was all my own effort."

    f "But once you become the top student at Seacliff, everyone learns to have expectations of you."

    f "Someone asked me to help them review, then another student recruited me for the debate team, then professors were inviting me to attend conferences with them."

    f "And then my classes started getting harder."

    f "By the time I realized, I was already drowning."

    m "You can say no sometimes, you know."

    show finn frown

    f "……"

    m "{i}I pause. He looks so desperate, I can’t help it.{/i}"

    m "Finn, I don’t give a shit whether you're cheating or not."

    show finn concerned

    f "??"

    m "What, you think I bought the whole golden boy act? I don’t care about academics."

    m "As far as I'm concerned, you’re just another student here."

    show finn pensive

    f "You know, I envy you."

    show mira surprised

    m "What?"

    f "What is it like to have so few eyes on you? No one cares whether you succeed or fail."

    show mira default

    m "{i}( …… If you knew the truth, you wouldn't be envious of me at all. ){/i}"

    m "How do you manage to get the test answers every time?"

    f "What?"

    m "You can’t copy assignments off other students, since you’re keeping this a secret. And you haven’t been caught by anyone important enough to create consequences."

    f "….It’s only for exams, and I don’t cheat on every exam. But I’m close with a lot of the professors, and several of them leave their office doors unlocked during breaks."

    f "You’re right, though. Academic dishonesty is much more difficult as a one-man act."

    hide mira
    hide finn
    with dissolve

    menu:

        "So I'm the only one who knows?":
            jump whoknows2

        "Is that why you missed the masquerade?":
            $ finn_alibi = True
            jump reason


label whoknows2:

    show mira default at left

    show finn pensive at right

    m "So I’m the only one who knows about this?"

    f "…..No."

    show mira surprised

    f "Vivi found out one day during one of our study sessions."

    jump continue17


label reason:

    show mira default at left

    show finn pensive at right

    m "Is that why you missed the masquerade? To break into an unsuspecting professor’s office?"

    f "…… No."

    f "To be honest, I skipped the masquerade because I didn’t want to be there."

    f "I knew I would be surrounded the entire night, and for once in my life, I couldn’t find the energy to meet everyone else's expectations of me."

    f "So I didn’t go."

    show mira sighing

    m "…….You were acting so secretive just because of that??"

    show finn concerned

    f "What was I supposed to say? I wasn’t there because the thought of anyone finding out the truth made me feel like the world was ending?"

    show mira default

    m "So no one else knows?"

    show finn pensive

    show mira surprised

    f "Vivi does. She found out one day during one of our study sessions."

    jump continue17


label continue17:

    f "She’d known I was struggling to keep up with my classes for a while, so I probably should’ve guessed that she’d figure it out sooner or later."
    
    f "I know she doesn’t think she’s smart enough, but she’s way too strategic for her own good."

    f "No one else knows aside from you two."
    
    show mira default

    m "I’ll keep your secret, don’t worry. Even if I think you’re making things unnecessarily harder for yourself." 

    f "I don’t know any other way."

    f "Most people have interests they’re passionate about, ways they want to change the world. I only have things I’m good at. "

    f "I don’t know where to go after I leave Seacliff."

    m "...I don’t either."

    m "{i}( Once, the Dean tried to encourage me to find something I was interested in. She said, “Passion is what makes you feel alive.” ).{/i}"

    m "{i}( I didn’t tell her that I only felt alive when looking at the ocean. ){/i}"

    m "{i}( What is it like to have no one care whether or not you fail? ){/i}"

    m "{i}( It’s like staring into the endless crash of waves. ){/i}"

    m "Is it because we’re so remote? It feels like Seacliff is the entire world."

    show finn default

    f "It does, doesn’t it?"

    show finn pensive

    m "{i}We sit in silence for a while, both staring out the tall windows.{/i}"

    m "{i}From the second story, the ocean is visible in the distance, glittering against the uncaring sky.{/i}"

    show finn default

    f "The view here has no right to be so romantic."

    m "Definitely not."

    f "Why did they design it this way? I’m trying to focus on the lecture, not fantasize about my 80-year-old professor."

    m "For the students that come here after school, obviously."

    m "{i}A beat passes. Neither of us move towards the other.{/i}"

    show finn pensive

    f "If I liked girls, I’d ask you out."

    m "If you did, I'd turn you down."

    $ newinfoupdate = True

    if finn_alibi == True:

        $ fupdate = 4

    else:

        $ fupdate = 3

    show finn default

    m "{i}At that, Finn's face splits into a smile, brighter and more genuine than any I've seen on him before.{/i}"

    show mira smile

    f "Glad we cleared that up."

    jump continue18


label continue18:
    
    $ remainingtime -= 2

    hide mira
    hide finn
    with dissolve

    menu:

        "Meet up with Sera":
            $ remainingtime -= 3
            jump SA2

        "Time travel":
            jump timetravel6



label timetravel6:

    if sera_day1 == True:    

        menu:

            "Meet Vivienne (-31 hrs)":
                $ time_travel_jump("V1")

            "Meet Finn (-29 hrs)":
                $ time_travel_jump("F1")

            "Meet Serafina (-28 hrs)":
                $ time_travel_jump("S1")

            "Meet Aster (-26 hrs)":
                $ time_travel_jump("A1")

            "Meet Elliot (-24 hrs)":
                $ time_travel_jump("E1")

            "Take Elliot's tests (-11 hrs)":
                $ time_travel_jump("E2")

            "Talk to Vivienne (-7 hrs)":
                $ time_travel_jump("V2")

            "Study with Finn (-2 hrs)":
                $ time_travel_jump("F2")

            "Never mind":
                jump continue18

    else: 

        menu:

            "Meet Vivienne (-31 hrs)":
                $ time_travel_jump("V1")

            "Meet Finn (-29 hrs)":
                $ time_travel_jump("F1")

            "Meet Elliot (-24 hrs)":
                $ time_travel_jump("E1")

            "Meet Serafina (-11 hours)":
                $ time_travel_jump("S1")

            "Meet Aster (-6 hrs)":
                $ time_travel_jump("A1")

            "Study with Finn (-2 hours)":
                $ time_travel_jump("F2")

            "Never mind":
                jump continue18


label SA2:

    $ sa2_done += 1

    scene hallway
    with fade

    $ hide_menu()

    centered "{font=Marker Felt.ttf} {size=35} 10:00 pm {/size} \n {size=40} Aster's Dorm {/size} {/font}"

    $ show_menu()

    "scene WIP"

    jump continue_infinite


label continue_infinite:

    $ remainingtime -= 2

    menu:

        "Go to sleep":
            jump sleep2

        "Time travel":
            jump timetravel7


label timetravel7:

    if sera_day1 == True:    

        menu:

            "Meet Vivienne (-36 hrs)":
                $ time_travel_jump("V1")

            "Meet Finn (-34 hrs)":
                $ time_travel_jump("F1")

            "Meet Serafina (-33 hrs)":
                $ time_travel_jump("S1")

            "Meet Aster (-31 hrs)":
                $ time_travel_jump("A1")

            "Meet Elliot (-29 hrs)":
                $ time_travel_jump("E1")

            "Take Elliot's tests (-16 hrs)":
                $ time_travel_jump("E2")

            "Talk to Vivienne again (-12 hrs)":
                $ time_travel_jump("V2")

            "Study with Finn (-7 hrs)":
                $ time_travel_jump("F2")

            "Break into Aster's dorm (-2 hrs)":
                $ time_travel_jump("SA2")

            "Never mind":
                jump continue_infinite

    else: 

        menu:

            "Meet Vivienne (-36 hrs)":
                $ time_travel_jump("V1")

            "Meet Finn (-34 hrs)":
                $ time_travel_jump("F1")

            "Meet Elliot (-29 hrs)":
                $ time_travel_jump("E1")

            "Meet Serafina (-16 hours)":
                $ time_travel_jump("S1")

            "Meet Aster (-11 hrs)":
                $ time_travel_jump("A1")

            "Study with Finn (-7 hours)":
                $ time_travel_jump("F2")

            "Break into Aster's dorm (-2 hrs)":
                $ time_travel_jump("SA2")

            "Never mind":
                jump continue_infinite


label sleep2:

    scene blackscreen
    with fade

    $ hide_menu1()

    centered "{color=#fffcf4}Dialogue WIP.{/color}"

    centered "{font=Marker Felt.ttf} {size=40} {color=#fffcf4} End of Day 2 {/size} \n {size=35} {color=#fffcf4} [remainingtime] hours remaining {/color} {/size} {/font}"

    if sera_day1 == True:
        $ remainingtime -= 7
        jump E1

    else:
        $ remainingtime -= 7
        jump V2


# "GAME ENDS HERE. PROGRESSING WILL RETURN YOU TO THE START MENU."



