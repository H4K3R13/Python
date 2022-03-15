import os
print("Loop over directories and files:\n")
path='/tmp/'
for root,dirs,files in os.walk(path):
  print(root)
  for _dir in dirs:
    print(_dir)
  for _files in files:
    print(_files)
