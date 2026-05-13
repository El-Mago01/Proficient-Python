filename=input("Enter the input file name     : ")
search_for=input("Enter a string to search for: ")
replace_by=input("Enter a string to replace by: ")


def search_and_replace(search_for,replace_by) -> bool:
    try:
        with open(filename,'r') as file:
            text=file.read()
            text = text.replace(search_for, replace_by)
            search_for=search_for[0].upper()+search_for[1:]
            replace_by=replace_by[0].upper()+replace_by[1:]
            text=text.replace(search_for, replace_by)
    except FileNotFoundError:
        print("File not found")
        return False
    except OSError:
        print("Could not open file")
        return False
    try:
        with open(filename+".new",'w') as file:
            file.write(text)
    except OSError:
        print("Could not write to the new file")
        return False

search_and_replace(search_for,replace_by)