import subprocess
import shutil

def open_system_monitor():
    # Check for btop
    if not shutil.which("btop"):
        return "btop is not installed. Run: sudo apt install btop"

    # Detect terminal emulator
    terminal = shutil.which("gnome-terminal") or shutil.which("x-terminal-emulator") or shutil.which("xterm")

    if not terminal:
        return "No terminal emulator found. Install gnome-terminal or xterm."

    try:
        # Open btop in new terminal
        subprocess.Popen([terminal, "--", "btop"])
        return "Launching system monitor..."
    except Exception as e:
        return f"Error launching monitor: {e}"
    