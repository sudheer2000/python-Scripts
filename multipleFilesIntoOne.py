import os

# Folder Path
path = "/Users/i1097/Downloads/schema-manager-master/v9/l1"
path = "/Users/i1097/Downloads/schema-manager-master1/banner/l2"

path = "/Users/i1097/Downloads/schema-manager-master/v9/l2"

# Change the directory
os.chdir(path)


# Read text File


def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())


# iterate through all file
for file in sorted(os.listdir()):
    # Check whether file is in text format or not
    print('-- '+file)
    read_text_file(file)
