# Mission 0 — Create your GitHub workspace

## 1. Task / objective
Set up the digital detective assignment workspace, verify the local development tools (Git and Python), prepare a clear folder structure for all nine missions with required empty files, draft the root assignment README, and publish the repository publicly on GitHub.

## 2. Work completed
- Selected repository name as `digital-detective-8543` following the naming rule (`digital-detective-` followed by the last four digits of my USN: `8543`).
- Created the local assignment project folder inside the workspace.
- Initialised local Git version control and set `main` as the default branch.
- Created all required mission folders (`mission-00-setup` through `mission-08-final-report`) and the `evidence` directory.
- Created empty Markdown files and placeholder script files according to the structure specified in Step 3.
- Drafted the root `README.md` containing the project overview, student details, security notice, and mission index.
- Connected the local repository to GitHub and pushed the setup commit.

## 3. Commands / tools used
- `git --version`: Checked Git installation and version (`git version 2.54.0 (Apple Git-157)`).
- `python3 --version`: Verified Python 3 interpreter version (`Python 3.9.6`).
- `mkdir`: Created the project directory and mission subdirectories.
- `touch`: Created empty Markdown files and placeholder script files.
- `git init`: Initialised the local Git repository.
- `git branch -M main`: Set default branch name to `main`.
- `git remote add origin <url>`: Linked the local repository to the remote GitHub repository.
- `git status`: Inspected the repository status before staging.
- `git add .`: Staged all setup files and folders.
- `git commit -m "..."`: Created the setup checkpoint commit.
- `git push -u origin main`: Published the local repository and branch to GitHub.

## 4. My understanding
A Git repository acts as a tracked project workspace. Instead of saving static copies or relying on manual backups, Git takes snapshots of the project state at every commit. This ensures that every milestone is preserved and reversible.

Organising the project into individual mission folders is helpful because:
- Each mission has a distinct focus and set of deliverables, so keeping them in modular folders prevents clutter.
- It makes it straightforward to follow the required workflow of finishing, documenting, and committing one mission before beginning the next.
- Anyone visiting the repository can easily navigate between topics and inspect the specific README and code associated with each learning objective.

## 5. Difficulties faced
When checking Python from the terminal, running `python --version` prompted an error or alias warning because macOS has deprecated the legacy Python 2 command. Additionally, during remote setup on GitHub, it is easy to accidentally check the option to "Add a README file" on GitHub's web interface, which would create a conflicting initial commit and cause push rejections.

## 6. How I resolved them
I ran `python3 --version` instead, which properly detected Python 3.9.6. When creating the GitHub repository online, I left it completely uninitialized (no README, license, or .gitignore) so that the local folder and commits pushed cleanly without any branch divergence.

## 7. Evidence / files
- Root `README.md`
- `mission-00-setup/README.md`
- Mission directories: `mission-00-setup` to `mission-08-final-report`
- Initial empty files:
  - `mission-01-computer-basics/README.md`
  - `mission-02-terminal/README.md`
  - `mission-03-operating-system/README.md`
  - `mission-04-programs/README.md`
  - `mission-04-programs/hello.py`
  - `mission-05-numbers-data/README.md`
  - `mission-05-numbers-data/number_converter.py`
  - `mission-06-git-github/README.md`
  - `mission-07-networking/README.md`
  - `mission-08-final-report/README.md`
  - `evidence/.gitkeep`

## 8. Commit details
- Commit message: `Set up Digital Detective mission structure`
- Status: Staged and committed on `main`, pushed to GitHub remote `origin/main`.
