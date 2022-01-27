import mysql.connector
db = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="",
 database="db_akademik_"
)

cursor = db.cursor()
sql = "INSERT INTO tbl_students_ (id, nim, nama, jk, jurusan, alamat) VALUES (%s, %s, %s, %s, %s, %s)"
values = [
 ("1","20.90.1234","Mansur Tri","L","Teknik Komputer","Yogyakarta"),
 ("2","20.90.1235","Agung Surya","L","Informatika","Sleman"),
 ("3","20.90.1236","Krisna Imran","L","Sistem Informasi","Bantul"),
 ("4","20.90.1237","Kusuma Ruslan","L","Teknologi Informasi","Gunung Kidul"),
 ("5","20.90.1238","Bagus Sri","L","Teknik Elektro","Kulonprogo"),
 ("6","20.90.1239","Irfan Harun","L","Informatika","Sleman"),
 ("7","20.90.1230","Dian Akhmad","L","Informatika","Sleman"),
 ("8","20.90.1231","Lutfi Ali","L","Sistem Informasi","Sleman"),
 ("9","20.90.1232","Zulfikar Amir","L","Teknik Komputer","Sleman"),
 ("10","20.90.1232","Yuda Ismail","L","Teknologi Informasi","Bantul"),
 ("11","20.90.1241","Saiful Lutfi","L","Teknik Komputer","Gunung Kidul"),
 ("12","20.90.1242","Mahmud Amir","L","Teknik Komputer","Sleman"),
 ("13","20.90.1243","Buana Wira","L","Teknik Elektro","Sleman"),
 ("14","20.90.1244","Zakaria Aditya","L","Teknik Elektro","Bantul"),
 ("15","20.90.1245","Bima Hasan","L","Teknik Komputer","Sleman"),
 ("16","20.90.1246","Dwi Anwar","L","Teknik Komputer","Gunung Kidul"),
 ("17","20.90.1247","Eka Imran","L","Teknik Komputer","Bantul"),
 ("18","20.90.1248","Bachtiar Abdul","L","Teknik Komputer","Sleman"),
 ("19","20.90.1249","Akbar Lutfi","L","Teknik Komputer","Sleman"),
 ("20","20.90.1250","Adi Eka","L","Teknik Komputer","Sleman"),
 ("21","20.90.1252","Nur Arif","L","Sistem Informasi","Sleman"),
 ("22","20.90.1253","Tirto Guntur","L","Sistem Informasi","Sleman"),
 ("23","20.90.1251","Akhmad Ahmad","L","Teknik Komputer","Gunung Kidul"),
 ("24","20.90.1255","Muhamad Anwar","L","Sistem Informasi","Yogyakarta"),
 ("25","20.90.1254","Amir Mansur","L","Teknik Komputer","Gunung Kidul")
 #{"id":"26","nim":"20.90.1257","nama":"Wati Sri Batari","jk":"P","jurusan":"Informatika","alamat":"Sleman"},
 #{"id":"27","nim":"20.90.1256","nama":"Annisa Ratna Dwi","jk":"P","jurusan":"Teknik Komputer","alamat":"Sleman"},
 #{"id":"28","nim":"20.90.1258","nama":"Aisyah Annisa Vina","jk":"P","jurusan":"Teknik Komputer","alamat":"Sleman"},
 #{"id":"29","nim":"20.90.1259","nama":"Kusuma Nurul Kasih","jk":"P","jurusan":"Informatika","alamat":"Sleman"},
 #{"id":"30","nim":"20.90.1261","nama":"Dwi Yuliana Nurul","jk":"P","jurusan":"Teknik Komputer","alamat":"Sleman"},
 #{"id":"31","nim":"20.90.1260","nama":"Wangi Tri Kasih","jk":"P","jurusan":"Teknik Komputer","alamat":"Bantul"},
 #{"id":"32","nim":"20.90.1263","nama":"Mawar Yuliana Nirmala","jk":"P","jurusan":"Teknologi Informasi","alamat":"Sleman"},
 #{"id":"33","nim":"20.90.1265","nama":"Wangi Putri Siti","jk":"P","jurusan":"Teknologi Informasi","alamat":"Kulonprogo"},
 #{"id":"34","nim":"20.90.1264","nama":"Annisa Aisyah Cahaya","jk":"P","jurusan":"Teknik Komputer","alamat":"Kulonprogo"},
 #{"id":"35","nim":"20.90.1266","nama":"Aisyah Ratna Fatimah","jk":"P","jurusan":"Teknik Komputer","alamat":"Bantul"},
 #{"id":"36","nim":"20.90.1267","nama":"Kusuma Latifah Yuliana","jk":"P","jurusan":"Teknik Komputer","alamat":"Sleman"},
 #{"id":"37","nim":"20.90.1268","nama":"Cahaya Intan Melati","jk":"P","jurusan":"Teknik Komputer","alamat":"Sleman"},
 #{"id":"38","nim":"20.90.1269","nama":"Asih Alya Tri","jk":"P","jurusan":"Teknik Komputer","alamat":"Sleman"},
 #{"id":"39","nim":"20.90.1270","nama":"Nirmala Mega Ratna","jk":"P","jurusan":"Teknik Komputer","alamat":"Yogyakarta"},
 #{"id":"40","nim":"20.90.1271","nama":"Ratna Siti Kusuma","jk":"P","jurusan":"Teknik Komputer","alamat":"Kulonprogo"},
 #{"id":"41","nim":"20.90.1272","nama":"Batari Iman Alya","jk":"P","jurusan":"Teknik Komputer","alamat":"Kulonprogo"},
 #{"id":"42","nim":"20.90.1273","nama":"Vina Mawar Aminah","jk":"P","jurusan":"Teknik Komputer","alamat":"Sleman"},
 #{"id":"43","nim":"20.90.1274","nama":"Tirta Wati Sitti","jk":"P","jurusan":"Teknik Komputer","alamat":"Sleman"},
 #{"id":"44","nim":"20.90.1275","nama":"Dewi Tirta Fatimah","jk":"P","jurusan":"Teknologi Informasi","alamat":"Bantul"},
 #{"id":"45","nim":"20.90.1276","nama":"Kusuma Bulan Kasih","jk":"P","jurusan":"Teknik Komputer","alamat":"Sleman"},
 #{"id":"46","nim":"20.90.1277","nama":"Indah Nirmala Intan","jk":"P","jurusan":"Sistem Informasi","alamat":"Sleman"},
 #{"id":"47","nim":"20.90.1278","nama":"Fatimah Alya Sitti","jk":"P","jurusan":"Teknik Komputer","alamat":"Yogyakarta"},
 #{"id":"48","nim":"20.90.1279","nama":"Batari Fatimah Aminah","jk":"P","jurusan":"Sistem Informasi","alamat":"Bantul"},
 #{"id":"49","nim":"20.90.1280","nama":"Fatimah Putri Tirta","jk":"P","jurusan":"Teknik Komputer","alamat":"Sleman"},
 #{"id":"50","nim":"20.90.1288","nama":"Intan Mawar Anisa","jk":"P","jurusan":"Teknik Komputer","alamat":"Yogyakarta"}
]

