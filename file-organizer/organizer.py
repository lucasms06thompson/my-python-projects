import os
import shutil
import argparse

# Mapping of extensions to directory names
# You can easily add more categories and extensions here
FILE_TYPE_MAP = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.doc', 'docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Video': ['.mp4', '.mov', '.avi', '.mkv'],
    'Scripts': ['.py', '.js', '.sh', '.bat'],
}

def organize_directory(path):
    """
    Organizes files in the specified directory into subfolders based on their extension.
    
    :param path: The path to the directory to organize.
    """
    print(f"Scanning directory: {path}\n")

    # Get a list of all files in the directory
    try:
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    except FileNotFoundError:
        print(f"Error: Directory not found at '{path}'")
        return

    if not files:
        print("No files to organize in this directory.")
        return

    # Create directories and move files
    for file in files:
        file_extension = os.path.splitext(file)[1].lower()
        moved = False

        # Find the correct category for the file
        for folder_name, extensions in FILE_TYPE_MAP.items():
            if file_extension in extensions:
                # Create the destination folder if it doesn't exist
                dest_folder = os.path.join(path, folder_name)
                os.makedirs(dest_folder, exist_ok=True)
                
                # Move the file
                src_path = os.path.join(path, file)
                dest_path = os.path.join(dest_folder, file)
                shutil.move(src_path, dest_path)
                
                print(f"Moved: {file}  ->  {folder_name}/")
                moved = True
                break
        
        # If the file type is not in our map, move it to an 'Other' folder
        if not moved:
            other_folder = os.path.join(path, 'Other')
            os.makedirs(other_folder, exist_ok=True)
            
            src_path = os.path.join(path, file)
            dest_path = os.path.join(other_folder, file)
            shutil.move(src_path, dest_path)

            print(f"Moved: {file}  ->  Other/")

    print("\nOrganization complete!")


if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Organize files in a directory into subfolders based on file type.")
    parser.add_argument('directory', type=str, nargs='?', default='.', 
                        help="The path to the directory to organize. Defaults to the current directory.")
    
    args = parser.parse_args()

    # Get the absolute path to handle relative paths correctly
    target_directory = os.path.abspath(args.directory)
    
    organize_directory(target_directory)
