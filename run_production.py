#!/usr/bin/env python3
"""
Production runner for the Flask app without debug mode
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Read and execute the main Flask app file
with open('flask-game-app.py', 'r') as f:
    code = f.read()

# Replace debug=True with debug=False
code = code.replace('app.run(debug=True, host=\'0.0.0.0\', port=5010)', 'app.run(debug=False, host=\'0.0.0.0\', port=5010)')

# Execute the modified code
exec(code)
