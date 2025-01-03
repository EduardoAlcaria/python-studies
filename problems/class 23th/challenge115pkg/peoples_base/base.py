import os
import shutil
green = "\033[1;32m"
color_reset = "\033[m"
def createfile():
    def findfile(path, file): #/media/eduardoalcaria/DADOS/linux/programming/studies/python_studies/problems/class 23th/challenge115pkg/peoples_base
        for root, dirs, files in os.walk(path):
            if file in files:
                return os.path.join(root, file)
        return None
    global_dir = os.getcwd() 
    print(global_dir)
    peopleBase_dir = "/media/eduardoalcaria/DADOS/linux/programming/studies/python_studies/problems/class 23th/challenge115pkg/peoples_base"
    try:
        peopleBase = open('peopleBASE.txt', 'w')
        name = 'peopleBASE.txt'
        resultG = findfile(global_dir, name)
        shutil.move(resultG, peopleBase_dir)
        resultP = findfile(peopleBase_dir, name) 
    except shutil.Error as e:
        if os.path.exists(resultG):
            os.remove(resultG)
            print(f"{green}{name}'s has already been created{color_reset}")
    else:
        print(f"{green}{name}'s file has been created{color_reset}")
        peopleBase.write("Hello word")
        r = open('peopleBASE.txt', 'r')
        print(r.readline())
createfile()