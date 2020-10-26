from common import *


class O:

    def __init__(self):
        self.files = sorted(grabFiles())
        self.d = loadPickle(self.files[-1])
        self.last = None
        self.keys = list(self.d.keys())
        self.n = len(self.d[self.keys[0]])
        self.isRunning = False
        self.runingTime = 0

        [exec3(f"mv {os.path.join( PARSED_DIR,fp)} {CACHED_FOLDER}") for fp in self.files[:-1]]
        self.start()
        return


    def stop(self):
        self.isRunning = False


    def start(self):
        self.isRunning = True
        threading_func_wrapper(self.update, 0.1)


    def compare(self):
        return


    def update(self):
        if not self.isRunning: return
        self.runingTime += 1
        self.files = sorted(grabFiles())
        self.last = self.d
        self.d = loadPickle(self.files[-1])
        self.compare()
        print(f"\rListening, up for {self.runingTime} seconds, last file: "
              f"{self.files[-1].split('2020_')[1]}", end="")
        threading_func_wrapper(self.update, 1)

if "o" in globals(): o.stop()
o = O()

#%%















