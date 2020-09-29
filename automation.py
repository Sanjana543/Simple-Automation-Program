#This is simple program to open notepad file copy the material in it automatically and paste it to ecllipse(I've made this for my comp. to run it in others need to change file name
#and resize it acc.to your screen)
#simple program but made my work easy.
# updated contributed by Nullcoder08

from pywinauto.application import Application as ap
import numpy
import pyautogui as pg
import time
pg.FAILSAFE = True
pg.hotkey('winleft')
time.sleep(1)
pg.typewrite('notepad\n',0.25)
pg.hotkey('winleft','up')
time.sleep(1)
pg.click(30,30)
time.sleep(1)
pg.moveRel(50,80)
time.sleep(1)
pg.click()
time.sleep(1)
pg.typewrite('try\n',0.1)
pg.click(50,80)
time.sleep(3)
pg.hotkey('ctrl','a')
time.sleep(2)
pg.hotkey('ctrl','c')
time.sleep(2)
app=ap().start(r"C:\Users\Anubhav\eclipse\java-2019-06\eclipse\eclipse.exe")
time.sleep(3)
app.EclipseIDELauncher.Launch.click()
time.sleep(14)
app.eclipseworkspaceEclipseIDE.menu_select("File->New->Class")
time.sleep(1)
pg.click(949,284)
time.sleep(1)
pg.typewrite('autonnnnn\n',0.1)
time.sleep(2)
pg.click(133,72)
time.sleep(1)
pg.click(1034,356)
pg.click(627,173)
time.sleep(1)
pg.hotkey('ctrl','v')
time.sleep(1)
pg.click(180,71)
time.sleep(20)
app.kill()
