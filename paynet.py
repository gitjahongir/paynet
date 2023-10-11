from datetime import datetime,timedelta

def paynet(a):
    if a == "1":
        b = input("Siz 1 ni tanladingiz!\nIltimos,hisob raqamingizni kiriting:")
        if (b[0] == "+") and (b[1:4] == "998") and ((b[1:]).isnumeric()) and (b[4:6] == 33 or 50 or 66 or 90 or 91 or 92 or 93 or 94 or 95 or 99):
            c = int(input("Hisob Raqamingizga qancha mablag' kiritmoqchisiz?:"))
            prosent = c/100*10
            return f"Hisob raqam:{b}\nKiritildi:{c} so'm\nO'tkazildi:{c-prosent} so'm\nOperatsiya vaqti:{datetime.now()}"
        else:
                return "Hisob raqamingizni to'g'ri kiriting!"
    elif a == "2":
        b2 = input("Siz 2 ni tanladingiz!\nDavlat xizmatlari uchun oylik to'lov:400,000 so'mni tashkil qiladi\nTo'lovni amalga oshirmoqchimisiz?:")
        if b2 == "Ha":
            c2 = input("Hisob Raqamingizni kirting:")
            if (c2[0] == "+") and (c2[1:4] == "998") and ((c2[1:]).isnumeric()) and (c2[4:6] == 33 or 50 or 66 or 90 or 91 or 92 or 93 or 94 or 95 or 99):
                return f"Hisob Raqam:{c2}\nYechib olindi:400,000 so'm\nOperatsiya vaqti:{datetime.now()}"
        elif b2 == "Yo'q":
            return f"Keyingi to'lov amalga oshirish vaqti:{datetime.now()} sanadan boshlab  {datetime.now()+timedelta(days=31)} gacha"
print(paynet(input("Assalomu Alaykum,Paynet Ilovasiga hush kelibsiz!\nHisob raqamingizga to'lov qilmoqchi bo'lsangiz,1 ni bosing\nJarima va davlat xizmatlariga to'lov qilmoqchi bo'lsangiz,2ni bosing:")))
