# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image durangspin:
    "durangospin/1.png"
    pause 0.05
    "durangospin/2.png"
    pause 0.05
    "durangospin/3.png"
    pause 0.05
    "durangospin/4.png"
    pause 0.05
    "durangospin/5.png"
    pause 0.05
    "durangospin/6.png"
    pause 0.05
    "durangospin/7.png"
    pause 0.05
    "durangospin/8.png"
    pause 0.05
    "durangospin/9.png"
    pause 0.05
    "durangospin/10.png"
    pause 0.05
    repeat

image explode:
    "explode/0.png"
    pause 0.05
    "explode/1.png"
    pause 0.05
    "explode/2.png"
    pause 0.05
    "explode/3.png"
    pause 0.05
    "explode/4.png"
    pause 0.05
    "explode/5.png"
    pause 0.05
    "explode/6.png"
    pause 0.05
    "explode/7.png"
    pause 0.05
    "explode/8.png"
    pause 0.05
    "explode/9.png"
    pause 0.05
    "explode/10.png"
    pause 0.05
    "explode/11.png"
    pause 0.05
    "explode/12.png"
    pause 0.05
    "explode/13.png"
    pause 0.05
    "explode/14.png"
    pause 0.05
    "explode/15.png"
    pause 0.05
    "explode/16.png"
    pause 0.05


define l = Character("Luke")
define k = Character("Knux")
define f = Character("Frisbee")
define d = Character("Durango")
define j = Character("Johnny")
define e = Character("Erika")
define kk = Character("Kk")
define c = Character("Connie")
define s = Character("Swinxy")
define mn = Character("Mienai")
define p = Character("Pickle")
define bus = Character("Programmer Man")
define discordceo = Character("Discord CEO")
define question = Character("????")
define mc = Character("Mi-san")
define pp = Character("Pablo Richardson")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    centered"In the beginning God created the heaven and the earth."
    centered"And the earth was without form, and void; and darkness was upon the face of the deep."
    centered"And the Spirit of God moved upon the face of the waters. And God said, Let there be light..."
    centered"...and there was light."
    scene skyscraper
    play music "audio/spring.mp3"
    "May 13, 2015: The inception of mankind."
    scene business

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show businessman1 at left
    show businessman2 at right

    # These display lines of dialogue.

    bus "Sir, we are about to make the greatest communication platform in the history of mankind!"
    bus "It will revolutionize the future of how people communicate between oneanother and bring about a new era of artistic and formal expression!"
    discordceo "Great, I, as a massive multibillionare, love helping people for free out of my sheer willpower and knowledge!"
    discordceo "But, what if I might ask, what of the moderation and team maintaining the platform?"
    bus "Why, it's great! I hired these awesome guys to moderate channels and everythin-"
    stop music fadeout 1.0
    show hiddencorden at center
    question"no."retro lounge
    discordceo "n.... no, your lord of darkness?"
    question"I said no."
    play music "audio/ofortuna.mp3"
    question"We will have this miserable platform moderate itself."
    question"the entire staff of every single server will be over the age of 40 and into 12 year olds!"
    question"everyone will be jerks to eachother and spread malware throughout the land!"
    discordceo"s- sir? have you lost your mind?"
    question"no... I'm satan"
    stop music fadeout 0.0
label intro:retro lounge
    scene black
    play sound "audio/boom.ogg"
    centered"{size=+50}{cps=20}{i}April 21st, 2023{/i}{/cps}{/size}"
    play music "audio/outside.ogg"
    scene schooloutside with fade
    show pissed  with dissolve
    mc"fuck"
    mc"im late to class"
    hide pissed
    show happyopen
    mc"OwO! Today's my first day at a new school~ It's so scary but I'm so happy to start a new life at {color=#f00}{b}{font=fonts/blood.ttf}Discord University{/font}{/b}{/color}"
    # This ends the game.
    scene classroom with fade
    play music "audio/everyday.mp3"
    show happyopen
    mc"I'm so scared for class~! I wonder what kind of wacky shenanigans are gonna happen in class!"
    show horny
    mc"I sure do hope i don't meet a very attractive man right here, right now, right in front of me standing there,"
    show hornyopen
    mc"{color=#f00}right in front of me, all for me, only for me, that i can solo out and attack AGGRESSIVELY {b}attempting to mate with said individual{/b}, i REALLY hope that doesnt happen{/color}"
    stop music
    play music "audio/helicopter.ogg"
    show durangspin at left:
        yalign -25.0
        linear 5 yalign 0.5
    $renpy.pause(5,hard=True)
    hide durangspin at left
    show explode at left:
        yalign -0.5
    show horny
    show durangosmirk at left
    play music "audio/everyday.mp3"
    d"bro"
    menu:

        "Flirt.":
            jump durangflirt

        "Ignore.":
            jump durangignore

        "Berrate.":
            jump duranganger

    return
label durangflirt:
    hide hornyopen
    show horny
    mc"holy crap thats hot"
    d"bro"
    jump durangignore
label duranganger:
    mc "What the hell was that supposed to be?"
    hide durangosmirk at left
    show durangouch at left
    d"ouch bro. that hurt."

