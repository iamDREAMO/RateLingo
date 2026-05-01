"""
RateLingo - Twi Language Service Pricing Calculator
Entry point for the application
"""

import sys
from cli import main as cli_main

if __name__ == "__main__":
    # Check if GUI mode is requested (for future GUI implementation)
    if len(sys.argv) > 1 and sys.argv[1] == "--gui":
        print("GUI mode coming soon!")
        print("For now, running CLI mode...\n")
    
    # Run CLI application
    cli_main()