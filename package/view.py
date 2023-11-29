from . import operasi

def read_console():
    no = "No"
    judul = "Judul"
    ongakuka = "Ongakuka"
    tahun = "Tahun"

    print(100*"=")
    print(f"{no:3} | {judul:40} | {ongakuka:40} | {tahun:5}")
    print(100*"-")

    data = operasi.read()

    for no,isi in enumerate(data):
        isian = isi.split(",")
        pk = isian[0]
        dateadd = isian[1]
        judul = isian[2]
        ongakuka = isian[3]
        tahun = isian[4][:-1]
        print(f"{no+1:3} | {judul:.40} | {ongakuka:.40} | {tahun:5}")
    print("-"*100)

def create_console():
    while True:
        judul = input("Atarashii uta wo irete kudasai: ")
        ongakuka = input("Atarashii ongakuka wo irete kudasai: ")
        while True:
            try:
                tahun = int(input("atarashii toshi wo irete kudasai: "))
                if len(str(tahun)) == 4:
                    break
                else:
                    print("toshi no nagasa wa yon shika dekimasen")
            except:
                print("toshi wa bango desu")
        print("\nkono data de yoroshii desune?")
        print(f"1. judul = {judul}")
        print(f"2. ongakuka = {ongakuka}")
        print(f"3. tahun = {tahun}")

        yes = input("hai/iie: ")
        if yes == "hai":
            operasi.creato(judul,ongakuka,tahun)
            break

def update_console():
    read_console()
    while True:
        print("dono data wo kaetaindesuka?")
        try:
            no_anisong = int(input("bango:"))
            data = operasi.read(index = no_anisong)
        except:
            print("bango desu!")
        
        if data:
            data_break = data.split(",")
            pk = data_break[0]
            dateadd = data_break[1]
            judul = data_break[2]
            ongakuka = data_break[3]
            tahun = data_break[4][:-1]

            print("\n")
            print("dono paruto wo kaetaindesuka?")
            print(f"1. judul = {judul:.40}")
            print(f"2. ongakuka = {ongakuka:.40}")
            print(f"3. tahun = {tahun}")

            paruto = input("bango: ")
            match paruto:
                case "1" : judul = input("atarashii taitoru wo irete kudasai: ")
                case "2" : ongakuka = input("atarashii ongakuka wo irete kudasai: ")
                case "3" :
                    while True:
                        try:
                            tahun = int(input("atarashii toshi wo irete kudasai: "))
                            if len(str(tahun)) == 4:
                                break
                            else:
                                print("toshi no nagasa wa yon shika dekimasen!")
                        except:
                            print("toshi wa bango desu!")
            
            print("\n")
            print("kono data de yoroshii desune?")
            print(f"1. judul = {judul:.40}")
            print(f"2. ongakuka = {ongakuka:.40}")
            print(f"3. tahun = {tahun}")
            isyes = input("hai/iie: ")
            if isyes == "hai":
                operasi.apudeto(no_anisong,pk,dateadd,judul,ongakuka,tahun)
                break
        else:
            print("data wo yomu no ga dekimasen")
        
def delete_console():
    read_console()
    while True:
        print("dono data wo delito shitaindesuka?")
        try:
            no_anisong = int(input(("bango:")))
            data = operasi.read(index = no_anisong)
        except:
            print("data wa arimasen")
        if data:
            data_break = data.split(",")
            pk = data_break[0]
            dateadd = data_break[1]
            judul = data_break[2]
            ongakuka = data_break[3]
            tahun = data_break[4][:-1]

            print("\nkono data de yoroshii desuka?")
            print(f"1. judul: {judul:.40}")
            print(f"2. ongakuka: {ongakuka:.40}")
            print(f"3. tahun: {tahun}")
            isuyes = input("hai/iie: ")
            if isuyes == "hai":
                operasi.delete(no_anisong)
                break
        else:
            print("chanto yatte kudasai")
