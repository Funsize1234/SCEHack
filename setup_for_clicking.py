#!/usr/bin/env python3
"""
One-time setup script for SCE Question App
Run this once to set up everything needed for double-clicking the app.
"""

import os
import sys
import subprocess
import platform

def main():
    print("=" * 60)
    print("SCE Question App - One-Time Setup")
    print("=" * 60)
    print("This will set up everything needed to double-click the app!")
    print()
    
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required")
        print(f"   You have: Python {sys.version.split()[0]}")
        sys.exit(1)
    
    print(f"✅ Python {sys.version.split()[0]} detected")
    
    # Create virtual environment
    venv_path = 'venv'
    if os.path.exists(venv_path):
        print("✅ Virtual environment already exists")
    else:
        print("🔧 Creating virtual environment...")
        try:
            subprocess.run([sys.executable, '-m', 'venv', 'venv'], check=True)
            print("✅ Virtual environment created")
        except subprocess.CalledProcessError:
            print("❌ Failed to create virtual environment")
            sys.exit(1)
    
    # Install dependencies
    print("🔧 Installing dependencies...")
    
    # Get the appropriate pip executable
    if platform.system() == "Windows":
        pip_executable = os.path.join('venv', 'Scripts', 'pip')
    else:
        pip_executable = os.path.join('venv', 'bin', 'pip')
    
    try:
        subprocess.run([pip_executable, 'install', '-r', 'requirements.txt'], 
                      check=True, capture_output=True, text=True)
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError as e:
        print("❌ Failed to install dependencies")
        print(f"   Error: {e.stderr}")
        sys.exit(1)
    
    # Test that everything works
    print("🧪 Testing installation...")
    
    # Get the appropriate python executable
    if platform.system() == "Windows":
        python_executable = os.path.join('venv', 'Scripts', 'python')
    else:
        python_executable = os.path.join('venv', 'bin', 'python')
    
    try:
        result = subprocess.run([python_executable, '-c', 'import numpy, pyopencl; print("All imports successful!")'], 
                               capture_output=True, text=True, check=True)
        print("✅ All dependencies working correctly")
    except subprocess.CalledProcessError as e:
        print("⚠️  Dependencies installed but there might be issues:")
        print(f"   {e.stderr}")
        print("   The app might still work - try double-clicking it!")
    
    print()
    print("=" * 60)
    print("🎉 Setup Complete!")
    print("=" * 60)
    
    if platform.system() == "Darwin":  # macOS
        print("You can now double-click 'SCE Question.app' to run the app!")
    elif platform.system() == "Windows":
        print("You can now double-click 'run.bat' to run the app!")
    else:
        print("You can now run './run.sh' to start the app!")
    
    print()
    print("If you encounter any issues, check the 'app_launch.log' file for details.")

if __name__ == "__main__":
    main()
