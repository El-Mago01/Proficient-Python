import os
print(os.listdir())
print(os.getcwd())
# os.rename('copy.txt', 'test_dir/copy.txt')
# os.chdir("test_dir")
print(os.listdir())
print(os.environ['PATH'])
try:
    os.chdir("data")
except FileNotFoundError:
    os.mkdir("data")
    os.chdir("data")
print(os.listdir())
print(os.getcwd())
os.chdir("../.")
print(os.getcwd())
while True:
    try:
        os.rmdir("data")
        break
    except (FileNotFoundError, OSError):
        try:
            os.chdir("Backup")
            os.chdir("../.")
        except FileExistsError:
            os.mkdir("Backup")
        all_files_in_data=os.listdir("data")
        for file in all_files_in_data:
            os.rename(os.path.join("data",file),os.path.join("Backup",file))
print(os.listdir("Backup"))
print(os.getcwd())
print(os.listdir())
dir=os.path.join("test_dir","test_1")

# print(os.listdir(dir))
