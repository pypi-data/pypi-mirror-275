num_processes = int(input("Enter the number of processes: "))
processes = []

for i in range(num_processes):
    arrival_time = int(input(f"Enter Arrival Time for Process {i + 1}: "))
    burst_time = int(input(f"Enter Burst Time for Process {i + 1}: "))
    processes.append([i + 1, arrival_time, burst_time])

overhead = int(input("Enter the overhead time: "))

print("\nEntered Process Information:")
print("Process ID\tArrival Time\tBurst Time")
print("-----------------------------------")
for process in processes:
    process_id, arrival_time, burst_time = process
    print(f"{process_id}\t\t{arrival_time}\t\t{burst_time}")

processes.sort(key=lambda x: x[1])
completion_times = []
current_time = 0
gantt_chart = []

for process in processes:
    process_id, arrival_time, burst_time = process

    if current_time < arrival_time:
        gantt_chart.append(("Idle", arrival_time - current_time))
        current_time = arrival_time

    if overhead > 0:
        gantt_chart.append(("Idle", overhead))
        current_time += overhead

    gantt_chart.append((f"P{process_id}", burst_time))
    completion_time = current_time + burst_time
    completion_times.append(completion_time)
    current_time = completion_time

turnaround_times = []
waiting_times = []
total_turnaround_time = 0
total_waiting_time = 0

for i in range(num_processes):
    process_id, arrival_time, burst_time = processes[i]
    completion_time = completion_times[i]
    turnaround_time = completion_time - arrival_time
    waiting_time = turnaround_time - burst_time
    turnaround_times.append(turnaround_time)
    waiting_times.append(waiting_time)
    total_turnaround_time += turnaround_time
    total_waiting_time += waiting_time

print("\nProcesses after sorting based on Arrival Time:")
print("Process ID\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
print("----------------------------------------------------")
for i in range(num_processes):
    process_id, arrival_time, burst_time = processes[i]
    completion_time = completion_times[i]
    turnaround_time = turnaround_times[i]
    waiting_time = waiting_times[i]
    print(f"{process_id}\t\t{arrival_time}\t\t{burst_time}\t\t{completion_time}\t\t{turnaround_time}\t\t{waiting_time}")

average_turnaround_time = total_turnaround_time / num_processes
average_waiting_time = total_waiting_time / num_processes

print("\nAverage Turnaround Time:", average_turnaround_time)
print("Average Waiting Time:", average_waiting_time)

print("\nGantt Chart:")
print("-" * 45)

current_time = 0
for item in gantt_chart:
    process_name, time = item
    if process_name != "Idle" or overhead > 0:
        print(f"|{current_time:2d}-{current_time + time:2d}", end="")
        current_time += time
print("|\n" + "-" * 45)

for item in gantt_chart:
    process_name, time = item
    if process_name != "Idle" or overhead > 0:
        print(f"|{process_name.center(time * 5)}", end="")
print("|\n" + "-" * 45)
