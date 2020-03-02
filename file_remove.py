import argparse
import os
from os.path import isfile, join

def remove(directory, filename):
    #Gets the files in the directory, doesn't include other directories
    files = [f for f in os.listdir(directory) if isfile(join(directory, f))]

    if not files:
        print('Directory is empty or contains only other directories')

    elif not filename:
        print('Directory has the following files:\n')
        for file in files:
            print(file)
        print('')
        while True:
            try:
                num = input('To remove the files input a non-zero number, to cancel input 0: ')
                break
            except:
                print("Invalid input, please input a number.")

        if num:
            if not directory.endswith('/'):
                directory = directory + '/'
            for file in files:
                os.remove(directory + file)
                print('Removed ' + file)
        else:
            print('Files not removed')
    
    else:
        filteredFiles = [f for f in files if filename in f]
        if filteredFiles:
            print('Found the following files including ' + filename + ' in their filename\n')
            for file in filteredFiles:
                print(file)
            print('')
            while True:
                try:
                    num = input('To remove the files input a non-zero number, to cancel input 0: ')
                    break
                except:
                    print("Invalid input, please input a number.")

            if num:
                if not directory.endswith('/'):
                    directory = directory + '/'
                for file in filteredFiles:
                    os.remove(directory + file)
                    print('Removed ' + file)
            else:
                print('Files not removed')


if __name__ == '__main__':
    #Parser creation to get inputs from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', required=False, default=os.getcwd())
    parser.add_argument('-n', '--name', default='')
    args = parser.parse_args()

    remove(args.directory, args.name)