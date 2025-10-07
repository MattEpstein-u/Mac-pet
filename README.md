# Cross-Platform Desktop Pet 🐱

A cute, simple desktop pet for macOS and Windows that lives in a small container on your desktop background and provides companionship while you work!

## Features

- **Small container**: Lives in a compact area (1/8 screen size) in desktop corner
- **Desktop background**: Only visible when all apps are minimized to desktop
- **Cross-platform**: Works on both macOS and Windows
- **Interactive**: Click and drag to move within container, double-click to play
- **Smart behavior**: Follows your cursor and wanders randomly in container
- **Multiple states**: Idle, walking, sleeping, and playing animations
- **Auto-startup**: Automatically starts when you log in
- **Non-intrusive**: Subtle design that blends with your wallpaper

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

- **Container**: Pet lives in a small, subtle container in the corner of your desktop
- **Visibility**: Only appears when all applications are minimized to show the desktop
- **Move**: Click and drag the pet to move it within its container space
- **Play**: Double-click on the pet to make it happy and playful
- **Follow**: Move your cursor near the container and the pet will follow
- **Wandering**: Pet randomly explores different spots within its container
- **Automatic behaviors**: Pet will randomly sleep, play, and idle
- **Subtle design**: Container blends nicely with most desktop wallpapers

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

### Preview and Test the Pet
See what your pet will look like and test its behavior before installing:
```bash
# macOS/Linux
python3 demo.py              # Animation preview
python3 test_container.py    # Container size preview  
python3 test_interactive.py  # Interactive test mode - play with the pet!

# Windows  
python demo.py               # Animation preview
python test_container.py     # Container size preview
python test_interactive.py   # Interactive test mode - play with the pet!
```

### 🎮 Interactive Testing Mode - **TRY IT FIRST!**
**Test all pet behaviors in a regular window before installing:**

**Quick Start:**
```bash
python3 test_interactive.py    # Direct interactive test
# OR
python3 play_test.py          # Guided launcher with instructions
```

**What you can test:**
- 🎮 **Control buttons** - Trigger play, sleep, walk, and random movement
- 🖱️ **Mouse following** - Move mouse near pet to make it follow
- 🎯 **Click and drag** - Move the pet around the container
- 🏠 **Container preview** - See exactly how it will look on desktop  
- 📊 **Live status** - See current pet state in real-time
- ✨ **All behaviors** - Test wandering, animations, and interactions
- 🔄 **No restart needed** - Test everything without installation!

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
- `test_container.py` - Container size and position preview
- `test_interactive.py` - **Interactive test mode - play with the pet!**
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