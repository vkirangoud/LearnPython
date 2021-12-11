import os
def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r"C:\SDrive\prac\prank") # r - stands for rawpack, take this string as it is
    #print(file_list);
    saved_path = os.getcwd()
    print("Current working Directory is "+saved_path)
    os.chdir(r"C:\SDrive\prac\prank")
    # (2) for each file, rename filename
    for file_name in file_list:     
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print(file_name)
    os.chdir(saved_path)
rename_files()
