import subprocess


print("Hello, welcome to nodelink.\n")

while True:
    start = input("Ready to start? (y/n)").lower()
    if start == 'y':
        break;
        
subprocess.run("colcon build", shell=True)
subprocess.run("source install/setup.bash", shell=True)
subprocess.run("ros2 run nodelink listener", shell=True)