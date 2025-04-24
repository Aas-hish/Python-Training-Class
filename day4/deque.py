from collections import deque



def Find(tasks,time_slice):
    Q= deque()
    for i in range(len(tasks)):
        Q.append((tasks[i],i+1))
        
    total_time =0
    
    while Q:
        task,task_id = Q.popleft()
        executed_time = min(task,time_slice)
        total_time = total_time + executed_time
        print("Task {} --> executed {} units : Time - {}".format(task_id,executed_time,total_time))
        
        if(task>time_slice):
            Q.append((task - executed_time, task_id))
    print("Total time taken : {}".format(total_time))




tasks = [10,5,8]
time_slice= 4

Find(tasks,time_slice)

   
        
