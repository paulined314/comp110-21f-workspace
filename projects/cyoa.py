"""Dating the lovely boys at UNC."""

__author__ = "730390549"
from random import randint
NAMED_CONSTANT: str = '\u2764\uFE0F'
player: str = input("What is your name? ")
points: int = 0


def greet() -> None:
    """Greetings."""
    player = input("What is your name? ")
    print(f"Greetings {player}!")
    print("Welcome to the UNC Dating Sim")
    print("You will be playing as a UNC student, trying to survive your first of college. From staying up all night to finish assignments to going on your first date at Spicy 9, you'll get to meet the very special boys UNC has to offer.")
    return None


def frat() -> None:
    """Frat boy."""
    points = 0
    print("Story: It's a Saturday night and your roomate talks you into coming with her to a frat party. (Imagine that this is pre-Covid because you totally wouldn't go to a party during the panorama right?)")
    print("Hi my name is Chet. I'm in Alpha Beta Delta. ")
    player = input("What is your name? ")
    print(f"Chet: It's nice to meet you {player}.")
    print(f"{player}: Hi.")
    print("Daniel: Do you usually come to these parties?")
    print("1. Yeah, all the time.")
    print("2. No, not really.")
    a: int = randint(1, 2)
    print(a)
    if a == 1:
        print("Chet: Well then, I'd love to get to know you if I'm going to be seeing you all the time.")
        print("1. Sure!")
        print("2. No thanks.")
        a_1 = int(input("CHOOSE AN OPTION. "))
        if a_1 == 1:
            print("Chet: Great. Then I'll see you Friday night at La Res.")
            points = 20
        else:
            print("Game Over")
            print(f"Points: {points}")
            return None
    else:
        print("Chet: That's too bad. I really wish I could see you more. Could I take you out sometime? Say Friday nigth at La Res?")
        print("1. Yeah, I'd like that.")
        print("2. Sorry, I'm not really interested.")
        a_2 = int(input("CHOOSE AN OPTION. "))
        if a_2 == 1:
            print("Chet: Great. Then I'll see you Friday night at La Res.")
            points = 20
        else:
            return None
    if points >= 10:
        print("Story: Friday night comes around and you've arrived at La Res. Chet has just walked up.")
        print(f"Chet: Hey {player}")
        print("You look nice.")
        print("1. Thanks, you too.")
        print("2. I always look nice")
        b = int(input("CHOOSE AN OPTION. "))
        if b == 1:
            points = points + 10
        print("Chet: Shall we head inside?")
        print("Story: You two head inside and are seated. After looking over the menu, Chet orders the Grilled Hanger Steak. You order the...")
        print("1. Seared Salmon.")
        print("2. La Rez Burger")
        print("3. Spagetti Alla Gricia")
        input("CHOOSE AN OPTION. ")
        points = points + 10
        major = input("Chet: So what's your major? ")
        print(f"Wow, {major} is interesting. Don't you have to take COMP 110 for that?")
        print("1. Yeah. I'm taking it with Kris Jordan. He's great.")
        print("2. No. I hate COMP 110 and the professor sucks")
        c = int(input("CHOOSE AN OPTION"))
        if c == 1:
            points = points + 10
        else:
            points = points - 10
        print("Story: Your food arrives and it is delicious.")
        print("You: So what do you like to do in your free time?")
        print("Chet: I don't have a lot of free time. But when I do, my frat is usually having some sort of event. I guess in my down time I like to golf or go boating.")
        print("1. Wow that sounds fun.")
        print("2. Ew, that sounds lame.")
        d = int(input("CHOOSE AN OPTION"))
        if d == 1:
            points = points + 10
        else:
            points = points - 10
        print("Chet: What about you? What do you like to do in your free time?")
        hobby = input("ENTER A HOBBY: ")
        print(f"Chet: Wow, thats cool. I don't know many people who like {hobby}")
        print("Chet: Hey my frat is hosting a party next week. Do you want to possible be my date?")
        print("1. I'd love to.")
        print("2. No, I think I'll pass.")
        e = int(input("CHOOSE AN OPTION"))
        if e == 1:
            points = points + 10
            print("Cool. I'm looking foward to it.")
        else:
            points = points - 10
            print("Oh. That's too bad.")
    print(f"Story: {player} and Chet have finished their food. Chet picks up the check to pay. You argue that you can pay, but he insists. He gives you a ride home and with that, your date has concluded.")
    print(f"Points: {points}")
    if points >= 50:
        print("Congratualtions! Your date with Chet was a success and you two are now dating! Your future is full of parties and lake trips. You can definitely say you've been living up the college party scene, although you probably won't want to tell that to your parents.")
        print(NAMED_CONSTANT)
        print("Do you want to play again?")
        print("1. Yes")
        print("2. No")
        gm = int(input("CHOOSE AN OPTION. "))
        if gm == 2:
            print("Thank you for playing.")
            return None
    else:
        print("Unfortunately, Chet's frat got invovled in a huge scandal that invovled a hazing going very badly. Chet and everyone in his frat were arrested but will probably post bail. Either way, you decided that you two really just did not click.")
        print("Do you want to play again?")
        print("1. Yes")
        print("2. No")
        gm = int(input("CHOOSE AN OPTION. "))
        if gm == 2:
            print("Thank you for playing.")
            return None


