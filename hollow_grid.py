import pygame
from pygame.locals import *
from rect_numbers import check_if_mines
hollow_rects = {}




def check_if_hollow(rleft,rtop,mines,wind,cindex):
    hollow_rects.clear()
    for index in mines.keys():
        
        check_if_hollowyu(rleft,rtop,mines,index,cindex)
        check_if_hollowyd(rleft,rtop,mines,index,cindex)
        for rect in hollow_rects.keys():
            pygame.display.update(pygame.draw.rect(wind, (180, 180, 180),[hollow_rects[rect]['x'],hollow_rects[rect]['y'],23,23]))
            pygame.display.update(pygame.draw.rect(wind, [50,50,50],[hollow_rects[rect]['x'],hollow_rects[rect]['y'],23,23],1))
            recttop = hollow_rects[rect]['y'] 
            rectleft = hollow_rects[rect]['x']
            if (check_if_mines(
            checkXneg = rectleft - 21,
            checkXplus = rectleft + 21,
            checkYneg = recttop - 22,
            checkYplus = recttop + 22,
            mines = mines,
            recttop = recttop,
            rectleft = rectleft,
            wind = wind,
            )):
                pass
            
           
       
        hollows = hollow_rects
        
      
        return hollows
        break
            
        
        



def check_if_hollowxp(rleft,rtop,mines,cindex):
    check_if_mine = False
    
    for num in range(304):
        rleftp = rleft + 21
        
        for recta in mines.keys():
            if (
                rleftp in mines[recta].values()
                and rtop in mines[recta].values()
            ): 
                if (rleft not in mines[recta].values()
                and rtop not in mines[recta].values()):
                    hollow_rects.update({cindex: {'x':rleft,'y':rtop}})
                check_if_mine = True
                return
        hollow_rects.update({cindex: {'x':rleft,'y':rtop}})
        if check_if_mine:
            break
        if (rleft > 379):
            rtop += 22
            rleft = -19
        rleft += 21
        cindex += 1
        if cindex > 359:
            cindex -= 1
               
       
            
       
    return True

        
                
       


def check_if_hollowxm(rleft,rtop,mines,cindex):
    check_if_mine = False
    
    for num in range(304):
        rleftm = rleft - 21
        
        for recta in mines.keys():
            if (
                rleftm in mines[recta].values()
                and rtop in mines[recta].values()
            ): 
                if (rleft not in mines[recta].values()
                and rtop not in mines[recta].values()):
                    hollow_rects.update({cindex: {'x':rleft,'y':rtop}})
                check_if_mine = True
                return
        if (rleft < 2):
            rtop -= 22
            rleft = 2
       
        hollow_rects.update({cindex: {'x':rleft,'y':rtop}})
        if check_if_mine:
            break
        rleft -= 21
        cindex -= 1
        if cindex < 0:
            cindex += 1
               
      
            
       
    return True

        
def check_if_hollowyd(rleft,rtop,mines,index,cindex):
    check_if_mine = False
    
    for num in range(304):
        rtopu = rtop - 22
        
        for recta in mines.keys():
            if (
                rtopu in mines[recta].values()
                and rleft in mines[recta].values()
            ): 
                if (rleft not in mines[recta].values()
                and rtop not in mines[recta].values()):
                    hollow_rects.update({cindex: {'x':rleft,'y':rtop}})
                check_if_mine = True
                break
        if (rtop < 50):
            rtop = 50
        check_if_hollowxp(rleft,rtop,mines,cindex)
        check_if_hollowxm(rleft,rtop,mines,cindex)
        hollow_rects.update({cindex: {'x':rleft,'y':rtop}})
        if check_if_mine:
            check_if_hollowxp(rleft,rtop,mines,cindex)
            check_if_hollowxm(rleft,rtop,mines,cindex)
            break
        rtop -= 22
        cindex -= 18
        if cindex < 0:
            cindex += 18
               
      
            
       
    return True

def check_if_hollowyu(rleft,rtop,mines,index,cindex):
    check_if_mine = False
    
    for num in range(304):
        rtopu = rtop + 22
        
        for recta in mines.keys():
            if (
                rtopu in mines[recta].values()
                and rleft in mines[recta].values()
            ): 
                if (rleft not in mines[recta].values()
                and rtop not in mines[recta].values()):
                    hollow_rects.update({cindex: {'x':rleft,'y':rtop}})
                check_if_mine = True
                break
        if (rtop > 380):
            rtop = 380
        
        hollow_rects.update({cindex: {'x':rleft,'y':rtop}})
        check_if_hollowxp(rleft,rtop,mines,cindex)
        check_if_hollowxm(rleft,rtop,mines,cindex)
        if check_if_mine:
            check_if_hollowxp(rleft,rtop,mines,cindex)
            check_if_hollowxm(rleft,rtop,mines,cindex)
            break
        rtop += 22
        cindex += 18
        if cindex > 359:
            cindex -=18
               
      
            
       
    return True
