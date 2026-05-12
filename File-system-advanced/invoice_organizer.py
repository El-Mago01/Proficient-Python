import os
import datetime
import shutil

CUR_DIR=os.getcwd()
INVOICE_DIR="invoices"
BACKUP_DIR="Backup"
MIN_LENGTH=5
MONTHS_LIST=["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November",
             "December"]

def cleanup():
    """
    Cleanup checks moves all the content of the folders that represents a month
    to the Backup folder. Additionally, it adds a timestamp to the filename and
    moves it to the backup folder.
    """
    if not os.path.exists(BACKUP_DIR):
        os.mkdir(BACKUP_DIR)

    for directory in os.listdir(CUR_DIR):
        if directory in MONTHS_LIST:
            files_to_move = os.listdir(os.path.join(CUR_DIR,directory))
            for file in files_to_move:
                print(f"backing up {file} to {BACKUP_DIR}")
                timestamp=datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
                src_dir=os.path.join(CUR_DIR, directory)
                src_file=os.path.join(src_dir,file)
                target_dir=os.path.join(CUR_DIR, BACKUP_DIR)
                target_file=os.path.join(target_dir, file) + timestamp
                try:
                    os.rename(src_file,target_file)
                except (FileNotFoundError,NotADirectoryError) as e:
                    print("Could not move file to the backup folder due to : ", e)
                    
                print(f"Successfully moved {file} to {target_file}")
            os.rmdir(directory)

def get_invoice_name(invoice_name : str):
    if ".pdf" not in invoice_name:
        return None
    file_name = invoice_name.split(".")[0]
    if "_" not in file_name or len(file_name) < MIN_LENGTH:
        return None
    month = file_name.split("_")[-1]
    return month

def main():
    cleanup()
    invoice_list = os.listdir(INVOICE_DIR)
    print(invoice_list)
    for invoice in invoice_list:
        month=get_invoice_name(invoice)
        if month:
            try:
                print(f"moving invoice {invoice} to the folder {month}")
                os.rename(os.path.join('invoices',invoice),os.path.join(month,invoice))
            except (FileNotFoundError,NotADirectoryError) as e:
                os.mkdir(month)
                try:
                    os.rename(os.path.join('invoices',invoice),os.path.join(month,invoice))
                except (FileNotFoundError,NotADirectoryError) as e:
                    print("Could not move invoice to the right location")
                    break
        else:
            print(f"Wrong name for the invoice {invoice}. File will not be moved")

if __name__ == "__main__":
    main()
