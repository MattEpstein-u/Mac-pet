#!/usr/bin/env python3
"""
Container size test - shows what the pet container will look like
"""

import tkinter as tk
import platform

def test_container_size():
    """Show a preview of the container size and position"""
    
    print("=== Desktop Pet Container Preview ===")
    print()
    
    try:
        # Create a temporary window to get screen dimensions
        root = tk.Tk()
        root.withdraw()  # Hide the window
    except Exception as e:
        print(f"Running in headless environment: {e}")
        print("Using default screen dimensions for preview...")
        # Use common screen resolutions for preview
        screen_width = 1920
        screen_height = 1080
        root = None
    
    # Get screen dimensions
    if root:
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
    # If no root (headless), dimensions already set above
    
    # Calculate container size (1/8 of screen area)
    total_area = screen_width * screen_height
    container_area = total_area // 8
    container_side = int(container_area ** 0.5)
    
    # Constrain to reasonable limits
    container_width = max(200, min(container_side, 600))
    container_height = max(200, min(container_side, 400))
    
    # Position in bottom-right corner
    margin = 50
    container_x = screen_width - container_width - margin
    container_y = screen_height - container_height - margin
    
    print(f"Screen Resolution: {screen_width} x {screen_height}")
    print(f"Total Screen Area: {total_area:,} pixels")
    print(f"Container Area (1/8): {container_area:,} pixels")
    print(f"Container Size: {container_width} x {container_height}")
    print(f"Container Position: ({container_x}, {container_y})")
    print(f"Container Area Percentage: {(container_width * container_height / total_area * 100):.1f}%")
    print()
    
    # Show visual preview
    try:
        if root:
            root.deiconify()  # Show the window
        else:
            raise Exception("No display available")
        root.title("Pet Container Preview")
        root.geometry(f"{container_width}x{container_height}+{container_x}+{container_y}")
        root.configure(bg='#f0f0f0')
        root.attributes('-alpha', 0.85)
        
        # Create canvas with preview
        canvas = tk.Canvas(root, width=container_width, height=container_height, 
                          bg='#f0f0f0', highlightthickness=0)
        canvas.pack()
        
        # Draw container background
        canvas.create_rectangle(5, 5, container_width-5, container_height-5,
                               fill='#f8f8f8', outline='#e0e0e0', width=1)
        
        # Add preview pet
        pet_x = container_width // 2
        pet_y = container_height // 2
        canvas.create_text(pet_x, pet_y, text='🐱', font=('Arial', 32), anchor='center')
        
        # Add labels
        canvas.create_text(container_width-10, 10, text='🏠', 
                          font=('Arial', 12), anchor='ne', fill='#c0c0c0')
        
        canvas.create_text(10, container_height-30, 
                          text=f'{container_width}x{container_height}',
                          font=('Arial', 10), anchor='w', fill='#888')
        
        canvas.create_text(container_width//2, 30, 
                          text='Desktop Pet Container Preview',
                          font=('Arial', 12, 'bold'), anchor='center', fill='#666')
        
        print("Preview window opened!")
        print("This shows the size and position of your pet's container.")
        print("Close the preview window when you're done.")
        print()
        
        # Auto close after 10 seconds or user interaction
        def close_preview():
            root.quit()
            
        root.bind('<Button-1>', lambda e: close_preview())
        root.bind('<Key>', lambda e: close_preview())
        root.focus_set()
        root.after(10000, close_preview)  # Auto close after 10 seconds
        
        root.mainloop()
        
    except Exception as e:
        print(f"Could not show preview (headless environment): {e}")
        print("Preview would show a container window at the calculated position.")
    
    finally:
        if root:
            root.destroy()
    
    print("Container preview complete!")
    return container_width, container_height, container_x, container_y

if __name__ == "__main__":
    test_container_size()