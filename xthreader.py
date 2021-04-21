#!/usr/bin/python3

import os
import sys
import getopt
import xt_libx


logo = r"""

 ___  ___  ___________  __    __    _______    _______       __       ________    _______   _______   
|"  \/"  |("     _   ")/" |  | "\  /"      \  /"     "|     /""\     |"      "\  /"     "| /"      \  
 \   \  /  )__/  \\__/(:  (__)  :)|:        |(: ______)    /    \    (.  ___  :)(: ______)|:        | 
  \\  \/      \\_ /    \/      \/ |_____/   ) \/    |     /' /\  \   |: \   ) || \/    |  |_____/   ) 
  /\.  \      |.  |    //  __  \\  //      /  // ___)_   //  __'  \  (| (___\ || // ___)_  //      /  
 /  \   \     \:  |   (:  (  )  :)|:  __   \ (:      "| /   /  \\  \ |:       :)(:      "||:  __   \  
|___/\___|     \__|    \__|  |__/ |__|  \___) \_______)(___/    \___)(________/  \_______)|__|  \___) 
                                                                                                      

                                Coded By Jxbt
"""
menu = """

Usage: xthreader [options]


Flags:

    -c,--command                 the command or the template of the command that you want to thread.(required)

    -t,--threads                 the amount of threads.(optional)(default is 10)

    -i,--input                   the input file or the list of input files.(optional)

    -s,--sleep                   the time interval in seconds between each group of threads.(optional)(default is 0s)

    -n,--timesnum                the number of the times that you want to execute the group of threads if your command is not a template.(optional) (default is 1 loop)

    -v,--verbose                 turn on verbose mode.(optional)

    -h,--help                    to show the help menu.(optional)


Examples:

    1- xthreader -c 'ping 192.168.1.1' -t 10 -n 2 -s 1

    2- xthreader -c 'dig A $var1' -i domains.txt -t 50 -v

    3- xthreader -c 'echo "$var1$var2" > $var3' -i f1.txt,f2.txt,f3.txt -t 10

"""

command = ""
threads_num = 10
input_files = []
input_var_values = {}
sleep_time = 0
verbose = False

thread_loops_num = 1

min_values_varName = "var1"

argvs = sys.argv[1:]

opts = []
args = []

if len(argvs) == 0:
    print(logo)
    print(menu)
    sys.exit(1)

try:
    opts,args = getopt.getopt(argvs,"c:t:i:n:s:hv",["command=","threads=","input=","timesnum=","sleep=","help","verbose"])

except Exception as ex:
    print(logo)
    print(menu)
    sys.exit(1)

for opt,arg in opts:

    if opt == "-c" or opt == "--command":
        command = str(arg)
    
    elif opt == "-t" or opt == "--threads":
        threads_num = int(arg)

    elif opt == "-i" or opt == "--input":

        files_str = str(arg)

        if "," in files_str:
            input_files = files_str.split(",")
        else:
            input_files.append(files_str)
    
    elif opt == "-n" or opt == "--timesnum":
        thread_loops_num = int(arg)
    elif opt == "-s" or opt == "--sleep":
        sleep_time = int(arg)

    elif opt == "-v" or opt == "--verbose":
        verbose = True
    elif opt == "-h" or opt == "--help":
        print(menu)
        sys.exit(0)
    else:
        pass



for i_file in input_files:

    if os.path.isfile(i_file) == False:
        print(menu)
        sys.exit(1)
    else:
        pass




file_num = 1
for i_file in input_files:

    
    var_values = []

    with open(i_file,"r") as f:

        line = str(f.readline()).replace("\n","")

        while len(line) > 0:

            var_values.append(line)
            
            line = str(f.readline()).replace("\n","")
            
    


    input_var_values[f"var{file_num}"] = var_values
    
    
    

    if file_num != 1:

        if len(input_var_values[f"var{file_num}"]) < len(input_var_values[f"var{file_num-1}"]):
            min_values_varName = f"var{file_num}"
        else:
            pass
    else:
        pass

    file_num+=1



print(logo)


def main():
    
    xt = xt_libx.xt(input_var_values,min_values_varName,command,verbose)
    
    if len(input_var_values) >= 1:

        xt.Thread1(threads_num,sleep_time)

    else:
        xt.Thread2(threads_num,sleep_time,thread_loops_num)
    



if __name__ == "__main__":
    main()