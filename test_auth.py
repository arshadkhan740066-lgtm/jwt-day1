from auth import hash_password, verify_password


password = "123456"

hashed_password = hash_password(password)

print("Original password:", password)
print("Hashed password:", hashed_password)

result = verify_password(password, hashed_password)

print("Password correct:", result)