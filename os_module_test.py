import os


print("#"*50)
print("This script gives information about the")
os.system('python3 --version')
print("#"*50)
print(os.name)
print(os.ctermid())
print(os.environ["_"])
print(os.environ["PATH"])
print(os.system('ps'))