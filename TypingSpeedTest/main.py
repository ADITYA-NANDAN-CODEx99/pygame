import pygame, random
pygame.init()

screen = pygame.display.set_mode((1000,400))
pygame.display.set_caption("TYPING SPEED CALCULATOR")
text_font = pygame.font.Font("freesansbold.ttf", 20)
heading_font = pygame.font.Font("freesansbold.ttf", 40)

GREEN = (0, 255, 0)
RED = (255, 0, 0)

font_c = GREEN

def start_game():
    global font_c
    statements = [
        "Please take your dog, Cali, out for a walk – he really needs some exercise!",
        "What a beautiful day it is on the beach, here in beautiful and sunny Hawaii.",
        "Rex Quinfrey, a renowned scientist, created plans for an invisibility machine.",
        "Do you know why all those chemicals are so hazardous to the environment?",
        "You never did tell me how many copper pennies where in that jar; how come?",
        "Max Joykner sneakily drove his car around every corner looking for his dog.",
        "The two boys collected twigs outside, for over an hour, in the freezing cold!",
        "When do you think they will get back from their adventure in Cairo, Egypt?",
        "Trixie and Veronica, our two cats, just love to play with their pink ball of yarn.",
        "We climbed to the top of the mountain in just under two hours; isn’t that great?",
        "I am the King of the world.",
        "Isn't that great?",
        "How can you say that?", 
        "I live in America.",
        "I am the king.",
        "I have tons of apple in my pocket.",
        "I like Apples.",
        "I like pizza the most.",
        "We are going to USA next week.",
    ]

    def result(inp, statement, time_taken):
        c = 0
        C = 0
        inp_words = inp.split(" ")
        statement_words = statement.split(" ")

        wpm = (len(inp_words)/time_taken) * 60

        for i in range(len(inp_words)):
            for j in range(len(inp_words[i])):
                C += 1
                if inp_words[i][j] == statement_words[i][j]:
                    c += 1
        return((str(c/C*100)[:3]), str(wpm)[:3])

    statement = random.choice(statements)
    inp = ''
    enter = 0
    start = 0

    MainGame = True

    while MainGame:
        screen.fill((0,0,0))

        # pygame.draw.rect(screen, (255,255,0), pygame.Rect(50,100,900,40), 3)
        sentence = text_font.render(statement, True, (255,255,255))
        sentence_rect = sentence.get_rect(center=(500, 110), height=40)
        screen.blit(sentence, (sentence_rect.x, sentence_rect.y + 10))
        pygame.draw.rect(screen, (255, 255, 0), sentence_rect, 3)

        # pygame.draw.rect(screen, (0,255,0), pygame.Rect(50,200,900,40), 3)
        if start == 0:
            inp_sentence = text_font.render("(PRESS 1 TO START)", True, (128,128,128))
        else:
            inp_sentence = text_font.render(inp, True, font_c)

        inp_rect = inp_sentence.get_rect(height=40, center=(500, 210))
        screen.blit(inp_sentence, (inp_rect.x, inp_rect.y + 10))
        pygame.draw.rect(screen, (255, 255, 0), inp_rect, 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MainGame = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    start = 1
                    start_time = pygame.time.get_ticks()
                elif event.key == pygame.K_RETURN:
                    enter = 1
                    end_time = pygame.time.get_ticks()
                    accuracy, wpm = result(inp, statement, (end_time-start_time)/1000)
                
                elif event.key == pygame.K_ESCAPE:
                    Display_Page()

                elif event.key == pygame.K_BACKSPACE:
                    inp = inp[:-1]

                else:
                    try:
                        if statement[len(inp)] != event.unicode:
                            font_c = RED
                        else:
                            font_c = GREEN
                    except IndexError:
                        pass
                    inp += event.unicode

        if enter == 1:
            Accuracy_msg = text_font.render("ACCURACY: " + accuracy + "%", True, (255,255,255))
            screen.blit(Accuracy_msg, (400, 300))
            WPM_msg = text_font.render("WPM: " + wpm, True, (255,255,255))
            screen.blit(WPM_msg, (440,350))

        pygame.display.update()

def Display_Page():
    MainRun = True
    while MainRun:
        screen.fill((0,0,0))
        Game_msg = heading_font.render("TYPING SPEED CALCULATOR", True, (255,255,0))
        screen.blit(Game_msg, (240,100))

        Display_msg = text_font.render("PRESS SPACE TO START", True, (255,255,200))
        screen.blit(Display_msg, (380,300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MainRun = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    MainRun = False
                    start_game()

        pygame.display.update()


Display_Page()
