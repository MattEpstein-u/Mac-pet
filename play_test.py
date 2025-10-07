#!/usr/bin/env python3
"""
Quick launcher for the interactive desktop pet test
"""

import sys
import os

def main():
    print("🎮 Desktop Pet Interactive Test Launcher")
    print("=" * 50)
    print()
    print("This will open a window where you can:")
    print("• Play with the pet using mouse and buttons")
    print("• Test all behaviors (following, wandering, sleeping)")  
    print("• See exactly how the pet will behave on your desktop")
    print("• Try different interactions without installation")
    print()
    
    try:
        # Import and run the interactive test
        import test_interactive
        
        print("Starting interactive test... (close window when done)")
        print()
        
        pet = test_interactive.TestDesktopPet()
        pet.run()
        
        print()
        print("✅ Interactive test completed!")
        print()
        print("Ready to install? Run:")
        print("• macOS: ./install.sh")
        print("• Windows: install_windows.bat")
        
    except ImportError as e:
        print(f"❌ Error: Could not import test_interactive: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error running interactive test: {e}")
        print()
        print("This might happen if:")
        print("• You're in a headless environment (no display)")
        print("• Tkinter is not properly installed")
        print("• Python version is too old")
        print()
        print("Try running: python3 test_compatibility.py")
        sys.exit(1)

if __name__ == "__main__":
    main()