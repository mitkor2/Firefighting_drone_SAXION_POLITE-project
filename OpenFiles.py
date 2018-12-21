import glob   
path = 'Pic/*.jpg'   
files=glob.glob(path)   
for file in files:     
    f=open(file, 'r')
    print(f)
    f.close()


