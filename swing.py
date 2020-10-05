import pyautogui
import pygetwindow as gw
playing = True
testing = True
width, height = pyautogui.size()
print(gw.getAllTitles())
gameWindow = gw.getWindowsWithTitle('PGA TOUR 2K21')[0]
gameWindow.activate()
pyautogui.moveTo(gameWindow.center.x,gameWindow.center.y,0)

if playing:
    gameWindow.activate()
    pyautogui.moveTo(gameWindow.center.x,gameWindow.center.y,0)
    pyautogui.mouseDown()
    pyautogui.moveRel(0,400,0.36)
    pyautogui.moveRel(0,-600,0.36)
    pyautogui.mouseUp()
    pyautogui.moveTo(1455,810,0)
if testing:
    gw.getWindowsWithTitle('pySwing – swing.py PyCharm')[0].activate()


