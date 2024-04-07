import pygame as pg
from mahjong import mahjong
from player import player
from player import AI
from test import *


m = mahjong()
p = player()
a = AI()
for i in range(13):
    p.getPreHand(m.drawCard())
    p.getHand()
for i in range(13):
    a.AIgetPreHand(m.drawCard())
    a.AIgetHand()
p.sortHand()
a.AIsortHand()
# print(p.hand)
pg.init()
screen = pg.display.set_mode((1600, 900))
screen.fill((0, 100, 0))
pg.display.set_caption('MahJong')

imageLst = loadImage(p.hand)
AIimageLst = loadImage(a.AIHand)
rectLst = loadRect(p.hand)
rectAILst = loadRect(a.AIHand)
if p.preHand is not None:
    preImageLst = loadImage(p.preHand)
    preRectLst = loadRect(p.preHand)
if a.AIpreHand is not None:
    preImageAILst = loadImage(a.AIHand)
    preRectAILst = loadRect(a.AIHand)

while True:
    screen.fill((0, 100, 0))
    handShow(screen, imageLst, rectLst)
    AIHandShow(screen,AIimageLst,rectAILst)
    if p.preHand is not None:
        preHandShow(screen, preImageLst[0], preRectLst[0])
    if a.AIpreHand is not None:
        preHandShow(screen, preImageAILst[0], preRectAILst[0])
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            clickHand(p.hand, rectLst)
            clickPreHand(p.preHand, preRectLst[0])

    pg.display.update()
    pg.display.flip()
