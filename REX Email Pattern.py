import re
check_email = "dineshgautam@prisma-soft.com.np"
pattern = r'^[a-zA-Z0-9]([._%+-]?[a-zA-Z0-9]){0,63}@(([a-zA-Z0-9]([-][a-zA-Z0-9])?)+)\.[a-zA-Z0-0]{2,}(\.[a-zA-Z])?'
match = re.match(pattern, check_email)

if match:
    print("It perfectly follows the valid email pattern.")
else:
    print("It does not follow the valid email pattern")

parts = check_email.split("@")
print(f"The local part is: {parts[0]} and the domain is: {parts[1]}")