def snake() -> None:
    """Snake."""
    points = 0
    print("Story: It's the first day of your ECON 101 class. You're sitting next to an attractive boy with short blond hair and hazel eyes that seemed to be capturing your attention more than the lecture ever could. He noticed you stealing glaces at him.")
    print("Hi my name is Jayden. What's your name?")
    player = input("What is your name? ")
    print(f"Jayden: It's nice to meet you {player}.")
    print(f"{player}: Hi.")
    print("Jayden: Do you usually stare at other students during class?")
    print("1. Yeah, all the time.")
    print("2. No, not really.")
    print("3. Depends. Are you usually here?")
    a = int(input("CHOOSE AN OPTION. "))
    points = points + 10
    if a == 1:
        points = points + 10
        print("Jayden: Aw, here I was feeling special. Too bad, I would have asked you to TOPO if I was.")
        print("1. Hey, you're the one who said you weren't special.")
        print("2. Yeah, too bad.")
        a_1 = int(input("CHOOSE AN OPTION. "))
        if a_1 == 1:
            print("Jayden: Well then, I guess you and I will be meeting at TOPO firday night.")
            points = 20
        else:
            print("Game Over")
            print(f"Points: {points}")
            print("Do you want to play again?")
            print("1. Yes")
            print("2. No")
            gm = int(input("CHOOSE AN OPTION. "))
            if gm == 2:
                print("Thank you for playing.")
                return None
    else:
        if a == 2:
            points = 20
            print("Jayden: Well if you enjoy stealing glances at me during class, would you like to be stealing glaces at me over dinner? Maybe Friday night at TOPO?")
            print("1. Yeah, I'd like that.")
            print("2. Sorry, I'm not really interested.")
            a_2 = int(input("CHOOSE AN OPTION. "))
            if a_2 == 1:
                print("Jayden: Great. Then I'll see you Friday night at TOPO.")
                points = 20
            else:
                print("Game Over")
                print(f"Points: {points}")
                print("Do you want to play again?")
                print("1. Yes")
                print("2. No")
                gm = int(input("CHOOSE AN OPTION. "))
                if gm == 2:
                    print("Thank you for playing.")
                    return None
        else: 
            if a == 3:
                points == points + 10
                print("Jayden: Sure, but I'd hate for you to fail ECON because I keep stealing your attention away from our dear professor. How about focusing now and Friday night I get your full attention over dinner at TOPO?")
                print("1. Sounds good to me.")
                print("2. No thanks.")
                a_3 = int(input("CHOOSE AN OPTION. "))
                if a_3 == 1:
                    print("Jayden: Great. Then I'll see you Friday night at TOPO.")
                    points = 20
                else:
                    print("Game Over")
                    print(f"Points: {points}")
                    print("Do you want to play again?")
                    print("1. Yes")
                    print("2. No")
                    gm = int(input("CHOOSE AN OPTION. "))
                    if gm == 2:
                        print("Thank you for playing.")
                        return None
    if points >= 20:
        print("Story: Friday night comes around and you've arrived at TOPO. Jayden has just walked up.")
        print(f"Jayden: Hey {player}")
        print("You look nice.")
        print("1. Thanks, you too.")
        print("2. I always look nice")
        b = int(input("CHOOSE AN OPTION. "))
        if b == 1:
            points = points + 10
        print("Jayden: Shall we head inside?")
        print("Story: You two head inside and are seated. After looking over the menu, Chet orders the New York Strip Steak. You order the...")
        print("1. Southwest Chicken Pasta.")
        print("2. Top Burger")
        print("3. Quinao Bowl")
        input("CHOOSE AN OPTION. ")
        points = points + 10
        print(f"{player}: So what are your plans after college?")
        print("Personally, I plan on working on Wall Street after college or be the CEO of my own small business.")
        print("Jayden: So what are your plans after college?")
        print("1. Yeah. I also have  very lucrative job prospects for my major after college.")
        print("2. Wow, I don't really know where my major is going to take me.")
        c = int(input("CHOOSE AN OPTION"))
        if c == 1:
            points = points + 10
        else:
            points = points - 10
        print("Story: Your food arrives and it is delicious.")
        print("You: So is there anywhere you want to work in particular?")
        print("Jayden: Well besides Wallstreet, somewhere international could be fun. There is a lot of money in international trade.")
        print("1. Wow that sounds fun.")
        print("2. You know, not everything has to be about the money.")
        d = int(input("CHOOSE AN OPTION"))
        if d == 1:
            points = points + 10
        else:
            points = points - 10
        print("Jayden: Why would you like to live after college?")
        print("1. A booming city with lots of economic opportunity.")
        print("2. A smaller place that has its own charm and beauty.")
        e = int(input("CHOOSE AN OPTION"))
        if e == 1:
            points = points + 10
            print("Yeah, I'd like to live in a city too.")
        else:
            points = points - 10
            print("Oh. That's too bad.")
    print(f"Story: {player} and Jayden have finished their food. You wonder if you really just had an entire date talking about after college.")
    print(f"Points: {points}")
    if points >= 50:
        print("Congratualtions! Your date with Jayden was a success and you two are now dating! You two become business tycoon that can't be stopped. He even becomes a shark on Shark Tank at some point in his career.")
        print(NAMED_CONSTANT)
        print("Do you want to play again?")
        print("1. Yes")
        print("2. No")
        gm = int(input("CHOOSE AN OPTION. "))
        if gm == 2:
            print("Thank you for playing.")
            return None
    else:
        print("Unfortunately, Jayden projected your future retirement and broke things off because you didn't match his stock portfolio")
        print("Do you want to play again?")
        print("1. Yes")
        print("2. No")
        gm = int(input("CHOOSE AN OPTION. "))
        if gm == 2:
            print("Thank you for playing.")
            return None


