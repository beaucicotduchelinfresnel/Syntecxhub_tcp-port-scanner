🔐 TCP Port Scanner (Python)

A fast and lightweight TCP port scanner built with Python to identify open, closed, and filtered ports on a target host.
This project was developed as part of a Cybersecurity Virtual Internship and focuses on network fundamentals, socket programming, and concurrency.

🚀 Features

Scan a single host for open TCP ports

Support for custom port ranges

Multithreaded scanning for faster execution

Accurate detection of:

Open ports

Closed ports

Timeouts / filtered ports

Console output with clear status indicators

Optional logging of results for later analysis

🛠️ Technologies & Concepts

Python 3

TCP/IP Networking

Socket Programming

Multithreading

Cybersecurity Fundamentals

📂 Project Structure
tcp-port-scanner/
│
├── scanner.py          # Main scanning logic
├── utils.py            # Helper functions (if applicable)
├── logs/               # Scan results (optional)
├── requirements.txt    # Dependencies (if any)
└── README.md


(Adjust structure based on your actual files — do not lie.)

⚙️ Installation
git clone https://github.com/beaucicotduchelin/tcp-port-scanner.git
cd tcp-port-scanner
python scanner.py


Make sure Python 3.x is installed on your system.

▶️ Usage

Scan a target host on a specific port range:

python scanner.py --host 192.168.1.1 --ports 1-1024


Example output:

[OPEN]    Port 22
[CLOSED]  Port 80
[TIMEOUT] Port 443

📌 Learning Outcomes

Through this project, I gained hands-on experience in:

Understanding how TCP connections work at a low level

Building real-world tools using Python sockets

Improving performance using thread-based concurrency

Writing clean, readable, and maintainable security scripts

📈 Future Improvements

Service and banner detection

Output export to JSON / CSV

Stealth scan modes

Basic vulnerability mapping

👤 Author

Duchelin Fresnel Beaucicot
Junior Cybersecurity Analyst & Web Developer | Cybersecurity & Web 
📍 Remote
🔗 LinkedIn: https://www.linkedin.com/in/duchelin-fresnel-beaucicot-b6a599222/

⚠️ Disclaimer

This tool is intended for educational and ethical purposes only.
Only scan systems you own or have explicit permission to test.
