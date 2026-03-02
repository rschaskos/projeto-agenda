# Commit Guidelines for Projeto Agenda

## Conventional Commit Format

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

## Commit Types

| Type | Usage | Example |
|------|-------|---------|
| `feat` | New feature | feat: add contact search |
| `fix` | Bug fix | fix: resolve null pointer in detail view |
| `refactor` | Code restructuring | refactor: reorganize views |
| `style` | CSS/styling changes | style: add responsive tables |
| `docs` | Documentation | docs: update readme |
| `test` | Tests | test: add contact model tests |
| `chore` | Dependencies, config | chore: update django version |

## Scope (Optional)

Common scopes for this project:
- `contact` - Contact model/views
- `admin` - Django admin customization
- `template` - HTML templates
- `api` - API endpoints
- `style` - CSS/styling
- `db` - Database/migrations
- `settings` - Configuration

Examples:
- `feat(contact): add phone validation`
- `fix(admin): handle empty list`
- `style(contact): improve form layout`

## Subject Line Rules

1. Use imperative mood: "add" not "added" or "adds"
2. Don't capitalize first letter (lowercase)
3. No period at the end
4. Keep under 50 characters when possible
5. Be specific: "fix connection timeout" not "fix bug"

✅ Good:
- `feat: add contact search functionality`
- `fix: handle null response gracefully`
- `refactor: simplify contact list template`

❌ Bad:
- `feat: Add contact search functionality` (capitalized)
- `feat: Added contact search` (wrong tense)
- `fix: Fixed bug in the contact module.` (period)
- `feat: stuff` (too vague)

## Body (Optional)

Use when the change needs explanation:

```
refactor: reorganize views into modular structure

This prevents the views.py file from becoming too large and hard
to maintain. By splitting into contact_views.py, we can organize
related views together while keeping __init__.py clean.

Benefits:
- Easier to navigate
- Clearer organization
- Follows Django conventions
```

Rules:
- Wrap at 72 characters
- Explain **what** and **why**, not **how**
- Use bullet points for multiple points

## Footer (Optional)

Reference issues or breaking changes:

```
fix: prevent contact deletion bug

Fixes #234
Closes #567
```

Common prefixes:
- `Fixes #123` - closes issue 123
- `Closes #123` - same as fixes
- `Relates to #123` - related but not closing
- `BREAKING CHANGE: description` - for major changes

## Project-Specific Rules

1. **Model changes should be separate from view changes**
   - `feat: add phone field to Contact model`
   - `feat(contact): update list view for phone field`

2. **Template changes should be separate from styles**
   - `feat: create contact detail template`
   - `style: add contact detail page styling`

3. **Admin customizations should document the intent**
   - `refactor(admin): add show field with inline editing`

4. **Always test before committing**
   - Each commit should leave the code in a working state

5. **Database migrations get their own commits**
   - `feat: add phone field migration`
   - Then: `feat: add phone field to Contact model`

## Common Patterns in This Project

```bash
# Feature with related changes
git add feature_files
git commit -m "feat(scope): implement new feature

- Implementation detail 1
- Implementation detail 2"

# Bug fix
git add bug_files
git commit -m "fix(scope): resolve specific bug

Brief explanation of the issue and how it was fixed."

# Refactoring for clarity
git add refactored_files
git commit -m "refactor(scope): improve code organization

No behavioral changes."

# Style/CSS updates
git add css_files
git commit -m "style(scope): improve layout and appearance"

# Documentation
git add docs_files
git commit -m "docs: add setup instructions"
```

## Quick Reference

**To create an atomic commit:**

1. See changes: `git status`
2. Review diff: `git diff [file]`
3. Stage related files: `git add path/to/files`
4. Commit: `git commit -m "type(scope): message"`
5. Verify: `git log --oneline -3`

**To fix the last commit:**
```bash
# Undo and restage
git reset --soft HEAD~1
git add [files]
git commit -m "new message"
```

**To split a large commit:**
```bash
git reset --soft HEAD~1
git reset                    # unstage everything
git add [file1]            # stage first group
git commit -m "first message"
git add [file2]            # stage second group
git commit -m "second message"
```
