EVTX to JSON Converter

This Python tool converts **Windows Event Log (.evtx)** files into **readable JSON format**, enabling easy viewing, parsing, and forensic analysis across platforms (Linux, macOS, Windows).


Features

- Converts `.evtx` to clean JSON.
- Works on **Linux**, **macOS**, and **Windows**.
- Interactive: prompts for input path.
- Handles malformed records gracefully.
- Useful for forensic analysis, reverse engineering, and log correlation.

Requirements

- Python 3.x
- Modules:
  - `python-evtx`
  - `xmltodict`

Forensics & Reverse Engineering Use
You can use this output with tools like:

SIEM (Splunk, Graylog)

MITRE ATT&CK mapping

Custom alerting and enrichment

Timeline creation (e.g., Plaso)

<code><pre>
python -m venv foldername #to create venv 
source foldername/bin/activate # to activate the venv
pip install python-evtx xmltodict
<code></pre>

<code><pre>
git clone https://github.com/moon0deva/3v7-converter.git
cd 3v7-converter
python json.py
<code></pre>
