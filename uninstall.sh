#!/bin/bash
# Uninstallation script for Desktop Pet on macOS

echo "=== Desktop Pet Uninstallation ==="
echo

LAUNCH_AGENTS_DIR="$HOME/Library/LaunchAgents"
PLIST_FILE="$LAUNCH_AGENTS_DIR/com.user.desktoppet.plist"

# Stop any running pet processes
echo "Stopping any running desktop pet processes..."
pkill -f "desktop_pet.py" 2>/dev/null || true

# Unload the LaunchAgent
if [ -f "$PLIST_FILE" ]; then
    launchctl unload "$PLIST_FILE" 2>/dev/null || true
    echo "✓ Unloaded LaunchAgent"
    
    # Remove the plist file
    rm -f "$PLIST_FILE"
    echo "✓ Removed LaunchAgent plist file"
else
    echo "! LaunchAgent plist file not found"
fi

# Clean up log files
rm -f /tmp/desktop_pet.log /tmp/desktop_pet_error.log

echo
echo "=== Uninstallation Complete! ==="
echo "The desktop pet has been removed from auto-startup."
echo "You can still run it manually with ./start_pet.sh if you want."
echo