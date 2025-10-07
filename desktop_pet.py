#!/usr/bin/env python3
"""
Cross-platform Desktop Pet for macOS and Windows
A cute animated pet that sits on your desktop background and follows your cursor around.
Only visible when all applications are minimized to desktop.
"""

import tkinter as tk
from tkinter import PhotoImage
import random
import math
import platform
import sys

class DesktopPet:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_pet()
        self.setup_animations()
        
        # Pet state
        self.target_x = 100
        self.target_y = 100
        self.current_x = 100
        self.current_y = 100
        self.is_dragging = False
        self.drag_start_x = 0
        self.drag_start_y = 0
        self.animation_frame = 0
        self.idle_counter = 0
        self.state = "idle"  # idle, walking, sleeping, playing
        
        # Start the main loops
        self.animate()
        self.update_behavior()
        
    def setup_window(self):
        """Configure the main window"""
        self.root.title("Desktop Pet")
        self.root.geometry("100x100+100+100")
        
        # Get the operating system
        self.os_type = platform.system()
        
        # Configure window to stay on desktop background (below other apps)
        if self.os_type == "Darwin":  # macOS
            # On macOS, use level -1 to stay below normal windows
            self.root.attributes('-alpha', 0.9)  # Slight transparency
            self.root.overrideredirect(True)  # Remove window decorations
            # Set window level to desktop level (below normal windows)
            try:
                # This puts the window at desktop level on macOS
                self.root.call('wm', 'attributes', '.', '-topmost', False)
                self.root.call('wm', 'attributes', '.', '-level', 'desktop')
            except:
                # Fallback: just don't stay on top
                pass
                
        elif self.os_type == "Windows":  # Windows
            # On Windows, use specific attributes to stay on desktop
            self.root.overrideredirect(True)  # Remove window decorations
            self.root.attributes('-alpha', 0.9)  # Slight transparency
            # Try to set window to desktop level
            try:
                # Import Windows-specific modules if available
                import win32gui
                import win32con
                # Get window handle and set it below normal windows
                hwnd = int(self.root.wm_frame(), 16)
                win32gui.SetWindowPos(hwnd, win32con.HWND_BOTTOM, 0, 0, 0, 0, 
                                    win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_NOACTIVATE)
            except ImportError:
                # If win32gui not available, just don't stay on top
                print("Note: Install pywin32 for better Windows desktop integration")
                pass
        else:  # Linux and others
            self.root.overrideredirect(True)
            self.root.attributes('-alpha', 0.9)
            # Try to stay below other windows
            try:
                self.root.attributes('-type', 'desktop')
            except:
                pass
        
        # Make window click-through for the background but not the pet
        self.root.configure(bg='white')
        try:
            self.root.wm_attributes('-transparentcolor', 'white')
        except:
            # Some systems don't support transparent color
            pass
        
    def setup_pet(self):
        """Create the pet display"""
        self.canvas = tk.Canvas(self.root, width=100, height=100, 
                               bg='white', highlightthickness=0)
        self.canvas.pack()
        
        # Create simple pet sprite (we'll use text/shapes since we don't have image files)
        self.pet_sprites = {
            'idle1': '🐱',
            'idle2': '😺', 
            'walk1': '🐾',
            'walk2': '🐱',
            'sleep': '😴',
            'play': '😸'
        }
        
        # Create the pet on canvas
        self.pet = self.canvas.create_text(50, 50, text=self.pet_sprites['idle1'], 
                                         font=('Arial', 32), anchor='center')
        
        # Bind mouse events
        self.canvas.bind('<Button-1>', self.start_drag)
        self.canvas.bind('<B1-Motion>', self.drag_pet)
        self.canvas.bind('<ButtonRelease-1>', self.end_drag)
        self.canvas.bind('<Double-Button-1>', self.pet_interaction)
        
    def setup_animations(self):
        """Setup animation sequences"""
        self.animations = {
            'idle': ['idle1', 'idle2', 'idle1', 'idle1'],
            'walk': ['walk1', 'walk2', 'walk1', 'walk2'],
            'sleep': ['sleep', 'sleep', 'sleep', 'sleep'],
            'play': ['play', 'idle1', 'play', 'idle2']
        }
        
    def start_drag(self, event):
        """Start dragging the pet"""
        self.is_dragging = True
        self.drag_start_x = event.x
        self.drag_start_y = event.y
        
    def drag_pet(self, event):
        """Handle pet dragging"""
        if self.is_dragging:
            # Calculate new window position
            new_x = self.root.winfo_x() + (event.x - self.drag_start_x)
            new_y = self.root.winfo_y() + (event.y - self.drag_start_y)
            
            # Keep pet on screen
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            
            new_x = max(0, min(new_x, screen_width - 100))
            new_y = max(0, min(new_y, screen_height - 100))
            
            self.root.geometry(f"100x100+{new_x}+{new_y}")
            
    def end_drag(self, event):
        """End dragging"""
        self.is_dragging = False
        
    def pet_interaction(self, event):
        """Handle double-click interaction"""
        self.state = "play"
        self.idle_counter = 0
        
    def get_cursor_position(self):
        """Get mouse cursor position"""
        try:
            x = self.root.winfo_pointerx()
            y = self.root.winfo_pointery()
            return x, y
        except:
            return self.current_x, self.current_y
            
    def ensure_desktop_level(self):
        """Ensure the window stays at desktop level (platform-specific)"""
        try:
            if self.os_type == "Darwin":  # macOS
                # Periodically ensure we stay at desktop level
                self.root.call('wm', 'attributes', '.', '-level', 'desktop')
            elif self.os_type == "Windows":  # Windows
                try:
                    import win32gui
                    import win32con
                    hwnd = int(self.root.wm_frame(), 16)
                    win32gui.SetWindowPos(hwnd, win32con.HWND_BOTTOM, 0, 0, 0, 0, 
                                        win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_NOACTIVATE)
                except ImportError:
                    pass
        except:
            pass
            
    def follow_cursor(self):
        """Make pet follow cursor when idle"""
        if self.is_dragging or self.state != "idle":
            return
            
        cursor_x, cursor_y = self.get_cursor_position()
        pet_x = self.root.winfo_x() + 50
        pet_y = self.root.winfo_y() + 50
        
        # Calculate distance to cursor
        distance = math.sqrt((cursor_x - pet_x)**2 + (cursor_y - pet_y)**2)
        
        # Follow if cursor is close but not too close
        if 100 < distance < 300:
            self.target_x = cursor_x - 50
            self.target_y = cursor_y - 50
            self.state = "walking"
            
    def update_position(self):
        """Smoothly move pet towards target"""
        if self.state == "walking" and not self.is_dragging:
            current_pet_x = self.root.winfo_x()
            current_pet_y = self.root.winfo_y()
            
            # Move towards target
            dx = self.target_x - current_pet_x
            dy = self.target_y - current_pet_y
            distance = math.sqrt(dx**2 + dy**2)
            
            if distance > 5:
                # Move step by step
                step_size = min(2, distance / 10)
                new_x = current_pet_x + (dx / distance) * step_size
                new_y = current_pet_y + (dy / distance) * step_size
                
                # Keep on screen
                screen_width = self.root.winfo_screenwidth()
                screen_height = self.root.winfo_screenheight()
                new_x = max(0, min(new_x, screen_width - 100))
                new_y = max(0, min(new_y, screen_height - 100))
                
                self.root.geometry(f"100x100+{int(new_x)}+{int(new_y)}")
            else:
                self.state = "idle"
                
    def update_behavior(self):
        """Update pet behavior and state"""
        self.idle_counter += 1
        
        # Ensure we stay at desktop level every few cycles
        if self.idle_counter % 50 == 0:  # Every 5 seconds
            self.ensure_desktop_level()
        
        # Random behavior changes
        if self.idle_counter > 100:  # About 10 seconds
            behaviors = ["idle", "sleep", "play"]
            if self.state == "idle":
                # Occasionally do something random
                if random.random() < 0.3:
                    self.state = random.choice(["sleep", "play"])
            elif self.state in ["sleep", "play"]:
                # Return to idle after a while
                if random.random() < 0.1:
                    self.state = "idle"
            self.idle_counter = 0
            
        # Follow cursor behavior
        self.follow_cursor()
        
        # Update position
        self.update_position()
        
        # Schedule next behavior update
        self.root.after(100, self.update_behavior)
        
    def animate(self):
        """Animate the pet sprite"""
        # Get current animation sequence
        current_animation = self.animations.get(self.state, self.animations['idle'])
        
        # Update animation frame
        sprite_name = current_animation[self.animation_frame % len(current_animation)]
        sprite = self.pet_sprites[sprite_name]
        
        # Update pet display
        self.canvas.itemconfig(self.pet, text=sprite)
        
        # Advance animation frame
        self.animation_frame += 1
        
        # Schedule next frame (slower for sleep)
        delay = 800 if self.state == "sleep" else 500
        self.root.after(delay, self.animate)
        
    def run(self):
        """Start the pet application"""
        # Center pet on screen initially
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 100) // 2
        y = (screen_height - 100) // 2
        self.root.geometry(f"100x100+{x}+{y}")
        
        # Start the main loop
        self.root.mainloop()

if __name__ == "__main__":
    pet = DesktopPet()
    pet.run()