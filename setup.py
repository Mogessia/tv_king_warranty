import os
import subprocess
import sys

def run_cmd(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def main():
    print("--- የ TV-King ዋስትና ሲስተም መጫን ተጀምሯል ---")
    
    # 1. Django መጫን
    run_cmd(f"{sys.executable} -m pip install django")
    
    # 2. የጃንጎ መዋቅር መፍጠር
    if not os.path.exists("tv_king_warranty"):
        run_cmd("django-admin startproject tv_king_warranty .")
    
    # 3. የጥገና App መፍጠር
    if not os.path.exists("repairs"):
        run_cmd(f"{sys.executable} manage.py startapp repairs")
        
    print("\n[ትልቅ ስኬት!] የጃንጎ መዋቅር በራሱ ተፈጥሯል።")
    print("አሁን ፋይሎቹን ማስተካከል እንችላለን።")

if __name__ == "__main__":
    main()