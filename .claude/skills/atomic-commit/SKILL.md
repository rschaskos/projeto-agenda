---
name: atomic-commit
description: Create atomic git commits organized by logical changes, feature, bug fix, or refactoring. Use when you need to organize multiple changes into clean, focused commits following best practices.
argument-hint: [optional-commit-pattern]
disable-model-invocation: false
allowed-tools: Bash(git *)
---

# Atomic Commit Helper

An atomic commit is a single logical change that stands alone and can be reverted independently without breaking functionality.

## Your task

Help organize staged and unstaged changes into well-structured atomic commits following these principles:

1. **One responsibility per commit**: Each commit addresses a single concern
2. **Logical grouping**: Related changes together, unrelated changes separated
3. **Independent testability**: Each commit should be independently testable
4. **Clear messages**: Use conventional commit format

## Process to follow

1. Check `git status` and `git diff` to understand all changes
2. Identify logical groupings in the modifications
3. Stage changes by logical unit using `git add`
4. Create commit with a descriptive message (conventional commit format)
5. Repeat until all changes are committed

## Commit message format

Use conventional commits:

```
<type>(<scope>): <subject>

<body (optional)>

<footer (optional)>
```

- **type**: feat, fix, refactor, style, docs, test, chore
- **scope**: Area of code affected (optional)
- **subject**: Brief description (imperative, lowercase, no period)
- **body**: Detailed explanation of what and why (wrap at 72 chars)
- **footer**: Reference issues (Fixes #123)

## When to split commits

Create separate commits for:
- Different features
- Bug fixes vs refactoring
- Documentation vs code changes
- Configuration vs implementation
- Test updates vs feature code
- Backend vs frontend changes

## When to combine commits

Keep together:
- A feature and its tests
- A bug fix and its test
- Related documentation updates
- Configuration changes for a feature

## Example commits

### Feature with related changes
```bash
git add contact/models.py contact/templates/contact/index.html
git commit -m "feat: add phone number field to contact

- Add phone field to Contact model
- Update contact list template to display phone
- Add phone validation in model"
```

### Bug fix
```bash
git add contact/views/contact_views.py
git commit -m "fix: handle empty contact list gracefully"
```

### Refactoring
```bash
git add contact/views/
git commit -m "refactor: reorganize views into modular structure"
```

### Documentation
```bash
git add README.md docs/
git commit -m "docs: add setup and installation instructions"
```

## Helpful git commands

```bash
# See current changes
git status
git diff

# Stage specific files
git add path/to/file

# Stage parts of a file
git add -p path/to/file

# See staged changes
git diff --staged

# Create commit
git commit -m "message"

# View recent commits
git log --oneline -10

# Undo last commit (keeps changes)
git reset --soft HEAD~1
```

## Best practices

- Commits should be logically independent
- Avoid mixing formatting with functional changes
- Test each commit in isolation if possible
- Write messages that explain the "why" not just the "what"
- Keep commits focused and reasonably sized
