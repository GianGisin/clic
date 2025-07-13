# Custom Line Counter
Count lines of code in a file or folder

## Features
* Count lines in a file or a folder (includin subfolders)
* Customize counting by in-/excluding:
    * comments
    * empty lines


## Usage
### Counting the lines in one file
Use the `-s` flag to specify the symbol that denotes comments.
```bash
clic <filepath> -s "#"
```
By default, empty lines are not counted. If you would like to count them anyways, use the `-w` flag to count whitespace
```bash
clic <filepath> -s "#" -w
```
### Counting the lines of files in a given directory
When specifying a directory, you must define a file extension that will be searched using the `-e` flag.
```bash
clic <directory_path> -e ".py" -s "#" 
```

comments can be included in the count using the `-c` flag.
