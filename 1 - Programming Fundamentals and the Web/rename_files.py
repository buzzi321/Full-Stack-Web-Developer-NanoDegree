import os

def rename_files():
    file_list = os.listdir("C:\Sekhar_DTV\Learning\Full Stack Web Developer NanoDegree\phabet\phabet")
    program_path = os.getcwd()
    os.chdir("C:\Sekhar_DTV\Learning\Full Stack Web Developer NanoDegree\phabet\phabet")

    for file_name in file_list:
        print ("Old File Name - " ,file_name)
        print ("New File Name - ", file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
        #os.rename("file_name.txt", file_name.translate(None, "0123456789"))
    os.chdir(program_path)

rename_files()