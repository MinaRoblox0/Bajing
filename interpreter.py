class sys:
    import random
    import sys
    import time


filename = sys.sys.argv[1]

with open(filename, "r") as file:
    global input, input1, input2, x

    x = sys.random.randint(1, 3)
    lines = file.readlines()  # Read the file into a list
    for line in lines:
        if line == "":
            continue
        elif line.startswith("PRINT "):
            prompt = line[len("PRINT "):].strip()
            if prompt == "$FILENAME":
                print(filename)
            else:
                print(prompt)

        elif line.startswith("MATH "):
            prompt = line[len("MATH "):].strip()
            try:
                result = eval(prompt)
                print(result)
            except:
                print("ERROR 132")
                print("PLEASE ONLY USE MATH")

        elif line.startswith("SLEEP "):
            prompt = line[len("SLEEP "):].strip()
            try:
                promptInt = int(prompt)
                sys.time.sleep(promptInt)
            except ValueError:
                print("VALUE ERROR 102")
                print("PLEASE ONLY USE NUMBERS OR DELETE THE VALUE ERROR")
        elif line == "EXIT" or line == "LEAVE":
            exit()