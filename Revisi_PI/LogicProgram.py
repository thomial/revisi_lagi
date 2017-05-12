import numpy as np

from models import *
import math

class Regresi:

    def __init__(self, nil, nil2, ber, ber2, nilber, n):
        self.nil = nil
        self.nil2 = nil2
        self.ber = ber
        self.ber2 = ber2
        self.nilber = nilber
        self.n = n

    def a(self):
        return ((self.nil * self.nil2) - (self.ber * self.nilber)) / ((self.n * self.ber2) - (self.ber ** 2))

    def b(self):
        return ((self.n * self.nilber) - (self.ber * self.nil)) / ((self.n * self.nil2) - (self.nil ** 2))

    def regresi(self, x):
        a = self.a()
        b = self.b()
        reg = a + (b * x)
        return reg


class Korelasi:
    def korelasi(self, nil, nil2, ber, ber2, nilber, n):
        return ((n * nilber) - (nil * ber)) / (math.sqrt(((n * ber2) - ber ** 2) * ((n * nil2) - nil ** 2)))


class Hitung_Regresi_korelasi:
    def __init__(self, id):
        self.nil2 = 0
        self.nil = 0
        self.ber = 0
        self.ber2 = 0
        self.nilber = 0
        self.id = id
        # self.x = x

    def ambil_data(self):
        data = Import_Nilai.objects.filter(post_id=self.id)
        for i in data:
            nil2p = i.nilai ** 2
            self.nil2 += nil2p  # y2
            self.nil += i.nilai  # y
            ber2p = i.berat ** 2
            self.ber2 += ber2p  # x2
            self.ber += i.berat  # x
            nilberp = i.berat * i.nilai
            self.nilber += nilberp  # xy\
            self.tahun = i.tahun

        n = data.count()
        ObjRegresi = Regresi(self.nil, self.nil2, self.ber, self.ber2, self.nilber, n)
        ObjKorelasi = Korelasi()
        # Reg = ObjRegresi.regresi(self.x)
        Reg_a = ObjRegresi.a()
        Reg_b = ObjRegresi.b()
        Kor = ObjKorelasi.korelasi(self.nil, self.nil2, self.ber, self.ber2, self.nilber, n)
        return Reg_a, Reg_b, Kor, self.tahun


class Data:

    def __init__(self, id):

        self.id = id

    def ambil_data(self):
        import numpy as np
        nil_imp = Import_Nilai
        upload = table_post_description.objects.get(id = self.id)
        upload_doc = upload.document

        data = np.genfromtxt("media/%s" %upload_doc, dtype=None, delimiter=',', names=True )

        for row in data :
            a = nil_imp(
                tahun=row['tahun'],
                bulan=row['bulan'],
                berat=row['berat'],
                nilai=row['nilai']
            )
            a.post_id = upload.id
            a.save()

    def set_regresi_korelasi(self):
        regkor = Hitung_Regresi_korelasi(self.id)
        reg_a, reg_b, kor, tahun = regkor.ambil_data()

        a = regresi_korelasi(
            tahun= tahun,
            hasil_regresi_a= reg_a,
            hasil_regresi_b= reg_b,
            hasil_korelasi= kor
        )

        a.post_id = self.id
        a.save()










