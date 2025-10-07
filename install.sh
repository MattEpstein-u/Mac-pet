#!/bin/bash
# Installation script for Desktop Pet on macOS

echo "=== Desktop Pet Installation for macOS ==="
echo

# Get current directory
CURRENT_DIR="$(pwd)"
LAUNCH_AGENTS_DIR="$HOME/Library/LaunchAgents"

# Check if we're in the right directory
if [ ! -f "desktop_pet.py" ]; then
    echo "Error: Please run this script from the directory containing desktop_pet.py"
    exit 1
fi

echo "Installing Desktop Pet..."

# Make the startup script executable
chmod +x start_pet.sh
echo "✓ Made start_pet.sh executable"

# Create LaunchAgents directory if it doesn't exist
mkdir -p "$LAUNCH_AGENTS_DIR"
echo "✓ Created LaunchAgents directory"

# Update the plist file with the correct path
PLIST_CONTENT=$(cat com.user.desktoppet.plist)
UPDATED_PLIST="${PLIST_CONTENT//REPLACE_WITH_FULL_PATH/$CURRENT_DIR}"
echo "$UPDATED_PLIST" > "$LAUNCH_AGENTS_DIR/com.user.desktoppet.plist"
echo "✓ Installed LaunchAgent plist file"

# Load the LaunchAgent
launchctl load "$LAUNCH_AGENTS_DIR/com.user.desktoppet.plist" 2>/dev/null || true
echo "✓ Loaded LaunchAgent"

echo
echo "=== Installation Complete! ==="
echo
echo "Your desktop pet is now installed and will start automatically when you log in."
echo
echo "Manual Controls:"
echo "• To start the pet manually: ./start_pet.sh"
echo "• To stop the pet: killall Python (or use Activity Monitor)"
echo "• To uninstall: ./uninstall.sh"
echo
echo "Pet Features:"
echo "• Lives in a small container in the corner of your desktop"
echo "• Click and drag to move the pet within its container"
echo "• Double-click to make it play"
echo "• The pet will follow your cursor and wander randomly"
echo "• It will sleep, play, and be idle randomly"
echo "• Only visible when all apps are minimized to desktop"
echo
echo "Starting the pet now..."
./start_pet.sh

echo
echo "Enjoy your new desktop companion! 🐱"