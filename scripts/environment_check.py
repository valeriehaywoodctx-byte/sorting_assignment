import os
import sys

def check_env():
    print("--- 🔬 Week 2 Laboratory Check ---")
    
    # List of everything your instructions require
    required_folders = ['src', 'benchmarks', 'tests', 'scripts', 'analysis']
    
    all_passed = True
    for folder in required_folders:
        if os.path.exists(folder):
            print(f"✅ Folder '{folder}' found.")
        else:
            print(f"❌ MISSING: '{folder}' folder.")
            all_passed = False

    if all_passed:
        print("\n🚀 All folders present! You are ready for Week 2.")
    else:
        print("\n⚠️  Action Required: Create the missing folders listed above.")

if __name__ == "__main__":
    check_env()