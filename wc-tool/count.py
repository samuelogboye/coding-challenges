#!/usr/bin/env python3

import argparse
import sys

def throw_error(filename):
    raise ValueError(f"count: {filename}: No such file or directory")

def count_all(content, filename):
    """Count all metrics in a file."""
    num_lines = count_lines(content)
    num_words = count_words(content)
    num_bytes = count_bytes(content)
    return f"{num_lines} {num_words} {num_bytes}"

def count_characters(content):
    """Count the number of characters in a file."""
    num_chars = len(content)
    return num_chars

def count_bytes(content):
    """Count the number of bytes in a file."""
    num_bytes = len(content.encode('utf-8'))
    return num_bytes

def count_lines(content):
    """Count the number of lines in a file."""
    lines = content.splitlines()
    num_lines = len(lines)
    return num_lines

def count_words(content):
    """Count the number of words in a file."""
    words = content.split()
    num_words = len(words)
    return num_words

def count_specific_char(content, char):
    """Count the occurrences of a specific character in a file."""
    num_specific_char = content.count(char)
    return num_specific_char

def count_pattern_lines(content, pattern):
    """Count the number of lines matching a pattern in a file."""
    lines = content.splitlines()
    matching_lines = [line for line in lines if pattern in line]
    num_matching_lines = len(matching_lines)
    return num_matching_lines

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        print(f"count: {message}\nTry 'count --help' for more information")
        raise SystemExit(2)

def read_content(filename):
    """Read the content from a file or from standard input."""
    if filename:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read(), filename
        except FileNotFoundError:
            throw_error(filename)
        except Exception as e:
            print(f"An error occurred: {e}")
            raise SystemExit(1)
    else:
        content = sys.stdin.read()
        return content, ''

def main():
    parser = CustomArgumentParser(description='Count characters, bytes, lines, or words in a text file.')
    parser.add_argument('filename', type=str, nargs='?', help='The name of the file to process (reads from stdin if not provided)')
    
    # Dynamically create flags
    flags = {
        '-c': ('Count size of file in bytes', count_bytes),
        '-l': ('Count lines in the file', count_lines),
        '-w': ('Count words in the file', count_words),
        '-m': ('Count number of characters in the file', count_characters)
    }

    for flag, (help_text, _) in flags.items():
        parser.add_argument(flag, action='store_true', help=help_text)

    parser.add_argument('--char', type=str, help='Count occurrences of a specific character')
    parser.add_argument('--pattern', type=str, help='Count lines matching a specific pattern')

    args = parser.parse_args()

    # Read content from file or stdin
    content, source = read_content(args.filename)

    # Determine which function to call based on the flags
    selected_functions = [func for flag, (_, func) in flags.items() if getattr(args, flag.replace('-', ''))]

    # Include specific character and pattern counting if specified
    if args.char:
        selected_functions.append(lambda content: count_specific_char(content, args.char))
    if args.pattern:
        selected_functions.append(lambda content: count_pattern_lines(content, args.pattern))

    # Default to counting all if no specific flag is provided
    if not selected_functions:
        selected_functions = [count_all]

    # Call the selected functions and print results
    try:
        if count_all in selected_functions:
            output = count_all(content, source)
            print(f"{output} {source}")
        else:
            results = [str(func(content)) for func in selected_functions]
            print(f"{' '.join(results)} {source}")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
