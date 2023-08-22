Advanced Hashing Tool
A versatile tool for hashing data and files, built with Python. This tool supports a variety of hashing algorithms and allows for the optional addition of salt for enhanced security.

Features
Multiple Algorithms: md5, sha1, sha256, sha512, blake2b, blake2s
Salting: Option to add a salt to your hashing process.
File Hashing: Can hash files of any size.
Command Line Interface: Easy to use command line interface for efficient hashing.
Installation
Clone the repository to your local machine:
git clone https://github.com/razabhadur/hashing_tool.git
Navigate to the directory:
cd hashing_tool
Ensure you have Python installed on your system.
Usage
Hashing Data
python your_script_name.py -d "data_to_hash" -a sha256 -s "mysalt"
Hashing a File

python your_script_name.py -f "path_to_file" -a sha512
Available Arguments
-d, --data: The string data you want to hash.
-f, --file: The path to the file you want to hash.
-a, --algorithm: The hashing algorithm you want to use. Default is md5.
-s, --salt: Optional salt you want to add to the hashing process.
Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.
