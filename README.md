# SCE Question App

A fun interactive application that asks "Do you like SCE?" and responds accordingly. If you answer "No", it will run a GPU stress test to show you what happens when you don't appreciate SCE! 😄

## Features

- Clean, modern GUI built with tkinter
- Interactive question with Yes/No buttons
- GPU stress test using OpenCL for the "wrong" answer
- Cross-platform compatibility (Windows, macOS, Linux)

## Requirements

- Python 3.7 or higher
- OpenCL-compatible GPU (for the stress test)
- Virtual environment support

## Quick Start

### Option 1: Double-Click to Run (macOS)

**Simply double-click `SCE Question.app` in Finder!** 

The app will automatically:
- Set up the virtual environment
- Install dependencies
- Launch the GUI

### Option 2: Command Line (All Platforms)

**On macOS/Linux:**
```bash
./run.sh
```

**On Windows:**
```bash
run.bat
```

**Any platform:**
```bash
python run.py
```

### Option 3: Manual Setup

1. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python gui_app.py
   ```

## How It Works

1. The application opens with a simple question: "Do you like SCE?"
2. **If you click "Yes":** The app displays "Good" and closes gracefully
3. **If you click "No":** The app displays "Wrong Answer." and launches a GPU stress test that will make your computer work hard!

## Files Structure

- `gui_app.py` - Main GUI application
- `main.py` - GPU stress test using OpenCL
- `SCE Question.app/` - macOS application bundle (double-click to run!)
- `run.py` - Cross-platform setup and runner script
- `run.sh` - Unix shell script for easy execution
- `run.bat` - Windows batch file for easy execution
- `requirements.txt` - Python dependencies
- `venv/` - Virtual environment (created automatically)

## Dependencies

- `numpy` - For numerical operations in the stress test
- `pyopencl` - For GPU computing and stress testing
- `tkinter` - For the GUI (included with Python)

## Troubleshooting

**OpenCL Issues:**
- Make sure you have OpenCL drivers installed for your GPU
- On macOS, OpenCL is included by default
- On Linux, install `opencl-headers` and appropriate GPU drivers
- On Windows, install GPU manufacturer's drivers

**Virtual Environment Issues:**
- Make sure Python 3.7+ is installed
- Try running `python -m pip install --upgrade pip` before installing dependencies

**Permission Issues on macOS/Linux:**
- Make sure the run script is executable: `chmod +x run.sh`

## Warning

The GPU stress test in `main.py` will run indefinitely and use significant system resources. Use Ctrl+C to stop it if needed. Don't run this on battery power or systems with cooling issues!