import sys, pygame as pg, random as r

Game1 = True
phase = 1
clicked = False

def main():
    global window, Game1, clock
    pg.init()

    state = "W.I.P"
    window = pg.display.set_mode((1200, 700))
    pg.display.set_caption(state + " - Rock Pa-[Py]-per Scissors ")
    Game1 = True

    clock = pg.time.Clock()
    

def rock():
    global rock_image
    rock_image = pg.image.load("rock.png").convert_alpha()
    width, height = rock_image.get_width(), rock_image.get_height()

    width /= 1.5
    height /= 1.5

    rock_image = pg.transform.scale(rock_image, (int(width), int(height)))
    

    
def paper():
    global paper_image, paper_rect
    paper_image = pg.image.load("paper.png").convert_alpha()
    width, height = paper_image.get_width(), paper_image.get_height()

    width /= 1.5
    height /= 1.5

    paper_image = pg.transform.scale(paper_image, (int(width), int(height)))
    paper_rect = paper_image.get_rect
    
def scissors():
    global scissors_image, scissors_rect
    scissors_image = pg.image.load("scissors.png").convert_alpha()
    width, height = scissors_image.get_width(), scissors_image.get_height()

    width /= 1.5
    height /= 1.5

    scissors_image = pg.transform.scale(scissors_image, (int(width), int(height)))
    scissors_rect = scissors_image.get_rect()

    


if __name__ == "__main__":
    main()
    while Game1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                sys.exit()
                
               
        pos = pg.mouse.get_pos()       
        window.fill((255, 255, 255))       
        clock.tick(60)
                     
        if phase == 1:
            
                    rock()
                    x = 50
                    y = 200      
                    window.blit(rock_image, (x, y))
                    rock_rect = rock_image.get_rect()
                    
                    
                    
                    x = 450
                    y = 200 
                    paper()
                    window.blit(paper_image, (x, y))
                    
                    
                    x = 850
                    y = 200    
                    scissors()
                    window.blit(scissors_image, (x, y))
                    
                    pg.display.flip()
                    
                    if rock_rect.collidepoint(pos):
                        if pg.mouse.get_pressed()[0] == 1 and clicked == False:
                            clicked = True
                            print("CLICKED Rock")
                            
                        if pg.mouse.get_pressed()[0] == 0:
                            clicked = False