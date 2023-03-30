import subprocess


print("Hello, welcome to nodelink.\n")
while True:
    start = input("Ready to start? (y/n) ").lower()
    if start == 'y':
        break;
        
subprocess.run("colcon build", shell=True)

print("""
  nodelink build completed.
  
  Instructions:
    1. Type "source install/setup.bash"
    2. Type "ros2 run nodelink listener"
    3. Open a second terminal
    4. Navigate to nodelink-main
    5. Type "source install/setup.bash"
    6. Type "ros2 run nodelink talker"
    7. Enjoy
    """)