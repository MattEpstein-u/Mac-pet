# Cross-Platform Desktop Pet 🐱

A cute, simple desktop pet for macOS and Windows that lives on your desktop background and provides companionship while you work!

## Features

- **Desktop background**: Only visible when all apps are minimized to desktop
- **Cross-platform**: Works on both macOS and Windows
- **Interactive**: Click and drag to move, double-click to play
- **Smart behavior**: Follows your cursor when nearby
- **Multiple states**: Idle, walking, sleeping, and playing animations
- **Auto-startup**: Automatically starts when you log in
- **Non-intrusive**: Won't interfere with your work or applications

## Installation

### macOS Installation

1. **Download or clone this repository** to your Mac
2. **Open Terminal** and navigate to the Mac-pet folder:
   ```bash
   cd /path/to/Mac-pet
   ```
3. **Run the installation script**:
   ```bash
   chmod +x install.sh
   ./install.sh
   ```

### Windows Installation

1. **Download or clone this repository** to your Windows PC
2. **Open Command Prompt as Administrator** and navigate to the Mac-pet folder:
   ```cmd
   cd C:\path\to\Mac-pet
   ```
3. **Run the installation script**:
   ```cmd
   install_windows.bat
   ```

That's it! Your desktop pet will start immediately and will automatically appear every time you restart your computer.

## Manual Usage

### macOS
- **Start the pet**: `./start_pet.sh`
- **Stop the pet**: Use Activity Monitor or `killall Python`
- **Uninstall**: `./uninstall.sh`

### Windows
- **Start the pet**: `start_pet.bat`
- **Stop the pet**: Use Task Manager to end Python process
- **Uninstall**: `uninstall_windows.bat`

## Interacting with Your Pet

- **Visibility**: The pet only appears when all applications are minimized to show the desktop
- **Move**: Click and drag the pet to move it around your desktop
- **Play**: Double-click on the pet to make it happy and playful
- **Follow**: Move your cursor near the pet and it will follow you around
- **Automatic behaviors**: Your pet will randomly sleep, play, and idle
- **Non-intrusive**: Won't appear over your applications while you work

## Requirements

- **macOS** (tested on Sonoma 14.6.1) OR **Windows 10/11**
- **Python 3** (usually pre-installed on Mac, download from python.org for Windows)
- **Tkinter** (included with Python)
- **Optional for Windows**: pywin32 (automatically installed for better desktop integration)

## Troubleshooting

### Pet doesn't start automatically
1. Check if the LaunchAgent is loaded:
   ```bash
   launchctl list | grep desktoppet
   ```
2. If not found, try reinstalling:
   ```bash
   ./uninstall.sh
   ./install.sh
   ```

### Preview the Pet
See what your pet will look like before installing:
```bash
# macOS/Linux
python3 demo.py

# Windows  
python demo.py
```

### Testing Compatibility
Run the compatibility test before installation:
```bash
# macOS/Linux
python3 test_compatibility.py

# Windows
python test_compatibility.py
```

### Pet appears but doesn't respond
- Make sure you're clicking directly on the pet emoji
- Try double-clicking to wake it up

### Permission issues
If you get permission errors, you may need to give Terminal or Python accessibility permissions:
1. Go to System Preferences > Security & Privacy > Privacy
2. Click on "Accessibility" 
3. Add Terminal or Python to the list of allowed apps

## Customization

You can customize your pet by editing `desktop_pet.py`:

- **Change the pet appearance**: Modify the `pet_sprites` dictionary with different emojis
- **Adjust behavior timing**: Change the values in the `update_behavior()` function
- **Modify animations**: Edit the `animations` dictionary

## Files Included

- `desktop_pet.py` - Main pet application (cross-platform)
- `demo.py` - Preview script to see pet animations
- `test_compatibility.py` - System compatibility checker
- `start_pet.sh` - macOS startup script
- `start_pet.bat` - Windows startup script
- `install.sh` - macOS installation script
- `install_windows.bat` - Windows installation script
- `uninstall.sh` - macOS removal script
- `uninstall_windows.bat` - Windows removal script
- `com.user.desktoppet.plist` - macOS LaunchAgent configuration

## Cross-Platform Notes

This desktop pet is designed to work seamlessly on both macOS and Windows:

### macOS Features:
- Uses macOS LaunchAgents for automatic startup
- Desktop-level window positioning to stay below applications
- Optimized for macOS Sonoma 14.6.1

### Windows Features:
- Uses Windows Startup folder for automatic startup
- Optional pywin32 integration for better desktop positioning
- Compatible with Windows 10 and 11

### Both Platforms:
- Tkinter's transparency features for clean desktop integration
- Smart window management to stay on desktop background only
- Cross-platform cursor following and interaction

Enjoy your new desktop companion! 🐾