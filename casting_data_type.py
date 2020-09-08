# CASTING
# Mengubah suatu tipe data menjadi tipe data yang lain
# Tipe data yang tersedia: int, float, str, bool

print("=== INTEGER ===")
# Initial data (Integer)
dataInteger = 5
print("Data :", dataInteger, ", bertipe :", type(dataInteger))

# Mengubah menjadi Float
dataFloat = float(dataInteger)
print("Data :", dataFloat, ", bertipe :", type(dataFloat))

# Mengubah menjadi String
dataString = str(dataInteger)
print("Data :", dataString, ", bertipe :", type(dataString))

# Mengubah menjadi Boolean (Jika nilai int = 0, hasil False)
dataBoolean = bool(dataInteger)
print("Data :", dataBoolean, ", bertipe :", type(dataBoolean))

print("\n=== FLOAT ===")
# Initial data (Float)
dataFloat = 9.5
print("Data :", dataFloat, ", bertipe :", type(dataFloat))

# Mengubah menjadi Integer (akan dibulatkan ke bawah)
dataInteger = int(dataFloat)
print("Data :", dataInteger, ", bertipe :", type(dataInteger))

# Mengubah menjadi String
dataString = str(dataFloat)
print("Data :", dataString, ", bertipe :", type(dataString))

# Mengubah menjadi Boolean (Jika nilai float = 0, hasil False)
dataBoolean = bool(dataFloat)
print("Data :", dataBoolean, ", bertipe :", type(dataBoolean))

print("\n=== BOOLEAN ===")
# Initial data (Boolean)
dataBoolean = True
print("Data :", dataBoolean, ", bertipe :", type(dataBoolean))

# Mengubah menjadi Integer (True = 1, False = 2)
dataInteger = int(dataBoolean)
print("Data :", dataInteger, ", bertipe :", type(dataInteger))

# Mengubah menjadi String
dataString = str(dataBoolean)
print("Data :", dataString, ", bertipe :", type(dataString))

# Mengubah menjadi Float (True = 1.0, False = 0.0)
dataFloat = float(dataBoolean)
print("Data :", dataFloat, ", bertipe :", type(dataFloat))

print("\n=== STRING ===")
# Initial data (String)
dataString = "4"
print("Data :", dataString, ", bertipe :", type(dataString))

# Mengubah menjadi Integer (hanya karakter berupa angka yang bisa diubah)
dataInteger = int(dataString)
print("Data :", dataInteger, ", bertipe :", type(dataInteger))

# Mengubah menjadi Boolean (Jika string kosong menghasilkan False)
dataBoolean = str(dataBoolean)
print("Data :", dataBoolean, ", bertipe :", type(dataBoolean))

# Mengubah menjadi Float (hanya karakter berupa angka yang bisa diubah)
dataFloat = float(dataString)
print("Data :", dataFloat, ", bertipe :", type(dataFloat))