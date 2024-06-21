import os
from pathlib import Path


def list_files(directory, output_file=None):
    # Function to check if a path is ignored by gitignore rules
    def is_ignored(path):
        gitignore_path = Path(path)
        while gitignore_path != gitignore_path.parent:
            gitignore_path = gitignore_path.parent
            gitignore_file = gitignore_path / '.gitignore'
            if gitignore_file.exists():
                with open(gitignore_file, 'r') as f:
                    gitignore_content = f.read().splitlines()
                    for pattern in gitignore_content:
                        if pattern.startswith("#") or pattern.strip() == "":
                            continue
                        if Path(path).match(pattern):
                            return True
        return False

    # Recursive function to list files in directory
    def list_files_recursively(directory, indent='', output_file=None):
        # Function to sort files and directories alphabetically
        def sort_files_and_directories(files, directories):
            return sorted(files), sorted(directories)
        
        file_list = []
        # If output_file is None, use print to output
        if output_file is None:
            output_function = print
        else:
            output_function = output_file.write

        items = os.listdir(directory)
        files = [item for item in items if os.path.isfile(os.path.join(directory, item)) and not is_ignored(os.path.join(directory, item))]
        dirs = [item for item in items if os.path.isdir(os.path.join(directory, item)) and not is_ignored(os.path.join(directory, item))]

        files, dirs = sort_files_and_directories(files, dirs)

        # Print files
        for f in files:
            output_function(indent + '|- ' + f + '\n')
        # Print directories
        for d in dirs:
            output_function(indent + '- ' + d + '\n')
            file_list.extend(list_files_recursively(
                os.path.join(directory, d), indent + '  ', output_file=output_file))
        return file_list

    # Replace 'your_directory' with the directory you want to list files from
    return list_files_recursively(directory, output_file=output_file)


# Replace 'your_directory' with the directory you want to list files from
directory = os.getcwd()
with open('directory_tree.txt', 'w') as output_file:
    output_file.write(directory + '\n')
    files = list_files(directory, output_file=output_file)
