import sys
import numpy as np
import matplotlib.pyplot as plt
import math

print('NAMA : SRI ADININGSI')
print('NIM : E1E120020')
print('PROGRAM MENENTUKAN FUNGSI KEANGGOTAAN')


def Linear():
    print('1. Linear Naik')
    print('2. Linear Turun')
    menu = int(input('Masukkan pilihan anda : '))
    if (menu == 1):
        a = float(input('Masukkan nilai a = '))
        b = float(input('Masukkan nilai b = '))
        input_x = int(input('Masukkan nilai x = '))

        def linear_naik(a, b, x):
            if x <= a:
                return 0.0
            elif x >= b:
                return 1.0
            else:
                return (x - a) / (b - a)
        print('Nilai derajat keanggotaan = ', linear_naik(a, b, input_x))

        x = np.linspace(0, b+50, 10000)
        y = [linear_naik(a, b, i) for i in x]

        # menampilkan grafik
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('Keanggotaan')
        plt.title('Fungsi Keanggotaan Linear Naik')

        if input_x < 0 or input_x > 10000:
            print("Nilai x harus antara 0 dan 600")
        else:
            y_input = linear_naik(a, b, input_x)
            plt.plot(x, y)
            plt.xlabel('x')
            plt.ylabel('Keanggotaan')
            plt.title('Fungsi Keanggotaan Linear Naik')
            plt.axvline(x=input_x, color='r', linestyle='--')
            plt.axhline(y=y_input, color='r', linestyle='--')
            plt.text(input_x+5, y_input+0.05,
                     f'({input_x:.2f}, {y_input:.2f})')
            plt.show()

    elif (menu == 2):
        a = float(input('Masukkan nilai a = '))
        b = float(input('Masukkan nilai b = '))
        input_x = int(input('Masukkan nilai x = '))

        def linear_turun(a, b, x):
            if x <= a:
                return 1.0
            elif x >= b:
                return 0.0
            else:
                return (b - x) / (b - a)
        print('Nilai derajat keanggotaan = ', linear_turun(a, b, input_x))

        x = np.linspace(0, b+50, 10000)
        y = [linear_turun(a, b, i) for i in x]

        # menampilkan grafik
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('Keanggotaan')
        plt.title('Fungsi Keanggotaan Linear ')

        if input_x < 0 or input_x > 10000:
            print("Nilai x harus antara 0 dan 10000")
        else:
            y_input = linear_turun(a, b, input_x)
            plt.plot(x, y)
            plt.xlabel('x')
            plt.ylabel('Keanggotaan')
            plt.title('Fungsi Keanggotaan Linear Naik')
            plt.axvline(x=input_x, color='r', linestyle='--')
            plt.axhline(y=y_input, color='r', linestyle='--')
            plt.text(input_x+5, y_input+0.05,
                     f'({input_x:.2f}, {y_input:.2f})')
            plt.show()
    else:
        print('Pilihan anda tidak ada dalam program')


def Segitiga():
    a = float(input('Masukkan nilai a = '))
    b = float(input('Masukkan nilai b = '))
    c = float(input('Masukkan nilai c = '))
    x = float(input('Masukkan nilai x = '))

    def linear_segitiga(a, b, c, x):
        if x <= a:
            return 0.0
        elif a < x <= b:
            return (x - a) / (b - a)
        elif b < x < c:
            return (c - x) / (c - b)
        else:
            return 0.0
    print('Nilai derajat keanggotaan = ', linear_segitiga(a, b, c, x))

    y = linear_segitiga(a, b, c, x)

    plt.plot([a, b, c], [0, 1, 0])
    plt.axvline(x, color='r', linestyle='--')
    plt.plot(x, y, 'o')
    plt.axhline(y, color='r', linestyle='--')
    plt.title("Fungsi Keanggotaan Linear Segitiga")
    plt.xlabel("Nilai X")
    plt.ylabel("Nilai Keanggotaan")
    plt.ylim(-0.1, 1.1)
    plt.show()


