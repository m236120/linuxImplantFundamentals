#does it compile (without errors, if there are errors, log them)
#does it run
#does it listen on a port
#BONUS (If you activate the implant using "nc -z", does it do something? have it create a file and check if the file has been created)
#kill the process

import argparse, subprocess, logging, sys



logging.basicConfig(filename='example.log',format='%(asctime)s %(message)s')
logging.warning("=================================================")
logging.warning("~~~~~~~~~~~~~~~Testing sniffex.c~~~~~~~~~~~~~~~~~")
logging.warning("=================================================")

subprocess.check_call(["rm", "-f", "sniffex"])

logging.warning("TEST 1: Program Compilation")
try:
    subprocess.check_call(["make"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    logging.warning("  -> SUCCESS: The program compiles.")
except subprocess.CalledProcessError as e:
    logging.warning("  -> FAILURE: The program does not compile.")
    quit()

logging.warning("TEST 2: Program Running")
try:
    p = subprocess.Popen(["./sniffex","lo"], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    for x in range(0,5):
    	subprocess.call(["nc", "-z", "localhost", "69"])
    logging.warning("  -> SUCCESS: The program runs.")
except subprocess.CalledProcessError as e:
    logging.warning("  -> FAILURE: The program does not run.")

logging.warning("TEST 3: Program Listening")
output = subprocess.check_output("lsof | grep SOCK_RAW", shell=True, stderr=subprocess.PIPE)
if b"sniffex" in output:
    logging.warning("  -> SUCCESS: The program listens correctly.")
else:
    logging.warning("  -> FAILURE: The program does not listen correctly.")

p.kill()

