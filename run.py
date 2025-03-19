# run.py

try:
    with open("Tetsu.py", "r") as file:
        script_content = file.read().strip()  # Remove extra spaces
        exec(script_content)  # Execute the script inside Tetsu.py
except FileNotFoundError:
    print("Error: Tetsu.py not found! Make sure it is in the same directory.")
except Exception as e:
    print(f"An error occurred: {e}")