#Muhammad ibdaul mutafakkir
#TI23C
def konversi(string):
    try:
        intgr = int(string)
        print(f"{string} berhasil dikonversi ke integer")
        
    except ValueError:
        print(f'{string} tidak dapat diknversi ke integer')
konversi("123")
konversi("abc")

def akseselemen(daftr_list,indeks):
    try:
        elemen =daftr_list[indeks]
        print(f'elemen di index {indeks} adalah {elemen}')   
    except IndexError:
        print('kesalahan,index diluar jangkauan')

list_sy = [1,2,3]
akseselemen(list_sy,1)
akseselemen(list_sy,5)