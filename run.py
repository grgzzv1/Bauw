# run.py

# Open and read the contents of Tetsu.txt
try:
    with open("Tetsu.txt", "r") as file:
        content = file.read()
        print("Contents of Tetsu.txt:")
        print(content)
except FileNotFoundError:
    print("Error: Tetsu.txt not found! Make sure it is in the same directory.")