def premed() -> None:
    """Pre Med."""
    points = 0
    print("Story: It's the first day of your CHEM 101 class. You're in your recitation group with a boy who has messy brown hair and the bluest eyes you've ever seen. More importantly, he seems just as lost as you feel right now.")
    print("Hi my name is John. What's your name?")
    player = input("What is your name? ")
    print(f"Cameron: It's nice to meet you {player}.")
    print(f"{player}: Hi.")
    print("John: Do you understand what's going on in class?")
    print("1. Yeah, I do actually.")
    print("2. No, not really.")
    print("3. Sort of, but I definitely need to review today's lecture")
    a = int(input("CHOOSE AN OPTION. "))
    points == points + 10
    if a == 1:
        points = points + 10
        print("John: Really? Wow, I'm really struggling right now. Would you like to study together at Davis? I know you don't really need it, but I'd love to have a study buddy.")
        print("1. Actually, I'd love to have a study buddy.")
        print("2. Sorry, my friend and I are going to finnish a lab report after this.")
        a_1 = int(input("CHOOSE AN OPTION. "))
        if a_1 == 1:
            print("John: Great! I'll have someone to suffer through chemistry with.")
            points = 20
        else:
            print("Game Over")
            print(f"Points: {points}")
            print("Do you want to play again?")
            print("1. Yes")
            print("2. No")
            gm = int(input("CHOOSE AN OPTION. "))
            if gm == 2:
                print("Thank you for playing.")
                return None
    else:
        if a == 2:
            points = points + 10
            print("John: Yeah, I'm completely lost too. Would you like to study in Davis together? Maybe we can make sense of some of this gibberish.")
            print("1. Yeah, I'd like that.")
            print("2. Sorry, I'm not really interested.")
            a_2 = int(input("CHOOSE AN OPTION. "))
            if a_2 == 1:
                print("Jayden: Great! It's nice to know I'm not the only one lost.")
                points = 20
            else:
                print("Game Over")
                print(f"Points: {points}")
                print("Do you want to play again?")
                print("1. Yes")
                print("2. No")
                gm = int(input("CHOOSE AN OPTION. "))
                if gm == 2:
                    print("Thank you for playing.")
                    return None
        else: 
            if a == 3:
                points = points + 10
                print("John: Would you like to review it together in Davis? I have some notes form AP Chem in high school but it's been so long since I've looked at them.")
                print("1. Sounds good to me.")
                print("2. No thanks.")
                a_3 = int(input("CHOOSE AN OPTION. "))
                if a_3 == 1:
                    print("Jayden: Great. Hopefully we'll be able to figure some of this stuff out.")
                    points = 20
                else:
                    print("Game Over")
                    print(f"Points: {points}")
                    print("Do you want to play again?")
                    print("1. Yes")
                    print("2. No")
                    gm = int(input("CHOOSE AN OPTION. "))
                    if gm == 2:
                        print("Thank you for playing.")
                        return None
    if points >= 20:
        print("Story: You guys walk to Davis talking about all the other classes you guys are taking right now and how CHEM 101 falls into it your majors.He holds the door open for you.")
        print(f"John: After you, {player}")
        print("Thank you.")
        print("1. Hold the gate open for him.")
        print("2. Let him open the gate himself.")
        b = int(input("CHOOSE AN OPTION. "))
        if b == 1:
            points == points + 10
        print("John: Let's stay on the first floor.")
        print("Story: You walk around the first floor and manage to find some seats. What do you want to start with?")
        print("1. Reviewing today's lecture.")
        print("2. Pearson homework.")
        print("3. Readings for next class.")
        input("CHOOSE AN OPTION. ")
        points = points + 10
        print(f"{player}: So what are your plans after college?")
        print("John: Personally, I want to get into med school. Maybe Chapel Hill's but I'm just kind of aiming to get in somewhere right now.")
        print("John: So what do you want to go into?")
        print("1. A STEM major")
        print("2. A non-STEM major.")
        c = int(input("CHOOSE AN OPTION"))
        if c == 1:
            points = points + 10
        else:
            points = points - 10
        print("Story: You two crack open your laptops, books and notebooks. The entire table is covered with your guys' study materials.")
        print("You: How are you doing in lab?")
        print("John: They're terrible. They take so long. I think I spent over three hours on my last lab report.")
        print("1. Wow that sounds tough.")
        print("2. You're just making a big deal of nothing.")
        d = int(input("CHOOSE AN OPTION"))
        if d == 1:
            points = points + 10
        else:
            points = points - 10
        print("1. Continue studying in silence.")
        print("2. Keep trying to make small talk while he's focusing.")
        e = int(input("CHOOSE AN OPTION"))
        if e == 1:
            points = points + 10
            print("Yeah, I'd like to live in a city too.")
        else:
            points = points - 10
            print("Oh. That's too bad.")
    print(f"Story: {player} and Jayden have finished your study session. Both you and he seemed to get a lot of work done and it's been a productive day over all.")
    print(f"Points: {points}")
    if points >= 50:
        print("Congratualtions! Your date with John was a success and you two become regular study buddies for the rest of undergrad. He eventually gets into the UNC Med School and you family is so happy that you found a successful boyfriend.")
        print(NAMED_CONSTANT)
        print("Do you want to play again?")
        print("1. Yes")
        print("2. No")
        gm = int(input("CHOOSE AN OPTION. "))
        if gm == 2:
            print("Thank you for playing.")
            return None
    else:
        print("Unfortunately, John went off to study on his own the minute finals season hit and you guys haven't really talked since then.")
        print("Do you want to play again?")
        print("1. Yes")
        print("2. No")
        gm = int(input("CHOOSE AN OPTION. "))
        if gm == 2:
            print("Thank you for playing.")
            return None


