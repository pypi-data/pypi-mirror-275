import os 

pipe_read, pipe_write = os.pipe() 
 
pid = os.fork() 
if pid == 0: 

    os.close(pipe_write)
    child_data = os.read(pipe_read, 1024) 
    print(f"Child received: {child_data.decode()}") 
else: 
    os.close(pipe_read) 
    data_to_send = "Hello from Parent!" 
    os.write(pipe_write, data_to_send.encode()) 
    os.wait()