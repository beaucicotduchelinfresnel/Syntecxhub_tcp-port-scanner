# 🔐 TCP Port Scanner

> A fast and lightweight TCP port scanner built with Python to identify open, closed, and filtered ports on a target host.

**Project Status**: ✅ Complete | **Version**: 1.0 | **License**: Educational Use

This project was developed as part of a Cybersecurity Virtual Internship and focuses on network fundamentals, socket programming, and concurrency.

---

## 📋 Table of Contents

- [Features](#-features)
- [Technologies](#️-technologies--concepts)
- [Installation](#️-installation)
- [Usage](#️-usage)
- [Output Guide](#-output-guide)
- [Performance Tips](#-performance-tips)
- [Learning Outcomes](#-learning-outcomes)
- [Future Improvements](#-future-improvements)
- [Author](#-author)
- [Disclaimer](#️-disclaimer)
- [License](#-license)

---

## 🚀 Features

- ✅ Multi-threaded TCP port scanning for high performance
- ✅ Scan single host or custom port ranges
- ✅ Accurate detection of open, closed, and timeout/filtered ports
- ✅ Real-time console output with clear status indicators
- ✅ Persistent logging of results to `results.log`
- ✅ Configurable thread pool and timeout settings
- ✅ IPv4 and domain name support

## 🛠️ Technologies & Concepts

- **Python 3.6+**
- **TCP/IP Networking** - Socket-level port scanning
- **Socket Programming** - Direct socket connections
- **Multithreading** - Concurrent port scanning
- **Cybersecurity Fundamentals** - Network reconnaissance

## 📂 Project Structure

```
tcp-port-scanner/
│
├── port_scanner.py              # Main scanning application
├── results.log                  # Scan results and logs
├── README.md                    # Project documentation (this file)
├── .git/                        # Git version control
└── .gitignore                   # Git ignore configuration
```

### File Descriptions

| File | Purpose |
|------|---------|
| `port_scanner.py` | Main application - contains threading logic, socket operations, and CLI interface |
| `results.log` | Auto-generated log file storing all scan results with timestamps |
| `README.md` | Complete project documentation and usage guide |


## ⚙️ Installation

### Prerequisites

- **Python 3.6+** (Check with: `python --version`)
- **Git** (for cloning the repository)
- **Administrative access** (for scanning certain port ranges)

### Step-by-Step Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/beaucicotduchelinfresnel/Syntecxhub_tcp-port-scanner.git
cd Syntecxhub_tcp-port-scanner
```

#### 2. Verify Python Installation

```bash
python --version
# Output should be Python 3.6 or higher
```

#### 3. Run the Scanner

```bash
python port_scanner.py --help
```

✅ **No additional dependencies required** - Uses only Python standard library (socket, threading, argparse, datetime)


## ▶️ Usage

### Quick Start

```bash
# Scan default ports on a host
python port_scanner.py example.com
```

### Command Syntax

```bash
python port_scanner.py <host> [options]
```

### Arguments Reference

#### Required Arguments

| Argument | Type | Description | Example |
|----------|------|-------------|---------|
| `host` | string | Target host (IP or domain) | `192.168.1.1` or `google.com` |

#### Optional Arguments

| Flag | Full Name | Type | Default | Description |
|------|-----------|------|---------|-------------|
| `-s` | `--start` | int | 1 | Starting port number | `-s 20` |
| `-e` | `--end` | int | 1024 | Ending port number | `-e 8080` |
| `-t` | `--timeout` | float | 1.0 | Connection timeout (seconds) | `-t 2.0` |
| `-th` | `--threads` | int | 100 | Number of concurrent threads | `-th 200` |

### Usage Examples

#### Example 1: Basic Scan (Default)
```bash
python port_scanner.py localhost
```
Scans ports 1-1024 on localhost with default settings.

---

#### Example 2: Specific Port Range
```bash
python port_scanner.py 192.168.1.1 -s 1 -e 100
```
Scans ports 1-100 on the IP address.

---

#### Example 3: Web Ports with Custom Threads
```bash
python port_scanner.py example.com -s 80 -e 8080 -th 50
```
Scans common web ports (80-8080) with 50 threads.

---

#### Example 4: Full Port Scan with Increased Timeout
```bash
python port_scanner.py 10.0.0.1 -s 1 -e 65535 -t 2.0 -th 200
```
Performs a complete port scan (all 65535 ports) with 2-second timeout and 200 threads.

---

#### Example 5: Single Port Check
```bash
python port_scanner.py myserver.com -s 443 -e 443
```
Checks if port 443 is open on myserver.com.

---

### Example Output

```
============================================================
Scanning host: example.com
Port range: 1-1024
Threads: 100
Started at: 2026-01-19 14:30:45.123456
============================================================

[OPEN] Port 22
[OPEN] Port 80
[OPEN] Port 443
[CLOSED] Port 21
[CLOSED] Port 25
[TIMEOUT] Port 135
[ERROR] Port 445 -> Connection refused

Scan completed.
```

✅ **Results are automatically saved to `results.log` for later review**


## 📊 Output Guide

### Status Indicators

| Status | Symbol | Meaning | Interpretation |
|--------|--------|---------|-----------------|
| **OPEN** | ✅ | Port is accepting TCP connections | Service is likely running and accessible |
| **CLOSED** | ❌ | Port rejected the connection | Port is not listening or filtered |
| **TIMEOUT** | ⏱️ | Connection attempt timed out | Port may be filtered by firewall |
| **ERROR** | ⚠️ | Error occurred during attempt | Connection or permission issue |

### Understanding Log Files

The `results.log` file contains:
- **Timestamp** of each scan
- **Port status** for each attempted port
- **Host information** scanned
- **Total scan duration**

Example log entry:
```
Scan started: 2026-01-19 14:30:45.123456 | Host: example.com
[OPEN] Port 22
[OPEN] Port 80
Scan completed: 2026-01-19 14:30:52.654321
```


## 🎯 Performance Tips

### For Speed

| Scenario | Recommendation | Example |
|----------|-----------------|---------|
| **Large port range** | Increase thread count to 200-500 | `-th 300` for 1000+ ports |
| **Quick scan** | Scan common ports first (1-1024) | Default behavior |
| **Full network scan** | Use 500+ threads with higher timeout | `-th 500 -t 3.0` |

### For Accuracy

| Scenario | Recommendation | Example |
|----------|-----------------|---------|
| **Slow network** | Increase timeout to 2.0+ seconds | `-t 2.5` |
| **Distant hosts** | Use 3+ second timeout | `-t 3.0` |
| **Unreliable connection** | Lower thread count to 50-75 | `-th 50` |

### Balanced Configuration

```bash
# Good all-around settings
python port_scanner.py example.com -s 1 -e 1024 -th 150 -t 1.5
```

### Resource Considerations

- **CPU Usage**: Scales with thread count
- **Memory**: Minimal (< 50MB typically)
- **Network**: Increases with thread count and port range


## 📌 Learning Outcomes

Through this project, I developed expertise in:

### 🔧 Technical Skills

- **TCP/IP Networking** - Understanding protocol-level socket operations
- **Socket Programming** - Direct socket connections and error handling
- **Multithreading** - Concurrent thread management and synchronization
- **Python CLI** - Building command-line interfaces with argparse
- **Logging** - Persistent data recording and timestamps

### 🛡️ Security Fundamentals

- **Network Reconnaissance** - Gathering host information safely
- **Port Analysis** - Understanding port states and their meanings
- **Ethical Hacking** - Legal and responsible security testing
- **Risk Assessment** - Evaluating network vulnerabilities

### 💡 Software Engineering

- **Code Organization** - Clean, maintainable code structure
- **Error Handling** - Robust exception management
- **Performance Optimization** - Threading for I/O-bound operations
- **Documentation** - Clear code comments and user guides


## 🔄 Future Improvements

### Feature Roadmap

- [ ] **Service Detection** - Identify running services on open ports
- [ ] **Banner Grabbing** - Extract service version information
- [ ] **UDP Scanning** - Expand to UDP protocol scanning
- [ ] **Output Formats** - JSON/CSV export functionality
- [ ] **Stealth Modes** - Implement various scanning techniques
- [ ] **Vulnerability Integration** - CVE database lookups
- [ ] **GUI Interface** - Graphical user interface
- [ ] **Web Dashboard** - Real-time scanning visualization

### Known Limitations

- Currently TCP only (UDP planned)
- No service version detection
- Single host scans only (subnet scanning planned)


## 👤 Author

**Beaucicot Duchelin Fresnel**

- 🎓 Junior Cybersecurity Analyst & Web Developer
- 💼 Specializations: Cybersecurity, Network Security, Web Development
- 📍 Location: Remote
- 🔗 **LinkedIn**: [Beaucicot Duchelin Fresnel](https://www.linkedin.com/in/duchelin-fresnel-beaucicot-b6a599222/)

---

## ⚠️ Disclaimer

### ⚖️ Legal Notice

This tool is intended **for educational and ethical purposes only**.

**⚠️ IMPORTANT**: 
- Only scan systems and networks that **you own** or have **explicit written permission** to test
- Unauthorized port scanning may violate computer fraud and abuse laws in your jurisdiction
- The author assumes **no liability** for misuse of this tool
- Users are solely responsible for compliance with local laws and regulations

### Ethical Use Guidelines

✅ **DO**:
- Use on networks you own
- Obtain written permission before testing others' systems
- Document your findings securely
- Report vulnerabilities responsibly

❌ **DON'T**:
- Scan without permission
- Target government or critical infrastructure
- Use for malicious purposes
- Share findings publicly without authorization

---

## 📄 License

This project is provided **as-is** for educational purposes. No warranty is provided.

---

## 🤝 Contributing

Contributions, bug reports, and suggestions are welcome! Feel free to:
- Report issues
- Suggest improvements
- Submit pull requests
- Provide feedback

---

## 📞 Support

For questions or issues:
1. Check the **Usage** section above
2. Review **Example Output**
3. Verify your Python version and dependencies
4. Contact through LinkedIn

---

**Last Updated**: January 19, 2026  
**Version**: 1.0  
**Status**: ✅ Complete & Tested
