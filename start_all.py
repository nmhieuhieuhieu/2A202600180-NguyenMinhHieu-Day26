import subprocess
import time
import sys
import atexit
import os

processes = []

def cleanup():
    print("Stopping all services...")
    for p in processes:
        p.terminate()
        p.wait()

atexit.register(cleanup)

def start_module(module_name):
    print(f"Starting {module_name}...")
    # use uv run to ensure the right environment is used
    p = subprocess.Popen(["uv", "run", "python", "-m", module_name])
    processes.append(p)
    return p

def main():
    print("Starting Registry service on port 10000...")
    start_module("registry")
    time.sleep(2)
    
    print("Starting Tax Agent on port 10102...")
    start_module("tax_agent")
    
    print("Starting Compliance Agent on port 10103...")
    start_module("compliance_agent")
    time.sleep(3)
    
    print("Starting Law Agent on port 10101...")
    start_module("law_agent")
    time.sleep(3)
    
    print("Starting Customer Agent on port 10100...")
    start_module("customer_agent")
    
    print("\nAll services started. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
