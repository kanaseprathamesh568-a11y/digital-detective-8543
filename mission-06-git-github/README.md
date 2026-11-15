# Mission 6 — Git and GitHub

## 1. Task / objective
Understand distributed version control concepts, practice staging and committing files, create an isolated feature branch (`update-about`), open and merge a Pull Request on GitHub, synchronize merged remote changes back to the local computer, and compile a comprehensive Git command glossary.

---

## 2. Work completed
- Analyzed the basic Git workflow and documented the functional differences between the working tree, staging area, and commit history.
- Created and switched to a new branch named `update-about`.
- Updated the root `README.md` on the new branch with a "My Learning" reflection section highlighting key takeaways from earlier missions.
- Staged, committed, and pushed the `update-about` branch to GitHub.
- Opened Pull Request #1 on GitHub titled *"Add My Learning section to root README"*.
- Reviewed and merged Pull Request #1 into the `main` branch on GitHub.
- Switched back to the local `main` branch and ran `git pull origin main` to synchronize the merged changes into the local working copy.
- Compiled an 8-item Git command glossary with clear, practical one-line explanations.

---

## 3. Commands / tools used
- `git status`: Inspected the working tree to verify modified, staged, and untracked files.
- `git add <file>`: Staged modified files into the Git index.
- `git commit -m "..."`: Created immutable snapshots in local repository history.
- `git log --oneline`: Inspected concise commit history hashes and messages.
- `git checkout -b update-about`: Created and switched to the new feature branch.
- `git push -u origin update-about`: Published the local branch to the remote GitHub repository and set up upstream tracking.
- GitHub Pull Request Interface & REST API: Created, reviewed, and merged Pull Request #1.
- `git checkout main`: Switched the local working copy back to the primary branch.
- `git pull origin main`: Fetched and integrated changes from the remote `main` branch via fast-forward merge.

---

## 4. My understanding

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status (`git status`)** | Checks the current state of the working directory against the repository, listing untracked, modified, or staged files. |
| **Stage selected changes (`git add <file>`)** | Moves specific file edits from the working directory into the staging area (index), preparing them to be bundled into the next commit. |
| **Create a commit (`git commit -m "..."`)** | Captures an immutable snapshot of all staged changes, attaching a descriptive message, author metadata, and a unique cryptographic commit hash. |
| **View commit history (`git log --oneline`)** | Lists previous repository commits in reverse chronological order with short 7-character hashes and commit titles. |

#### Difference between Staging and Committing
Staging (`git add`) is like packing items into a parcel box, while committing (`git commit`) is sealing the box and attaching an official tracking label. Staging gives developers granular control over *what* goes into a commit, allowing unrelated edits across multiple files to be separated into distinct, coherent commits. Committing permanently records that curated group of changes into the repository's permanent history.

---

### Task 6.2 & 6.3 — Branches and Pull Requests

#### Workflow Execution Summary
1. Created branch `update-about` using `git checkout -b update-about`.
2. Updated root `README.md` to add the `## My Learning` section.
3. Staged and committed: `git commit -m "Add My Learning section to root README on update-about branch"`.
4. Pushed branch to remote: `git push -u origin update-about`.
5. Created Pull Request **#1** on GitHub comparing `update-about` into `main`.
6. Merged Pull Request #1 on GitHub using a merge commit.
7. Returned to local terminal, switched back via `git checkout main`, and updated local code via `git pull origin main`.

#### What is a Branch?
A branch is a lightweight, moveable pointer to a specific commit in Git. It creates an isolated workspace where a developer can build new features, test code, or make documentation changes without affecting the stable `main` codebase. If an experiment fails, the branch can simply be discarded without harming the primary project.

#### What is a Pull Request (PR)?
A Pull Request is a collaborative feature provided by code hosting platforms (like GitHub) that notifies repository collaborators that a feature branch is ready for review. It provides a visual interface displaying side-by-side file differences (diffs), allows teammates to review lines of code, leave comments, run automated tests, and formally approve the changes before safely merging them into `main`.

---

### Task 6.4 — Build your Git command glossary

1. **Initialise a repository (`git init`):** Creates a hidden `.git` directory in the current folder, transforming it into an active Git version-controlled repository.
2. **Check status (`git status`):** Displays which files are modified, untracked, or staged in the current working directory relative to the repository index.
3. **Stage changes (`git add`):** Adds file modifications from the working tree to the staging area to be included in the upcoming commit.
4. **Commit changes (`git commit`):** Records the staged changes as a permanent snapshot in repository history with a descriptive commit log message.
5. **View history (`git log`):** Displays the chronological log of all commits created in the current branch.
6. **Create or list branches (`git branch`):** Lists all local branches in the repository, or creates a new branch pointer when supplied with a branch name.
7. **Switch branches (`git checkout` / `git switch`):** Updates the working directory files to match a different branch and moves the HEAD pointer to that branch.
8. **Publish changes (`git push`):** Uploads local branch commits to a designated remote repository server (such as GitHub).
9. **Retrieve remote changes (`git pull`):** Downloads commits from the remote repository and immediately integrates them into the active local branch.

---

## 5. Difficulties faced
When pushing a newly created branch for the first time, simply typing `git push` fails with a message stating that the upstream branch does not exist yet on the remote server.

## 6. How I resolved them
Added the `-u` (or `--set-upstream`) flag during the initial branch push (`git push -u origin update-about`), which established tracking between the local branch and GitHub, allowing subsequent pushes and pulls to work seamlessly.

---

## 7. Evidence / files
- Root `README.md`: Contains the merged `## My Learning` section.
- Remote GitHub Branch: `update-about` pushed to GitHub.
- Remote Pull Request: PR #1 created and merged on GitHub (`https://github.com/kanaseprathamesh568-a11y/digital-detective-8543/pull/1`).
- `mission-06-git-github/README.md`: Git operations analysis, branch explanations, and command glossary.

---

## 8. Commit details
- Commit message: `Complete Git and GitHub collaboration mission`
- Status: Staged and committed on `main`, pushed to GitHub remote `origin/main`.
