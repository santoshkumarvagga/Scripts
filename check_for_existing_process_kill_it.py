    for proc in psutil.process_iter():
        # Check if process name contains the given name string.
        if "account pro" in proc.name().lower():
            proc.kill()
