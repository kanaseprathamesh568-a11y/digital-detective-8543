# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
Master core command-line interface (CLI) operations for directory navigation and file manipulation, safely create and manage files and backups, understand the behavior of command-line flags and pipes, and investigate package managers on macOS.

---

## 2. Work completed
- Explored and executed fundamental Terminal commands (`pwd`, `ls`, `ls -l`, `cd`, `mkdir`, `touch`, `cp`, `mv`, and `cat`).
- Created a dedicated `terminal-practice` folder inside the repository to safely perform file operations without risking assignment files.
- Demonstrated safe text redirection using `>` to write an initial line and `>>` to append a second line without overwriting.
- Created a file backup with `cp` and demonstrated renaming with `mv`.
- Analyzed command options and flags (`-l`, `-a`, `-h`) and combined commands using the pipe operator (`ls -la | head -n 5`).
- Inspected Homebrew as the local macOS package manager and documented its purpose and installed packages.

---

## 3. Commands / tools used
- `pwd`: Print Working Directory — displays the absolute pathname of the current working directory.
- `ls`: List directory contents — displays names of files and folders in the target directory.
- `ls -l`: Detailed list — formats directory contents showing permissions, owner, size, and modification timestamp.
- `cd`: Change Directory — navigates between directories in the filesystem hierarchy.
- `mkdir`: Make Directory — creates a new directory.
- `touch`: Creates an empty file or updates the access/modification timestamp of an existing file.
- `cp`: Copy — duplicates a file or folder from source to destination.
- `mv`: Move / Rename — moves or renames files or directories.
- `cat`: Concatenate and print — displays the text contents of one or more files in the terminal.
- `>` and `>>`: Shell redirection operators — `>` creates/overwrites file content; `>>` appends to existing file content.
- `|` (Pipe): Streams the standard output of the command on the left into the standard input of the command on the right.
- `head`: Filters and outputs the beginning lines of text input (e.g. `head -n 5`).
- `brew`: Homebrew package manager CLI used to inspect installed command-line formulae and tools.

---

## 4. My understanding

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display (`pwd`)** | Prints the full absolute path from the root directory `/` to the current working location. | Running `pwd` output `/Users/[redacted]/.../digital-detective-8543`, clearly showing my exact location in the filesystem. |
| **Directory listing (`ls`)** | Lists the visible files and folders residing in the current directory. | Output listed all mission folders (`mission-00-setup` through `mission-08-final-report`) and `README.md`. |
| **Detailed listing (`ls -l`)** | Provides a long-format listing showing file type, permission bits, link count, owner, group, file size, and timestamp. | Displayed detailed rows such as `drwxr-xr-x` for folders and `-rw-r--r--` for files, along with byte sizes. |
| **Change directory (`cd ..`)** | Moves one level upwards in the directory tree into the parent directory. | The shell prompt updated, and running `pwd` confirmed the path moved up one level from the repository folder. |
| **Create directory (`mkdir terminal-practice`)** | Creates a new subdirectory with the specified folder name. | A new folder named `terminal-practice` appeared in the `ls` directory listing. |
| **Create empty file (`touch sample.txt`)** | Creates a new zero-byte file if it doesn't exist, or refreshes timestamps if it does. | A new empty file was created in `terminal-practice` with an initial size of 0 bytes. |
| **Copy file (`cp sample.txt sample_copy.txt`)** | Creates a duplicate copy of the source file at the specified destination path. | Two identical independent files existed simultaneously in the practice folder. |
| **Move / rename file (`mv sample_copy.txt sample_renamed.txt`)** | Relocates or renames a file or directory without making a duplicate. | The file `sample_copy.txt` was renamed to `sample_renamed.txt`; the old filename ceased to exist. |
| **Display file contents (`cat sample_renamed.txt`)** | Reads the file sequentially and prints its contents directly to standard output. | The text inside the file printed directly onto the terminal screen without opening an external GUI editor. |

---

### Task 2.2 — Practise file changes safely
Inside the `terminal-practice` directory:
1. Created `practice_notes.txt` with an initial line:  
   `echo "Line 1: Exploring CLI file operations in digital detective assignment." > practice_notes.txt`
