
# 1-savol: print() bu...

# #Javob:
    #print() bu malumotlarni funksiyalarni ozgaruvchilarni ekranga yani terminalga chiqazib beradi
# Kod namunasi:
print('Salom')
let = 'salom'
print(let)
# 2-savol: input() bu...

# #Javob:
#input bu foydalanuvchidan malumot olish uchun foydalaniladigan kod
# Kod namunasi:
parol = input('Parol kiriting: ')
# 3-savol: O'zgaruvchi nima?

# #Javob:
#ozgaruvchi bu bosh quti deb faras qilsa boladi uni ichiga nima yozsa usha boladi: son tekst hohlagan narsa
# Kod namunasi:
ozgaruvchi = 'Python'
ozgaruvchi2 = 10
# 4-savol: 4 ta maʼlumot turini sanab oʻting va misol keltiring:

# #Javob:
#Boolean- True,False
#int-Butun sonlar: 1 10 20 23
#float-Nuqtali sonlar: 1.7 302.4
#string- "" yoki ''ichidagi malumotlar hammasi string boladi: teks son 

# Kod namunasi:
#Boolean
print(type(True))
print(type(False))
#int
print(type(20))
#float
print(type(10.1))
#str
print(type('10.1'))
print(type('salom'))

# 5-savol: String formatlash nima va Pythonda ikkita formatlash usuliga misol keltiring:

# #Javob:
# f string formatlashni kop ozgaruvchilar va tekstni birlashtirish uchun qollaniladi

# Kod namunasi:
a = 'qalesan'
print(f'salom {a}')
# 6-savol: If, elif, else for nima va ular bilan misol ko'ring:

# #Javob:

#If, elif, else-bu agar degan manoni bildiradi misol: agar 10=10 bolsa shu ishni bajar

# Kod namunasi:
if 10>9:
    print('10katta 9dan')    
elif 11>10:
    print('11katta 10dan')
else:
    print('2ta son ham  kichik!')

# 7-savol: Taqqoslash operatorlarini sanab bering va ularga misol keltiring:

# #Javob:

# teng ==
# kichik <
# katta >
# katta yoki teng >=
# kichik yoki ten <=
# teng emas !=

# Kod namunasi:

son1 = 3
son2 = 7
print(son1<son2)
print(son2>son1)
print(son1==son2)
print(son1>=son2)
print(son1<=son2)
print(son1!=son2)

# 8-savol: Mantiqiy operatorlar and or not misol keltiring:

# #Javob:
#and,not,or,

# Kod namunasi:
s = 10
print(10==10 and 10==1)
print(10==3 or 11==11)
print(not 11>13)
# 9-savol: Loop nima va while sikli qanday ishlaydi:

# #Javob:
#sikl bu- while yoki for
#while sikli tekshirish uchun kerak bolib agar berilgan shart togri bolsa while tohtamasdan aylanib tekshiradi
# Kod namunasi:
while 10==10:
    print('10')
    break
# 10-savol: For va while o'rtasidagi farq nima va misol keltiring:
#For biz hohlagan martta kodlarni aylanib chiqadi
#while brek kodi yozilmaguncha aylanib chiqaveradi
# #Javob:
r = 0
for r in range(1,11) :
    print(r)
e=0
while e<=10:
    print(e)
    e+=1
# Kod namunasi:

# 11-chi: Endi siz o'yin qilishingiz kerak: tosh, qog'oz, qaychi.

# Ya'ni, bu o'yinni ikkita o'yinchi o'ynashiga ishonch hosil qilishingiz kerak, omad tilaymiz!

import random
print('Siz tosh qaychi qogoz oyniga kirdingiz\nkompyuterga qarshi=1\n2ta oyinchi=2')
oyin = input('1yoki 2ni tanlang: ')
oyin = int(oyin)
if oyin ==1:
    print('Siz kompyuter bilan oynashni tanladingiz!')
    while True:
        tosh = input('tosh qaychi qogoz dan birini tanlang: ').lower()
        qaychi = ['tosh','qaychi','qogoz']
        x = random.choice(qaychi)
        if tosh=='tosh' and x=='tosh':
            print('hech kim yutmadi!')
        elif tosh =='tosh' and x=='qaychi':
            print('Siz yutdingiz!')
            break
        elif tosh =='tosh' and x =='qogoz':
            print('kompyuter yutdi!')
        elif tosh =='qaychi' and x=='tosh':
            print('kompyuter yutdi!')
        elif tosh =='qaychi' and x=='qaychi':
            print('hech kim yutmadi!')
        elif tosh =='qaychi' and x=='qogoz':
            print('Siz yutdingiz!')
            break
        elif tosh =='qogoz' and x=='tosh':
            print('Siz yutdingiz!')
            break
        elif tosh =='qogoz' and x=='qaychi':
            print('kompyuter yutdi!')
        elif tosh =='qogoz' and x=='qogoz':
            print('hech kim yutmadi!')
        else:
            print('togri kiriting!')
elif oyin==2:
    print('Siz 2ta odam bilan oynashni tanladingiz!')
    while True:
        tosh = input('1-oyinchi tosh qaychi qogoz dan birini tanlang: ').lower()
        x = input('2-oyinchi tosh qaychi qogoz dan birini tanlang: ').lower()
        
        if tosh=='tosh' and x=='tosh':
            print('hech kim yutmadi!')
        elif tosh =='tosh' and x=='qaychi':
            print('1chi oyinchi yutdingiz!')
            break
        elif tosh =='tosh' and x =='qogoz':
            print('2chi oyinchi yutdi!')
            break
        elif tosh =='qaychi' and x=='tosh':
            print('2chi oyinchi yutdi!')
            break
        elif tosh =='qaychi' and x=='qaychi':
            print('hech kim yutmadi!')
        elif tosh =='qaychi' and x=='qogoz':
            print('1chi oyinchi yutdingiz!')
            break
        elif tosh =='qogoz' and x=='tosh':
            print('1chi oyinchi yutdingiz!')
            break
        elif tosh =='qogoz' and x=='qaychi':
            print('2chi oyinchi')
            break
        elif tosh =='qogoz' and x=='qogoz':
            print('hech kim yutmadi!')
        else:
            print('togri kiriting!')
