# === Tipe Data Standar ===

# INTEGER (Angka Satuan)
dataInteger = 100
print("Data :", dataInteger, ", bertipe :", type(dataInteger))

# FLOAT (Angka dengan Koma)
dataFloat = 5.5
print("Data :", dataFloat, ", bertipe :", type(dataFloat))

# STRING (Karakter, diapit dengan tanda petik)
dataString = "Frisco"
print("Data :", dataString, ", bertipe :", type(dataString))

# BOOLEAN (True or False)
dataBoolean = True
print("Data :", dataBoolean, ", bertipe :", type(dataBoolean))


# === Tipe Data Khusus === #

# Tipe Data dari Bahasa C
from ctypes import c_double, c_char, c_long
dataDouble = c_double(10.5)
print("Data :", dataDouble, ", bertipe :", type(dataDouble))