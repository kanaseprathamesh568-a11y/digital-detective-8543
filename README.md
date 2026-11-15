# The Digital Detective — Diwali Independent Learning Assignment

A comprehensive, hands-on foundational computer science exploration covering computer architectures, command-line operations, operating system fundamentals, programming paradigms, data representation, distributed version control, and computer networking.

**Student Name:** Garv Sanveria  
**USN / Registration No:** 2302008543  
**Degree Program:** B.Tech - Computer Science and Engineering (AI & ML)  
**Institution:** S-VYASA Deemed to be University  
**Repository Name:** `digital-detective-8543`  
**GitHub Repository Link:** [https://github.com/kanaseprathamesh568-a11y/digital-detective-8543](https://github.com/kanaseprathamesh568-a11y/digital-detective-8543)

---

## Assignment Introduction & Objectives

The **Digital Detective** assignment is designed as an independent learning investigation into how computers function from the silicon and hardware level up through high-level networking and collaborative software engineering. 

Rather than relying purely on theoretical definitions, every mission requires direct practical experimentation using macOS terminal tools, standard Unix utilities, Python 3 scripts, and Git version control.

Each mission is housed in its own dedicated directory, accompanied by a standardized, self-contained `README.md` detailing the task, tools used, conceptual observations, difficulties encountered, and resolution steps. In adherence with assignment guidelines, every mission was finished, verified, and committed individually with dedicated, meaningful commit messages.

---

## Mission Index

| Mission | Title | Folder / Documentation | Key Artifacts | Status |
| :---: | :--- | :--- | :--- | :---: |
| **0** | **Create your GitHub workspace** | [`mission-00-setup/README.md`](mission-00-setup/README.md) | Project directory tree, Git remote setup | Completed |
| **1** | **Know your computer** | [`mission-01-computer-basics/README.md`](mission-01-computer-basics/README.md) | IPOS analysis, hardware/software taxonomy | Completed |
| **2** | **Become comfortable with the Terminal** | [`mission-02-terminal/README.md`](mission-02-terminal/README.md) | Safe redirection, flags, pipes, Homebrew | Completed |
| **3** | **Understand the operating system** | [`mission-03-operating-system/README.md`](mission-03-operating-system/README.md) | Kernel info, PID analysis, POSIX permissions | Completed |
| **4** | **How programs run** | [`mission-04-programs/README.md`](mission-04-programs/README.md) | `hello.py`, Compiler vs. Interpreter study | Completed |
| **5** | **Numbers and data** | [`mission-05-numbers-data/README.md`](mission-05-numbers-data/README.md) | `number_converter.py`, ASCII/UTF-8 notes | Completed |
| **6** | **Git and GitHub** | [`mission-06-git-github/README.md`](mission-06-git-github/README.md) | `update-about` branch, merged PR #1, glossary | Completed |
| **7** | **How computers communicate** | [`mission-07-networking/README.md`](mission-07-networking/README.md) | Ping diagnostics, DNS resolution, web trace | Completed |
| **8** | **Final report and submission** | [`mission-08-final-report/README.md`](mission-08-final-report/README.md) | Verification audit, submission checklist | Completed |

---

## Topics Explored

1. **Hardware & System Architecture:** The Input-Processing-Output-Storage (IPOS) cycle, CPU data buses, volatile RAM vs. non-volatile solid-state storage, and embedded computing in everyday automation (ATMs, traffic lights, transit gates).
2. **Command-Line Proficiency:** Directory navigation (`pwd`, `cd`, `ls`), non-destructive file editing using shell redirection (`>` vs `>>`), file archiving (`cp`, `mv`), flag modification (`-lah`), and standard stream piping (`|`).
3. **Operating System Internals:** Process lifecycles and identifiers (PIDs), CPU load averages, virtual memory allocation, hierarchical path resolutions (absolute vs. relative), and POSIX permission bits (`rwx`).
4. **Program Execution Paradigms:** High-level source code translation, ahead-of-time compilation vs. just-in-time runtime interpretation, execution speed trade-offs, and virtual machines.
5. **Data Representation & Encoding:** Base-2 (binary), Base-10 (decimal), and Base-16 (hexadecimal) positional numbering systems; manual conversion techniques; character encoding history from 7-bit ASCII to multi-byte UTF-8 Unicode.
6. **Collaborative Version Control:** Distributed repository management, staging mechanics, immutable commit histories, feature branch isolation, pull request peer reviews, and merge conflict prevention.
7. **Internet & Network Protocols:** Hierarchical network topologies (LAN, MAN, WAN), packet-switched routing, domain name resolution (DNS), Transmission Control Protocol (TCP), and the HTTP/HTTPS client-server web lifecycle.

---

## Instructions for Running the Number Converter

The Python number converter developed in **Mission 5** prompts the user for any positive decimal integer and outputs its binary and hexadecimal representations.

To run the converter from the repository root:

```bash
# 1. Navigate into the Mission 5 folder
cd mission-05-numbers-data

# 2. Run the script using Python 3
python3 number_converter.py
```

### Example Interactive Session
```text
==========================================
 Digital Detective — Number Converter
==========================================
Enter a positive decimal number: 42

--- Conversion Results ---
Decimal (Base 10)     : 42
Binary (Base 2)       : 0b101010
Hexadecimal (Base 16) : 0x2a
--------------------------
```

---

## My Learning

Across this independent assignment, several core concepts moved from textbook abstractions into practical, intuitive understanding:
- **Terminal as a Direct Control Surface:** Interacting directly with the shell showed me how much faster and more transparent command-line tools are compared to visual GUI abstractions. Understanding file redirection and piping demonstrated how simple Unix programs can be composed to perform complex operations.
- **Operating Systems as Resource Orchestrators:** Investigating process tables (`ps`, `top`) and file permission strings demystified how the kernel prevents applications from interfering with one another's memory and disk storage.
- **Collaborative Git Hygiene:** Practicing isolated feature branches (`update-about`), writing descriptive commit messages, and submitting formal Pull Requests on GitHub illustrated why professional engineering teams rely on structured code review workflows before merging code to production branches.

---

## Verification & Commit Separation

Each mission in this repository was completed sequentially and accompanied by its own dedicated Git commit checkpoint:
1. `Set up Digital Detective mission structure`
2. `Complete computer basics and IPOS mission`
3. `Complete Terminal and file management mission`
4. `Document operating system and file management`
5. `Compare compilers and interpreters`
6. `Build number converter and practise data representation`
7. `Complete Git and GitHub collaboration mission`
8. `Explain networking concepts and website communication`
9. `Complete final report and verify assignment submission`

All commits have been pushed and are publicly verifiable on GitHub.

---

## Security & Privacy Notice

In strict adherence to assignment submission rules, all identifying network addresses, local usernames, private hostkeys, and authentication tokens have been sanitized or replaced with privacy-safe placeholders (`[redacted]`).