label durangignore:
    hide horny
    show happyopen
    hide durangouch
    hide durangosmirk
    show durangosmile at left
    d"yoyoyo shhhhhhhh the teacher is coming."
    stop music
    hide happyopen
    show shocked
    play sound "audio/adminarrives.ogg"
    show teacher at right with Dissolve(5, alpha=True):
        yalign -0

    $renpy.pause(2.5,hard=False)
    hide shocked
    show pissed
    mc"dude what the HELL is that thing???"
    play music "audio/localforecast.mp3"
    pp"sit down kittens, it's time for moderation 101"
    menu:

        "Tolerate the smell":
            jump teacherending

        "Leave":
            jump duranghelp


label teacherending:

    hide pissed
    show happy
    mc"oooh, moderation? That sounds like a lot of fun!"
    d"y- you actually like this class"
    mc"Absolutely!"
    d"sorry, i'm outta here."
    hide durangosmile with dissolve
    pp"*disgustingly long burp, near throat rupturingly painful burp*"
    pp"you er ready to learn about moderation?"
    hide happy
    show shocked
    mc"Are you okay? You seem... Near cardiac arrest?"
    pp"y- yeah man, i just dont talk to women too much...?"
    hide shocked
    show horny
    menu:

        "Flirt":
            jump areushureflirtone

        "Ignore":
            jump nighttime
label areushureflirtone:
    menu:

        "Please for the love of god no":
            jump flirtyteacher

        "Ignore":
            jump nighttime

label flirtyteacher:
    show hornyopen
    mc"y'know, Mr. Pedro, your fat is kinda sexy"
    play sound heartbeat
    pp"R- really?"
    hide hornyopen
    show horny
    mc"hell yeah, and I'm sure you're REALLY attractive too underneath that beard"
    pp"I've... I've never talked to someone like you! you're like someone out of one of my favorite animes ''Revenge of the hot big boobie lady tits''"
    mc"oh yeah, well guess what..."
    hide horny
    show kink
    mc"...sex."
    stop music
    play sound heartattack
    hide teacher
    show explode at right
    hide kink
    show shocked
    mc"WHAT THE F-"
    scene bedatnight
    play music night
    mc"y'know, i'm an awful person."
    scene black
    play sound "audio/boom.ogg"
    centered"{size=+85}THE NEXT DAY{/size}"
    scene scarrryyyyending
    show durangpensive at left
    show happy at right
    mc"Hi Durango, ready for another great day of moderating?"
    d"hey uhhh not to pin a blame on you or anything, but where's the teacher and why's there a giant blood splatter across the wall where teacher normally stands?"
    mc"uhhhhhhhhhhhh"
    play sound siren
    scene black
    $renpy.pause(2.5,hard=False)
    stop sound
    scene jail
    bus"So what are you in for?"
    mc"Attempted and successful murder. You?"
    bus"Discord."
    mc"Fair enough."
    stop music
    scene black
    play music gatsu
    centered"{size=+50}{cps=20}{i}You willingly stayed with your awful teacher.{/i}{/cps}{/size}"
    centered"{size=+50}{cps=20}{i}You FLIRTED WITH HIM???{/i}{/cps}{/size}"
    centered"{size=+50}{cps=20}{i}Listen, I'm not usually a man to judge, but seriously?{/i}{/cps}{/size}"
    centered"{size=+50}{cps=20}{i}Anyways, you got convicted on Murder. You were found guilty by a jury of your ''peers'' (mostly his family members) and sentenced to death.{/i}{/cps}{/size}"
    centered"{size=+85}{cps=20}THE END.{/cps}{/size}"
    centered"{size=+20}{cps=20}(Ending: ENDINGS DONT GET MUCH WORSE THAN THIS WHAT){/cps}{/size}"
    $MainMenu(confirm=False)();







label nighttime:
    scene bedatnight
    play music night
    mc"why the hell did i stay in that class..."
    mc"Why am I here?"
    mc"...Just to suffer?"
    stop music
    scene black
    play music gatsu
    centered"{size=+50}{cps=20}{i}You willingly stayed with your awful teacher.{/i}{/cps}{/size}"
    centered"{size=+50}{cps=20}{i}You ignored his disgusting habits, and it ultimately lead you to a life of moderation.{/i}{/cps}{/size}"
    centered"{size=+50}{cps=20}{i}You gained 752lbs, and landed a high profile job maintaining and moderating pH values in sewers.{/i}{/cps}{/size}"
    centered"{size=+50}{cps=20}{i}You died at 32 of obesity and linked nuclear radiation from sewage output.{/i}{/cps}{/size}"
    centered"{size=+85}{cps=20}THE END.{/cps}{/size}"
    centered"{size=+20}{cps=20}(Ending: Literally the (second) worst ending){/cps}{/size}"
    $MainMenu(confirm=False)();


















label duranghelp:

    mc"SIR WHAT THE ACTUAL HELL IS GOING ON HERE???"
    d "shh, listen I can get us out of here. C'mon."
    stop music
    stop sound
    scene hallway
    show wtf at left
    show durangpensive at right
    d "you okay?"
    mc "barely alive, but yeah. The stinch from that man was unbearable."
