#A log checker is one of the most common automation scripts in DevOps and system administration. Instead of reading thousands of log lines manually, a script checks for important keywords and alerts you.

logs="INFO: Server started successfully INFO: Database connected WARNING: High memory usage ERROR: Database connection lost"
if "ERROR" and "WARNING" in logs:
    print("WARNING and ERROR both detected")
elif "ERROR" in logs:    
    print("ERROR Detected !!")
elif "WARNING" in logs:
    print("WARNING Detected !!")
else:
    print("Logs are Clean.")       