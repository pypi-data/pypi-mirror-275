def round_robin_scheduler(total_p_no, processes, time_quantum):
    total_time = 0
    total_time_counted = 0
    wait_time = 0
    turnaround_time = 0
    proc = []
    gantt_chart = []

    for arrival, burst in processes:
        remaining_time = burst
        proc.append([arrival, burst, remaining_time, 0])
        total_time += burst

    while total_time != 0:
        for i in range(len(proc)):
            if proc[i][2] <= time_quantum and proc[i][2] > 0:
                gantt_chart.extend([f'p{i + 1}'] * proc[i][2])
                total_time_counted += proc[i][2]
                total_time -= proc[i][2]
                proc[i][2] = 0
            elif proc[i][2] > 0:
                gantt_chart.extend([f'p{i + 1}'] * time_quantum)
                proc[i][2] -= time_quantum
                total_time -= time_quantum
                total_time_counted += time_quantum
            if proc[i][2] == 0 and proc[i][3] != 1:
                wait_time += total_time_counted - proc[i][0] - proc[i][1]
                turnaround_time += total_time_counted - proc[i][0]
                proc[i][3] = 1

    avg_waiting_time = wait_time / total_p_no
    avg_turnaround_time = turnaround_time / total_p_no

    return avg_waiting_time, avg_turnaround_time, gantt_chart

if __name__ == "__main__":
    total_p_no = int(input("Enter Total Process Number: "))
    processes = []
    for i in range(total_p_no):
        arrival, burst = map(int, input(f"Enter arrival time and burst time of process {i + 1}: ").split())
        processes.append((arrival, burst))
    
    time_quantum = int(input("Enter time quantum: "))

    avg_waiting_time, avg_turnaround_time, gantt_chart = round_robin_scheduler(total_p_no, processes, time_quantum)

    print("\nAvg Waiting Time is", avg_waiting_time)
    print("Avg Turnaround Time is", avg_turnaround_time)
    print("Gantt Chart:", gantt_chart)
