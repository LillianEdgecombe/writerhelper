#!/bin/bash
echo "Installing Character Developer Tool..."
python3 -m pip install -r requirements.txt
chmod +x main.py
echo "Installation complete."
echo "To run the tool in CLI mode: python3 main.py"
echo "To run the tool in Web mode: python3 main.py --web"
