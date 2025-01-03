import os
import shutil
green = "\033[1;32m"
red = "\033[1;31m"
color_reset = "\033[m"
global_dir = os.getcwd()
resultG = 0
fileName = "peopleBASE.txt"
num = list()
names = list()
peoples = dict()
def findfile(path, file): #/media/eduardoalcaria/DADOS/linux/programming/studies/python_studies/problems/class 23th/challenge115pkg/peoples_base
    for root, dirs, files in os.walk(path):
        if file in files:
            return os.path.join(root, file)
    return None
def createfile(per=0):
    if per == 1:
        try:
            FileCreate = open(fileName, 'x')
            global resultG
            resultG = findfile(global_dir, fileName)  
        except shutil.Error as e:
            print(f"{green}{fileName}'s has already been created{color_reset}")
        except:
            if os.path.exists(resultG):
                return None
def readfile():
    try:
        f = open("peopleBASE.txt", 'r')
    except:
        print(f"{red}an error had happened{color_reset}")
    else:
        for l in f:
            data = l.split(';')
            data[1] = data[1].replace('\n', '')
            print(f"{data[0]:<30} {data[1]:>3} years")
    finally:
        f.close()
def writefile(name='unknown', age=0):
    try:
        wf = open(fileName, mode='at')
    except:
        print(f"{red}an error has happened{color_reset}")
    else:
        try:
            wf.write(f"{name};{age}\n")
        except Exception as e:
            print(f"and error had happended {e}")
        else:
            return f"{green}{name} was succefully registered{color_reset}"
    finally:
        wf.close()
