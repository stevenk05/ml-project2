# CSC426 - Machine Learning :: Dr. Bloodgood 
    - Tyler Elvis, .......

---

# OBJECTIVE
Our objective is to implement the Find-S algorithm and to analyze the number of training examples required to exactly learn the target concept. 

-----


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

---

# Command Line 
```bash
#Adding matplotlib
module load python/3.10.11

python -m pip install matplotlib
