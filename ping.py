import subprocess
  
out = subprocess.run(['ping', '8.8.8.8'], capture_output=True)
print(out.stdout.decode())