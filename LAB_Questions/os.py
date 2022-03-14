import os
def current_path():
  print("\nCWD")
  print(os.getcwd())
  print()
print("Printing Current Working Directory")
cwd=os.getcwd()
print("\nos.getcwd()",cwd)

print("\nChanging Current Working: ")
#Driver Code
current_path()
#Changing CWD
os.chdir("../")
#print CWD
current_path()

print("\nCreating Directory")
path="/"
print("These are files in root directory:")
print(os.listdir(path))

print("\nDeleting Files and Directories")
file="q3.py" #Files name which has to be removed
location="/home/student/Documents/AC" #Directory in which files is presented
print("\nListing Out Files and Dirs.",os.listdir(location))
path=os.path.join(location,file)

#removing the file q1.py
os.remove(path)
print("\nListing Out Files and Dirs.",os.listdir(location))