def Dukey(choice: int) -> int:
    """Duke."""
    points: int = 0
    print("Story: You don't know what it is but you don't seem to really be clicking with anyone in your classes. You decide to Tinder as an option. To your suprise to find the most attractive man you've ever seen pop up and you swipe right on him. A few hours later, you check your notifications and found that you matched with him on Tinder. After a few messages, you really seem to be hitting it off, and then you find out... He's from Duke!")
    print("Hi my name is Cameron. What's your name?")
    player = input("What is your name? ")
    print(f"Cameron: It's nice to meet you {player}.")
    print(f"{player}: Hi.")
    print("Cameron: So you go to UNC?")
    print("1. Yeah, I do actually.")
    print("2. No, I just live in Chapel Hill.")
    print("3. Would my answer affect anything?")
    a = int(input("CHOOSE AN OPTION. "))
    points = points + 10
    if a == 1:
        points = points + 10
        print("Cameron: Well, I'd be willing to put aside our rivalry if you are. I think you're pretty cool and I'd like to take you to the Duke Gardens.")
        print("1. Deal.")
        print("2. Ew now way. Duke is puke.")
        a_1 = int(input("CHOOSE AN OPTION. "))
        if a_1 == 1:
            print("Cameron: Great! I've never really cared about the rivalry to begin with..")
            points = 20
        else:
            print("Game Over")
            print(f"Points: {points}")
            print("Do you want to play again?")
            print("1. Yes")
            print("2. No")
            gm = int(input("CHOOSE AN OPTION. "))
            if gm == 2:
                print("Thank you for playing.")
                return points
    else:
        if a == 2:
            points = points + 10
            print("Cameron: Um, your bio says UNC student. I really don't care if you are a UNC student. You seem really cool and I'd like to hang out sometime. Maybe the Duke Gardens?")
            print("1. Yeah, I'd like that.")
            print("2. Sorry, I can't be seen with a Dukey.")
            a_2 = int(input("CHOOSE AN OPTION. "))
            if a_2 == 1:
                print("Cameron: Great! I'll see you Saturday. By the way, you might want to leave your UNC merchandise.")
                points = 20
            else:
                print("Game Over")
                print(f"Points: {points}")
                print("Do you want to play again?")
                print("1. Yes")
                print("2. No")
                gm = int(input("CHOOSE AN OPTION. "))
                if gm == 2:
                    print("Thank you for playing.")
                    return points
        else: 
            if a == 3:
                points = points + 10
                print("Cameron: Not it wouldn't. I really like you. Would you like to go the the Duke Gardens with me?")
                print("1. Yeah, I'd like that.")
                print("2. I'm sorry I don't think we should go out.")
                a_3 = int(input("CHOOSE AN OPTION. "))
                if a_3 == 1:
                    print("Cameron: Great. I'll see you on Saturday.")
                    points = 20
                else:
                    print("Game Over")
                    print(f"Points: {points}")
                    print("Do you want to play again?")
                    print("1. Yes")
                    print("2. No")
                    gm = int(input("CHOOSE AN OPTION. "))
                    if gm == 2:
                        print("Thank you for playing.")
                        return points
    if points >= 20:
        print("Story: You guys meet at the Duke Gardens. You walk the romantic pathways together while looking at the beautiful plants.")
        print(f"{player}: So what's your major?")
        print("Cameron: Oh, I'm a pre-law.")
        print("1. Wow that's impressive.")
        print("2. Wow that's basic.")
        b = int(input("CHOOSE AN OPTION. "))
        if b == 1:
            points = points + 10
        print("Cameron: So what do you think of the Duke Gardens?")
        print("1. Yeah, it's beautiful.")
        print("2. Yeah, it's just as beautiful as the UNC arboretum.")
        input("CHOOSE AN OPTION. ")
        points = points + 10
        print("Cameron: Have you ever been to one of our basketball games?")
        print("1. Yeah, you guys gave us a run for our money.")
        print("2. Yeah and Duke sucked.")
        c = int(input("CHOOSE AN OPTION"))
        if c == 1:
            points = points + 10
        else:
            points = points - 10
        print("Cameron: Have you had Dame's Chicken and Waffles?.")
        print("1. Yeah, the one is Durham is amazing!.")
        print("2. Yeah, we have one on Franklin street. It's the best.")
        d = int(input("CHOOSE AN OPTION"))
        if d == 1:
            points = points + 10
        else:
            points = points - 10
        print("Cameron: Have you read Crime adn Punishment?")
        print("1. Yes.")
        print("2. No.")
        e = int(input("CHOOSE AN OPTION"))
        if e == 1:
            points = points + 10
            print("Cameron: Yeah, that's my favorite book.")
        else:
            points = points - 10
            print("Story: Cameron then proceed to explain Crime and Punishment in a pretentious way.")
    print(f"Story: {player} and Cameron have finished their date at Duke Gardens. There were a few close calls of being caught of being a Tar Heel in Devil's land but you made it our of there with everything still intact.")
    return points


