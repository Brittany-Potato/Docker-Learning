import sys
import os
import platform

def run_test():
    print("---------------------------")
    print(" Test Script Running ")
    print("---------------------------")
    
    print(f"1. Python Version: {sys.version.split()[0]}")
    print(f"2. Operating System: {platform.system()} {platform.release()}")
    print(f"3. Current Directory: {os.getcwd()}")
    
    print("\nScript finished successfully.")
    
if __name__ == "__main__":
    run_test()