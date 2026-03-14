#!/usr/bin/sh

# 1. Display pip version
echo "Using pip version:"
pip --version

# 2. Define the target directory
LIB_DIR="local_lib"
LOG_FILE="install.log"
GIT_URL="git+https://github.com/jaraco/path.git"

# 3. Crush the library if it already exists
if [ -d "$LIB_DIR" ]; then
    echo "Existing $LIB_DIR found. Crushing it..."
    rm -rf "$LIB_DIR"
fi

# 4. Install the dev version and redirect logs
echo "Installing path.py development version..."
pip install -t "$LIB_DIR" "$GIT_URL" > "$LOG_FILE" 2>&1
# pip install --target "$LIB_DIR" "$GIT_URL" > "$LOG_FILE" 2>&1

# 5. Check if install was successful and run the program
if [ $? -eq 0 ]; then
    echo "Installation successful! Running my_program.py..."
    # We must tell Python to look inside local_lib for the module
    export PYTHONPATH=$PYTHONPATH:$(pwd)/$LIB_DIR
    python3 my_program.py
else
    echo "Installation failed. Check $LOG_FILE for details."
fi