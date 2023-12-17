
import subprocess
from re import *
import os

print("Вы уверены что хотите начать проверку системы? Это может занять некоторое время")
response_user=input("[y/n]- ")

if(response_user=="y"):
    print("Проверка началась, не закрывайте терминал")
    answer=subprocess.run(["sfc/scannow"], shell=True, capture_output=True)
    answer=answer.stdout.decode("UTF-16-LE")
    pattern="Защита ресурсов Windows не обнаружила нарушений целостности."
    result=findall(pattern, answer)
    if(len(result)==1):
        print("в системе нет ошибок")
        p=input(print("нажмите Enter"))
    else:
        print("в системе были найдены ошибки, запустить восстановление?")
        response_user=input("[y/n]- ")
        if(response_user=="y"):
            print("Восстановление началось")
            os.system("dism /Online /Cleanup-Image /RestoreHealth")




























