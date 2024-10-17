label advanced_skipper:
    homa "[ion], sorry for this muting."
    homa "Hello! I'm Homatoz, the creator of the mod for this wonderful game."
    homa "First of all, I want to apologize for my Google Translate English. I hope you understand me."
    menu:
        homa "I would like to introduce you to an advanced skipper. Do you need a short instruction, or we will skip that too?"
        "Read":
            homa "The advanced skipper, unlike the original, allows you to go not only to the next act, but also to any chapter you have already read."
            homa "In doing so, he calculates all the sexual activity that we would have received if we had not skipped but read the chapter. Of course, with some limitations."
            homa "The calculations are influenced by the chosen path and the work of the lesbian mod."
            homa "Path of depravity - all characters will automatically choose the option for maximum sexual activity."
            homa "Path of innocence - [pov] will avoid sexual activity, other characters will be given a choice."
            homa "If the lesbian mod is enabled, scenes with girls will be selected, even if there is no sexual content."
            homa "If the lesbian mod is disabled, then preference will be given to heterosexual scenes, even if scenes with girls are more sexual."
            homa "I'm thinking about a more interactive skipper, but that's a lot more work."
            homa "Well, we're ready to skip chapters!"
        "Skip":
            pass
label skipper_check_new_game:
    if renpy.seen_label("chapter1"):
        jump skipper_yes_no
    else:
        jump skipper_unlocker
label skipper_unlocker:
    homa "It seems that this is your first time reading this novel. Then I recommend starting from the beginning and not skipping anything."
    homa "But maybe you erased your saves. Then I can help you and unlock all chapters."
    menu:
        homa "Anyway, just be honest with yourself."
        "I want to start from the beginning.":
            jump prologue
        "I want unlock all chapters":
            $ unlocked_chapter = 1
            while renpy.has_label("chapter"+str(unlocked_chapter)):
                $ renpy.mark_label_seen("chapter"+str(unlocked_chapter))
                $ unlocked_chapter += 1
            jump skipper_chapter_page_1
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
    menu:
        homa "Which path do you want to choose?"
        "Depravity":
            $ depravity_mode = True
        "Innocence":
            $ depravity_mode = False
label skipper_lesbian:
    menu:
        homa "Do you want to turn on the lesbian mode?"
        "Turn off":
            $ lesonly = False
        "Turn on":
            $ lesonly = True
label skipper_cum:
    if not lesonly:
        menu:
            homa "And finally, where will you cum?"
            "Cum inside":
                $ cum_inside = True
            "Cum outside":
                $ cum_inside = False
