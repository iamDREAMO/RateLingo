"""
RateLingo - Twi Language Service Pricing Calculator
Entry point for the application

Usage:
    python main.py          # Launches GUI (default)
    python main.py --cli    # Launches CLI
"""

import sys

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        # Run CLI
        from src.cli import main as cli_main
        cli_main()
    else:
        # Run GUI (default)
        from tkinter import Tk
        from src.gui import RateLingoGUI
        root = Tk()
        RateLingoGUI(root)
        root.mainloop()

if __name__ == "__main__":
    main()