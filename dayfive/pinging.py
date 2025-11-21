import subprocess

with open(r"D:\\Internship\Assignments\dayfive\sites.txt") as f:
    lines= f.readlines()
    
for line in lines :
    site= line.strip()
    print(f"pinging {line}")
    result = subprocess.run(["ping",line,"-n","1"],capture_output=True,text= True,shell=True)
    print(result.stdout)
    
    
    
