#penjumlahan
def add(a,b):
    return a + b
#pengurangan
def subtract(a,b):
    return a - b
#perkalian  
def multiply(a,b):
    return a * b
#pembagian
def devide(a,b):
    return a / b

#menu operasi
print("Pilihlah operasi berikut: ")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
choice = (input ("Masukkan metode (1/2/3/4): "))

num1 = int (input("Masukkan Bilangan Pertama: "))
num2 = int (input("Masukkan Bilangan Kedua: "))

if choice == '1':
    print (num1, "+" , num2, "=", add(num1,num2))
elif choice == '2':
    print (num1, "-" , num2, "=", subtract(num1,num2))
elif choice == '3':
    print (num1, "*", num2, "=", multiply(num1,num2))
elif choice == '4':
    print (num1, "/", num2,"=", devide(num1,num2))