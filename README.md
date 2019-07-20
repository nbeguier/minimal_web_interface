# Minimal interface

[![Build Status](https://travis-ci.org/nbeguier/minimal_web_interface.svg?branch=master)](https://travis-ci.org/nbeguier/minimal_web_interface) [![Python 3.5|3.7](https://img.shields.io/badge/python-3.5|3.7-green.svg)](https://www.python.org/)

## Prerequisites

```bash
pip3 install -r requirements.txt
```

## Usage

```bash
# Debug mode
python3 server.py

# gunicorn mode
gunicorn server:APP -b 127.0.0.1:8080 --access-logfile /var/log/minimal_web_interface.log --error-logfile /var/log/minimal_web_interface-error.log
```
