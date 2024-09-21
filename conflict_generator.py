def generate_conflict():
    with open('src/snake_game.py', 'r') as file:
        content = file.readlines()

    # Simulate a conflict by changing the game board size
    for i, line in enumerate(content):
        if 'def __init__' in line:
            content[i+1] = '        self.width = 30  # Changed from 20 to 30\n'
            content[i+2] = '        self.height = 30  # Changed from 20 to 30\n'
            break

    with open('src/snake_game.py', 'w') as file:
        file.writelines(content)

    print("Conflict generated in src/snake_game.py")
    print("The game board size has been changed to 30x30.")
    print("This may conflict with your implementation. Please resolve the conflict.")

if __name__ == "__main__":
    generate_conflict()
