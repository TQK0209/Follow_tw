import subprocess
import time

def RestartPhone():
    filepath="E:/EDIT FILE (py)/Follow/modules/open_airmode.bat"
    p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
    stdout, stderr = p.communicate()
    
    time.sleep(2)
    p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
    stdout, stderr = p.communicate()

   
        
