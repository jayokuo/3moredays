# POSITIONING --------------------------------------

transform left:
    xalign 0.25 yalign 0.0

transform right:
    xalign 0.75 yalign 0.0

transform closeleft:
    xalign 0.35 yalign 0.0

transform farleft:
    xalign 0.1 yalign 0.0

transform moveleft:
    ease 0.5 xalign 0.25

transform moveright:
    ease 0.5 xalign 0.75

transform movecenter:
    ease 0.5 xalign 0.5

transform movecloseleft:
    ease 0.4 xalign 0.35

transform movefarleft:
    ease 0.4 xalign 0.1

transform moveoffleft:
    ease 1.0 xalign -0.5

transform moveoffright:
    ease 2 xalign 1.5

transform flip:
    xzoom -1.0

transform reflip:
    xzoom 1.0

transform kabedon:
    xalign 0.5
    ease 0.3 xalign 0.35

# TRANSITIONS --------------------------------------

define fade = Fade(0.5, 0.0, 0.5)
define fadehold = Fade(0.5, 1.0, 0.5)

# UI --------------------------------------

default pagenumber = 0
default notebook = False
default hourglass = False

# NOTEBOOK --------------------------------------

default vphoto = False
default vupdate = 0
default fphoto = False
default fupdate = 0
default ephoto = False
default eupdate = 0

# COUNTERS --------------------------------------

default remainingtime = 72
default day = 1
default flirtmeter = 0

default v1_done = 0
default e1_done = 0

# VARIABLES --------------------------------------


# look for finn instead of elliot
default findfinn = False

# tell finn that intelligence is hot
default intelligence = False

# learn that vivienne is the daughter of the dean
default vividaughter = False

# tell vivienne that finn gave you this information
default finnsnitch = False

# meet sera on day 1
default sera_day1 = False

# suggest another way to get back at Aster
default aster_revenge = False
