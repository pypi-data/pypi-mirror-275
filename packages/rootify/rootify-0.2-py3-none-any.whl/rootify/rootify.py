import os
import sys

def change_to_parent_directory(levels_up=1):
    """Change the working directory to the nth parent directory."""
    new_dir = os.path.abspath(__file__)
    for _ in range(levels_up):
        new_dir = os.path.dirname(new_dir)
    os.chdir(new_dir)
    sys.path.append(new_dir)

def find_project_root(marker='.git'):
    """Find the number of levels up needed to reach the project root."""
    current_dir = os.path.abspath(os.path.dirname(__file__))
    levels_up = 0
    
    while not os.path.isdir(os.path.join(current_dir, marker)):
        parent_dir = os.path.dirname(current_dir)
        if current_dir == parent_dir:  # Reached the root of the filesystem
            raise FileNotFoundError(f"Marker '{marker}' not found in any parent directories.")
        current_dir = parent_dir
        levels_up += 1
    
    return levels_up

def rootify(marker='.git'):
    """Change the working directory to the project root based on a marker."""
    levels_up = find_project_root(marker)
    change_to_parent_directory(levels_up)