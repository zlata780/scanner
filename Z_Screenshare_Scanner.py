name: Build Z・Screenshare Scanner

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: windows-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: pip install pyinstaller psutil requests

    - name: Build executable
      run: pyinstaller --noconsole --onefile Z_Screenshare_Scanner.py

    - name: Upload executable artifact
      uses: actions/upload-artifact@v3
      with:
        name: Z_Screenshare_Scanner
        path: dist/Z_Screenshare_Scanner.exe
