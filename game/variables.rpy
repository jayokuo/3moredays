# POSITIONING --------------------------------------

transform left:
    xalign 0.25 yalign 0.0

transform right:
    xalign 0.75 yalign 0.0

transform closeleft:
    xalign 0.35 yalign 0.0

transform farleft:
    xalign 0.1 yalign 0.0

transform closeright:
    xalign 0.45 yalign 0.0

transform moveleft:
    ease 0.5 xalign 0.25

transform moveright:
    ease 0.5 xalign 0.75

transform movecenter:
    ease 0.5 xalign 0.5

transform movecloseleft:
    ease 0.4 xalign 0.35

transform movecloseleft2:
    ease 0.2 xalign 0.43

transform movecloseleft3:
    ease 0.3 xalign 0.45

transform movefarleft:
    ease 0.4 xalign 0.1

transform movecloseright:
    ease 0.5 xalign 0.45

transform moveoffleft:
    ease 1.0 xalign -0.55

transform moveoffright:
    ease 2 xalign 1.5

transform flip:
    xzoom -1.0

transform reflip:
    xzoom 1.0

transform kabedon:
    xalign 0.5
    ease 0.3 xalign 0.32

transform bindergrab:
    ease 0.3 xalign 0.5

# TRANSITIONS --------------------------------------

define fade = Fade(0.5, 0.0, 0.5)
define fadehold = Fade(0.5, 1.0, 0.5)

# UI --------------------------------------

default pagenumber = 0
default notebook = False
default hourglass = False
default choiceLeftToggle = False 

# NOTEBOOK --------------------------------------

default vphoto = False
default vupdate = 0
default fphoto = False
default fupdate = 0
default ephoto = False
default eupdate = 0
default sphoto = False
default supdate = 0
default aphoto = False
default aupdate = 0

default newinfoupdate = False

# COUNTERS --------------------------------------

default remainingtime = 72
default day = 2

default v1_done = 0
default e1_done = 0
default f1_done = 0
default s1_done = 0
default a1_done = 0

default v2_done = 0
default e2_done = 0
default f2_done = 0
default sa2_done = 0

default hourglass_string = ""

# VARIABLES --------------------------------------

# look for finn instead of elliot
default findfinn = False

# flirt with finn
default flirtmeter = 0

# tell finn that intelligence is hot
default intelligence = False

# learn that vivienne is the daughter of the dean
default vividaughter = False

# tell vivienne that finn gave you this information
default finnsnitch = False

# meet sera on day 1
default sera_day1 = False

# do as sera says
default obey = False

# push sera off
default push = False

# ask sera more about aster
default annoysera = False

# suggest another way to get back at Aster
default aster_revenge = False

# finally learn finn's alibi
default finn_alibi = False

# choose a test with elliot
default test = 0

# learn that finn was seen around aster's floor
default susfinn = False

# time travel back early to confront Finn about the missing page
default ttearly = False

# discover a missing page in Elliot's book
default missing_page = False