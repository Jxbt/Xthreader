#!/usr/bin/python3

import subprocess
import threading
import time



class xt:

    

    def __init__(self,input_var_values,min_values_varName,command_temp,verbose):

        self.input_vars_values = input_var_values
        self.min_val_varname = min_values_varName
        self.command_temp = command_temp
        self.verbose = verbose

   
    def sub_call(self,command,ex_signal):

        if ex_signal:
            return
        

        if self.verbose == True:
            p = subprocess.run(command,shell=True,capture_output=True,text=True)
            print(p.stdout)
        else:
            subprocess.run(command,shell=True,capture_output=True)

   
    def command_gen(self,value_index):
        

        command = self.command_temp

        
        
        for var in self.input_vars_values:

            command = str(command).replace(f"${var}",self.input_vars_values[var][value_index])
        
        return command
    

    def Thread1(self,threads_num,sleep_time):

        i = 0

        while i < len(self.input_vars_values[self.min_val_varname]):

            try:
                self.input_vars_values[self.min_val_varname][i+1]
            except Exception as ex:
                break


            ex_signal = False

            threads = []

            for _ in range(threads_num):
                
                command = self.command_gen(i)
                t = threading.Thread(target=self.sub_call,args=[command,ex_signal])
                t.start()

                threads.append(t)

                try:
                    self.input_vars_values[self.min_val_varname][i+1]
                    i+=1
                except Exception as ex:
                    ex_signal  = True
            
            for thread in threads:
                thread.join()
            

            time.sleep(sleep_time)



    def Thread2(self,threads_num,sleep_time,thread_loops_num):

        i = 0

        while i < thread_loops_num:


            ex_signal = False

            threads = []

            for _ in range(threads_num):
                
                command = self.command_temp
                t = threading.Thread(target=self.sub_call,args=[command,ex_signal])
                t.start()

                threads.append(t)
                
            
            for thread in threads:
                thread.join()
            

            i+=1
            time.sleep(sleep_time)