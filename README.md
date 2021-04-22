# Xthreader

Xthreader is a general purpose tool used to thread commands/command line tools.the tool allows you to execute a command multiple times very fast with ability to give the command different input in each thread using a command template.


___



## Usage:

```
xthreader [options]
```

### Flags:

| Flag          |  Description                                                                                                                             |
----------------|------------------------------------------------------------------------------------------------------------------------------------------|
  -c,--command  |   the command or the template of the command that you want to thread.(required) |  
  -t,--threads  |   the amount of threads.(optional)(default is 10) |
  -i,--input    |   the input file or the list of input files.(optional) | 
  -s,--sleep    |   the time interval in seconds between each group of threads.(optional)(default is 0s)  |
  -n,--timesnum |    the number of the times that you want to execute the group of threads if your command is not a template.(optional) (default is 1 loop)|
  -v,--verbose  |  turn on verbose mode.(optional)|
  -h,--help     |  to show the help menu.(optional) |


### Examples:

1. xthreader -c 'ping 192.168.1.1' -t 10 -n 2 -s 1
1. xthreader -c 'dig A $var1' -i domains.txt -t 50 -v
1. xthreader -c 'echo "$var1$var2" > $var3' -i f1.txt,f2.txt,f3.txt -t 10




## Installation:

```bash

chmod +x install.sh
sudo ./install.sh

```
