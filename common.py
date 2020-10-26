import os, pickle, json
from os import listdir
from os.path import isfile, join


PARSED_FOLDER = "/home/sotola/Coding/parsed"
CACHED_FOLDER = '/home/sotola/Coding/cache'
PATTERN_HOSE_SNAPSHOT = "HOSE_SNAPSHOT"
PARSED_DIR = "/home/sotola/Coding/parsed"
BIL = 1000*1000*1000



def exec3(cmd): #
  #print(f"****\n running: {cmd} ****")
  import subprocess
  process = subprocess.Popen(cmd.split(" "),
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE)
  stdout, stderr = process.communicate()
  # print (stdout.decode("utf-8"), stderr.decode("utf-8"))
  return stdout.decode("utf-8"), f"""error code: {stderr.decode("utf-8")}"""

def grabFiles(PATH=PARSED_FOLDER, pattern=PATTERN_HOSE_SNAPSHOT):
    onlyfiles = [f for f in listdir(PATH) if (
            isfile(join(PATH, f)) &
            f.__contains__(pattern) & (not f.__contains__("(")))]
    return onlyfiles


def readSingleFile(fn):
    with open(fn, "r") as file:
        raw = json.load(file)
    return raw

def threading_func_wrapper(func, delay=0.5, args=None, start=True):
    import threading
    if args is None:
        func_thread = threading.Timer(delay, func)
    else:
        func_thread = threading.Timer(delay, func, (args,))
    if start: func_thread.start()
    return func_thread

def mmap(*args):
    return list(map(*args))

def extractTimeOld(file):
    timeString = file[file.find("2020") + 4:file.find(".json")]
    hour, minute, second = mmap(int, timeString.split("_"))
    if len(timeString) == len("9_59_59"):
        timeString = "0" + timeString
    return timeString

def extractTime2(file, TIMESTAMP=False):
    import re
    timeString = file[file.find("2020") + 4:file.find(".json")]
    day, month, year, hour, minute, second = mmap(int, file.replace(".json", "").split("_")[2:])
    if TIMESTAMP:
        import datetime, time
        t = time.mktime(datetime.datetime.strptime(f"{day}/{month}/{year}", "%d/%m/%Y").timetuple())
        return int(t + hour * 3600 + minute * 60 + second)
    return hour + minute/60 + second/3600

def listIsSorted(l):
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def loadPickle(fn):
    fp = os.path.join(PARSED_DIR, fn)
    with open(fp, "rb") as file:
        return pickle.load(file)


def beautify(x, num_decimal=2):
  if num_decimal==2: return float(f"{x:.2f}")
  if num_decimal==3: return float(f"{x:.3f}")
  if num_decimal==4: return float(f"{x:.4f}")
  if num_decimal==5: return float(f"{x:.5f}")
  if num_decimal==6: return float(f"{x:.6f}")