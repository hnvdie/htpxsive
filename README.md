# htpxsive.py

A simple httpx recursive script based on Python.

## Description

`htpxsive.py` is a tool designed to recursively extract URLs from an input file using `httpx`. It processes the input file, extracts the URLs, and saves the results to an output file. The recursion depth can be specified to run the extraction process multiple times, using the results from the previous iteration as the input for the next.

## Usage

```bash
python htpxsive.py [input_file] -r=[depth]
```

### Arguments

- `input_file`: Path to the input file containing URLs.
- `-r=[depth]`: Recursive depth. The number of times to run the extraction process.

### Examples

Run the script once:
```bash
python htpxsive.py mylisturl.txt -r=1
```

Run the script four times recursively:
```bash
python htpxsive.py mylisturl.txt -r=4
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hnvdie/htpxsive.git
   ```
2. Change into the project directory:
   ```bash
   cd htpxsive
   ```
3. Ensure you have `httpx` installed:
   ```bash
   go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

Created by Rain.xvf
