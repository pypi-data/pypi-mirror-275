import pyzipper
import itertools
import PyPDF2

def crack_zip():
  
    zip_file_path = input("\nEnter ZIP File Path: ")
    numconfirm = input("\nIs The Password Contains Numbers? (if don't know, enter 'yes') (yes / no): ")
    charconfirm = input("\nIs The Password Contains Characters? (if don't know, enter 'yes') (yes / no): ")
    specialcharconfirm = input("\nIs The Password Contains Special Characters? (if don't know, enter 'yes') (yes / no): ")
   
    combinations = []

    if charconfirm.lower() in ("yes", "y"):
        combinations.append("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

    if specialcharconfirm.lower() in ("yes", "y"):
        combinations.append("!@#$%^&*()?/<>.,;':\"|\\")

    if numconfirm.lower() in ("yes", "y"):
        combinations.append("0123456789")

    exact_length = input("\nEnter Exact Length Of Password If You know Else Enter 'n' : ")
    password_length = 0

    if exact_length.lower() == "n":

        password_length = input("\nEnter Maximun Guessed Password Length (eg . 6 numbers or 9 characters ) : ")
        start_length = 1

    else:

        start_length = int(exact_length)
        password_length = exact_length

    print(combinations)
    password_found = False

    file_name = zip_file_path.split(".")[0]

    if "/" in file_name:
        file_name = file_name[file_name.rfind("/")+1:]
    print("\nCracking ZIP Password")
    for r in range(start_length, int(password_length) + 1):
        if password_found:
            break
        for combo in itertools.product(*combinations, repeat=r):
            password = ''.join(combo)
            
            try:
                with pyzipper.AESZipFile(zip_file_path) as zf:
                    zf.extractall(path=file_name + "/", pwd=password.encode())
                    print("Password Found:", password)
                    print("\nZip File Extracted To The Current Directory.")
                    password_found = True
                    break
            except:
                continue

    if not password_found:
        print("Password not found.")

def crack_pdf():
    
    pdf_file_path = input("\nEnter PDF File Path : ")

    combinations = ""

    numconfirm = input("\nIs The Password Contains Numbers ? ( if dont know , enter 'yes') ( yes / no ) : ")

    charconfirm = input("\nIs The Password Contains Characters ? ( if dont know , enter 'yes') ( yes / no ) : ")

    specialcharconfirm = input("\nIs The Password Contains Special Characters ? ( if dont know , enter 'yes') ( yes / no ) : ")

    if charconfirm.lower() == "yes" or charconfirm.lower() == "y":
        combinations += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if specialcharconfirm.lower() == "yes" or specialcharconfirm.lower() == "y":
        combinations += "!@#$%^&*()?/<>.,;':\"|\\"

    if numconfirm.lower() == "yes" or numconfirm.lower() == "y":
        combinations += "0123456789"

    exact_length = input("\nEnter Exact Length Of Password If You know Else Enter 'n' : ")
    password_length = 0

    if exact_length.lower() == "n":

        password_length = input("\nEnter Maximun Guessed Password Length (eg . 6 numbers or 9 characters ) : ")
        start_length = 1

    else:

        start_length = int(exact_length)
        password_length = exact_length

    print(combinations)

    password_found = False
    print("\nCracking PDF Password .....")
    for r in range(start_length, int(password_length)+1):
        if password_found:
            break  

        combination = itertools.product(combinations, repeat=r)
        for combo in combination:
            password = ''.join(combo)
           
            try:
            
                with open(pdf_file_path, 'rb') as pdf_file:
                    pdf_reader = PyPDF2.PdfReader(pdf_file)
                   
                    if pdf_reader.is_encrypted:
                        if pdf_reader.decrypt(password) == 1:
                            print("\nSuccessfully decrypted the PDF file.")
                            print("Password Is : " + password)
                            password_found = True
                            break  
                        
            except FileNotFoundError:
                print("Error: File not found.")
                break  
            
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                break 
        
        print(len(password) , "Iterations Completed")

def main():
    ascii_art = """
     _______         _____     _  __     _____          _                 
    |___  (_)        |  __ \  | |/ _|  / ____|         | |                
        / / _ _ __   | |__) |_| | |_  | |     _ __ __ _| | _____ ___ _ __ 
       / / | | '_ \  |  ___/ _` |  _| | |    | '__/ _` | |/ / __/ _ \ '__|
      / /__| | |_) | | |  | (_| | |   | |____| | | (_| |   < (_|  __/ |   
     /_____|_| .__/  |_|   \__,_|_|    \_____|_|  \__,_|_|\_\___\___|_|   
            | |                                                          
            |_|                                                          
    """
    print(ascii_art)
    print("=" * 60)
    print(" " * 16 + "Welcome to Zip / Pdf Cracker")
    print("=" * 60)

    print("\nPlease choose an option:\n")
    print("[1] Crack PDF Password")
    print("[2] Crack ZIP Password")
        
    while True:
        choice = input("\nEnter your choice (1 or 2): ").strip()
        if choice in ['1', '2']:
            break
        print("Invalid choice. Please enter 1 or 2.")
        
    print("=" * 60)
    if choice == '1':
        print("You selected Crack PDF Password.")
        crack_pdf()

    elif choice == '2':
        print("You selected Crack ZIP Password.")
        crack_zip()
    print("\n","=" * 60)

if __name__ == "__main__":
    main()