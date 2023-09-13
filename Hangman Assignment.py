#  Hangman 
# This program is a game of Hangman. 
# Includes: graphics, buttons for letters, and hints

from graphics import *
from random import randint
import time

screen = "title"
while screen == "title": # The game starts at the title screen
    while screen == "title":
        titleScreen = GraphWin("Title", 700, 600)
        background = Image(Point(350, 300), "background.gif")
        background.draw(titleScreen)
        title = Image(Point(330, 100), "Hangman.gif")
        title.draw(titleScreen)
        newGame = Image(Point(350, 300), "newGame.gif")
        newGame.draw(titleScreen)
        exitGame = Image(Point(350, 375), "exitGame.gif")
        exitGame.draw(titleScreen)
        # a bunch of graphics stuff
        while screen == "title":
            click = titleScreen.getMouse()
            if 450 >= click.getX() >= 250 and 322 >= click.getY() >= 278:
                titleScreen.close()
                topicScreen = GraphWin("Topics", 700, 600)
                screen = "topic"
                break
            #     if the user clicks new game, then the title screen is closed and the screen with topics is displayed
            elif 450 >= click.getX() >= 250 and 400 >= click.getY() >= 350:
                titleScreen.close()
                quit()
            #     if the user chooses to exit game, then the program just quits
    background = Image(Point(350, 300), "background.gif")
    background.draw(topicScreen)
    movietopic = Image(Point(350, 75), "movies.gif")
    movietopic.draw(topicScreen)
    boardGamesTopic = Image(Point(350, 230), "boardGames.gif")
    boardGamesTopic.draw(topicScreen)
    videoGamesTopic = Image(Point(350, 145), "videoGames.gif")
    videoGamesTopic.draw(topicScreen)
    miscellaneousTopic = Image(Point(350, 325), "miscellaneous.gif")
    miscellaneousTopic.draw(topicScreen)
    # these are the graphics for my topics buttons (I chose to use images for nice fonts)

    movies = ["SPIDERMAN", "SHREK", "ENDGAME", "TITANIC", "TRANSFORMERS"]
    boardGames = ["MONOPOLY", "SCRABBLE", "CHESS", "JENGA", "BATTLESHIP"]
    videoGames = ["FORTNITE", "MINECRAFT", "VALORANT", "TETRIS", "CYBERPUNK"]
    miscellaneous = ["TURTLE", "SCHOOL", "SKYSCRAPER", "WATER", "SCIENCE"]

    moviesHint = ["Tom Holland", "Side Character: Donkey", "Avengers", "We hate icebergs here", "Cool Robots"]
    boardGamesHint = ["Real Estate", "Better vocabulary means better player", "Kings and Queens", "It's Gonna Fall!!!!", "Guessing Coordinates"]
    videoGamesHint = ["Battle Royale", "Notch", "Shooting Game", "Fitting Blocks", "Keanu Reeves"]
    miscellaneousHint = ["Animal", "A Student's Curse", "Tall Buildings", "Essentials", "School Subject"]

    # stored words in lists related to the topics

    while screen == "topic":
        click = topicScreen.getMouse()
        listNum = randint(0, 4)
        chosenTopic = ""
        if 450 >= click.getX() >= 250 and 111 >= click.getY() >= 39:  # movies
            word = movies[listNum]
            screen = "game"
            chosenTopic = "movies"
        elif 538 >= click.getX() >= 162 and 265 >= click.getY() >= 195:  # board games
            word = boardGames[listNum]
            screen = "game"
            chosenTopic = "boardGames"
        elif 521 >= click.getX() >= 179 and 180 >= click.getY() >= 110:  # video games
            word = videoGames[listNum]
            screen = "game"
            chosenTopic = "videoGames"
        elif 563 >= click.getX() >= 137 and 360 >= click.getY() >= 290:  # miscellaneous
            word = miscellaneous[listNum]
            screen = "game"
            chosenTopic = "misc"
    #     waiting for the user to click on one of the topics

    topicScreen.close()
    gameScreen = GraphWin("Game Screen", 1000, 600)
    gameBackground = Image(Point(500, 300), "gameBackground.gif")
    gameBackground.draw(gameScreen)
    # when one of the topics are clicked, topic screen closes and game screen is shown.
    # I am not too familiar with lists so I literally copy and pasted for the letter buttons and changed the coordinates.
    # Sorry

    aRect = Rectangle(Point(70, 425), Point(120, 475))
    aRect.draw(gameScreen)
    a = Text(Point(95, 450), "A")
    a.draw(gameScreen)
    a.setSize(25)
    bRect = Rectangle(Point(130, 425), Point(180, 475))
    bRect.draw(gameScreen)
    b = Text(Point(155, 450), "B")
    b.draw(gameScreen)
    b.setSize(25)
    cRect = Rectangle(Point(190, 425), Point(240, 475))
    cRect.draw(gameScreen)
    c = Text(Point(215, 450), "C")
    c.draw(gameScreen)
    c.setSize(25)
    dRect = Rectangle(Point(250, 425), Point(300, 475))
    dRect.draw(gameScreen)
    d = Text(Point(275, 450), "D")
    d.draw(gameScreen)
    d.setSize(25)
    eRect = Rectangle(Point(310, 425), Point(360, 475))
    eRect.draw(gameScreen)
    e = Text(Point(335, 450), "E")
    e.draw(gameScreen)
    e.setSize(25)
    fRect = Rectangle(Point(370, 425), Point(420, 475))
    fRect.draw(gameScreen)
    f = Text(Point(395, 450), "F")
    f.draw(gameScreen)
    f.setSize(25)
    gRect = Rectangle(Point(430, 425), Point(480, 475))
    gRect.draw(gameScreen)
    g = Text(Point(455, 450), "G")
    g.draw(gameScreen)
    g.setSize(25)
    hRect = Rectangle(Point(490, 425), Point(540, 475))
    hRect.draw(gameScreen)
    h = Text(Point(515, 450), "H")
    h.draw(gameScreen)
    h.setSize(25)
    iRect = Rectangle(Point(550, 425), Point(600, 475))
    iRect.draw(gameScreen)
    iText = Text(Point(575, 450), "I")
    iText.draw(gameScreen)
    iText.setSize(25)
    jRect = Rectangle(Point(610, 425), Point(660, 475))
    jRect.draw(gameScreen)
    j = Text(Point(635, 450), "J")
    j.draw(gameScreen)
    j.setSize(25)
    kRect = Rectangle(Point(670, 425), Point(720, 475))
    kRect.draw(gameScreen)
    k = Text(Point(695, 450), "K")
    k.draw(gameScreen)
    k.setSize(25)
    lRect = Rectangle(Point(730, 425), Point(780, 475))
    lRect.draw(gameScreen)
    l = Text(Point(755, 450), "L")
    l.draw(gameScreen)
    l.setSize(25)
    mRect = Rectangle(Point(790, 425), Point(840, 475))
    mRect.draw(gameScreen)
    m = Text(Point(815, 450), "M")
    m.draw(gameScreen)
    m.setSize(25)
    nRect = Rectangle(Point(850, 425), Point(900, 475))
    nRect.draw(gameScreen)
    n = Text(Point(875, 450), "N")
    n.draw(gameScreen)
    n.setSize(25)

    oRect = Rectangle(Point(130, 485), Point(180, 535))
    oRect.draw(gameScreen)
    o = Text(Point(155, 510), "O")
    o.draw(gameScreen)
    o.setSize(25)
    pRect = Rectangle(Point(190, 485), Point(240, 535))
    pRect.draw(gameScreen)
    p = Text(Point(215, 510), "P")
    p.draw(gameScreen)
    p.setSize(25)
    qRect = Rectangle(Point(250, 485), Point(300, 535))
    qRect.draw(gameScreen)
    q = Text(Point(275, 510), "Q")
    q.draw(gameScreen)
    q.setSize(25)
    rRect = Rectangle(Point(310, 485), Point(360, 535))
    rRect.draw(gameScreen)
    r = Text(Point(335, 510), "R")
    r.draw(gameScreen)
    r.setSize(25)
    sRect = Rectangle(Point(370, 485), Point(420, 535))
    sRect.draw(gameScreen)
    s = Text(Point(395, 510), "S")
    s.draw(gameScreen)
    s.setSize(25)
    tRect = Rectangle(Point(430, 485), Point(480, 535))
    tRect.draw(gameScreen)
    t = Text(Point(455, 510), "T")
    t.draw(gameScreen)
    t.setSize(25)
    uRect = Rectangle(Point(490, 485), Point(540, 535))
    uRect.draw(gameScreen)
    u = Text(Point(515, 510), "U")
    u.draw(gameScreen)
    u.setSize(25)
    vRect = Rectangle(Point(550, 485), Point(600, 535))
    vRect.draw(gameScreen)
    v = Text(Point(575, 510), "V")
    v.draw(gameScreen)
    v.setSize(25)
    wRect = Rectangle(Point(610, 485), Point(660, 535))
    wRect.draw(gameScreen)
    w = Text(Point(635, 510), "W")
    w.draw(gameScreen)
    w.setSize(25)
    xRect = Rectangle(Point(670, 485), Point(720, 535))
    xRect.draw(gameScreen)
    x = Text(Point(695, 510), "X")
    x.draw(gameScreen)
    x.setSize(25)
    yRect = Rectangle(Point(730, 485), Point(780, 535))
    yRect.draw(gameScreen)
    y = Text(Point(755, 510), "Y")
    y.draw(gameScreen)
    y.setSize(25)
    zRect = Rectangle(Point(790, 485), Point(840, 535))
    zRect.draw(gameScreen)
    z = Text(Point(815, 510), "Z")
    z.draw(gameScreen)
    z.setSize(25)

    gallows = Image(Point(250, 250,), "gallows.gif")
    gallows.draw(gameScreen)
    newGame = Image(Point(650, 135), "newGame.gif")
    newGame.draw(gameScreen)
    exitGame = Image(Point(650, 195), "exitGame.gif")
    exitGame.draw(gameScreen)
    hint = Image(Point(650, 255), "hint.gif")
    hint.draw(gameScreen)
    hintUse = 1

    blanks = ""
    # blanks is what will appear on the game screen as text
    for i in range(0, len(word)):
        blanks = blanks + "_  "
    blanks = blanks[0:len(blanks) - 1]
    # this here makes blanks equal to the word, but with "_  " as each letter to make it not a
    # straight line

    blanksText = Text(Point(650, 350), blanks)
    blanksText.draw(gameScreen)
    blanksText.setSize(35)
    wrong = 0

    while screen == "game":
        click = gameScreen.getMouse()
        prevBlanks = blanks
        giveUp = "no"
        # I have prevBlanks to check if the user got the letter right or not
        if 750 >= click.getX() >= 550 and 157 >= click.getY() >= 113: # if user clicks on new game
            wrong = 10
            giveUp = "yes"
        elif 750 >= click.getX() >= 550 and 220 >= click.getY() >= 170: # if user wants to exit game
            quit()
        elif 280 >= click.getY() >= 230 and 697 >= click.getX() >= 603 and hintUse == 1: # if user wants hint
            hint.undraw()
            # make sure the suer doesn't have the option for hint again
            hintOutput = ""
            if chosenTopic == "movies":
                hintOutput = moviesHint[listNum]
            elif chosenTopic == "boardGames":
                hintOutput = boardGamesHint[listNum]
            elif chosenTopic == "videoGames":
                hintOutput = videoGamesHint[listNum]
            else:
                hintOutput = miscellaneousHint[listNum]
            print("Hint:", hintOutput)
            hintUse = 0
            continue

        elif 120 >= click.getX() >= 70 and 475 >= click.getY() >= 425:
            # if the user clicks on this letter, in this case, "A"
            for i in range(0, len(word)):
                if "A" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "A" + blanks[locationBlanks + 1:]
            # locationBlanks is where the letter is on the blanks variable. The index of the letter is 3x greater on
            # locationBlanks compared to it being on the actual word. Rest is all copy and paste for each individual
            # button. Again, I am sorry.
            # I will learn how to condense all this with lists because this was torture.
            blanksText.undraw()
            aRect.undraw()
            a.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 180 >= click.getX() >= 130 and 475 >= click.getY() >= 425:
            for i in range(0, len(word)):
                if "B" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "B" + blanks[locationBlanks + 1:]

            blanksText.undraw()
            bRect.undraw()
            b.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 240 >= click.getX() >= 190 and 475 >= click.getY() >= 425:
            for i in range(0, len(word)):
                if "C" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "C" + blanks[locationBlanks + 1:]

            blanksText.undraw()
            cRect.undraw()
            c.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 300 >= click.getX() >= 250 and 475 >= click.getY() >= 425:
            for i in range(0, len(word)):
                if "D" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "D" + blanks[locationBlanks + 1:]

            blanksText.undraw()
            dRect.undraw()
            d.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 360 >= click.getX() >= 310 and 475 >= click.getY() >= 425:
            for i in range(0, len(word)):
                if "E" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "E" + blanks[locationBlanks + 1:]

            blanksText.undraw()
            eRect.undraw()
            e.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 420 >= click.getX() >= 370 and 475 >= click.getY() >= 425:
            for i in range(0, len(word)):
                if "F" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "F" + blanks[locationBlanks + 1:]

            blanksText.undraw()
            fRect.undraw()
            f.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 480 >= click.getX() >= 430 and 475 >= click.getY() >= 425:
            for i in range(0, len(word)):
                if "G" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "G" + blanks[locationBlanks + 1:]

            blanksText.undraw()
            gRect.undraw()
            g.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 540 >= click.getX() >= 490 and 475 >= click.getY() >= 425:
            for i in range(0, len(word)):
                if "H" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "H" + blanks[locationBlanks + 1:]

            blanksText.undraw()
            hRect.undraw()
            h.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 600 >= click.getX() >= 550 and 475 >= click.getY() >= 425:
            for i in range(0, len(word)):
                if "I" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "I" + blanks[locationBlanks + 1:]

            blanksText.undraw()
            iRect.undraw()
            iText.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 660 >= click.getX() >= 610 and 475 >= click.getY() >= 425:
            for i in range(0, len(word)):
                if "J" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "J" + blanks[locationBlanks + 1:]

            blanksText.undraw()
            jRect.undraw()
            j.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 720 >= click.getX() >= 670 and 475 >= click.getY() >= 425:
            for i in range(0, len(word)):
                if "K" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "K" + blanks[locationBlanks + 1:]

            blanksText.undraw()
            kRect.undraw()
            k.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 780 >= click.getX() >= 730 and 475 >= click.getY() >= 425:
            for i in range(0, len(word)):
                if "L" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "L" + blanks[locationBlanks + 1:]

            blanksText.undraw()
            lRect.undraw()
            l.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 840 >= click.getX() >= 790 and 475 >= click.getY() >= 425:
            for i in range(0, len(word)):
                if "M" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "M" + blanks[locationBlanks + 1:]

            blanksText.undraw()
            mRect.undraw()
            m.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 900 >= click.getX() >= 850 and 475 >= click.getY() >= 425:
            for i in range(0, len(word)):
                if "N" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "N" + blanks[locationBlanks + 1:]

            blanksText.undraw()
            nRect.undraw()
            n.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 180 >= click.getX() >= 130 and 535 >= click.getY() >= 485:
            for i in range(0, len(word)):
                if "O" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "O" + blanks[locationBlanks + 1:]

            blanksText.undraw()
            oRect.undraw()
            o.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 240 >= click.getX() >= 190 and 535 >= click.getY() >= 485:
            for i in range(0, len(word)):
                if "P" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "P" + blanks[locationBlanks + 1:]

            blanksText.undraw()
            pRect.undraw()
            p.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 300 >= click.getX() >= 250 and 535 >= click.getY() >= 485:
            for i in range(0, len(word)):
                if "Q" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "Q" + blanks[locationBlanks + 1:]

            blanksText.undraw()
            qRect.undraw()
            q.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 360 >= click.getX() >= 310 and 535 >= click.getY() >= 485:
            for i in range(0, len(word)):
                if "R" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "R" + blanks[locationBlanks + 1:]

            blanksText.undraw()
            rRect.undraw()
            r.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 420 >= click.getX() >= 370 and 535 >= click.getY() >= 485:
            for i in range(0, len(word)):
                if "S" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "S" + blanks[locationBlanks + 1:]
            blanksText.undraw()
            sRect.undraw()
            s.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 480 >= click.getX() >= 430 and 535 >= click.getY() >= 485:
            for i in range(0, len(word)):
                if "T" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "T" + blanks[locationBlanks + 1:]
            blanksText.undraw()
            tRect.undraw()
            t.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 540 >= click.getX() >= 490 and 535 >= click.getY() >= 485:
            for i in range(0, len(word)):
                if "U" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "U" + blanks[locationBlanks + 1:]
            blanksText.undraw()
            uRect.undraw()
            u.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 600 >= click.getX() >= 550 and 535 >= click.getY() >= 485:
            for i in range(0, len(word)):
                if "V" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "V" + blanks[locationBlanks + 1:]
            blanksText.undraw()
            vRect.undraw()
            v.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 660 >= click.getX() >= 610 and 535 >= click.getY() >= 485:
            for i in range(0, len(word)):
                if "W" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "W" + blanks[locationBlanks + 1:]
            blanksText.undraw()
            wRect.undraw()
            w.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 720 >= click.getX() >= 670 and 535 >= click.getY() >= 485:
            for i in range(0, len(word)):
                if "X" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "X" + blanks[locationBlanks + 1:]
            blanksText.undraw()
            xRect.undraw()
            x.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 780 >= click.getX() >= 730 and 535 >= click.getY() >= 485:
            for i in range(0, len(word)):
                if "Y" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "Y" + blanks[locationBlanks + 1:]
            blanksText.undraw()
            yRect.undraw()
            y.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)

        elif 840 >= click.getX() >= 790 and 535 >= click.getY() >= 485:
            for i in range(0, len(word)):
                if "Z" == word[i]:
                    locationBlanks = i * 3
                    blanks = blanks[0:locationBlanks] + "Z" + blanks[locationBlanks + 1:]
            blanksText.undraw()
            zRect.undraw()
            z.undraw()
            blanksText = Text(Point(650, 350), blanks)
            blanksText.draw(gameScreen)
            blanksText.setSize(35)
        else:
            continue

        if blanks.find("_") == -1:  # if the user gets the whole word and "wins"
            time.sleep(1)
            gameScreen.close()
            winScreen = GraphWin("YOU WON!!!", 700, 600)
            winScreen.setBackground("black")
            youWin = Image(Point(325, 200), "youWin.gif")
            youWin.draw(winScreen)

            playAgain = Text(Point(350, 350), "Play Again?")
            playAgain.draw(winScreen)
            playAgain.setTextColor("white")
            playAgain.setSize(25)

            yesRect = Rectangle(Point(150, 450), Point(250, 500))
            yesRect.draw(winScreen)
            yesRect.setWidth(3)
            yesRect.setOutline("white")
            yes = Text(Point(200, 475), "Yes")
            yes.draw(winScreen)
            yes.setTextColor("white")
            yes.setSize(15)

            noRect = Rectangle(Point(550, 450), Point(450, 500))
            noRect.draw(winScreen)
            noRect.setWidth(3)
            noRect.setOutline("white")
            no = Text(Point(500, 475), "No")
            no.draw(winScreen)
            no.setTextColor("white")
            no.setSize(15)

            while True:
                click = winScreen.getMouse()
                if 550 >= click.getX() >= 450 and 500 >= click.getY() >= 450:
                    # if user clicks on no, and wants to quit game
                    quit()
                elif 250 >= click.getX() >= 150 and 500 >= click.getY() >= 450:
                    # if user wants to play again
                    screen = "title"
                    winScreen.close()
                    break
            continue  # makes sure to go back to the top bool for the program realize screen now equals to title

        if prevBlanks == blanks and giveUp == "no":
            # this is where I check if the user got the answer right or not
            wrong = wrong + 1
        if wrong == 1:
            circ = Circle(Point(310, 185), 25)
            circ.draw(gameScreen)
            circ.setWidth(3)
        elif wrong == 2:
            body = Line(Point(310, 210), Point(310, 280))
            body.draw(gameScreen)
            body.setWidth(3)
        elif wrong == 3:
            leftArm = Line(Point(310, 225), Point(290, 250))
            leftArm.draw(gameScreen)
            leftArm.setWidth(3)
        elif wrong == 4:
            rightArm = Line(Point(310, 225), Point(330, 250))
            rightArm.draw(gameScreen)
            rightArm.setWidth(3)
        elif wrong == 5:
            leftLeg = Line(Point(310, 278), Point(290, 305))
            leftLeg.draw(gameScreen)
            leftLeg.setWidth(3)
        elif wrong == 6:
            rightLeg = Line(Point(310, 278), Point(330, 305))
            rightLeg.draw(gameScreen)
            rightLeg.setWidth(3)
        elif wrong == 7:
            leftEye = Image(Point(300, 175), "eye.gif")
            leftEye.draw(gameScreen)
        elif wrong == 8:
            rightEye = Image(Point(320, 175), "eye.gif")
            rightEye.draw(gameScreen)
        elif wrong == 9:
            mouth = Line(Point(300, 190), Point(320, 190))
            mouth.draw(gameScreen)
            mouth.setWidth(2)
        elif wrong == 10:
            if giveUp == "no":
                tongue = Image(Point(310, 195), "tongue.gif")
                tongue.draw(gameScreen)
            # when the user gets 10 wrong answers, they lose. I close the game screen and bring them to a losing screen
            # where they can choose to play again or quit

            time.sleep(1)
            gameScreen.close()
            loseScreen = GraphWin("Game Over", 700, 600)
            gameOver = Image(Point(350, 300), "gameOver.gif")
            gameOver.draw(loseScreen)

            answerOutput = "The Answer was: " + word
            answer = Text(Point(350, 100), answerOutput)
            answer.draw(loseScreen)
            answer.setSize(20)
            answer.setFill("white")

            while True:
                click = loseScreen.getMouse()
                # wait for the user to play again or not
                if 350 >= click.getX() >= 240 and 519 >= click.getY() >= 459:
                    # if they want to play again, i set the screen variable back to title so every starts again
                    # at the very outside loop
                    screen = "title"
                    loseScreen.close()
                    break
                elif 463 >= click.getX() >= 388 and 519 >= click.getY() >= 459:
                    screen = "over"
                    loseScreen.close()
                    # when screen does not equal to title, game, or topic, there is nothing to run so it's all over.
                    break
titleScreen.mainloop()