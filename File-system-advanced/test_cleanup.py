import os
import pytest
from pathlib import Path
from invoice_organizer import cleanup

CUR_DIR = os.getcwd()
BACKUP_DIR=os.path.join(CUR_DIR,"Backup")
INVOICE_DIR = os.path.join(CUR_DIR, "invoices")
print(CUR_DIR)

def create_test_file(month, filename):
    try:
        target_dir=os.path.join(CUR_DIR, month)
        os.mkdir(target_dir)
    except FileExistsError:
        print(f"Directory {target_dir} already exists")
    try:
        Path(os.path.join(target_dir, filename)).touch()
    except FileExistsError as e:
        print(f"file {os.path.join(target_dir,filename)} already exists")

def test_cleanup_simple_case():
    print("HALLOOO - test_cleanup_simple_case")
    test_file = "martin_gorren_March.pdf"
    month="March"
    dir_to_check = os.path.join(CUR_DIR, month)
    create_test_file(month, test_file)
    cleanup()
    available_folders = os.listdir(CUR_DIR)
    file_stored = test_file
    assert (month in available_folders) == True
    assert (os.listdir(dir_to_check)) == []
    backup_files = os.listdir(BACKUP_DIR)
    file_moved_correctly = False
    for file in backup_files:
        if test_file in file:
            file_moved_correctly = True
            # print(file)
            break

    assert file_moved_correctly == True
