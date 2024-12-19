#Create a Python program to manage a text file. The program should provide the following functionality:
class FileManager:
    def __init__(self, filename):
        """
        Initialize the FileManager with a filename.
        """
        self.filename = filename

    def create_file(self):
        """
        Create a new file and write content to it.
        """
        content = input("Enter content to write in the file: ")
        with open(self.filename, 'w') as file:
            file.write(content)
        print("File created successfully!")

    def read_file(self):
        """
        Read and display the content of the file.
        """
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
            print("File Content:")
            print(content)
        except FileNotFoundError:
            print("File does not exist!")

    def append_to_file(self):
        """
        Append content to the file.
        """
        content = input("Enter content to append to the file: ")
        with open(self.filename, 'a') as file:
            file.write(content + "\n")
        print("Content appended successfully!")

    def delete_file(self):
        """
        Delete the file.
        """
        import os
        try:
            os.remove(self.filename)
            print("File deleted successfully!")
        except FileNotFoundError:
            print("File does not exist!")

    def display_menu(self):
        """
        Display the menu and handle user choices.
        """
        while True:
            print("\nMenu:")
            print("1. Create a File")
            print("2. Read File Content")
            print("3. Append Content")
            print("4. Delete File")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.create_file()
            elif choice == '2':
                self.read_file()
            elif choice == '3':
                self.append_to_file()
            elif choice == '4':
                self.delete_file()
            elif choice == '5':
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Create an instance of FileManager with the filename 'data.txt'
    file_manager = FileManager(filename="data.txt")

    # Display the menu to the user
    file_manager.display_menu()
