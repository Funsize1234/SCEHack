#!/usr/bin/env python3
"""
SCE Question App Runner
This script sets up and runs the SCE Question application.
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("Error: Python 3.7 or higher is required")
        sys.exit(1)
    print(f"✓ Python {sys.version.split()[0]} detected")

def check_virtual_environment():
    """Check if virtual environment exists and activate it"""
    venv_path = os.path.join(os.path.dirname(__file__), 'venv')
    
    if os.path.exists(venv_path):
        print("✓ Virtual environment found")
        return True
    else:
        print("Creating virtual environment...")
        try:
            subprocess.run([sys.executable, '-m', 'venv', 'venv'], check=True)
            print("✓ Virtual environment created")
            return True
        except subprocess.CalledProcessError:
            print("Error: Failed to create virtual environment")
            return False

def install_dependencies():
    """Install required dependencies"""
    print("Installing dependencies...")
    
    # Get the appropriate pip executable
    if platform.system() == "Windows":
        pip_executable = os.path.join('venv', 'Scripts', 'pip')
    else:
        pip_executable = os.path.join('venv', 'bin', 'pip')
    
    try:
        subprocess.run([pip_executable, 'install', '-r', 'requirements.txt'], check=True)
        print("✓ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("Error: Failed to install dependencies")
        return False

def run_application():
    """Run the GUI application"""
    print("Starting SCE Question App...")
    
    # Get the appropriate python executable
    if platform.system() == "Windows":
        python_executable = os.path.join('venv', 'Scripts', 'python')
    else:
        python_executable = os.path.join('venv', 'bin', 'python')
    
    try:
        subprocess.run([python_executable, os.path.join('src', 'gui_app.py')], check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to run the application")
        return False
    except KeyboardInterrupt:
        print("\nApplication stopped by user")
        return True
    
    return True

def main():
    """Main setup and run function"""
    print("=" * 50)
    print("SCE Question App Setup & Runner")
    print("=" * 50)
    
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Check Python version
    check_python_version()
    
    # Setup virtual environment
    if not check_virtual_environment():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("Setup complete! Starting application...")
    print("=" * 50)
    
    # Run the application
    run_application()

if __name__ == "__main__":
    main()
