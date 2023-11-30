# program untuk membuat database sederhana
import os
import package
import time


if __name__ == "__main__":
    start_time = time.time()
    sistem_operasi = os.name
    match sistem_operasi:
        case "pusix" : os.system("clear")
        case "nt" : os.system("cls")
    print("Anisong database he youkoso!")
    print("Sukina opening to ending wo irete kudasai!")
    print("="*100)
    package.database.init_console()
    while True:
        match sistem_operasi:
            case "pusix" : os.system("clear")
            case "nt" : os.system("cls")
        print("Anisong database he youkoso!")
        print("Sukina opening to ending wo irete kudasai!")
        print("="*100)
        print("kyou wa nani no nasai masuka?")
        print("1. data wo yomu")
        print("2. data wo tsukuru")
        print("3. data wo apudeto")
        print("4. data wo delito")
        erabe = input("bango: ")
        print('\n')
        match erabe:
            case "1" : package.view.read_console()
            case "2" : package.view.create_console()
            case "3" : package.view.update_console()
            case "4" : package.view.delete_console()
        
        ischoice = input("\nkorede yoroshii desuka (hai/iie): ")
        if ischoice == "hai":
            print(time.time()-start_time,"detik")
            time.sleep(3)
            break
    match sistem_operasi:
        case "pusix" : os.system("clear")
        case "nt" : os.system("cls")
