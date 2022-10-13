import os

def main():
    i = 0
    
    #When running, replace the folder name below with your folder name
    #(whichever folder you want to rename the files in, and
    #remember to change all back slashes to front slashes,
    #and add a front slash at the end of the folder name. :)
    path = "C:/Users/mcarron/Desktop/rename these/"
    
    for filename in os.listdir(path):
        my_dest = "file" + str(i) + ".txt"
        my_source =path + filename
        my_dest =path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == '__main__':
    main()
