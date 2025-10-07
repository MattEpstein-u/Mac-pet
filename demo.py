#!/usr/bin/env python3
"""
Demo script to show what the desktop pet looks like
"""

import time
import random

def demo_pet_animation():
    """Show a simple text-based demo of the pet animations"""
    
    print("=== Desktop Pet Animation Demo ===")
    print()
    print("Here's what your desktop pet will look like:")
    print()
    
    # Pet sprites
    sprites = {
        'idle1': '🐱',
        'idle2': '😺', 
        'walk1': '🐾',
        'walk2': '🐱',
        'sleep': '😴',
        'play': '😸'
    }
    
    # Animation sequences
    animations = {
        'idle': ['idle1', 'idle2', 'idle1', 'idle1'],
        'walk': ['walk1', 'walk2', 'walk1', 'walk2'],
        'sleep': ['sleep', 'sleep', 'sleep', 'sleep'],
        'play': ['play', 'idle1', 'play', 'idle2']
    }
    
    states = ['idle', 'walk', 'play', 'sleep']
    
    for state in states:
        print(f"--- {state.upper()} animation ---")
        animation = animations[state]
        
        for i in range(8):  # Show 2 full cycles
            sprite_name = animation[i % len(animation)]
            sprite = sprites[sprite_name]
            
            # Clear previous line and show new sprite
            print(f"\r{sprite} {state}...", end="", flush=True)
            time.sleep(0.5 if state != 'sleep' else 0.8)
        
        print()  # New line after each animation
        time.sleep(0.5)
    
    print()
    print("🎮 Interactive Features:")
    print("• Click and drag to move the pet around")
    print("• Double-click to trigger play animation")
    print("• Pet follows your cursor when you're nearby")
    print("• Automatically changes between idle, sleep, and play")
    print("• Only visible when desktop is showing (no apps on top)")
    print()
    print("Ready to install your desktop companion!")

if __name__ == "__main__":
    demo_pet_animation()