for val in values:
 cursor.execute(sql, val)
 db.commit()
print("{} data ditambahkan".format(len(values)))

Data = {};
loop = True;

print("============= MENU ============");
print("[1] Tampilkan Semua Data ");
print("[2] Tampilkan Data Limit");
print("[3] Cari Berdasarkan NIM");
print("[4] Keluar");


while(loop==True):
    print("\n\n");
    menu = int(input("Masukan menu : "));
    if menu == 1:
     cursor = db.cursor()
     sql = "SELECT * FROM tbl_students_"
     cursor.execute(sql)

     results = cursor.fetchall()

     for data in results:
      print(data)

    elif menu == 2:
     cursor = db.cursor()
     sql = "SELECT * FROM tbl_students_"
     cursor.execute(sql)

     results = cursor.fetchmany(int(input("masukkan limit: ")))

     for data in results:
      print(data)
    elif menu == 3:
     cursor = db.cursor()
     keyword = input("id: ")
     sql = "SELECT * FROM tbl_students_ WHERE id LIKE %s OR nama LIKE %s"
     val = ("%{}%".format(keyword), "%{}%".format(keyword))
     cursor.execute(sql, val)
     results = cursor.fetchall()

     if cursor.rowcount < 0:
      print("Tidak ada data")
     else:
      for data in results:
       print(data)

    elif menu == 4:
        loop = False;
    else:
        print("XXXX");



