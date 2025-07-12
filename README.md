# Custom Line Counter
Count lines of code in a file or folder

## Features
* Count lines in a file or a folder (includin subfolders)
* Customize counting by in-/excluding:
    * comments
    * empty lines


## Usage
### Counting the lines in one file
Use the `-c` flag to specify the symbol that denotes comments.
```bash
clic <filepath> -c "#"
```
By default, empty lines are not counted. If you would like to count them anyways, use the `-w` flag to count whitespace
```bash
clic <filepath> -c "#" -w
```
### Counting the lines of files in a given directory
When specifying a directory, you must define a file extension that will be searched using the `-s` flag.
```bash
clic <directory_path> -s ".py" -c "#" 
```

