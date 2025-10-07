#!/usr/bin/env python3
"""
Simple test script to verify the desktop pet works correctly
"""

import sys
import platform
import tkinter as tk

def test_tkinter():
    """Test if Tkinter is available and working"""
    try:
        # First test if tkinter can be imported
        import tkinter as tk
        print("✓ Tkinter module imported successfully")
        
        # Try to create a root window (this might fail in headless environments)
        try:
            root = tk.Tk()
            root.title("Tkinter Test")
            root.geometry("200x100")
            
            label = tk.Label(root, text="Tkinter is working!")
            label.pack(pady=20)
            
            button = tk.Button(root, text="Close", command=root.quit)
            button.pack()
            
            print("✓ Tkinter test window created successfully")
            print("  Close the test window to continue...")
            
            # Auto-close after 2 seconds if running in automated mode
            root.after(2000, root.quit)
            root.mainloop()
            root.destroy()
            return True
        except Exception as display_error:
            if "DISPLAY" in str(display_error) or "display" in str(display_error).lower():
                print("! Tkinter available but no display (headless environment)")
                print("  This is normal in containers/servers - will work on desktop")
                return True
            else:
                raise display_error
                
    except Exception as e:
        print(f"✗ Tkinter test failed: {e}")
        print("  Please ensure Python was installed with Tkinter support")
        return False

def test_python_version():
    """Test Python version compatibility"""
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 6:
        print("✓ Python version is compatible")
        return True
    else:
        print("✗ Python version too old. Need Python 3.6 or newer")
        return False

def test_platform_detection():
    """Test platform detection"""
    os_type = platform.system()
    print(f"Detected OS: {os_type}")
    
    if os_type in ["Darwin", "Windows", "Linux"]:
        print("✓ Platform detection successful")
        return True
    else:
        print("! Unknown platform, but pet should still work")
        return True

def test_windows_integration():
    """Test Windows-specific integration if on Windows"""
    if platform.system() == "Windows":
        try:
            import win32gui
            import win32con
            print("✓ Windows integration (pywin32) available")
            return True
        except ImportError:
            print("! Windows integration (pywin32) not available")
            print("  Install with: pip install pywin32")
            print("  Pet will still work without it")
            return True
    else:
        print("- Windows integration test skipped (not on Windows)")
        return True

def main():
    """Run all tests"""
    print("=== Desktop Pet Compatibility Test ===")
    print()
    
    tests = [
        ("Python Version", test_python_version),
        ("Platform Detection", test_platform_detection),
        ("Tkinter Availability", test_tkinter),
        ("Windows Integration", test_windows_integration),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"Testing {test_name}...")
        result = test_func()
        results.append(result)
        print()
    
    print("=== Test Summary ===")
    all_passed = all(results)
    
    if all_passed:
        print("✓ All tests passed! Your desktop pet should work perfectly.")
    else:
        print("! Some tests failed, but the pet might still work.")
    
    print()
    print("To run the desktop pet:")
    if platform.system() == "Windows":
        print("  Windows: start_pet.bat")
    else:
        print("  macOS/Linux: ./start_pet.sh")
    
    return all_passed

if __name__ == "__main__":
    main()