from . import operasi

DBNAME = "anisong.txt"

TEMPLATE = {
    "pk" : "XXXXXX",
    "dateadd" : "YYYY-MM-DD",
    "judul" : " "*255,
    "ongakuka" : " "*255,
    "tahun" : "XXXX"
}

def init_console():
    try:
        with open(DBNAME,"r") as file:
            print("databesu wa arimashita")
    except:
        print("databesu wa arimasendeshita, ima kara tsukurimasu")
        operasi.create_new_data()
