import platform, os, random, time

if platform.system() == "Windows":
    cmd = "cls"
    os.system("title Space Shuttle")

else: 
    cmd = "clear"

space = 0
reverse = False

while True:

    if space >= 15:
        reverse = True 

    elif space <= 0:
        reverse = False

    if reverse:
        space -= 1

    else:
        space += 1

    spaces = "\n" * space

    spaces_down = 20 - space
    spaces_down = "\n" * spaces_down 
    
    res = f"""
{spaces}
   __
   \ \_____ {' ' * random.choice(range(0, 10))} {random.choice(['-----', '-----', '-----', '•'])} {' ' * random.choice(range(0, 10))} ----- {' ' * random.choice(range(0, 10))} ----- {' ' * random.choice(range(0, 10))} ----- {' ' * random.choice(range(0, 10))} {random.choice(['-----', '-----', '-----', '•'])} {' ' * random.choice(range(0, 10))} {random.choice(['-----', '-----', '-----', '•'])}           
###[==_____>
   /_/       {' ' * random.choice(range(0, 10))} {random.choice(['-----', '-----', '-----', '•'])} {' ' * random.choice(range(0, 10))} ----- {' ' * random.choice(range(0, 10))} ----- {' ' * random.choice(range(0, 10))} ----- {' ' * random.choice(range(0, 10))} ----- {' ' * random.choice(range(0, 10))} {random.choice(['-----', '-----', '-----', '•'])} 
{spaces_down}
"""

    result = []

    for line in res.splitlines():
        if len(line) != 0:
            result.append(line)

        else:
            result.append(f"{' ' * random.choice(range(0, 10))} {random.choice(['-----', '-----', '-----', '•'])} {' ' * random.choice(range(0, 10))} {random.choice(['-----', '-----', '-----', '•'])} {' ' * random.choice(range(0, 10))} {random.choice(['-----', '-----', '-----', '•'])} {' ' * random.choice(range(0, 10))} ----- {' ' * random.choice(range(0, 10))} {random.choice(['-----', '-----', '-----', '•'])} {' ' * random.choice(range(0, 10))} {random.choice(['-----', '-----', '-----', '•'])} ") 
    
    os.system(cmd)
    print("\n".join(result))
    time.sleep(0.15)