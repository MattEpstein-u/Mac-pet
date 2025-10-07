#!/usr/bin/env python3
"""
Interactive Desktop Pet Test - Play with the pet in a regular window!
This allows you to test all pet behaviors without desktop-level positioning.
"""

import tkinter as tk
from tkinter import PhotoImage
import random
import math
import platform
import sys

class TestDesktopPet:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_test_window()
        self.setup_pet()
        self.setup_animations()
        
        # Pet state
        self.container_width = 600
        self.container_height = 400
        self.target_x = self.container_width // 2
        self.target_y = self.container_height // 2
        self.current_x = self.container_width // 2
        self.current_y = self.container_height // 2
        self.is_dragging = False
        self.drag_start_x = 0
        self.drag_start_y = 0
        self.animation_frame = 0
        self.idle_counter = 0
        self.state = "idle"  # idle, walking, sleeping, playing
        
        # Test mode variables
        self.mouse_in_window = False
        self.last_cursor_x = 0
        self.last_cursor_y = 0
        
        # Start the main loops
        self.animate()
        self.update_behavior()
        
    def setup_test_window(self):
        """Configure the test window"""
        self.root.title("Desktop Pet Test - Interactive Mode")
        self.root.geometry("600x450+100+100")  # Slightly taller for controls
        self.root.configure(bg='#f0f0f0')
        
        # Add control panel at top
        control_frame = tk.Frame(self.root, bg='#e0e0e0', height=50)
        control_frame.pack(fill='x', padx=5, pady=5)
        control_frame.pack_propagate(False)
        
        # Control buttons
        tk.Label(control_frame, text="🎮 Pet Controls:", bg='#e0e0e0', 
                font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        
        tk.Button(control_frame, text="😸 Play", command=self.trigger_play,
                 bg='#ffeb3b', font=('Arial', 9)).pack(side='left', padx=2)
        
        tk.Button(control_frame, text="😴 Sleep", command=self.trigger_sleep,
                 bg='#e1f5fe', font=('Arial', 9)).pack(side='left', padx=2)
        
        tk.Button(control_frame, text="🐾 Walk", command=self.trigger_walk,
                 bg='#c8e6c9', font=('Arial', 9)).pack(side='left', padx=2)
        
        tk.Button(control_frame, text="🎯 Random Spot", command=self.random_target,
                 bg='#f8bbd9', font=('Arial', 9)).pack(side='left', padx=2)
        
        # Status label
        self.status_label = tk.Label(control_frame, text="State: idle", 
                                   bg='#e0e0e0', font=('Arial', 9))
        self.status_label.pack(side='right', padx=5)
        
    def setup_pet(self):
        """Create the pet display"""
        # Create canvas for the pet area
        self.canvas = tk.Canvas(self.root, width=self.container_width, 
                               height=self.container_height, 
                               bg='#f8f8f8', highlightthickness=1,
                               highlightcolor='#d0d0d0')
        self.canvas.pack(padx=5, pady=5)
        
        # Add container background with rounded corners effect
        self.canvas.create_rectangle(5, 5, self.container_width-5, 
                                   self.container_height-5,
                                   fill='#fcfcfc', outline='#e0e0e0', width=2)
        
        # Add corner decorations
        self.canvas.create_text(self.container_width-15, 15, text='🏠', 
                              font=('Arial', 12), anchor='ne', fill='#c0c0c0')
        
        self.canvas.create_text(15, self.container_height-15, 
                              text=f'{self.container_width}x{self.container_height}',
                              font=('Arial', 8), anchor='sw', fill='#999')
        
        # Create simple pet sprite
        self.pet_sprites = {
            'idle1': '🐱',
            'idle2': '😺', 
            'walk1': '🐾',
            'walk2': '🐱',
            'sleep': '😴',
            'play': '😸'
        }
        
        # Create the pet on canvas (start in center)
        pet_size = 32
        self.pet_start_x = self.container_width // 2
        self.pet_start_y = self.container_height // 2
        
        self.pet = self.canvas.create_text(self.pet_start_x, self.pet_start_y, 
                                         text=self.pet_sprites['idle1'], 
                                         font=('Arial', pet_size), anchor='center')
        
        # Store pet bounds for collision detection
        self.pet_size = pet_size
        self.pet_radius = pet_size // 2
        
        # Bind mouse events
        self.canvas.bind('<Button-1>', self.start_drag)
        self.canvas.bind('<B1-Motion>', self.drag_pet)
        self.canvas.bind('<ButtonRelease-1>', self.end_drag)
        self.canvas.bind('<Double-Button-1>', self.pet_interaction)
        
        # Track mouse movement for following behavior
        self.canvas.bind('<Motion>', self.track_mouse)
        self.canvas.bind('<Enter>', self.mouse_enter)
        self.canvas.bind('<Leave>', self.mouse_leave)
        
        # Add instructions
        instructions = """
🎮 How to interact:
• Click and drag the pet around
• Double-click the pet to make it play
• Move mouse near pet to make it follow
• Use buttons above for direct control
• Pet will wander randomly when idle
        """
        
        instruction_label = tk.Label(self.root, text=instructions, 
                                   justify='left', bg='#f0f0f0', 
                                   font=('Arial', 9), fg='#666')
        instruction_label.pack(pady=5)
        
    def setup_animations(self):
        """Setup animation sequences"""
        self.animations = {
            'idle': ['idle1', 'idle2', 'idle1', 'idle1'],
            'walking': ['walk1', 'walk2', 'walk1', 'walk2'],
            'sleep': ['sleep', 'sleep', 'sleep', 'sleep'],
            'play': ['play', 'idle1', 'play', 'idle2']
        }
        
    def track_mouse(self, event):
        """Track mouse movement for following behavior"""
        self.mouse_in_window = True
        self.last_cursor_x = event.x
        self.last_cursor_y = event.y
        
    def mouse_enter(self, event):
        """Mouse entered the canvas"""
        self.mouse_in_window = True
        
    def mouse_leave(self, event):
        """Mouse left the canvas"""
        self.mouse_in_window = False
        
    def start_drag(self, event):
        """Start dragging the pet"""
        pet_coords = self.canvas.coords(self.pet)
        if pet_coords:
            pet_x, pet_y = pet_coords[0], pet_coords[1]
            distance = ((event.x - pet_x)**2 + (event.y - pet_y)**2)**0.5
            
            if distance <= self.pet_radius + 10:
                self.is_dragging = True
                self.drag_start_x = event.x
                self.drag_start_y = event.y
                self.state = "idle"  # Stop other behaviors while dragging
                
    def drag_pet(self, event):
        """Handle pet dragging"""
        if self.is_dragging:
            dx = event.x - self.drag_start_x
            dy = event.y - self.drag_start_y
            
            pet_coords = self.canvas.coords(self.pet)
            if pet_coords:
                new_x = pet_coords[0] + dx
                new_y = pet_coords[1] + dy
                
                # Keep pet within container bounds
                margin = self.pet_radius + 5
                new_x = max(margin, min(new_x, self.container_width - margin))
                new_y = max(margin, min(new_y, self.container_height - margin))
                
                # Move the pet
                self.canvas.coords(self.pet, new_x, new_y)
                
                # Update drag start position for smooth dragging
                self.drag_start_x = event.x
                self.drag_start_y = event.y
                
    def end_drag(self, event):
        """End dragging"""
        self.is_dragging = False
        
    def pet_interaction(self, event):
        """Handle double-click interaction"""
        pet_coords = self.canvas.coords(self.pet)
        if pet_coords:
            pet_x, pet_y = pet_coords[0], pet_coords[1]
            distance = ((event.x - pet_x)**2 + (event.y - pet_y)**2)**0.5
            
            if distance <= self.pet_radius + 15:
                self.trigger_play()
                
    def trigger_play(self):
        """Trigger play state"""
        self.state = "play"
        self.idle_counter = 0
        
    def trigger_sleep(self):
        """Trigger sleep state"""
        self.state = "sleep"
        self.idle_counter = 0
        
    def trigger_walk(self):
        """Trigger walking to cursor or random spot"""
        if self.mouse_in_window:
            self.set_target(self.last_cursor_x, self.last_cursor_y)
        else:
            self.random_target()
            
    def random_target(self):
        """Set random target within container"""
        margin = self.pet_radius + 20
        self.target_x = random.randint(margin, self.container_width - margin)
        self.target_y = random.randint(margin, self.container_height - margin)
        self.state = "walking"
        
    def set_target(self, x, y):
        """Set specific target coordinates"""
        margin = self.pet_radius + 10
        self.target_x = max(margin, min(x, self.container_width - margin))
        self.target_y = max(margin, min(y, self.container_height - margin))
        self.state = "walking"
        
    def follow_cursor(self):
        """Make pet follow cursor when idle"""
        if (self.is_dragging or self.state not in ["idle", "walking"] or 
            not self.mouse_in_window):
            return
            
        pet_coords = self.canvas.coords(self.pet)
        if pet_coords:
            pet_x, pet_y = pet_coords[0], pet_coords[1]
            cursor_x, cursor_y = self.last_cursor_x, self.last_cursor_y
            
            # Calculate distance to cursor
            distance = math.sqrt((cursor_x - pet_x)**2 + (cursor_y - pet_y)**2)
            
            # Follow if cursor is close but not too close
            if 30 < distance < 100:
                self.set_target(cursor_x, cursor_y)
                
    def update_position(self):
        """Smoothly move pet towards target"""
        if self.state == "walking" and not self.is_dragging:
            pet_coords = self.canvas.coords(self.pet)
            if pet_coords:
                current_pet_x, current_pet_y = pet_coords[0], pet_coords[1]
                
                # Move towards target
                dx = self.target_x - current_pet_x
                dy = self.target_y - current_pet_y
                distance = math.sqrt(dx**2 + dy**2)
                
                if distance > 3:
                    # Move step by step
                    step_size = min(2, distance / 6)
                    new_x = current_pet_x + (dx / distance) * step_size
                    new_y = current_pet_y + (dy / distance) * step_size
                    
                    # Keep within container bounds
                    margin = self.pet_radius + 5
                    new_x = max(margin, min(new_x, self.container_width - margin))
                    new_y = max(margin, min(new_y, self.container_height - margin))
                    
                    # Move the pet
                    self.canvas.coords(self.pet, new_x, new_y)
                else:
                    self.state = "idle"
                    
    def wander_randomly(self):
        """Make pet wander to a random spot in the container"""
        if not self.is_dragging:
            self.random_target()
            
    def update_behavior(self):
        """Update pet behavior and state"""
        self.idle_counter += 1
        
        # Update status
        self.status_label.config(text=f"State: {self.state}")
        
        # Random behavior changes
        if self.idle_counter > 80:  # About 8 seconds in test mode
            if self.state == "idle":
                rand = random.random()
                if rand < 0.15:
                    self.state = random.choice(["sleep", "play"])
                elif rand < 0.3:  # Random wandering
                    self.wander_randomly()
            elif self.state in ["sleep", "play"]:
                # Return to idle after a while
                if random.random() < 0.2:
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
        
        # Add a subtle bounce effect when walking
        if self.state == "walking" and self.animation_frame % 4 < 2:
            pet_coords = self.canvas.coords(self.pet)
            if pet_coords and len(pet_coords) >= 2:
                bounce_offset = 1 if self.animation_frame % 4 == 0 else -1
                self.canvas.coords(self.pet, pet_coords[0], pet_coords[1] + bounce_offset)
        
        # Advance animation frame
        self.animation_frame += 1
        
        # Schedule next frame (slower for sleep)
        delay = 1000 if self.state == "sleep" else 400
        self.root.after(delay, self.animate)
        
    def run(self):
        """Start the test application"""
        print("🎮 Desktop Pet Test Mode")
        print("• Window will open with interactive pet")
        print("• Try all the controls and interactions")
        print("• Close window when done testing")
        print()
        
        # Center window on screen
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
        # Start the main loop
        self.root.mainloop()

if __name__ == "__main__":
    try:
        pet = TestDesktopPet()
        pet.run()
    except Exception as e:
        print(f"Error running test: {e}")
        print("Make sure you have a display available (not in headless mode)")
        sys.exit(1)