import os
import shutil

def move_jpg_files(src_folder, dest_folder):
    # Create destination folder if it doesn’t exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Loop through files in source folder
    for file_name in os.listdir(src_folder):
        if file_name.lower().endswith(".jpg"):
            src_path = os.path.join(src_folder, file_name)
            dest_path = os.path.join(dest_folder, file_name)

            shutil.move(src_path, dest_path)
            print(f"Moved: {file_name}")

if __name__ == "__main__":
    # Example source and destination
    source = "sample_folder"
    destination = "output_folder"

    move_jpg_files(source, destination)
    print("✅ All .jpg files moved successfully!")
