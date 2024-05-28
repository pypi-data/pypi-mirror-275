# boolgen

`boolgen` is a Python library and command-line tool for generating and
simplifying Boolean expressions from truth tables. 

The library implements a version of the [Quine-McCluskey
method](https://en.wikipedia.org/wiki/Quine%E2%80%93McCluskey_algorithm) to
perform the simplification. I created it to help with [designing digital logic
circuits](https://github.com/SebLague/Digital-Logic-Sim) from truth tables.

## Installation

To install `boolgen`, use pip:

```bash
pip install boolgen
```

If you download the source, you can run the [unit tests](tests/).

## Command-Line Interface

The `boolgen` tool can be used from the command line to process truth tables
stored in files and output simplified Boolean expressions.

### Syntax

```bash
boolgen <input_file>
```

- `<input_file>`: Path to the input file containing the truth table.

If no filename is provided, then `boolgen` will try to read the table from
`STDIN`.

### Example Input File

Create a file named `input.txt` with the following content:

```
A B C D= E=
0 0 0 0 1
0 0 1 1 0
0 1 0 1 0
1 0 0 1 0
1 1 1 0 1
```

Input and output variables can be identified with any alphanumeric string
(including underscores). Output variables are identified by a pre- or postfix
'='. If no output variable is explicitly declared, the last column in the table
is assumed to be the output.

### Output

`boolgen` will output the simplified Boolean expressions for each output variable in the truth table.

```
D = A | B & ~C
E = ~A & ~B & ~C | A & B & C
```

In degenerate cases, an output variable might be set to `0` or `1`.

## Library

You can also `import boolgen` into your own project. See the function
definitions for an idea of how it all works.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See [LICENSE.md](LICENSE.md)
for details.

TBQH I used ChatGPT liberally when creating this module, so if you find your
own code in here, please let me know so I can remove it or else attribute you
properly.
