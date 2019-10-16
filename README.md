# diff-format

Takes a _DIFF_ formated file and removes all the unnecessary lines returning a new file containing just the changed lines (the ones that has a `+` at the beggining).

## Run

```bash
 $ ./diff-format.py --diff=FILE [--output=FILE]
```

#### Arguments
- `diff`: path to the _diff_ formated file
- `output`: if not specified the output is shown in the _standard output_

## Clean

```bash
 $ ./clean.sh
```

