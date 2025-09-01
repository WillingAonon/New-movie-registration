# 🎬 New Movie Registration - Sprint 1

def main():
    # dictionary for storing movie data (empty for now)
    movies = {}

    print("Welcome to the New Movie Registration System!")

    while True:
        print("\nPlease choose an option:")
        print(" - Type 'register' to add a new movie (coming soon)")
        print(" - Type 'view' to see all movies (coming soon)")
        print(" - Type 'quit' to exit")

        command = input("Enter command: ").strip().lower()

        if command == "quit":
            print("Goodbye!")
            break
        elif command in ["register", "view"]:
            print(f"'{command}' feature will be implemented in the next sprint.")
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
