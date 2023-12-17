import os
import shutil

# текущая деректория
print(os.getcwd())

# узнаём есть ли файл/директория 
if not os.path.isdir("newdir"):
    # создаём новую деректорию 
    os.mkdir("newdir")

# перейти в деректорию 
os.chdir("newdir")
print(os.getcwd())

# вернуться в предыдущию папку  
os.chdir("..")
print(os.getcwd())

# создание вложенной папки 
# makedirs("One/One")

# создание файла 
fp = open('sales.txt', 'w')
fp.close()

# измение имени 
# os.rename("sales.txt", "sales1.txt")

# перемещение файла
# os.replace('sales.txt','newdir/sales.txt')

# вывод всего содержимого директории 
print(os.listdir())

# удаление файлов 
os.remove('sales.txt')

# удаление пустой папки 
# os.removedirs('newdir')

# удаление папки с данными
shutil.rmtree('newdir')

# информация о файле
fp = open('sales.txt', 'w').write("ну и база")
print(os.stat('sales.txt'))

# используем команды из терминала 
# os.system("ping google.com")

# содержимая папок и того что в нутри папок
for i in os.walk(os.getcwd()):
    print(i)
























