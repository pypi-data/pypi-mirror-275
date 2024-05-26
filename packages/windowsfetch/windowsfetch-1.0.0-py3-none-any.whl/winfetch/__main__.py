import psutil, platform, subprocess, winreg
from datetime import timedelta

def main():
    def get_packages():
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall") as key:
                count = 0
                for i in range(1024):
                    try:
                        subkey_name = winreg.EnumKey(key, i)
                        count += 1
                    except OSError:
                        break
                return count
        except Exception as e:
            print(f"Error retrieving package count: {e}")
            return "Package info not available"
        
    def get_uptime():
        uptime_seconds = int(psutil.boot_time())
        current_time = int(psutil.time.time())
        uptime = current_time - uptime_seconds
        return str(timedelta(seconds=uptime))

    def get_gpu_info():
        try:
            gpu_info = subprocess.check_output("wmic path win32_VideoController get name", shell=True).decode().split('\n')[1].strip()
            return gpu_info
        except:
            return "N/A"
        
    def get_resolution():
        try:
            resolution = subprocess.check_output("wmic path Win32_VideoController get CurrentHorizontalResolution,CurrentVerticalResolution", shell=True).decode().split('\n')[1].strip().split()
            return f"{resolution[0]}x{resolution[1]}"
        except:
            return "Resolution not available"

    user = psutil.users()[0].name
    ops = f"{platform.system()} {platform.release()} {platform.version()}"
    host = platform.node()
    kernel = platform.version()
    uptime = get_uptime()
    packages = get_packages()
    cwd = subprocess.getoutput('cd').split('\n')[0]
    resolution = get_resolution()
    cpu_info = platform.processor() + f", {psutil.cpu_count(logical=False)} (Physical), {psutil.cpu_count(logical=True)} (Logical), {psutil.cpu_freq().current:.2f}MHz"
    gpu_info = get_gpu_info()
    memory = f"{psutil.virtual_memory().used // (1024 ** 2)}MiB / {psutil.virtual_memory().total // (1024 ** 2)}MiB"


    print(f"""
                  {user} @ {host}
      ,           ---------
   \  :  /        OS: {ops}
`. __/ \__ .'     Host: {host}
_ _\     /_ _     Kernel: {kernel}
   /_   _\        Uptime: {uptime}
 .'  \ /  `.      Packages: {packages}
   /  :  \        Current Directory: {cwd}
      '           Resolution: {resolution}
                  CPU: {cpu_info}
                  GPU: {gpu_info}
                  Memory: {memory}  
        """)

if __name__ == "__main__":
    main()