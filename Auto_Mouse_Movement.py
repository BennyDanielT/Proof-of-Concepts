import pyautogui as py

'''You can tell your script to wait after every function call, giving you a short window to take control of the mouse and keyboard if something goes wrong. To do this, set the pyautogui.PAUSE variable to the number of seconds you want it to pause. For example, after setting pyautogui.PAUSE = 1.5, every PyAutoGUI function call will wait one and a half seconds after performing its action. Non-PyAutoGUI instructions will not have this pause.

PyAutoGUI also has a fail-safe feature. Moving the mouse cursor to the upper-left corner of the screen will cause PyAutoGUI to raise the pyautogui.FailSafeException exception. Your program can either handle this exception with try and except statements or let the exception crash your program. Either way, the fail-safe feature will stop the program if you quickly move the mouse as far up and left as you can. You can disable this feature by setting pyautogui.FAILSAFE = False. Enter the following into the interactive shell:


>>> import pyautogui
>>> pyautogui.PAUSE = 1
>>> pyautogui.FAILSAFE = True'''

py.FAILSAFE = False
while True:
	py.moveTo(100, 100, duration = 1)
	py.moveTo(100, 200, duration = 1)
	py.moveTo(100, 100, duration = 1)
	
