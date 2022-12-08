from hashlib import md5

with open("../inputs/05.txt") as f:
    door_id = f.read().strip()

index = 0
password1 = ""
password2 = ["-"]*8

while len(password1) < 8 or "-" in password2:
    hashcode = md5(str.encode(door_id + str(index))).hexdigest()
    if hashcode.startswith("00000"): 
        if len(password1) < 8:
            password1 += hashcode[5] 
        if hashcode[5] in "01234567" and password2[int(hashcode[5])] == "-":
            password2[int(hashcode[5])] = hashcode[6]
    index += 1

print("Day 5 part 1: " + password1)
print("Day 5 part 2: " + "".join(password2))
