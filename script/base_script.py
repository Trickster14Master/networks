import os 

is_dir = os.listdir()
already_installed=[]

for i in is_dir:
    if(i=="base_script.exe"):
        continue 
    if (i in already_installed):
        continue
    os.system(i)
    already_installed.append(i)















