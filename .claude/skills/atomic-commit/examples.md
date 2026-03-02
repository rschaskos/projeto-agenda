# Atomic Commit Examples for Projeto Agenda

## Good atomic commits (from this project)

### Feature implementation
```
feat: implement contacts list template

- Create responsive table for contacts
- Add columns: id, first_name, last_name, phone, email
- Link contact ID to detail view
- Add table styling
```

### Refactoring module structure
```
refactor: reorganize views into modular structure

- Move contact/views.py to contact/views/contact_views.py
- Create contact/views/__init__.py to export views
- Benefits: keeps views.py from becoming too large
```

### Configuration setup
```
feat: add local settings configuration support

- Add import for local_settings in project/settings.py
- Add project/local_settings.py to .gitignore
- Allows developers to override settings locally
```

### Bug fix
```
fix: handle null response in contact detail view

- Add null check before accessing contact data
- Return 404 for non-existent contacts
- Prevents application crashes
```

### Admin improvements
```
refactor: improve django admin for contacts

- Add 'show' field to list_display
- Increase list_per_page from 10 to 15
- Make 'show' field editable inline
```

### Template restructuring
```
refactor: restructure base template with partials

- Extract head section to _head.html partial
- Extract header section to _header.html partial
- Benefits: easier to maintain, reusable components
```

### Documentation
```
docs: add api endpoint documentation

- Document all contact endpoints
- Include request/response examples
- Add error handling information
```

### Styling
```
style: update global stylesheet

- Add responsive table styles
- Improve contact form styling
- Add dark mode support
```

## Examples of BAD commits (should be split)

❌ BAD - Too many concerns:
```
feat: update contact module

- Add phone validation
- Restructure views
- Update admin
- Create list template
- Add detail page
- Update CSS
```

✅ GOOD - Split properly:
```
refactor: reorganize views into modular structure
feat: add contact detail and search routes
refactor: improve django admin for contacts
feat: implement contacts list template
feat: add contact detail template
style: update global stylesheet
```

## Project-specific guidelines

For **projeto-agenda**:

- Keep Django model changes separate from view changes
- Keep template changes separate from style changes
- Group related migrations together
- Document admin customizations
- Use consistent naming in commit messages:
  - `feat:` for new features (contacts list, detail page)
  - `fix:` for bug fixes
  - `refactor:` for restructuring (views, templates, admin)
  - `style:` for CSS/styling changes
  - `docs:` for documentation
  - `test:` for test additions
