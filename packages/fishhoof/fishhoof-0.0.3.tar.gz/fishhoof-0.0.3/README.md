# fishhoof

## Usage



Example:
```bash

fishhoof /Users/mtm/pdev/taylormonacelli/notes /Users/mtm/Documents/Obsidian\ Vault  --exclude=pyc --exclude=.git --exclude=.venv --newer=1d
```

Which is same as

```bash

find /Users/mtm/pdev/taylormonacelli/notes /Users/mtm/Documents/Obsidian\ Vault -type f -not -path "*/\.git/*" -not -path "*/\.venv/*" -not -name "*.pyc" -mmin -$((24 * 60 * 60))


```
