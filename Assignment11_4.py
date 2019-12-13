import os;
import sys;
import Helper_Module;
import time

def DuplicateRemoval(path):
    f=open("log.txt","w")
    data={}
    for Folder, Subfolder, Files in os.walk(path):
        for name in Files:
            name = os.path.join(Folder, name);
            checksum = Helper_Module.Checksum(name);
            if checksum in data:
                f.write(str(data[checksum]))
                f.write(str(name) + "\n")
                f.write(str(checksum) + "\n")
                data[checksum].append(name);
                os.remove(name)
            else:
                data[checksum] = [name];


def main():
    starttime=time.time()
    if os.path.exists(sys.argv[1]):
        DuplicateRemoval(sys.argv[1]);
    else:
        print("no such folder")
    endtime= time.time()
    print(starttime-endtime)

if __name__ == "__main__":
    main();