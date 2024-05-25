
# Count - A File Metrics Counting Tool

`count` is a versatile command-line tool written in Python that allows you to count characters, bytes, lines, words, specific characters, and lines matching a pattern in a text file. It can read from a file or from standard input, making it more flexible than the traditional `wc` command.


### Explanation

- **Features**: A summary of the functionalities provided by the tool.
- **Installation**: Steps to make the script executable and accessible from anywhere in your PATH.
- **Usage**: Examples of basic and advanced usage of the `count` tool.
- **Testing**: Instructions on how to run the provided test script to ensure the `count` tool's functionality matches that of `wc`.
- **Example**: Sample commands and their outputs.
- **Contributing**: Information on how to contribute to the project.
- **License**: The license under which the project is distributed.

This `README.md` provides a comprehensive guide to understanding, installing, using, and testing the `count` tool.


## Features

- Count characters (`-m`)
- Count bytes (`-c`)
- Count lines (`-l`)
- Count words (`-w`)
- Count occurrences of a specific character (`--char`)
- Count lines matching a specific pattern (`--pattern`)
- Read from standard input if no filename is specified

## Installation

1. Clone the repository or download `count.py`.
2. Make the script executable:

    ```sh
    chmod +x count.py
    ```

3. Move the script to a directory in your PATH:

    ```sh
    mv count.py /usr/local/bin/count
    ```

## Usage

### Basic Usage

- To count all metrics (lines, words, bytes) in a file by default:

    ```sh
    count test.txt
    ```

- To count bytes in a file:

    ```sh
    count -c test.txt
    ```

- To count lines and words in a file:

    ```sh
    count -l -w test.txt
    ```

- To count characters from standard input:

    ```sh
    echo "Hello, world!" | count -m
    ```

- To count words and lines from standard input:

    ```sh
    echo "Hello, world!" | count -w -l
    ```

### Advanced Usage

- To count occurrences of a specific character:

    ```sh
    count --char a test.txt
    ```

- To count lines matching a specific pattern:

    ```sh
    count --pattern "Hello" test.txt
    ```

## Testing

A test script `test_count.py` is provided to compare the outputs of the `count` tool with the traditional `wc` command. The script runs various tests and checks if the results match.

### Running the Test

1. Ensure `test_count.py` is executable:

    ```sh
    chmod +x test_count.py
    ```

2. Run the test script:

    ```sh
    ./test_count.py
    ```

The script will output "pass" if all tests pass. If any test fails, it will specify which test failed and then print "Some tests failed".

## Example

```sh
$ count -l -w test.txt
```
10 50 test.txt

```sh
$ echo "Hello, world!" | count --char o
```
2

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you have any suggestions or bug reports.

## License

This project is licensed under the MIT License.