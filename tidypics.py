#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
""" 
Tile: Tidypics Python 
Auteur: CipherMike
Date: 01-Jan-2025 
Description: A tool to clean duplicate pictures especially on synoligy NAS 
Version: 1.0.0
"""


import os
import shutil
import sys
import random

def move_files(src_dir, dest_dir, extensions, verbose=False):
    for root, dirs, files in os.walk(src_dir, topdown=False):
        for file in files:
            # check if ZbThumbnail.info exits, remove it
            if file == "ZbThumbnail.info" or ".picasa.ini":
                os.remove(os.path.join(root, file)) 
                print(f"Deleted : {os.path.join(root, file)}")

            if any(file.lower().endswith(ext) for ext in extensions):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, file)

                while os.path.exists(dest_file):
                    print(f"exist, : {src_file} \n")
                    name, ext = os.path.splitext(file) 
                    random_suffix = f"{random.randint(100, 999)}" 
                    file = f"{name}_{random_suffix}{ext}" 
                    dest_file = os.path.join(dest_dir, file)
   
                shutil.move(src_file, dest_file)
                print(f"Moved: {src_file} -> {dest_file}")
              
                    

        # Supprimer les répertoires vides avec confirmation
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                if verbose:
                    confirm = input(f"Do you want to delete the empty directory {dir_path}? (y/no): ")
                    if confirm.lower() == 'y':
                        os.rmdir(dir_path)
                        print(f"Deleted: {dir_path}")
                    else:
                        print(f"Deletion for {dir_path} is canceled.")
                else:
                    os.rmdir(dir_path)
                    print(f"Deleted: {dir_path}")

    
    try:
        # Supprimer le répertoire src_dir si vide
        os.rmdir(src_dir)
        print(f"Directory {src_dir} deleted successfully.")
    except OSError as e:
        print(f"Error while deleting directory : {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: python tidypics.py <répertoire_source> <répertoire_destination> [-v]")
        sys.exit(1)

    source_directory = sys.argv[1]
    
    destination_directory = sys.argv[2]
    
    verbose = '-v' in sys.argv
    if verbose:
        print("verbose mode : on")
        print(f"Source dir is : {source_directory}")
        print(f"Dest dir is : {destination_directory}")
    else:
        print("verbose mode : off")

    file_extensions = [".jpg", ".mp3", ".mp4", ".heic", ".wma", ".rar", ".avi", "zip", ".jpeg"]

    move_files(source_directory, destination_directory, file_extensions, verbose)