def main() -> None:
    """The program's entrypoint."""
    points = 0
    repeat = 0
    while repeat < 1:
        greet()
        print("Which is the following special UNC boys would you like to pursue a relationship with?")
        print("1. The frat boy. He's fun and wild and your weekends are always a guaranteed fun time. The secret and chaotic life of a fraternity is something that will always keep you on your toes.")
        print("2. The business snake. Sweet smiles and deceptive words. He's got the mind more cunning that anyone else and a plan for the future filled with riches and success. You could have a place in it too if you're able to reach past his business exterior and into his heart.")
        print("3. The Pre-Med. He's driven and motivated to be the best. An instant approval from your family and they'll be rooting for him to win your heart.")
        print("4. The Dukey. A forbidden love story that rivals Romeo and Juliet. Two lovers torn apart by two schools with a rival that goes back further than anyone can remember. Secret rendezvous and stealing glances at each other during basketball games. It’s a romance story William Shakespere would applaud.")
        print("5. None. I'm into girls/ I am aro/ace.")
        choice = int(input("Which person would you like to select? (Please input their number) "))
        points = points + 10
        if choice == 1:
            frat()
            print("Do you want to play again?")
            print("1. Yes")
            print("2. No")
            gm = int(input("CHOOSE AN OPTION. "))
            if gm == 2:
                print("Thank you for playing.")
                return None
        else:
            if choice == 2:
                snake()
                print("Do you want to play again?")
                print("1. Yes")
                print("2. No")
                gm = int(input("CHOOSE AN OPTION. "))
                if gm == 2:
                    print("Thank you for playing.")
                    return None
            else:
                if choice == 3:
                    premed()
                    print("Do you want to play again?")
                    print("1. Yes")
                    print("2. No")
                    gm = int(input("CHOOSE AN OPTION. "))
                    if gm == 2:
                        print("Thank you for playing.")
                        return None
                else:
                    if choice == 4:
                        Dukey(choice)
                        print(f"Points: {points}")
                        if points >= 50:
                            print("Congratualtions! Your date with Cameron went well you guys stayed together. You guys managed to graduate together and now you can be togheter without the fear of one of you guys being jumped when one visits the other. However, game day will always cause a bit of tension between you two.")
                            print(NAMED_CONSTANT)
                            print("Do you want to play again?")
                            print("1. Yes")
                            print("2. No")
                            gm = int(input("CHOOSE AN OPTION. "))
                            if gm == 2:
                                print("Thank you for playing.")
                                return None
                        else:
                            print("Unfortunately, Cameron wasn't feeling it an ghosted you.")
                            print("Do you want to play again?")
                            print("1. Yes")
                            print("2. No")
                            gm = int(input("CHOOSE AN OPTION. "))
                            if gm == 2:
                                print("Thank you for playing.")
                                return None
                    else:
                        print("So you've chosen none of these options. Smart move. You make it through college on the Dean's list and save yourself the heartache and trauma. You move on with your life and find yourself a well-paying job in your major. Maybe now, you’ll finally find a real romance for you...")
                        print("Or not. No one needs a romance to have a happy and fulfilling life.")
                        print(f"Points: {points}")
                        print("Do you want to play again?")
                        print("1. Yes")
                        print("2. No")
                        gm = int(input("CHOOSE AN OPTION. "))
                        if gm == 2:
                            print("Thank you for playing.")
                            return None


if __name__ == "__main__":
    main()