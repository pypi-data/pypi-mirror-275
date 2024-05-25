def sjf(process_list):
    completed_process = {}
    gantt_chart = []
    t = 0
    while process_list != []:
        available = [process for process in process_list if process[1] <= t]

        if available == []:
            gantt_chart.append(("Idle", t))
            t += 1
            continue
        else:
            available.sort()
            process = available[0]
            t += process[0]
            gantt_chart.append((process[2], t))
            process_list.remove(process)
            process_name = process[2]
            ct = t
            tt = ct - process[1]
            wt = tt - process[0]
            completed_process[process_name] = [ct, tt, wt]

    # Display Gantt Chart
    print("\nGantt Chart:")
    print("-" * 35)
    print("| {:<10} | {:<10} |".format("Process", "Time"))
    print("-" * 35)
    for entry in gantt_chart:
        print("| {:<10} | {:<10} |".format(entry[0], entry[1]))
    print("-" * 35)

    # Display Completed Process List
    print("\nCompleted Process List:")
    print("{:<5} {:<15} {:<15} {:<15}".format("PID", "Completion Time", "Turnaround Time", "Waiting Time"))
    total_waiting_time = 0
    total_turnaround_time = 0
    for pid, values in completed_process.items():
        wt = values[2]
        tt = values[1]
        total_waiting_time += wt
        total_turnaround_time += tt
        print("{:<5} {:<15} {:<15} {:<15}".format(pid, values[0], tt, wt))

    # Calculate and print average waiting time and turnaround time
    avg_waiting_time = total_waiting_time / len(completed_process)
    avg_turnaround_time = total_turnaround_time / len(completed_process)
    print("\nAverage Waiting Time:", avg_waiting_time)
    print("Average Turnaround Time:", avg_turnaround_time)

if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes: "))
    process_list = []

    for i in range(num_processes):
        pid = input(f"Enter the process ID for process {i + 1}: ")
        bt = int(input(f"Enter the burst time for process {pid}: "))
        at = int(input(f"Enter the arrival time for process {pid}: "))
        process_list.append([bt, at, pid])

    sjf(process_list)
