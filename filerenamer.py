import os, glob
from pathlib import Path

class Renamer:

    file_types = [
        '.nef',
        '.jpeg',
        '.jpg',
        '.png'
    ]

    def getBaseDirectory(self):
        return input("What is the base directory to rename files: ")

    def process(self):
        selected_directory = self.getBaseDirectory()

        if not os.path.isdir(selected_directory):
            print("\033[1;31;40mThis directory does not exist")
            exit()

        os.chdir(selected_directory)
        file_basename = os.path.basename(os.getcwd())

        currentFileNo = 0
        for file in os.listdir(os.getcwd()):
            currentFileNo += 1
            if file.endswith(tuple(self.file_types)):
                new_filename = '{}_{}{}'.format(file_basename, currentFileNo, Path(file).suffix)
                os.rename(file, new_filename)        
                
        print("\033[1;32;40mRenaming process completed successfully!")


renamer = Renamer()
renamer.process()