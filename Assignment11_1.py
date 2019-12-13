import os;
import sys;
import Helper_Module;


def DuplicateRemoval(path):
    f=open("log.txt","w")
    for Folder, Subfolder, Files in os.walk(path):
        for name in Files:
            f.write(str(name)+"\n")
            name = os.path.join(Folder, name);
            checksum = Helper_Module.Checksum(name);
            f.write(str(checksum)+"\n")
            



def main():
    if os.path.exists(sys.argv[1]):
        DuplicateRemoval(sys.argv[1]);
    else:
        print("no such folder")


if __name__ == "__main__":
    main();