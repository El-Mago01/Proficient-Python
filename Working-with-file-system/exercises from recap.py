import os

PROJECT_DIR = "project"
MODULE_DIR = "module"
CURRENT_DIR = os.getcwd()

try:
    print("Making both directories Project and Module")
    os.mkdir(PROJECT_DIR)
    os.mkdir(os.path.join(PROJECT_DIR, MODULE_DIR))

    print("Content of Project Dir: ", os.listdir(PROJECT_DIR))

    print(f"Changing directory to {PROJECT_DIR}")
    os.chdir(PROJECT_DIR)

    print(f"Renaming {MODULE_DIR} to ../. ")
    # print(f"Command provided: os.rename({MODULE_DIR},)")
    os.rename(MODULE_DIR,os.path.join("..",MODULE_DIR))
    print("Rename successful")

    print(f"Changing directory to {CURRENT_DIR}")
    os.chdir(CURRENT_DIR)
    print("Deleting both directories Project and Module")
    os.rmdir(MODULE_DIR)
    os.rmdir(PROJECT_DIR)
    print("All is good. ")
except (FileExistsError, OSError) as e:
    print("sequence of file / directory transformations not possible due to : ", e)
    print(os.getcwd())
    print(os.listdir())
    try:
        print("Deleting both directories Project and Module")
        os.chdir(CURRENT_DIR)
        os.rmdir(os.path.join(PROJECT_DIR, MODULE_DIR))
        os.rmdir(PROJECT_DIR)
        print(f"Deletion of {PROJECT_DIR} and {MODULE_DIR} directories succeeded")
        print("Content of CWD",os.listdir())
    except (FileExistsError, OSError) as e:
        print("sequence of file / directory transformations not possible due to : ", e)
        print(os.getcwd())
        print(os.listdir())
