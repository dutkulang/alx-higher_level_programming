#!/usr/bin/python3

for i in range(100):
    if i <= 9:
        print(f"0{i:2.f}", end=", ")
    else:
        print(i, end=", ")
#!/usr/bin/python3

for i in range(100):
    if i <= 9:
        print("0{}".format(i), end=", ")
    else:
        print("{}".format(i), end=", ")
