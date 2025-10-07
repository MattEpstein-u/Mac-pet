#!/bin/bash
# Desktop Pet Startup Script for macOS

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Path to the desktop pet Python script
PET_SCRIPT="$SCRIPT_DIR/desktop_pet.py"

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "Error: Python not found. Please install Python 3."
    exit 1
fi

# Check if the pet script exists
if [ ! -f "$PET_SCRIPT" ]; then
    echo "Error: desktop_pet.py not found in $SCRIPT_DIR"
    exit 1
fi

# Run the desktop pet
echo "Starting Desktop Pet..."
cd "$SCRIPT_DIR"
$PYTHON_CMD "$PET_SCRIPT" &

echo "Desktop Pet started! Check your desktop."