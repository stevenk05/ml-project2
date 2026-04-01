# CSC426 - Machine Learning :: Dr. Bloodgood 

---

# Project 2: Find-S Algorithm and Random Training Example Experiment

    - Brian, Tyler, Steven, and A.J

---

# OBJECTIVE
Our objective is to implement the Find-S algorithm to find the maximally 
specific hypothesis consistent with a set of training examples.

-----




# Command Line 
```bash
#Adding matplotlib
module load python/3.10.11

#install matplotlib 
python -m pip install matplotlib

#cd to project location

# run the script 
python3 main.py

````

---

# What's In What?

- main.py
  - Responsible for running the full script 
  - Find-s, Random Examples, Graphing and, Driver.
  

- README.md 
  -  responsible for the readme

---

## Commit Convention

We use a Conventional Commits–style format so the git history is easy to scan.

```
<type>(<scope>): <subject>
```

| Type         | Purpose                                      |
| ------------ | -------------------------------------------- |
| **feat**     | New feature                                  |
| **fix**      | Bug fix                                      |
| **docs**     | Documentation only                       e   |
| **refactor** | Code change that doesn't alter behavior      |
| **chore**    | Maintenance (deps, formatting, repo hygiene) |
| **ci**       | CI/CD and workflow changes                   |

**Examples:**

- `feat(ui): add GlassIconButton`
- `fix(api): handle null patientId`
- `ci: install pnpm via npm`
- `docs(readme): add commit convention section`
- `chore: bump deps`
- `feat(api)!: rename /v1/messages to /v2/messages` ← breaking change

Keep subjects short (< 72 chars), imperative mood ("add", "fix", "remove").
