import os
import sys
import subprocess

display = ':0'
xserver = subprocess.Popen(['Xvfb', display])
os.environ['DISPLAY'] = display
testing = subprocess.Popen(
    ['python', '-m', 'unittest'], env={'DISPLAY': display}
)
retval = testing.wait()
xserver.kill()
sys.exit(retval)
