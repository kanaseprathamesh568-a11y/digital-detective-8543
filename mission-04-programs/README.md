# Mission 4 — How programs run

## 1. Task / objective
Create and execute a standalone Python program from the terminal, observe program execution output, and compare the execution paradigms of compiled languages versus interpreted languages.

---

## 2. Work completed
- Created the Python source file `hello.py` inside the `mission-04-programs` folder containing a single-line print statement.
- Executed `hello.py` from the Terminal using `python3` and confirmed the expected console output (`Hello from Python`).
- Built a structured comparison table analyzing the key differences between compilers and interpreters across timing of translation, output artifacts, language examples, and architectural advantages.
- Summarized the conceptual differences between compilers and interpreters in plain, authentic student language.

---

## 3. Commands / tools used
- `python3 hello.py`: Invoked the CPython interpreter to parse, compile into bytecode, and execute `hello.py`.
- `cat hello.py`: Inspected the source code inside the terminal.
- VS Code: Authored the Python script and documentation.
- Git: Tracked changes, created the mission commit, and synchronized with GitHub.

---

## 4. My understanding

### Task 4.1 — Python program execution
The script `hello.py` contains:
```python
print("Hello from Python")
```

When executing `python3 hello.py` in the terminal:
- The command invokes the Python 3 interpreter (`Python 3.9.6`).
- The interpreter reads the source file, compiles it into internal bytecode instructions, and executes the bytecode within the Python Virtual Machine (PVM).
- Standard output receives the string, and the terminal displays:
  ```text
  Hello from Python
  ```

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translates the entire source code file into native machine instructions in advance during a separate build phase before any execution begins. | Reads, translates, and executes the code statement-by-statement (or line-by-line) at runtime while the program is running. |
| **Typical output** | Produces a permanent, standalone binary executable file (such as an `.exe`, `.out`, or Mach-O executable) that can run directly on the operating system without the compiler. | Does not produce a standalone machine-code binary; it executes instructions directly in memory and yields immediate runtime output. |
| **One example** | **C / C++** (compiled using `gcc` or `clang`), or **Rust** (using `rustc`). | **Python** (executed by CPython), **JavaScript** (in browser engines/Node.js), or **Ruby**. |
| **One advantage** | **Superior execution speed:** Since translation to raw machine instructions happens beforehand, compiled programs run with maximum performance and minimal runtime overhead. | **Rapid development & portability:** Code can be modified and tested instantly without waiting for lengthy compilation steps, making debugging and interactive experimentation much easier. |

#### Conceptual Explanation
A compiler processes an entire program upfront and converts it into a standalone machine-code executable that runs directly on the computer's CPU. In contrast, an interpreter translates and carries out instructions line-by-line on the fly while the program is actively executing. 

Because of this difference, compiled languages like C or Rust run significantly faster since the heavy translation work is already complete before launch. Interpreted languages like Python offer greater flexibility, rapid interactive testing, and simpler cross-platform portability because you can immediately run code on any system that has the interpreter installed without having to recompile binaries for each target architecture.

---

## 5. Difficulties faced
Initially, running `python hello.py` on macOS failed because `python` was pointing to a nonexistent legacy interpreter, while `python3 hello.py` ran immediately without issue.

## 6. How I resolved them
Always explicitly invoke `python3` in the terminal to ensure the correct, modern Python 3 environment is executing scripts.

---

## 7. Evidence / files
- `mission-04-programs/hello.py`: Working one-line Python script.
- `mission-04-programs/README.md`: Program output verification and compiler vs. interpreter comparison study.

---

## 8. Commit details
- Commit message: `Compare compilers and interpreters`
- Status: Staged and committed on `main`, pushed to GitHub remote `origin/main`.
