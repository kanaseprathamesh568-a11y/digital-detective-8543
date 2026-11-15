# Mission 5 — Numbers and data

## 1. Task / objective
Perform manual number conversions between decimal, binary, and hexadecimal number systems; verify mathematical working using Python's built-in conversion functions; develop a standalone Python command-line utility (`number_converter.py`) to convert user-input decimal numbers; and explain character encoding standards used to store text.

---

## 2. Work completed
- Worked out step-by-step manual conversions for all seven assignment questions (successive division by 2, polynomial weighted expansion, and hexadecimal nibble grouping).
- Verified each manual calculation using Python interactive commands (`bin()`, `hex()`, and `int(..., base)`).
- Authored, tested, and documented `number_converter.py`, executing it with three test inputs (`42`, `128`, `255`) and logging the results.
- Investigated text storage mechanisms, recorded decimal ASCII codes for `A` and `a`, and explained why modern computing relies on UTF-8 encoding.

---

## 3. Commands / tools used
- Python 3 interactive shell: Used `bin()`, `hex()`, and `int()` to verify base conversions.
- `python3 number_converter.py`: Executed the custom number conversion script from the terminal.
- Python built-in `ord()` function: Verified ASCII numerical values for characters.
- Text Editor (VS Code): Authored the conversion script and documentation.
- Git: Tracked changes, created the mission commit, and published to GitHub.

---

## 4. My understanding

### Task 5.1 — Convert numbers by hand

#### 1. Convert decimal 13 to binary
Use repeated division by 2, recording each remainder:
- $13 \div 2 = 6$ remainder **1** (Least Significant Bit)
- $6 \div 2 = 3$ remainder **0**
- $3 \div 2 = 1$ remainder **1**
- $1 \div 2 = 0$ remainder **1** (Most Significant Bit)  
Reading remainders from bottom to top:  
**Result:** $13_{10} = \mathbf{1101_2}$

#### 2. Convert decimal 25 to binary
Use repeated division by 2:
- $25 \div 2 = 12$ remainder **1** (LSB)
- $12 \div 2 = 6$ remainder **0**
- $6 \div 2 = 3$ remainder **0**
- $3 \div 2 = 1$ remainder **1**
- $1 \div 2 = 0$ remainder **1** (MSB)  
Reading remainders from bottom to top:  
**Result:** $25_{10} = \mathbf{11001_2}$

#### 3. Convert binary 1010 to decimal
Use positional weights (powers of 2):
$$\begin{aligned}
1010_2 &= (1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0) \\
&= 8 + 0 + 2 + 0 \\
&= \mathbf{10_{10}}
\end{aligned}$$

#### 4. Convert binary 1101 to decimal
Use positional weights:
$$\begin{aligned}
1101_2 &= (1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0) \\
&= 8 + 4 + 0 + 1 \\
&= \mathbf{13_{10}}
\end{aligned}$$

#### 5. Convert hexadecimal A to decimal
In base 16, single digits range from $0$ to $9$ and letters $A$ through $F$ represent values $10$ through $15$.  
$A_{16} = (10 \times 16^0) = \mathbf{10_{10}}$

#### 6. Convert hexadecimal 1F to decimal
Use positional weights (powers of 16), where $F = 15$:
$$\begin{aligned}
1F_{16} &= (1 \times 16^1) + (15 \times 16^0) \\
&= 16 + 15 \\
&= \mathbf{31_{10}}
\end{aligned}$$

#### 7. Convert binary 1111 to hexadecimal
Calculate the 4-bit nibble value:
$$\begin{aligned}
1111_2 &= (1 \times 2^3) + (1 \times 2^2) + (1 \times 2^1) + (1 \times 2^0) \\
&= 8 + 4 + 2 + 1 = 15_{10}
\end{aligned}$$
In hexadecimal, the decimal value $15$ is represented by the symbol **F**.  
**Result:** $1111_2 = \mathbf{F_{16}}$ (or `0xF`)

---

### Task 5.2 — Verify using Python

| Question / Conversion | Python Expression Tested | Python Result | Matches Manual Calculation? |
| :--- | :--- | :--- | :---: |
| Decimal 13 to binary | `bin(13)` | `'0b1101'` | Yes |
| Decimal 25 to binary | `bin(25)` | `'0b11001'` | Yes |
| Binary 1010 to decimal | `int('1010', 2)` | `10` | Yes |
| Binary 1101 to decimal | `int('1101', 2)` | `13` | Yes |
| Hexadecimal A to decimal | `int('A', 16)` | `10` | Yes |
| Hexadecimal 1F to decimal | `int('1F', 16)` | `31` | Yes |
| Binary 1111 to hexadecimal | `hex(0b1111)` | `'0xf'` | Yes |

*Note:* Python prefixes binary string literals with `0b` and hexadecimal string literals with `0x`.

---

### Task 5.3 — Build a small number converter

The utility `number_converter.py` was built to prompt the user for a decimal number, validate that it is a positive integer, and output its binary and hexadecimal equivalents.

#### Test Execution Results

| Test Number | Binary Output | Hexadecimal Output |
| :---: | :---: | :---: |
| **42** | `0b101010` | `0x2a` |
| **128** | `0b10000000` | `0x80` |
| **255** | `0b11111111` | `0xff` |

#### Explanation of Python conversion functions
- **`bin(x)`**: Takes an integer as an argument and returns its binary representation formatted as a string prefixed with `'0b'`. It computes the binary bits corresponding to powers of 2.
- **`hex(x)`**: Takes an integer as an argument and returns its lowercase hexadecimal representation formatted as a string prefixed with `'0x'`. It groups the binary bits into 4-bit nibbles and maps each nibble to digits `0`-`9` and letters `a`-`f`.

---

### Task 5.4 — How is text stored?

#### ASCII Codes
- Uppercase letter **`A`**: Decimal **65** (Binary: `01000001`, Hex: `0x41`)
- Lowercase letter **`a`**: Decimal **97** (Binary: `01100001`, Hex: `0x61`)  
*(Observation: The difference between uppercase and lowercase is exactly $32$, corresponding to bit 5 being set).*

#### Why computers need an encoding standard
Computers operate strictly with binary electronic switches and can only store numbers (`0` and `1`). A character encoding standard provides a universal, standardized mapping table between numeric values and readable symbols, ensuring that a text document written on one system appears identically without corruption when opened on another computer.

#### Non-ASCII Character Example
The Indian Rupee symbol (**`₹`**) or the emoji **`🚀`** (Rocket) are not part of basic 7-bit ASCII (which only defines codes 0 to 127). They require modern multi-byte encoding systems such as **UTF-8** (Unicode), which allocates up to 4 bytes per character to represent thousands of symbols and alphabets worldwide.

---

## 5. Difficulties faced
When doing manual division by 2, it is easy to accidentally write down the remainders in top-to-bottom order instead of reading them bottom-to-top (from MSB to LSB). In Python, remembering that `int()` requires the string as the first argument and the base integer as the second argument (e.g. `int('1F', 16)`) was an important syntax detail.

## 6. How I resolved them
Double-checked each binary manual calculation by reconstructing the value using positional powers of 2 ($2^0, 2^1, 2^2\dots$), and verified all answers interactively in the Python 3 terminal.

---

## 7. Evidence / files
- `mission-05-numbers-data/number_converter.py`: Complete Python number converter script.
- `mission-05-numbers-data/README.md`: Mathematical working, conversion verification tables, and encoding notes.

---

## 8. Commit details
- Commit message: `Build number converter and practise data representation`
- Status: Staged and committed on `main`, pushed to GitHub remote `origin/main`.
