#!/usr/bin/env python3
import sys
import argparse
from char_dev import CharacterDeveloperCLI
from app import app

def main():
    parser = argparse.ArgumentParser(description="Character Developer Tool")
    parser.add_argument('--web', action='store_true', help="Start the web application")
    parser.add_argument('--port', type=int, default=5000, help="Port for the web application (default: 5000)")
    parser.add_argument('--cli', action='store_true', help="Start the CLI tool (default if no arguments)")

    args = parser.parse_args()

    if args.web:
        print(f"Starting web application on port {args.port}...")
        app.run(host='0.0.0.0', port=args.port, debug=True)
    else:
        # Default to CLI if --web is not specified
        dev = CharacterDeveloperCLI()
        dev.run()

if __name__ == "__main__":
    main()
