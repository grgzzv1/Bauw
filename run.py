# run.py

try:
    with open("Tetsu.so", "r") as file:
        script_content = file.read()
        exec(script_content)  # Execute the script inside Tetsu.txt
except FileNotFoundError:
    print("Error: Tetsu.txt not found! Make sure it is in the same directory.")
except Exception as e:
    print(f"An error occurred: {e}")