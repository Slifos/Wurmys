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

def interpretation(input):
    if input == pygame.K_a:
        return "a"
    elif input == pygame.K_b:
        return "b"
    elif input == pygame.K_c:
        return "c"
    elif input == pygame.K_d:
        return "d"
    elif input == pygame.K_e:
        return "e"
    elif input == pygame.K_f:
        return "f"
    elif input == pygame.K_g:
        return "g"
    elif input == pygame.K_h:
        return "h"
    elif input == pygame.K_i:
        return "i"
    elif input == pygame.K_j:
        return "j"
    elif input == pygame.K_k:
        return "k"
    elif input == pygame.K_l:
        return "l"
    elif input == pygame.K_m:
        return "m"
    elif input == pygame.K_n:
        return "n"
    elif input == pygame.K_o:
        return "o"
    elif input == pygame.K_p:
        return "p"
    elif input == pygame.K_q:
        return "q"
    elif input == pygame.K_r:
        return "r"
    elif input == pygame.K_s:
        return "s"
    elif input == pygame.K_t:
        return "t"
    elif input == pygame.K_u:
        return "u"
    elif input == pygame.K_v:
        return "v"
    elif input == pygame.K_w:
        return "w"
    elif input == pygame.K_x:
        return "x"
    elif input == pygame.K_y:
        return "y"
    elif input == pygame.K_z:
        return "z"
    elif input == pygame.K_KP0:
        return "0"
    elif input == pygame.K_KP1:
        return "1"
    elif input == pygame.K_KP2:
        return "2"
    elif input == pygame.K_KP3:
        return "3"
    elif input == pygame.K_KP4:
        return "4"
    elif input == pygame.K_KP5:
        return "5"
    elif input == pygame.K_KP6:
        return "6"
    elif input == pygame.K_KP7:
        return "7"
    elif input == pygame.K_KP8:
        return "8"
    elif input == pygame.K_KP9:
        return "9"
    else:
        return ""

