import argparse, subprocess, logging, sys
parser = argparse.ArgumentParser()
parser.add_argument("-g","--debug",action="store_true", help="Show debugging information")
parser.add_argument("-v","--valgrind",action="store_true", help="Show valgrind memleak information")
parser.add_argument("-c","--clear",action="store_true", help="Clear the log")
args = parser.parse_args()

if args.clear:
    file = open("example.log","r+")
    file.truncate(0)
    file.close()
    print("Log Cleared.")
    quit()

if not args.debug:
    #subprocess.call(["gcc","sniffex.c", "-o", "sniffex", "-lpcap"])
    subprocess.call(["make"])
    logging.basicConfig(filename='example.log',format='%(asctime)s %(message)s')
    logging.warning("Sniffex was called.")
else:
    #subprocess.call(["gcc","sniffex.c", "-o", "sniffex", "-lpcap", "-D", "DEBUG"])
    subprocess.call(["make","debug"])
    logging.basicConfig(filename='example.log',format='%(asctime)s %(message)s')
    logging.warning("Sniffex was called in DEBUG mode.")

if args.valgrind:
    subprocess.call(["make","valgrind"])
else:
    subprocess.call(["./sniffex", "lo"])