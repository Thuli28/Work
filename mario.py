# TODO
# keep prompting user for input until positive integer is enterd
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, Please input a positive integer,")
# Height of the pyramid
height = get_int("Height: ")
# Validate the height
while height < 1 or height > 8:
    print("Height must be between 1 and 8")
    height = get_int("height: ")
# Genarate the pyramid
for i in range(1, height + 1):
    print(" " * (height - i) + "#" * i)
