import os
import shutil

def organize_files(directory):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    #  Get all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    #  Organize files by their extensions
    for file in files:
        # Extract the file extension
        file_extension = file.split('.')[-1]

        # Create a folder for the file extension if it doesn't exist
        folder_path = os.path.join(directory, file_extension)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Move the file into the corresponding folder
        shutil.move(os.path.join(directory, file), os.path.join(folder_path, file))

    print(f"Files in '{directory}' have been organized by their extensions.")

if __name__ == "__main__":
    # Specify the directory to organize
    directory_to_organize = input("Enter the directory path to organize:" )
    
    # Run the file organizer
    organize_files(directory_to_organize)
