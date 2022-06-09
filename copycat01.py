#! /usr/bin/env python3

#import additional code to complete our task
import shutil  #shell utilities
import os  #os compatibility


def main():
    #move into the working directory path
    os.chdir("/home/student/mycode/")

    #copy the fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    #copy the entire directorA to directoryB
    shutil.copytree("5g_research/", "5g_research_backup/")

    #copy the entire directoryA to directoryB
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()





