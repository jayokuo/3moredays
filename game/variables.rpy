# POSITIONING --------------------------------------

transform left:
    xalign 0.25 yalign 0.0

transform right:
    xalign 0.75 yalign 0.0

transform closeleft:
    xalign 0.4 yalign 0.0

transform moveleft:
    ease 0.5 xalign 0.25

transform moveright:
    ease 0.5 xalign 0.75

transform movecenter:
    ease 0.5 xalign 0.5

transform movecloseleft:
    ease 0.4 xalign 0.4

transform moveoffleft:
    ease 0.6 xalign -0.5

transform moveoffright:
    ease 2 xalign 1.5

transform flip:
    xzoom -1.0

transform reflip:
    xzoom 1.0

# TRANSITIONS --------------------------------------

define fade = Fade(0.5, 0.0, 0.5)
define fadehold = Fade(0.5, 1.0, 0.5)

# UI --------------------------------------

default pagenumber = 0
default notebook = False
default hourglass = False

# NOTEBOOK --------------------------------------

default viv = False
default vupdate = 1
default fin = False
default fupdate = 1

# COUNTERS --------------------------------------

default flirtmeter = 0
default remainingtime = 72

# INFORMATION --------------------------------------

# learn that vivienne is the daughter of the dean
default vividaughter = False

# tell vivienne that finn gave you this information
default finnsnitch = False

# look for finn instead of elliot
default findfinn = False