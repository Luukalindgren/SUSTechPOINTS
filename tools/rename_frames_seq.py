import os
from pathlib import Path
"""
Used to rename weird naming in point cloud and label files.
Input paths to LiDAR and Label files
Results into renaming these from 000001.bin/.txt ->
"""

# Paths to your dataset folders
velodyne_path = Path('/home/luuka/Desktop/Custom_KITTI_Dataset_Final/training/velodyne')
label_path = Path('/home/luuka/Desktop/Custom_KITTI_Dataset_Final/training/label_2')

# Get all .bin and .txt files and sort them to keep order consistent
velodyne_files = sorted(velodyne_path.glob('*.bin'))
label_files = sorted(label_path.glob('*.txt'))

# Rename velodyne and label files to 6-digit zero-padded filenames
for i, (velodyne_file, label_file) in enumerate(zip(velodyne_files, label_files)):
    new_name = f"{i:06d}"  # Zero-padded 6-digit number
    print(new_name)
    
    # Rename velodyne file
    velodyne_file.rename(velodyne_path / f"{new_name}.bin")
    
    # Rename corresponding label file
    label_file.rename(label_path / f"{new_name}.txt")

print("Files have been renamed successfully!")
