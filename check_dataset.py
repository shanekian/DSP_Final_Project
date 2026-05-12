import os

dataset_path = "data/raw"

for root, dirs, files in os.walk(dataset_path):

    print("Folder:", root)

    print("Number of files:", len(files))

    print("-" * 40)