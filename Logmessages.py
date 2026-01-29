from datetime import datetime

log_file = "log.txt"

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print("Message logged.")

# Example usage
log_message("Program started")
log_message("An action occurred")