2. Appended a second line without erasing the first:  
   `echo "Line 2: Successfully appended second line using double chevron operator." >> practice_notes.txt`
3. Verified both lines using `cat practice_notes.txt`:  
   ```text
   Line 1: Exploring CLI file operations in digital detective assignment.
   Line 2: Successfully appended second line using double chevron operator.
   ```
4. Created a backup copy:  
   `cp practice_notes.txt practice_notes_backup.txt`
5. Renamed the backup copy:  
   `mv practice_notes_backup.txt practice_notes_backup_v1.txt`

#### Reflection Questions
- **Difference between replacing a file's contents (`>`) and adding text to the end (`>>`):**  
  The single chevron `>` is an overwrite redirection operator; it truncates the target file to 0 bytes before writing, erasing everything previously saved. The double chevron `>>` is an append operator; it preserves all existing content and appends the new text directly to the end of the file.
- **Difference between copying a file and moving a file:**  
  Copying (`cp`) duplicates the file data, creating a second independent copy in storage while keeping the original intact. Moving (`mv`) changes the file's path or name within the file system index without duplicating data, meaning the file in the original location is no longer there.
- **What information the current-directory display (`pwd`) provides:**  
  `pwd` gives the unambiguous absolute path to where the terminal shell is currently executing. This is vital before executing destructive commands (like `rm` or file moves) to ensure you are operating in the intended directory.
- **Why a directory-listing operation is useful:**  
  `ls` lets you verify that files and folders actually exist, check their exact spelling and extensions before referencing them in commands, and inspect file attributes (like hidden status or permissions) before acting on them.

---

### Task 2.3 — Understand flags and pipes
- **Comparing listing flags:**
  - Standard listing (`ls`): Shows only filenames in column layout without hidden files or metadata.
  - Detailed listing (`ls -l`): Shows full metadata (file permissions, link count, owner, group, byte size, date/time, and name).
  - All files including hidden (`ls -a`): Reveals entries starting with a dot `.`, including current directory `.`, parent directory `..`, and configuration directories like `.git`.
  - Human-readable sizes (`ls -lh` or `ls -lah`): Translates raw byte counts into understandable human units (e.g. `4.0K`, `128B`, `2.6M`).
- **Piping demonstration (`ls -la | head -n 5`):**  
  The pipe operator `|` takes the stdout stream produced by `ls -la` and connects it directly into the stdin stream of `head -n 5`. The left-hand command (`ls -la`) generates a complete directory listing including hidden files, but instead of printing everything to screen, the pipe passes it to `head -n 5`, which captures only the first 5 lines (the total block header, `.`, `..`, `.git`, and `README.md`) and outputs them to the console.

---

### Task 2.4 — Understand package managers
- **Homebrew on macOS:**  
  Homebrew is installed on my system (`Homebrew 7.0.13`). Running `brew list --formula` revealed packages managed by the system (such as `ca-certificates`, `cairo`, `boost`, and `cloudflared`).
- **Why package managers are useful:**  
  A package manager automates downloading, compiling, configuring, updating, and removing software libraries and command-line tools from trusted repositories. It automatically tracks and resolves complex dependencies so you do not have to manually locate source code, compile binaries, or configure system paths yourself.

---

## 5. Difficulties faced
When experimenting with text redirection, it is easy to accidentally use `>` instead of `>>`, which immediately overwrites the existing file. Additionally, when using pipes, terminal outputs that include personal usernames or system serial numbers must be sanitized before being recorded in documentation.

## 6. How I resolved them
Always verified redirection with `cat` immediately after running the command. For documentation, sanitized all absolute paths and user identifiers with `[redacted]` to ensure privacy safety.

---

## 7. Evidence / files
- `terminal-practice/practice_notes.txt`: Text file with original and appended lines.
- `terminal-practice/practice_notes_backup_v1.txt`: Renamed backup file created during Task 2.2.
- `mission-02-terminal/README.md`: Command reference and answers.

---

## 8. Commit details
- Commit message: `Complete Terminal and file management mission`
- Status: Staged and committed on `main`, pushed to GitHub remote `origin/main`.
