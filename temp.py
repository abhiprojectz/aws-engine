from pyvirtualdisplay import Display
import os

disp = Display(size=(1536, 864), color_depth=24)
disp.start()
print(os.environ['DISPLAY'])