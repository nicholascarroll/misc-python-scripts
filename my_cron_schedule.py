import cron_descriptor as cd                                                                 
import subprocess as sp                                                                      
                                                                                             
                                                                                             
def crontabline2english(line):                                                               
    words = line.split()                                                                     
    schedule = ' '.join(words[:5])                                                           
    command = ' '.join(words[5:])                                                            
    sched_eng = cd.get_description(schedule)                                                 
    activity = sched_eng + ', ' + command                                                    
    return activity                                                                          
                                                                                             
                                                                                             
# execute a linux command and get the output                                                 
lines = sp.check_output('crontab -l', shell=True).decode('utf-8').strip()                    
                                                                                             
# make a list of lines, removing the lines that start with #                                 
lines = [line.strip() for line in lines.split('\n') if not line.startswith('#')]             
                                                                                             
if lines:                                                                                    
    print("My Cron Schedule:")                                                               
    for line in lines:                                                                       
        print(' * ' + crontabline2english(line))
else:
    print("No Cron jobs scheduled")
