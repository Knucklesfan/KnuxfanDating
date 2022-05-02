# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

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
    question"no."
    discordceo "n.... no, your lord of darkness?"
    question"I said no."
    play music "audio/ofortuna.mp3"
    question"We will have this miserable platform moderate itself."
    question"the entire staff of every single server will be over the age of 40 and into 12 year olds!"
    question"everyone will be jerks to eachother and spread malware throughout the land!"
    discordceo"s- sir? have you lost your mind?"
    question"no... I'm satan"
    stop music fadeout 0.0
label intro:
    scene black
    play music "audio/boom.ogg"
    centered"{size=+50}{cps=20}{i}April 21st, 2023{/i}{/cps}{/size}"
    scene schooloutside
    show pissed
    mc"fuck"
    # This ends the game.

    return
