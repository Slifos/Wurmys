            l = Image_h("alpha/6.png",espace,(0,0))
        elif letter == "7":
            l = Image_h("alpha/7.png",espace,(0,0))
        elif letter == "8":
            l = Image_h("alpha/8.png",espace,(0,0))
        elif letter == "9":
            l = Image_h("alpha/9.png",espace,(0,0))
        surface.blit(l.image,(espace/1.7*i,0))
        #pygame.image.save(surface, "mot.png")

        i+=1
    return surface
"""utile dans le futur"""
def input():
    taping = False
    while taping==False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                running = False

                return event.key
