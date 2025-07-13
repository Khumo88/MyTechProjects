# 🗒️ LOG FLE CHECKER SCRIPT

def check_log_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    
        print("\n🚨 Log Alerts Fond:")
        for i, line in enumerate(lines):
            if "error" in line.lower() or "warning" in line.lower():
                print(f"Line {i + 1}: {line.strip()}")
    
    except FileNotFoundError:
        print(f"❌ Log file not found.")
    except Exception as e:
        print(f"❌ Somethng went wrong: {e}")

def main():
    print("🗒️ Log File Checker\n")
    file_path = input("Enter the path to the log file: ")
    check_log_file(file_path)

if __name__ == "__main__":
    main()