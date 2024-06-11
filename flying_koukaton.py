import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    tmr = 0
    x = 0
    kktn_img = pg.image.load("fig/3.png")
    kktn_img = pg.transform.flip(kktn_img, True, False)
    bg_imgf = pg.transform.flip(bg_img, True, False)
    kktn_rct = kktn_img.get_rect()
    kktn_rct.center = (300, 200)
    x1 = 0
    y1 = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [x, 0])
        screen.blit(bg_imgf, [x+1600, 0])
        screen.blit(bg_img, [x + 3200, 0] )
        screen.blit(bg_imgf, [x + 4800, 0])

        key_list = pg.key.get_pressed()
        if key_list[pg.K_UP]:
            y1 = -1
        elif key_list[pg.K_DOWN]:
            y1 = 1
            
        elif key_list[pg.K_RIGHT]:
            x1 = 2
        elif key_list[pg.K_LEFT]:
            x1 = -1
        else:
            x1 = -1
            y1 = 0
        kktn_rct.move_ip((x1, y1))
        

        
        screen.blit(kktn_img, kktn_rct)
        pg.display.update()
        tmr += 1     
        x -= 1
        if x == -3200:
            x = 0   
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()