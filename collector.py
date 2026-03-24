import paramiko

def get_server_stats(ip, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password, timeout=5)

        def run(cmd):
            _, stdout, _ = ssh.exec_command(cmd)
            return stdout.read().decode().strip()

        cpu      = run("top -bn1 | grep 'Cpu(s)' | awk '{print $2}'")
        ram      = run("free | grep Mem | awk '{printf \"%.1f\", $3/$2*100}'")
        disk     = run("df / | tail -1 | awk '{print $5}' | tr -d '%'")
        uptime   = run("uptime -p")
        hostname = run("hostname")

        ssh.close()

        return {
            "ip":       ip,
            "hostname": hostname,
            "cpu":      float(cpu)  if cpu  else 0,
            "ram":      float(ram)  if ram  else 0,
            "disk":     float(disk) if disk else 0,
            "uptime":   uptime,
            "status":   "online"
        }

    except Exception as e:
        return {
            "ip":       ip,
            "hostname": ip,
            "cpu":      0,
            "ram":      0,
            "disk":     0,
            "uptime":   "N/A",
            "status":   "offline",
            "error":    str(e)
        }