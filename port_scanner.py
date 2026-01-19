import socket
import threading
import argparse
from datetime import datetime


print_lock = threading.Lock()


LOG_FILE = "results.log"

def log_result(message):
    with open(LOG_FILE, "a") as file:
        file.write(message + "\n")

def scan_port(host, port, timeout):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        result = sock.connect_ex((host, port))
        sock.close()

        with print_lock:
            if result == 0:
                msg = f"[OPEN] Port {port}"
            else:
                msg = f"[CLOSED] Port {port}"

            print(msg)
            log_result(msg)

    except socket.timeout:
        with print_lock:
            msg = f"[TIMEOUT] Port {port}"
            print(msg)
            log_result(msg)

    except Exception as e:
        with print_lock:
            msg = f"[ERROR] Port {port} -> {e}"
            print(msg)
            log_result(msg)

def main():
    parser = argparse.ArgumentParser(description="TCP Port Scanner")
    parser.add_argument("host", help="Target host (IP or domain)")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port")
    parser.add_argument("-e", "--end", type=int, default=1024, help="End port")
    parser.add_argument("-t", "--timeout", type=float, default=1.0, help="Timeout in seconds")
    parser.add_argument("-th", "--threads", type=int, default=100, help="Number of threads")

    args = parser.parse_args()

    host = args.host
    start_port = args.start
    end_port = args.end
    timeout = args.timeout
    max_threads = args.threads

    print("\n" + "=" * 60)
    print(f"Scanning host: {host}")
    print(f"Port range: {start_port}-{end_port}")
    print(f"Threads: {max_threads}")
    print(f"Started at: {datetime.now()}")
    print("=" * 60 + "\n")

    log_result(f"\nScan started: {datetime.now()} | Host: {host}")

    threads = []

    for port in range(start_port, end_port + 1):
        while threading.active_count() > max_threads:
            pass

        thread = threading.Thread(
            target=scan_port,
            args=(host, port, timeout)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\nScan completed.")
    log_result(f"Scan completed: {datetime.now()}\n")

if __name__ == "__main__":
    main()
