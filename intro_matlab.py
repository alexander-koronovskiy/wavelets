# Подключаем модуль
import os

# Каталог из которого будем брать файлы
directory = 'D:\\Matlab\\bin\\New Folder\\data'

# Получаем список файлов в переменную files
files = os.listdir(directory)
files_new = list()

# операция для составления команд
for i in range(len(files)):
    files_new.append('load data/' + files[i] + ';' + '\n' + 'signal1 = X'
                     + files[i][:-4] + ';' + '\n'
                     + '[Hq1,tq1,hq1,Dq1,Fq1]=MFDFA1(signal1,scale,q,m,1); \n')

# запись названия файлов / команд в файл
with open(r"lines.txt", "w") as file:
    file.writelines("%s\n" % line for line in files_new)
