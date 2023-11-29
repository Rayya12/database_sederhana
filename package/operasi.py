from time import time
import time
from . import database
from .kunci import kagi
import os


def create_new_data():
    judul = input("taitoru wo irete kudasai: ")
    ongakuka = input("ongakuka wo irete kudasai: ")
    while True:
        try:
            tahun = int(input("toshi wo irete kudasai: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("tsumanai ga, dekimasen")
        except:
            print("toshi wa bango desu")
    
    data = database.TEMPLATE.copy()
    data['pk'] = kagi(6)
    data['dateadd'] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data['judul'] = judul + database.TEMPLATE['judul'][len(judul):]
    data['ongakuka'] = ongakuka + database.TEMPLATE['ongakuka'][len(ongakuka):]
    data['tahun'] = str(tahun)

    data_str = f"{data['pk']},{data['dateadd']},{data['judul']},{data['ongakuka']},{data['tahun']}\n"

    try:
        with open(database.DBNAME,"w",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("data wo tsukurunoga dekimasen")

def read(**kwargs):
    try:
        with open(database.DBNAME,"r") as file:
            hasil = file.readlines()
            if "index" in kwargs:
                index = kwargs["index"] - 1
                if index > len(hasil) or index <= 0:
                    return False
                else:
                    return hasil[index]
            return hasil
        
    except:
        print("nazeka data wo yomu koto ga dekimasen")

def creato(judul,ongakuka,tahun):
    data = database.TEMPLATE.copy()
    data['pk'] = kagi(6)
    data['dateadd'] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data['judul'] = judul + database.TEMPLATE['judul'][len(judul):]
    data['ongakuka'] = ongakuka + database.TEMPLATE['ongakuka'][len(ongakuka):]
    data['tahun'] = str(tahun)

    data_str = f"{data['pk']},{data['dateadd']},{data['judul']},{data['ongakuka']},{data['tahun']}\n"

    try:
        with open(database.DBNAME,"a",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("data wo creato suru no ga dekimasen!")

def apudeto(no_anisong,pk,dateadd,judul,ongakuka,tahun):
    data = database.TEMPLATE.copy()
    data['pk'] = pk
    data['dateadd'] = dateadd
    data['judul'] = judul + database.TEMPLATE['judul'][len(judul):]
    data['ongakuka'] = ongakuka + database.TEMPLATE['ongakuka'][len(ongakuka):]
    data['tahun'] = str(tahun)

    data_str = f"{data['pk']},{data['dateadd']},{data['judul']},{data['ongakuka']},{data['tahun']}\n"

    panjang = len(data_str)

    try:
        with open(database.DBNAME,"r+",encoding="utf-8") as file:
            file.seek(panjang*(no_anisong-1))
            file.write(data_str)
    except:
        print("databesu apudeto dekimasen")

def delete(no_anisong):
    try:
        with open(database.DBNAME,'r') as file:
            counter = 0
            while True:
                hasil = file.readline()
                if len(hasil) == 0:
                    break
                if (no_anisong-1) == counter:
                    pass
                else:
                    with open("datatemp.txt","a",encoding="utf-8") as newfile:
                        newfile.write(hasil)
                counter += 1

    except:
        print("daijobudesuka?")
    
    os.remove(database.DBNAME)
    os.rename("datatemp.txt",database.DBNAME)
