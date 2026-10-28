# Security Log Analyzer

## Overview
A beginner-friendly Python cybersecurity project that analyzes fictional login logs and identifies IP addresses with repeated failed login attempts.

## Objectives
- Count total login events.
- Count successful and failed login attempts.
- Identify IP addresses that reach a configurable failed-login threshold.
- Practise basic defensive security monitoring and log analysis.

## Technologies
- Python 3
- Python standard library (`collections`, `unittest`)
- Visual Studio Code

## How It Works
The program reads `sample_logs.txt`, examines each event, counts successful and failed logins, and flags IP addresses with three or more failed attempts.

## How to Run
```bash
python log_analyzer.py
```

## How to Run Tests
```bash
python -m unittest discover -s tests -v
```

## Sample Results
The supplied sample data contains six login events, two successful logins, and four failed logins. The tool should flag `192.168.1.25` because it has three failed login attempts.

## Limitations
This is an educational prototype that processes a simplified log format. Repeated failures may have legitimate causes and do not prove malicious activity. The tool does not automatically block IP addresses or investigate real systems.

## Future Improvements
- Export results to a report file.
- Validate malformed log entries.
- Add timestamps and user-based summaries.
- Add tests for the actual analysis function.

## Safety
The project uses fictional sample data and is intended for defensive cybersecurity learning.