label skipper_main:
    if skip_to_chapter >= 1:
        # Rita teases the guys
        if not lesonly:
            if depravity_mode:
                $ boys_horny +=1
            else:
                $ inn +=1
            $ sexexp +=1

    if skip_to_chapter >= 2:
        # Rita wants to become a model
        if depravity_mode:
            $ model_motive+=1

        # Rita at the test shoot
        if depravity_mode:
            $ model_seduction +=1
        else:
            $ inn +=1

        # Rita teases the guys
        if not lesonly:
            if depravity_mode:
                $ boys_horny +=1
                $ sexexp +=1
            else:
                $ inn +=1

        # Rita's first day as a model
        if depravity_mode:
            $ model_seduction +=1
        else:
            $ inn +=1

        # A stranger is harassing Rita.
        $ sexexp +=1

    if skip_to_chapter >= 3:
        # Rita talks to a stranger on the street
        if depravity_mode:
            $ sexexp +=1
            if lesonly:
                $ c2girl_sed +=2
            else:
                $ c2boy_sed +=2
        else:
            $ inn +=1

        # Rita in the home pool
        if lesonly:
            $ inn +=1
            $ c2pervertpolice = True
        else:
            if depravity_mode:
                $ sexexp +=1
                $ c2poolex = True
                $ exh +=1
            else:
                $ inn +=1

        # Rita spies on Violet and Nick having sex
        if depravity_mode and not lesonly:
            $ c2see = True

        # Rita undresses in the laundry room
        if depravity_mode:
            $ exh +=1
            $ sexexp +=1
            if lesonly:
                $ les+=1
        else:
            $ inn +=1

        # Rita's dream about sex
        if lesonly:
            $ c2_end2 = True
            $ les+=1
        else:
            if depravity_mode:
                $ c2_end3 = True
            else:
                $ c2_end1 = True

    if skip_to_chapter >= 4:
        # Rita and Haruka talking about guys
        if not depravity_mode:
            $ inn +=1

        # Rita goes to work
        if lesonly or inn >=2:
            $ sexexp+=1
            if depravity_mode:
                $ les+=1
        else:
            if depravity_mode:
                $ sexexp+=1
                $ exh+=1

        #Rita teases the pizza delivery guy
        if not lesonly:
            if depravity_mode:
                $ c3pizza = True
                $ exh+=1
                $ sexexp+=1
            else:
                $ inn+=1

        # Rita teases the guys again and then goes to the pool
        if boys_horny >=2:
            $ sexexp +=1
            $ c3boytease = True
            $ c3pool = True
        else:
            $ c3nopool = True

        # Rita swims in a public pool
        if lesonly:
            $ les+=1
        else:
            $ het+=1

        # Nick and Violet discussing their sex life
        if depravity_mode:
            $ c3vioopenminded = True

    if skip_to_chapter >= 5:
        # Rita takes a photo for a fansite
        if depravity_mode:
            $ exh+=2
            $ c4fansitetopless=True
        else:
            $ inn+=1

        # Rita orders pizza
        $ sexexp+=1
        if lesonly:
            $ les+=1

        # Violet and Nick in a nightclub
        if lesonly or not depravity_mode:
            $ c4viostranger = True

        # Violet and Nick talking about a threesome
        if depravity_mode:
            $ c4viosharing = True
        else:
            menu:
                "(Chapter 4) Nick offers [vio] a threesome."
                "[vio] considers the idea.":
                    $ c4viosharing = True
                "[vio] gets mad at his comments.":
                    pass

        # Half-naked Rita in bed thinking about what to do
        if depravity_mode:
            $ sexexp+=1
            $ exh+=1
        else:
            $ inn+=1

        # Drunk Rita and Haruka kissing
        $ sexexp+=1

        # Rita in the shower thinking about a kiss
        if lesonly:
            $ les+=1
            $ c4kissenjoy = True
        else:
            $ het+=1

    if skip_to_chapter >= 6:
        # Rita is walking after work
        if lesonly:
            $ c5pool = True
            if depravity_mode:
                $ les+=1
                $ sexexp+=1
                $ c5leslocker = True
        else:
            $ c5outside = True
            if depravity_mode:
                $ sexexp+=1
                $ c5touch = True

        # Rita orders pizza again
        if lesonly:
            $ c5pizzagirl = True
            $ les+=1
        else:
            $ c5pizzaboy = True
            if depravity_mode:
                $ c5handjob = True
                $ rita_held_dick = True
                $ hjcount+=1
                $ sexexp+=1

        # Violet and Nick meeting another couple
        if c4viosharing:
            if depravity_mode:
                if lesonly:
                    $ c5viomff = True
                else:
                    $ c5viommf = True
            else:
                menu:
                    "(Chapter 5) [vio] and Nick meet another couple, who invite them to a swinger party."
                    "[vio] accepts their proposal.":
                        if lesonly:
                            $ c5viomff = True
                        else:
                            $ c5viommf = True
                    "[vio] politely declines.":
                        pass

        # Rita takes a picture of her breasts
        if not lesonly:
            if depravity_mode:
                $ exh+=1
                $ c5pic = True
            else:
                $ inn+=1

    if skip_to_chapter >= 7:
        # Rita takes a photo in a suit
        menu:
            "(Chapter 6) Who will [pov] send a photo in a suit to?"
            "Send it to [fr].":
                $ c6frpic = True
            "Send it to Luna.":
                $ c6lunapic = True

        # Rita decides what to do
        if lesonly:
            $ c6parkgirl = True
            $ rita_met_mia = True
        else:
            if depravity_mode:
                $ c6poolhj = True
                $ rita_held_dick = True
                $ hjcount+=1
                $ sexexp +=1

        # Rita and CJ go to the cinema
        if not lesonly:
            if depravity_mode:
                $ c6theaterhj = True
                $ rita_held_dick = True
                $ hjcount+=1
                $ sexexp +=1
                $ boys_horny +=1
            else:
                $ inn+=1

        # Rita and Josh after watching anime
        if not lesonly:
            if depravity_mode:
                $ c6joshfj = True
                $ rita_held_dick = True
                $ fjcount+=1
                $ sexexp +=1
                $ boys_horny +=1

    if skip_to_chapter >= 8:
        # Rita watches the show with Connor
        if not lesonly:
            if depravity_mode:
                $ sexexp+=1
                $ bjcount+=1
                $ c7connorbj = True
                $ rita_held_dick = True

        # Rita decides which pool to go to
        if lesonly:
            if depravity_mode:
                $ les+=1
                $ sexexp+=1
                $ c7lockerles = True
            else:
                $ inn+=1
                $ c7lockertalk = True
        else:
            if depravity_mode:
                $ bjcount+=1
                $ sexexp+=1
                $ c7poolbj = True
                $ rita_held_dick = True
            else:
                $ inn+=1
                $ c7poolinnocent = True

        # Changing clothes after work
        if lesonly:
            $ c7lunatalk=True
            $ les+=1
        else:
            $ c7lucastalk=True
            $ het+=1

        # Another swinger party of Violet and Nick
        if c5viomff or c5viommf:
            if lesonly:
                $ c7violes = True
            else:
                $ c7viommf = True

    if skip_to_chapter >= 9:
        # Violet admits that she would like to be with Rita
        if depravity_mode:
            $ c8viokiss=True
            $ les+=1
            $ sexexp+=1

        # Rita decides what to do
        if lesonly:
            $ c8mia = True
            $ rita_met_mia = True
            $ les+=1
        else:
            if depravity_mode:
                $ bjcount+=1
                $ hjcount+=1
                $ tjcount+=1
                $ sexexp+=1
                $ c8josh = True
            else:
                $ inn+=1

        # And again Rita orders pizza
        if lesonly:
            if depravity_mode:
                $ les+=1
                $ sexexp+=1
                $ c8pizzagirl = True
            else:
                $ inn+=1
        else:
            if depravity_mode:
                $ bjcount+=1
                $ sexexp+=1
                $ c8pizzaboy = True
            else:
                $ inn+=1

        # Rita visiting Haruka
        if depravity_mode:
            $ c8frkiss=True
            $ les+=1
            $ sexexp+=1

        # Rita and Luna changing clothes after work
        if depravity_mode:
            $ les+=1
            $ sexexp+=1
            $ c8lunaundress=True

        # Rita takes another photo for the fansite
        if depravity_mode:
            $ c8fansitenude=True
            $ exh+=2

    if skip_to_chapter >= 10:
        # Rita decides whether to have sex in the near future
        if depravity_mode:
            $ c9sexflag=True
            if lesonly:
                menu:
                    "(Chapter 9) Who will [pov] have sex with in the nearest future?"
                    "Luna.":
                        $ c9lunasex=True
                    "[vio].":
                        $ c9viosex=True
                    "[fr].":
                        $ c9harukasex=True
            else:
                $ c9cjflag=True
        else:
            $ c9nosex=True
            $ inn+=1

        # Rita talks to Lucas after work
        $ lucas+=1
        $ c9luctalk=True

        # Rita talks to guys on the street
        if depravity_mode and not lesonly:
            $ het+=1

        # Rita makes the final decision whether to have sex
        if c9sexflag:
            if c7lockerles:
                $ virgin=False
                call first_partner("Evelyn")
                call add_partner("Evelyn")
                $ c9evelyn_is_partner = True
                $ lesexp+=1
            $ c9hadsex=True

        # Rita fucks CJ
        if c9cjflag and c9hadsex:
            $ virgin=False
            call first_partner("CJ")
            call add_partner("Connor")
            call add_partner("Josh")
            $ scount+=2
            $ bjcount+=2
            $ hjcount+=2
            $ sexexp+=1
            $ cjhadsex=True
            menu:
                "(Chapter 9) Who will fuck [pov] first?"
                "Connor.":
                    $ c9connorfirst=True
                "Josh.":
                    $ c9joshfirst=True

        # Rita fucks Luna
        if c9lunasex and c9hadsex:
            $ virgin=False
            call first_partner("Luna")
            call add_partner("Luna")
            $ sexexp+=1
            $ les+=1
            $ lesexp+=1

        # Rita fucks Violet
        if c9viosex and c9hadsex:
            $ virgin=False
            call first_partner(vioname)
            call add_partner(vioname)
            $ sexexp+=1
            $ les+=1
            $ lesexp+=1

        # Rita fucks Haruka
        if c9harukasex and c9hadsex:
            $ virgin=False
            call first_partner(frname)
            call add_partner(frname)
            $ sexexp+=1
            $ les+=1
            $ lesexp+=1

    if skip_to_chapter >= 11:
        # Rita decides what to do in the evening
        if lesonly:
            $ c10mia = True
            $ rita_met_mia = True
            if depravity_mode:
                $ c10miacamp=True
                $ les+=1
            else:
                $ les+=1
        else:
            if depravity_mode:
                $ c10pool=True
                $ virgin=False
                call first_partner("Pool pervert")
                call add_partner("Pool pervert")
                $ sexexp+=1
                $ scount+=1
                $ hjcount+=1
                $ c10poolsex=True
            else:
                $ inn+=1

        # Rita teases Jason after photo shoot
        if not lesonly:
            if depravity_mode:
                $ c10jasontease=True
                $ rita_teased_jason = True

        # Rita meets a guy on the street
        if not lesonly:
            if depravity_mode:
                $ bjcount+=1
                $ hjcount+=1
                $ sexexp+=1
                $ c10outsidebj=True
            else:
                $ inn+=1

        # Rita is streaming
        if depravity_mode:
            $ c10stream=True
        else:
            $ inn+=1

    if skip_to_chapter >= 12:
        # Rita decides what to do on her day off
        if lesonly:
            if depravity_mode:
                $ c11les=True
                $ virgin=False
                call first_partner("Female stranger")
                $ lesexp+=1
                $ les+=1
                $ sexexp+=1
                call add_partner("Female stranger from the street")
            else:
                $ inn+=1
        else:
            if depravity_mode:
                $ c11pizzasex=True
                $ virgin=False
                call first_partner("Pizza boy")
                call add_partner("Pizza boy")
                $ sexexp+=1
                $ bjcount+=1
                $ hjcount+=1
                $ scount+=1
            else:
                $ inn+=1

        # Violet and Nick are having a fun evening
        if c5viomff or c5viommf:
            if lesonly:
                $ c11violes=True
            else:
                $ c11viommf=True

        # Shift with Luna in a cafe
        if depravity_mode:
            $ les+=1
            $ c11lunakiss=True
        else:
            $ het+=1
            $ inn+=1

        # Rita changes clothes after her shift
        if not lesonly:
            if depravity_mode:
                $ c11lucastease=True
                $ exh+=1
            else:
                $ inn+=1

        # Rita is streaming
        if c10stream==True:
            if depravity_mode:
                $ exh+=1
                $ c11adultstream=True
            else:
                $ inn+=1

    if skip_to_chapter >= 13:
        # Rita at a photo shoot
        $ c12jasontalk=True
        if not lesonly:
            if depravity_mode:
                $ c12jasonflirt=True
                $ rita_teased_jason = True

        # Rita goes camping with Mia
        if c10miacamp==True:
            if depravity_mode:
                $ virgin=False
                call first_partner("Mia")
                call add_partner("Mia")
                $ lesexp+=1
                $ les+=1
                $ sexexp+=1
                $ c12miasex=True
            else:
                $ inn+=1

        # Rita meets Connor and Josh
        if c10miacamp==False:
            if not lesonly:
                if depravity_mode:
                    $ c12connorhj=True
                    $ hjcount+=1
                    $ sexexp+=1
                    $ c12cjsex=True
                    $ virgin=False
                    call first_partner("CJ")
                    call add_partner("Connor")
                    call add_partner("Josh")
                    $ sexexp+=1
                    $ scount+=2
                    $ hjcount+=2
                    $ bjcount+=1
                    $ cjhadsex=True
                    if cum_inside:
                        $ creampiecount+=1
                else:
                    $ inn+=1

        # Rita is offered sex at the water park
        if lesonly:
            if depravity_mode:
                $ virgin=False
                call first_partner("Female stranger")
                call add_partner("Female stranger from the water park")
                $ lesexp+=1
                $ les+=1
                $ sexexp+=1
                $ c12waterparkfemale=True
            else:
                $ inn+=1
        else:
            if inn < 5:
                if depravity_mode:
                    $ bjcount+=1
                    $ sexexp+=1
                    $ c12waterparkmale=True
                else:
                    $ inn+=1

    if skip_to_chapter >= 14:
        # Rita plans to take a photo for a fansite
        if depravity_mode:
            $ exh+=1
            menu:
                "(Chapter 13) What costume does [pov] plan to wear for the fansite photo?"
                "Lingerie.":
                    $ c13lingerie=True
                "School cosplay.":
                    $ c13schooloutfit=True
                "Maid cosplay.":
                    $ c13maid=True
        else:
            $ inn+=1

        # Rita watches anal porn
        if depravity_mode:
            $ c13analyes=True
            $ analinterest+=1
        else:
            $ c13analno=True

        # Luna decides which club to join
        if depravity_mode:
            if lesonly:
                $ c13lunafemaleclub=True
            else:
                $ c13lunamaleclub=True
        else:
            menu:
                "(Chapter 13) Will Luna join the club?"
                "Luna will join the Art Society {b}(Male){/b}" if not lesonly:
                    $ c13lunamaleclub=True
                "Luna will join the Art Association {b}(Female){/b}":
                    $ c13lunafemaleclub=True
                "Luna is not interested in joining right now.":
                    $ c13lunanoclub=True

        # Rita is relaxing on the beach
        if depravity_mode:
            $ exh+=1
            if lesonly:
                $ c13femalebeach=True
            else:
                $ c13mixedbeach=True
        else:
            $ inn+=1

        # Rita invites Connor
        if not lesonly:
            if depravity_mode:
                $ c13connorseduce=True
                $ sexexp+=1
                menu:
                    "(Chapter 13) How will [pov] jerk off Connor?"
                    "Give Connor a footjob.":
                        $ fjcount+=1
                    "Use boobs.":
                        $ tjcount+=1

        # Rita goes to change clothes after her shift
        if not lesonly:
            if depravity_mode:
                $ c13lucashj=True
                $ sexexp+=1
                $ hjcount+=1
            else:
                $ inn+=1

        # Rita goes to visit Luna
        if depravity_mode:
            $ c13lunasex=True
            $ virgin=False
            call first_partner("Luna")
            call add_partner("Luna")
            $ lesexp+=1
            $ sexexp+=1
            $ les+=1
        else:
            $ het+=1

        # Rita goes to a massage parlor
        if lesonly:
            $ c13spafemale=True
        else:
            $ het+=1
            $ c13spamale=True

        # Rita's new toys
        if c13analyes:
            if depravity_mode:
                $ analinterest+=1
        if c13analno:
            if depravity_mode:
                $ sexexp+=1
                $ virgin=False
                call first_partner("Dildo")

    if skip_to_chapter >= 15:
        # Luna in the club
        if depravity_mode:
            if c13lunamaleclub:
                $ c14lunamodelm=True
            if c13lunafemaleclub:
                $ c14lunamodelf=True
        else:
            if c13lunamaleclub or c13lunafemaleclub:
                menu:
                    "(Chapter 14) Will Luna pose in her underwear?"
                    "Luna will pose.":
                        if c13lunamaleclub:
                            $ c14lunamodelm=True
                        if c13lunafemaleclub:
                            $ c14lunamodelf=True
                    "Luna will refuse.":
                        if c13lunamaleclub:
                            $ c14lunamodelcancelm=True
                        if c13lunafemaleclub:
                            $ c14lunamodelcancelf=True

        # Rita goes to the beach
        # In depravity mode, Rita was already on some nudist beach
        if depravity_mode:
            if c13femalebeach:
                $ sexexp+=1
                $ lesexp+=1
                call add_partner("Female stranger 1 from the beach")
                call add_partner("Female stranger 2 from the beach")
                $ virgin=False
                call first_partner("Beach strangers")
                $ c14beachfemalesex=True
            if c13mixedbeach:
                $ sexexp+=1
                $ bjcount+=1
                $ hjcount+=2
                $ c14beachmalesex=True
        else:
            $ inn+=1

        # Rita invites Haruka to visit
        if depravity_mode:
            $ c14harukasex=True
            $ virgin=False
            call first_partner(frname)
            call add_partner(frname)
            $ lesexp+=1
            $ sexexp+=1

        # Rita is thinking about how to spend her day off
        if depravity_mode:
            if lesonly:
                menu:
                    "(Chapter 14) What will [pov] choose for sex with [vio]?"
                    "Vaginal toys.":
                        $ c14viosexvag=True
                        $ virgin=False
                        call first_partner(vioname)
                        call add_partner(vioname)
                        $ lesexp+=1
                        $ sexexp+=1
                    "Try anal.":
                        $ c14viosexanal=True
                        $ analvirgin=False
                        $ ascount+=1
                        $ lesexp+=1
                        $ sexexp+=1
            else:
                $ boys_horny +=1
                $ c14cjsex=True
                $ cjhadsex=True
                $ sexexp+=1
                $ bjcount+=2
                $ hjcount+=2
                $ scount+=2
                $ virgin=False
                call first_partner("CJ")
                call add_partner("Connor")
                call add_partner("Josh")
                $ ascount+=2
                $ analvirgin=False
                if cum_inside:
                    $ creampiecount+=2
        else:
            $ inn+=1

    if skip_to_chapter >= 16:
        # Rita came to the hot springs
        if lesonly:
            $ c15hotspringsles=True
        else:
            $ c15hotspringsmixed=True

        # Rita chats with Jason after the photo shoot
        if not lesonly:
            if depravity_mode:
                $ c15jasontease=True
                $ rita_teased_jason = True

        # Rita wakes up at night
        if depravity_mode:
            $ exh+=1
            menu:
                "(Chapter 15) What did [pov] wear for a walk at night?"
                "Garter and stockings.":
                    $ c15parkgarter=True
                "Stickers and thong.":
                    $ c15parkpasties=True
                "Completely nude.":
                    $ c15parknude=True
                    $ exh+=1
        else:
            $ inn+=1

        # Violet in a night club
        if depravity_mode:
            if lesonly:
                $ c15violes=True
            else:
                $ c15viomale=True
        else:
            if c5viommf or c5viomff:
                menu:
                    "(Chapter 15) Who will [vio] leave the club with?"
                    "With man." if not lesonly:
                        $ c15viomale=True
                    "With woman.":
                        $ c15violes=True
                    "Just go home.":
                        pass

        # Rita invites Luna and Haruka to watch a movie
        if depravity_mode:
            $ les+=1
            menu:
                "(Chapter 15) Who will [pov] kiss first?"
                "Luna.":
                    $ lunalove+=1
                "[fr].":
                    $ harukalove+=1
            $ sexexp+=1
            $ lesexp+=1
            $ virgin=False
            call first_partner("Luna & " + frname)
            call add_partner(frname)
            call add_partner("Luna")
            $ c15girlsthreesome=True
        else:
            $ inn+=1

        # Rita came to the massage parlor again
        if lesonly:
            if depravity_mode:
                $ sexexp+=1
            else:
                $ inn+=1
        else:
            $ het+=1
            if depravity_mode:
                $ sexexp+=1
            else:
                $ inn+=1

    if skip_to_chapter >= 17:
        # Luna in the club
        if depravity_mode:
            if c14lunamodelm:
                $ c16lunamalemodel=True
            if c14lunamodelf:
                $ c16lunafemmodel=True
        else:
            if c14lunamodelm or c14lunamodelf:
                menu:
                    "(Chapter 16) Will Luna offer to pose naked?"
                    "Luna will offer to pose nude.":
                        if c14lunamodelm:
                            $ c16lunamalemodel=True
                        if c14lunamodelf:
                            $ c16lunafemmodel=True
                    "Luna will stand silently.":
                        if c14lunamodelm:
                            $ c16lunamalecancel=True
                        if c14lunamodelf:
                            $ c16lunafemcancel=True

        # Rita sends a photo
        menu:
            "(Chapter 16) Who will [pov] send a photo of herself in her new suit to?"
            "Luna.":
                $ c16textluna=True
            "[vio].":
                $ c16textvio=True
            "[fr].":
                $ c16texthar=True
            "Sara.":
                $ c16textsara=True
            "Josh.":
                $ c16textjosh=True
            "Connor.":
                $ c16textcon=True

        # Rita returns home and decides what to do
        if depravity_mode:
            $ exh+=2
            $ c16streamnude=True
        else:
            $ inn+=1

        # Rita goes to the hot springs
        if c15hotspringsmixed:
            if depravity_mode:
                $ bjcount+=1
                menu:
                    "(Chapter 16) What kind of sex would [pov] prefer with a man at the hot springs?"
                    "Vaginal":
                        if cum_inside:
                            $ creampiecount+=1
                        $ virgin=False
                        call first_partner("Hotsprings man")
                        $ sexexp+=1
                        call add_partner("Hotsprings man")
                        $ scount+=1
                        $ c16mixedvag = True
                    "Anal":
                        $ analvirgin=False
                        $ ascount+=1
                        $ sexexp+=1
                        call add_partner("Hotsprings man")
                        $ scount+=1
                        $ c16mixedanal = True
            else:
                $ inn+=1
                $ c16hotspringsmcancel=True

        # Rita shows the guys her new suit
        if not lesonly:
            if depravity_mode:
                $ exh+=1
                $ c16threeboystease=True

        # Rita makes plans for strip poker
        if depravity_mode:
            if lesonly:
                $ c16pokergirls=True
            else:
                menu:
                    "(Chapter 16) Who will [pov] invite to play poker?"
                    "Invite girls only.":
                        $ c16pokergirls=True
                    "Invite guys only.":
                        $ c16pokermale=True
                    "Invite both girls and guys.":
                        $ c16pokermix=True
        else:
            $ inn+=1

    if skip_to_chapter >= 18:
        # Rita goes to a massage parlor
        if depravity_mode and inn < 5:
            if lesonly:
                $ virgin=False
                call first_partner("Masseuse")
                call add_partner("Masseuse")
                $ lesexp+=1
                $ sexexp+=1
            else:
                $ c17spamale=True
                if cum_inside:
                    $ creampiecount+=1
                $ virgin=False
                call first_partner("Masseur")
                call add_partner("Masseur")
                $ sexexp+=1
                $ scount+=1

        # Who will Rita invite to a poker game?
        if c16pokermix:
            menu:
                "(Chapter 17) Who will [pov] invite to play poker?"
                "[vio]":
                    $ c17pokermixedvio=True
                "[fr]":
                    $ c17pokermixedharuka=True

        # Rita with Violet at the hot springs
        if lesonly or c15hotspringsles:
            if depravity_mode:
                $ c17hotspringsthreesome=True
                $ virgin=False
                call first_partner("Hotsprings girl")
                $ les+=1
                call add_partner("Hotsprings girl")
                $ lesexp+=2
                $ sexexp+=1
            else:
                $ inn+=1

        # Poker with guys
        if c16pokermale:
            $ c17pokersexboys=True
            $ virgin=False
            call first_partner("CJ & Cedrick")
            call add_partner("Connor")
            call add_partner("Josh")
            call add_partner("Cedrick")
            $ scount+=3
            $ sexexp+=3
            $ bjcount+=3
            $ hjcount+=3
            if cum_inside:
                $ creampiecount+=2
                $ ascount+=1
            $ analvirgin=False
            $ ascount+=2

        # Poker with girls
        if c16pokergirls:
            $ c17pokersexgirls=True
            $ virgin=False
            call first_partner(frname)
            call add_partner(frname)
            call add_partner(vioname)
            $ lesexp+=2
            $ sexexp+=2

        # Poker with guys and Violet
        if c17pokermixedvio:
            $ c17pokersexvio=True
            $ virgin=False
            call first_partner("Nick")
            call add_partner("Nick")
            $ scount+=1
            $ sexexp+=1
            $ bjcount+=1
            $ hjcount+=1

        # Poker with guys and Haruka
        if c17pokermixedharuka:
            $ c17pokersexhar=True
            if cum_inside:
                $ creampiecount+=1
            $ virgin=False
            call first_partner("Josh")
            call add_partner("Josh")
            $ scount+=1
            $ bjcount+=1
            $ hjcount+=1
            $ sexexp+=1

    if skip_to_chapter >= 19:
        # Rita is being harassed on the bus
        if depravity_mode:
            $ sexexp+=1
            $ c18busendure=True
        else:
            $ inn+=1

        # Luna in the club
        if depravity_mode:
            if c16lunamalemodel:
                $ c18lunasexmale=True
            if c16lunafemmodel:
                $ c18lunasexfemale=True
        else:
            if c16lunamalemodel or c16lunafemmodel:
                menu:
                    "(Chapter 18) Will Luna have sex with a fellow club member?"
                    "Luna will agree.":
                        if c16lunamalemodel:
                            $ c18lunasexmale=True
                        if c16lunafemmodel:
                            $ c18lunasexfemale=True
                    "Luna will ask to stop.":
                        pass

        # Rita and Violet talk about striptease
        if depravity_mode:
            $ c18stripperinterest=True

        # Rita and Violet in a strip club
        if depravity_mode:
            if lesonly:
                menu:
                    "(Chapter 18) Who will [pov] go and have fun with in the strip club toilet?"
                    "Fool around with girls.":
                        $ c18stripclubsexfemale=True
                        $ virgin=False
                        call first_partner("Stripclub girl")
                        call add_partner("Stripclub girl")
                        $ lesexp+=1
                        $ sexexp+=1
                    "Fool around with [vioname].":
                        $ c18stripclubsexvio=True
                        $ virgin=False
                        call first_partner(vioname)
                        call add_partner(vioname)
                        $ lesexp+=1
                        $ sexexp+=1
            else:
                $ ascount+=1
                $ c18stripclubsexmale=True
                $ virgin=False
                call first_partner("Stripclub strangers")
                call add_partner("Male stranger 1 from the stripclub")
                call add_partner("Male stranger 2 from the stripclub")
                $ bjcount+=1
                $ scount+=2
                $ sexexp+=1
        else:
            $ inn+=1

        # Rita is thinking about shooting amateur porn
        if depravity_mode:
            $ c18amateurporninterest=True

        # Rita is thinking about what kind of relationship she wants
        menu:
            "(Chapter 18) What kind of relationship does [pov] want?"
            "[pov] wants a romantic relationship.":
                $ wantromance=True
            "[pov] wants an open-relationship.":
                $ wantopenrelationship=True
            "[pov] wants to stay single.":
                $ wantsingle=True

    if skip_to_chapter >= 20:
        # Rita seduces the delivery driver
        if depravity_mode:
            $ exh+=1
            $ sexexp+=1
            if lesonly:
                $ c19deliveryles=True
                $ les+=1
            else:
                $ c19deliverymale=True
                $ hjcount+=1
        else:
            $ inn+=1

        # A subway passenger looks at the Luna's spread legs
        if depravity_mode:
            $ lunaexh+=1
        else:
            menu:
                "(Chapter 19) What does Luna feel when a subway passenger looks at her spread legs?"
                "Luna liked being looked at.":
                    $ lunaexh+=1
                "Luna became uncomfortable.":
                    $ lunainn+=1

        # Rita after the photo shoot
        if not lesonly:
            if rita_teased_jason:
                if depravity_mode:
                    $ c19jasonbj=True
                    $ bjcount+=1
                    $ sexexp+=1
                else:
                    $ inn+=1

        # Rita is looking for a site with orgies
        if depravity_mode:
            if c14beachmalesex or c14beachfemalesex:
                $ c19beachorgyinterest=True
            else:
                $ c19orgyinterest=True
        else:
            $ inn+=1

        # Rita meets Violet at the club
        if wantsingle:
            $ c19viorefuse = True
        else:
            if depravity_mode:
                if wantromance:
                    $ ritaviorelationship = True
                if wantopenrelationship:
                    $ ritavioopenrelationship = True
                call first_partner(vioname)
                $ virgin=False
                call add_partner(vioname)
                $ scount+=1
                $ lesexp+=1
            else:
                $ c19viorefuse = True

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

    homa "We've skipped everything you wanted, and now we can continue."
    jump expression "chapter" + str(skip_to_chapter)