def Trapesium():
    a = float(input('Masukkan nilai a = '))
    b = float(input('Masukkan nilai b = '))
    c = float(input('Masukkan nilai c = '))
    d = float(input('Masukkan nilai d = '))
    x = float(input('Masukkan nilai x = '))

    def linear_trapesium(a, b, c, d, x):
        if x <= a or x >= d:
            return 0.0
        elif a < x <= b:
            return (x - a) / (b - a)
        elif b < x <= c:
            return 1.0
        elif c < x < d:
            return (d - x) / (d - c)
        else:
            return 0.0
    print('Nilai derajat keanggotaan = ', linear_trapesium(a, b, c, d, x))

    y = linear_trapesium(a, b, c, d, x)

    plt.plot([a, b, c, d], [0, 1, 1, 0])
    plt.axvline(x, color='r', linestyle='--')
    plt.axvline(b, color='g', linestyle='--')
    plt.axvline(c, color='g', linestyle='--')
    plt.plot(x, y, 'o')
    plt.axhline(y, color='r', linestyle='--')
    plt.title("Fungsi Keanggotaan Linear Trapesium")
    plt.xlabel("Nilai X")
    plt.ylabel("Nilai Keanggotaan")
    plt.ylim(-0.1, 1.1)
    plt.show()


def Sigmoid():
    print('1. Sigmoid Pertumbuhan')
    print('2. Sigmoid Penyusutan')
    menu = int(input('Masukkan pilihan anda : '))
    if (menu == 1):
        r1 = float(input("Masukkan nilai r1 = "))
        r2 = float(input("Masukkan nilai r2 = "))
        x = float(input("Masukkan nilai x = "))

        def sigmoid_pertumbuhan(r1, r2, x):
            if x <= r1:
                return 0.0
            elif r1 < x <= r2-r1:
                return 2*((x-r1)/(r2-r1))**2
            elif r2-r1 <= x <= r2:
                return 1-2*((r2-x)/(r2-r1))**2
            else:
                return 1.0
        print('Nilai derajat keanggotaan = ', sigmoid_pertumbuhan(r1, r2, x))

    elif (menu == 2):
        r1 = float(input("Masukkan nilai r1 = "))
        r2 = float(input("Masukkan nilai r2 = "))
        x = float(input("Masukkan nilai x = "))

        def sigmoid_penyusutan(r1, r2, x):
            if x <= r1:
                return 1.0
            elif r1 < x <= r2-r1:
                return 1-2*((x-r1)/(r2-r1))**2
            elif r2-r1 <= x <= r2:
                return 2*((r2-x)/(r2-r1))**2
            else:
                return 0.0
        print('Nilai derajat keanggotaan = ', sigmoid_penyusutan(r1, r2, x))


def Gauss():
    x = float(input("Masukkan nilai x = "))
    a = float(input("Masukkan nilai a = "))
    k = float(input("Masukkan nilai k = "))

    def linear_gaus(x, a, k):
        return math.exp(-k * (a - x)**2)
    print('Nilai derajat keanggotaan = ', linear_gaus(x, a, k))


def Beta():
    a = float(input("Masukkan nilai a = "))
    b = float(input("Masukkan nilai b = "))
    x = float(input("Masukkan nilai x = "))

    def linear_beta(a, b, x):
        return 1 / (1 + ((x - a) / b) ** 2)
    print('Nilai derajat keanggotaan = ', linear_beta(a, b, x))


def Keluar():
    print("Program Selesai")
    sys.exit()


print("\n")
pilih = 1
while pilih <= 7:
    print('Pilih Menu Fungsi : ')
    print('1. Linear ')
    print('2. Segitiga')
    print('3. Trapesium')
    print('4. Sigmoid')
    print('5. Gauss')
    print('6. Beta')
    print('7. Keluar')
    pilih = int(input('Masukkan Pilihan anda : '))
    if pilih == 1:
        Linear()
        print("\n")
    if pilih == 2:
        Segitiga()
        print("\n")
    if pilih == 3:
        Trapesium()
        print("\n")
    if pilih == 4:
        Sigmoid()
        print("\n")
    if pilih == 5:
        Gauss()
        print("\n")
    if pilih == 6:
        Beta()
        print("\n")
    if pilih == 7:
        Keluar()
        print("\n")
