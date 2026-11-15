# Mission 1 — Know your computer

## 1. Task / objective
Explain how a modern computer system receives input, processes information, produces output, and stores data (the IPOS cycle). Identify and classify hardware and software components across different software categories, and investigate computer-based systems used in everyday life outside of personal computers and phones.

---

## 2. Work completed
- Traced a complete end-to-end user activity ("Typing and saving a college lab report in a text editor") through every stage of the Input-Processing-Output-Storage (IPOS) model.
- Added supplementary steps covering secondary file retrieval and network synchronization to show how modern systems extend basic IPOS.
- Identified four essential hardware components and four distinct software items, properly categorising the software into operating system, application, and utility software with clear explanations of their functions.
- Researched and documented three real-world embedded and dedicated computer systems (ATM, Smart Traffic Signal, and Metro Fare Collection System), identifying their main purpose along with specific hardware inputs and outputs.
- Documented all findings in this mission README using the standard required structure.

---

## 3. Commands / tools used
- Text Editor (VS Code) / Markdown editor: Used to draft and structure tables and technical observations.
- Terminal & Git: Used to verify file status, stage mission files, commit changes, and push progress to GitHub.
- System Profiler (`system_profiler SPHardwareDataType`): Inspected local Mac hardware details to ground the hardware descriptions in real specifications.

---

## 4. My understanding

### Task 1.1 — Trace one activity using IPOS
**Chosen activity:** Typing a college lab report in a text editor and saving it to the drive.

| Stage | What happens in this activity? | Hardware / Component involved |
| :--- | :--- | :--- |
| **Input** | The user presses mechanical keys on the keyboard to enter alphanumeric text and uses the trackpad/mouse to position the cursor and select menu options. | Built-in Keyboard, Trackpad / Mouse |
| **Processing** | The keyboard controller sends scan codes to the operating system kernel. The CPU interprets the scan codes, translates them into UTF-8 character codes, updates the document data structure held in RAM, and coordinates text rendering. | Central Processing Unit (CPU) and RAM (Random Access Memory) |
| **Output** | The display controller and GPU convert the text buffer into visual frame data, updating pixels on the monitor so the user instantly sees each typed character. | Retina Display / Monitor |
| **Storage** | When the user triggers the Save command (`Cmd + S`), the operating system transfers the document content from volatile RAM to non-volatile flash storage blocks, creating or updating a permanent file. | Internal Solid-State Drive (PCIe NVMe SSD) |

#### Supplementary Stages & Data Flow Explanation
1. **Secondary Retrieval (Reading):** When the editor reopens the document later, the flow reverses: the CPU directs the SSD controller to read the saved binary blocks from flash memory back into volatile RAM so it can be edited again.
2. **Cloud Synchronization:** Many modern systems include an automated synchronization step where a background agent reads the newly saved SSD file, encrypts the payload, and transmits it via the Wi-Fi network card to remote cloud servers for backup.

**How the activity moves from input to output and storage:**  
Data begins as physical kinetic energy (a finger striking a key). This triggers an electrical switch that generates an interrupt to the CPU. The CPU executes interrupt handler routines to place the corresponding character code into an active text buffer residing in fast, volatile RAM. Immediately, the window compositor draws the updated character into the video frame buffer so it appears on the monitor (output) within milliseconds. The data remains temporary in RAM until the user or an auto-save routine issues a write command, prompting the file system driver to write the blocks to flash storage (SSD), making the data safe from power loss.

---

### Task 1.2 — Identify hardware and software
The table below classifies four hardware devices and four software components used on my system, distinguishing between system software, application software, and utilities.

| Item / software name | Hardware or software? | Software type (if applicable) | Purpose |
| :--- | :--- | :--- | :--- |
| **Mechanical / Laptop Keyboard** | Hardware | *Not applicable* | Primary text input device that converts keystroke motions into electrical scan codes for alphanumeric input and navigation. |
| **Retina Display Monitor** | Hardware | *Not applicable* | Visual output hardware device that displays graphical user interfaces, active application windows, and visual feedback. |
| **Apple M-Series Processor (CPU/SoC)** | Hardware | *Not applicable* | Primary computing engine that fetches, decodes, and executes machine instructions and coordinates memory buses. |
| **PCIe NVMe SSD** | Hardware | *Not applicable* | High-speed, non-volatile solid-state storage medium that preserves the operating system, user programs, and saved data when power is off. |
| **macOS Sequoia** | Software | Operating system software | Core system software that manages hardware resources, schedules processes, handles virtual memory, and exposes system calls. |
| **Google Chrome** | Software | Application software | End-user web browser application used to navigate websites, download files, view web documentation, and interact with web services. |
| **Visual Studio Code** | Software | Application software | Integrated text and code editor tailored for software development, featuring syntax highlighting, file exploration, and terminal integration. |
| **Activity Monitor / Disk Utility** | Software | Utility software | System maintenance utility used to diagnose system health, inspect CPU/memory utilisation per process, and manage drive storage volumes. |

---

### Task 1.3 — Computer systems around you
Computers are embedded into numerous public and industrial systems beyond conventional personal computers.

| System | Main purpose | One input | One output |
| :--- | :--- | :--- | :--- |
| **ATM (Automated Teller Machine)** | Provides 24/7 self-service banking, enabling account holders to authenticate, check balances, deposit funds, and withdraw physical cash. | Encrypted numeric keypad for entering account PIN; EMV magnetic/chip card reader. | Motorized cash dispensing mechanism; high-contrast customer guidance display screen; printed receipt. |
| **Smart Traffic Signal System** | Dynamically controls vehicular traffic flow and pedestrian crossings at intersections to optimize safety and reduce queue times. | Sub-surface inductive loop sensors detecting the presence of metal vehicles; physical pedestrian crossing buttons. | Colored signal heads (Red, Amber, Green optical arrays); audible pedestrian crossing buzzer; digital seconds-countdown display. |
| **Metro Automated Ticket Barrier / Gate** | Validates passenger travel credentials, deducts transit fare, and controls physical access into paid station concourses. | High-frequency RFID / NFC smartcard reader that senses commuter cards or dynamic QR code scanner. | Motorised pneumatic barrier gates that swing open upon valid scan; directional green arrow/red cross LCD indicator; audio feedback chime. |

---

## 5. Difficulties faced
When classifying software, it was initially easy to confuse an Operating System with Utility software, or to treat utilities as generic applications. For example, tools like Disk Utility or Activity Monitor are launched by the user like regular applications, but their function is strictly administrative and focused on supporting the computer infrastructure itself.

## 6. How I resolved them
I reviewed standard software classifications: applications solve user-oriented tasks (like browsing or word processing), system software (the OS) provides the fundamental execution environment and controls hardware, and utility software assists in optimizing, configuring, maintaining, and analyzing system resources.

## 7. Evidence / files
- `mission-01-computer-basics/README.md`: Contains the completed IPOS analysis, hardware/software classification table, and everyday embedded systems study.

## 8. Commit details
- Commit message: `Complete computer basics and IPOS mission`
- Status: Staged and committed on `main`, pushed to GitHub remote `origin/main`.
