# Advanced Hashing Tool

A versatile tool for hashing data and files, built with Python. This tool supports a variety of hashing algorithms and allows for the optional addition of salt for enhanced security.

## Features

- **Multiple Algorithms**: Supports md5, sha1, sha256, sha512, blake2b, and blake2s.
- **Salting**: Enhance security by adding a salt to your hashing process.
- **File Hashing**: Efficiently hash files of any size.
- **Command Line Interface**: Intuitive command line interface for quick hashing operations.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/razabhadur/hashing_tool.git
Navigate to the directory:

bash
Copy code
cd hashing_tool
Ensure you have Python installed on your machine.

Usage
Hashing Data
bash
python your_script_name.py -d "data_to_hash" -a sha256 -s "mysalt"
Hashing a File
bash
python your_script_name.py -f "path_to_file" -a sha512
Command Line Arguments
-d, --data: Specify the string data you wish to hash.
-f, --file: Specify the path to the file you wish to hash.
-a, --algorithm: Choose the hashing algorithm (default: md5).
-s, --salt: Optionally add a salt to the hashing process.
Contributing
We appreciate all contributions! If you have suggestions or improvements, please open a pull request or issue.

License
This project falls under the MIT License. See the LICENSE.md file for more information.


