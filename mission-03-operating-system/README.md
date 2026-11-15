# Mission 3 — Understand the operating system

## 1. Task / objective
Explore core operating system metrics, running processes, storage systems, filesystem paths, and file permission models. Analyze the six primary responsibilities of a modern operating system with practical, real-world examples.

---

## 2. Work completed
- Queried and documented live OS platform information, kernel architecture, user identity, filesystem disk space, and active system resource utilization.
- Inspected the process table using `ps` and `top`, identifying process IDs (PIDs), CPU usage, and memory footprints of running programs.
- Analyzed filesystem paths, differentiating between absolute paths from the root filesystem and relative paths from the active working directory.
- Investigated POSIX file permission modes (`r`, `w`, `x`) on practice files and determined user, group, and other access rights.
- Documented the six essential responsibilities of an Operating System with concrete, student-relatable examples.

---

## 3. Commands / tools used
- `sw_vers` & `uname -srm`: Checked the operating system name, version, and hardware CPU architecture (macOS Darwin 27.2.0 arm64).
- `whoami`: Displayed the active logged-in user account session.
- `df -h /`: Reported total, used, available, and percentage capacity of the mounted root storage volume in human-readable units.
- `top -l 1`: Generated a one-time non-interactive summary of CPU, memory, process counts, and load averages.
- `ps aux`: Listed active system processes with user attribution, PID, CPU/RAM percentages, and process execution command paths.
- `ls -l`: Displayed the 10-character file permission string and file ownership.

---

## 4. My understanding

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | Identifies the OS product, release version, and underlying kernel architecture. | macOS Darwin kernel version `27.2.0`, running on Apple Silicon `arm64` 64-bit architecture. |
| **Current account identity** | Identifies the username of the user account executing the terminal session. | `[redacted]` — standard administrative user account with local shell access. |
| **Available and used storage** | Shows the overall disk partition size, consumed storage space, and remaining free space on the primary volume. | Root filesystem mounted on `/dev/disk3s1s1`: Total Size = `460Gi`, Used = `13Gi`, Available = `301Gi` (`5%` capacity utilized). |
| **System activity snapshot** | Provides real-time metrics on total running/sleeping processes, thread count, CPU load distribution, and physical RAM usage. | `709` total processes (`2` running, `707` sleeping); CPU usage: `~5.5%` user, `~10.4%` system, `~84%` idle; Physical RAM: `13G` used, `~2.7G` available. |

---

### Task 3.2 — Understand processes

#### Key Questions
1. **What is a process?**  
   A process is an active, executing instance of a computer program loaded into main memory (RAM). Unlike a passive file stored on disk, a process possesses allocated CPU time, its own address space, an instruction pointer, call stack, and associated operating system resources (such as open file handles and network sockets).

2. **What does the PID column represent?**  
   PID stands for **Process Identifier**. It is a unique positive integer assigned sequentially by the operating system kernel whenever a process is spawned. The kernel uses PIDs to track, prioritize, schedule, and signal (e.g. terminate via `kill <PID>`) individual programs.

3. **Two examples of processes running on my computer:**  
   - `WindowServer` (PID `418`): The macOS core compositor process responsible for drawing windows, menus, and graphics on the screen.
   - `Antigravity Helper / Google Chrome` (PID `26353`): An application process executing the user's graphical interface and code editor environment.

---

### Task 3.3 — Understand paths and permissions

#### Absolute vs. Relative Paths
- **Absolute Path:** The complete, unambiguous location of a file or directory starting from the root of the filesystem (`/`). It is independent of the current working directory.  
  *Example from assignment:* `/Users/[redacted]/.../digital-detective-8543/mission-03-operating-system`
- **Relative Path:** A path that specifies a target location relative to the shell's current working directory, often using `.` (current folder) or `..` (parent folder).  
  *Example from assignment:* `mission-03-operating-system` (navigating into the folder) or `../terminal-practice/practice_notes.txt` (referencing across sibling folders).

#### File Permissions Analysis
Inspecting `practice_notes.txt` inside `terminal-practice` produced:  
`-rw-r--r--@ 1 [redacted] staff 144 Nov 15 practice_notes.txt`

| Permission Bit | Meaning | Owner Rights for `practice_notes.txt` |
| :---: | :--- | :--- |
| **r** (Read) | Allows reading and opening the file contents (or listing directory entries). | **Yes (`r`)**: The owner can read and view the file content. |
| **w** (Write) | Allows modifying, editing, appending to, or deleting the file. | **Yes (`w`)**: The owner can edit and overwrite the file. |
| **x** (Execute) | Allows executing the file as an application/script (or traversing a directory). | **No (`-`)**: The file is a plain text document, not an executable binary or shell script. |

*Summary:* The file owner has Read and Write permissions (`rw-`), while group members and others have Read-only permissions (`r--`).

---

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | The OS creates, schedules, monitors, and terminates processes. It allocates CPU time slices fairly among running threads so multiple applications can run concurrently without freezing. | Switching CPU execution smoothly between a Spotify music player stream and a VS Code editor instance. |
| **Memory management** | The OS allocates memory blocks in RAM to active applications and prevents programs from overwriting each other's memory. When an application exits, the OS reclaims its memory for other programs. | Allocating 400 MB of RAM to a browser tab when opened, and recycling that memory back to the system pool when the tab is closed. |
| **Device management** | The OS bridges software and peripheral hardware using device drivers, translating generic software requests into hardware-specific signals. | Translating a print request from a word processor into print head commands sent over USB to an HP inkjet printer. |
| **File management** | The OS manages files and folders on physical storage media, maintaining directory structures, filenames, file metadata, and access permissions. | Creating, storing, locating, and retrieving markdown files on an APFS-formatted solid-state drive. |
| **User interface / shell** | The OS provides an interface enabling humans to interact with the system, either visually through a Graphical User Interface (GUI) or textually through a Command-Line Interface (CLI). | The macOS desktop window environment (GUI) and the Zsh terminal command shell (CLI). |
| **Security and permissions** | The OS enforces access control rules to ensure users and programs can only access resources they are authorized to use, protecting sensitive system files from unauthorized tampering. | Prompting for biometric Touch ID or admin password before allowing a system update or editing protected `/etc/hosts` configurations. |

---

## 5. Difficulties faced
Understanding the 10-character POSIX permission string format (`-rw-r--r--`) can be confusing initially, especially distinguishing between the file type indicator (first character `-` or `d`) and the three distinct sets of user, group, and other permission triplets.

## 6. How I resolved them
Broke down the permission string into its mathematical triplets: `[type: -] [user: rw-] [group: r--] [other: r--]`. This made it easy to recognize that the owner has full read/write privileges, while all other system users are restricted to read-only access.

---

## 7. Evidence / files
- `mission-03-operating-system/README.md`: Complete OS investigation tables, process analysis, path/permission reference, and operating system responsibility study.

---

## 8. Commit details
- Commit message: `Document operating system and file management`
- Status: Staged and committed on `main`, pushed to GitHub remote `origin/main`.
