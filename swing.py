import pyautogui
width, height = pyautogui.size();

pyautogui.moveTo(width/2,height/2,1)
pyautogui.mouseDown()
pyautogui.moveRel(0,400,0.60)
pyautogui.moveRel(0,-600,0.1)
pyautogui.mouseUp()
pyautogui.moveTo(1455,810,1)


