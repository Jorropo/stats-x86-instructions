# Instruction Stater

This shell and python script will use objdump to count how many instruction is in a binary file (and order them by that).

## Usage

```sh
./scan.sh <command name OR binary path>
```

### Output

It output as CSV in stdout without headers.

## Need

- objdump
- python 3 (can run with 2 but slowly, to do change python3 to python2 in parse.py)
- Bash (and some utils, whereis, cut, pwd, dirname (should be allready in it))

## License

[GPLv3](LICENSE.md)
