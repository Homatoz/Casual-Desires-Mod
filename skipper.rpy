label advanced_skipper:
    homa "Hello! I'm Homatoz, the creator of the mod for this wonderful game."
label skipper_yes_no:
    menu:
        homa "I noticed that you've already played this game. Want to skip what you've already read?"
        "Yeah, I want to skip a bit.":
            jump skipper_chapter_page_1
        "No, I want to start from the beginning.":
            homa "I understand perfectly well that a good game can be played from the very beginning more than once."
            jump prologue
label skipper_chapter_page_1:
    menu:
        homa "Great, choose the chapter you want to start with."
        "Chapter 1" if renpy.seen_label("chapter1"):
            $ skip_to_chapter = 1
        "Chapter 2" if renpy.seen_label("chapter2"):
            $ skip_to_chapter = 2
        "Chapter 3" if renpy.seen_label("chapter3"):
            $ skip_to_chapter = 3
        "Chapter 4" if renpy.seen_label("chapter4"):
            $ skip_to_chapter = 4
        "Chapter 5" if renpy.seen_label("chapter5"):
            $ skip_to_chapter = 5
        "Next" if renpy.seen_label("chapter6"):
            jump skipper_chapter_page_2
    jump skipper_path
label skipper_chapter_page_2:
    menu:
        homa "Great, choose the chapter you want to start with."
        "Chapter 6" if renpy.seen_label("chapter6"):
            $ skip_to_chapter = 6
        "Chapter 7" if renpy.seen_label("chapter7"):
            $ skip_to_chapter = 7
        "Chapter 8" if renpy.seen_label("chapter8"):
            $ skip_to_chapter = 8
        "Chapter 9" if renpy.seen_label("chapter9"):
            $ skip_to_chapter = 9
        "Chapter 10" if renpy.seen_label("chapter10"):
            $ skip_to_chapter = 10
        "Previous" if renpy.seen_label("chapter1"):
            jump skipper_chapter_page_1
        "Next" if renpy.seen_label("chapter11"):
            jump skipper_chapter_page_3
    jump skipper_path
label skipper_chapter_page_3:
    menu:
        homa "Great, choose the chapter you want to start with."
        "Chapter 11" if renpy.seen_label("chapter11"):
            $ skip_to_chapter = 11
        "Chapter 12" if renpy.seen_label("chapter12"):
            $ skip_to_chapter = 12
        "Chapter 13" if renpy.seen_label("chapter13"):
            $ skip_to_chapter = 13
        "Chapter 14" if renpy.seen_label("chapter14"):
            $ skip_to_chapter = 14
        "Chapter 15" if renpy.seen_label("chapter15"):
            $ skip_to_chapter = 15
        "Previous" if renpy.seen_label("chapter6"):
            jump skipper_chapter_page_2
        "Next" if renpy.seen_label("chapter16"):
            jump skipper_chapter_page_4
    jump skipper_path
label skipper_chapter_page_4:
    menu:
        homa "Great, choose the chapter you want to start with."
        "Chapter 16" if renpy.seen_label("chapter16"):
            $ skip_to_chapter = 16
        "Chapter 17" if renpy.seen_label("chapter17"):
            $ skip_to_chapter = 17
        "Chapter 18" if renpy.seen_label("chapter18"):
            $ skip_to_chapter = 18
        "Chapter 19" if renpy.seen_label("chapter19"):
            $ skip_to_chapter = 19
        "Chapter 20" if renpy.seen_label("chapter20"):
            $ skip_to_chapter = 20
        "Previous" if renpy.seen_label("chapter11"):
            jump skipper_chapter_page_3
        "Next" if renpy.seen_label("chapter21"):
            jump skipper_chapter_page_5
    jump skipper_path
label skipper_chapter_page_5:
    menu:
        homa "Great, choose the chapter you want to start with."
        "Chapter 21" if renpy.seen_label("chapter21"):
            $ skip_to_chapter = 21
        "Chapter 22" if renpy.seen_label("chapter22"):
            $ skip_to_chapter = 22
        "Chapter 23" if renpy.seen_label("chapter23"):
            $ skip_to_chapter = 23
        "Chapter 24" if renpy.seen_label("chapter24"):
            $ skip_to_chapter = 24
        "Chapter 25" if renpy.seen_label("chapter25"):
            $ skip_to_chapter = 25
        "Previous" if renpy.seen_label("chapter16"):
            jump skipper_chapter_page_4
        "Next" if renpy.seen_label("chapter26"):
            jump skipper_chapter_page_1
    jump skipper_path
label skipper_path:       
    homa "Now you must choose the path of depravity or innocence."
    homa "Path of depravity - all characters will automatically choose the option for maximum sexual interaction."
    homa "Path of innocence - [pov] will avoid sexual interaction, other characters will be given a choice."
    menu:
        homa "Which path do you want to choose - depravity or innocence?"
        "Depravity":
            $ depravity_mode = True
        "Innocence":
            $ depravity_mode = False
label skipper_lesbian:
    menu:
        homa "And finally, do you want to turn on the lesbian mode?"
        "Turn off":
            $ lesonly = False
        "Turn on":
            $ lesonly = True
label skipper_main:
    if skip_to_chapter >= 1:
        pass
    if skip_to_chapter >= 2:
        pass
    if skip_to_chapter >= 3:
        pass
    if skip_to_chapter >= 4:
        pass
    if skip_to_chapter >= 5:
        pass
    if skip_to_chapter >= 6:
        pass
    if skip_to_chapter >= 7:
        pass
    if skip_to_chapter >= 8:
        pass
    if skip_to_chapter >= 9:
        pass
    if skip_to_chapter >= 10:
        pass
    if skip_to_chapter >= 11:
        pass
    if skip_to_chapter >= 12:
        pass
    if skip_to_chapter >= 13:
        pass
    if skip_to_chapter >= 14:
        pass
    if skip_to_chapter >= 15:
        pass
    if skip_to_chapter >= 16:
        pass
    if skip_to_chapter >= 17:
        pass
    if skip_to_chapter >= 18:
        pass
    if skip_to_chapter >= 19:
        pass
    if skip_to_chapter >= 20:
        pass
    if skip_to_chapter >= 21:
        pass
    if skip_to_chapter >= 22:
        pass
    if skip_to_chapter >= 23:
        pass
    if skip_to_chapter >= 24:
        pass
    if skip_to_chapter >= 25:
        pass
    jump expression "chapter" + str(skip_to_chapter)

