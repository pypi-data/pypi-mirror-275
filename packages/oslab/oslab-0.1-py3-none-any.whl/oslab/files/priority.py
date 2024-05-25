def non_preemptive_priority(processes, arrival_time, burst_time, priority):
    n = len(processes)
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    process_sequence = []

    sorted_processes = sorted(range(n), key=lambda x: (arrival_time[x], priority[x]))

    current_time = 0  
    for i in sorted_processes:
        if current_time < arrival_time[i]:
            current_time = arrival_time[i]
        current_time += burst_time[i]
        completion_time[i] = current_time
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]
        process_sequence.append(processes[i])

    return completion_time, turnaround_time, waiting_time, process_sequence

def preemptive_priority(processes, arrival_time, burst_time, priority):
    n = len(processes)
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    process_sequence = []

    remaining_time = burst_time.copy()
    current_time = min(arrival_time)
    completed_processes = 0

    while completed_processes < n:
        min_priority = float('inf')
        selected_process = None

        for i in range(n):
            if arrival_time[i] <= current_time and priority[i] < min_priority and remaining_time[i] > 0:
                min_priority = priority[i]
                selected_process = i

        if selected_process is None:
            current_time += 1
        else:
            process_sequence.append(processes[selected_process])
            current_time += 1
            remaining_time[selected_process] -= 1

            if remaining_time[selected_process] == 0:
                completed_processes += 1
                completion_time[selected_process] = current_time
                turnaround_time[selected_process] = completion_time[selected_process] - arrival_time[selected_process]
                waiting_time[selected_process] = turnaround_time[selected_process] - burst_time[selected_process]

    return completion_time, turnaround_time, waiting_time, process_sequence

def display_gantt_chart(process_sequence, completion_time):
    n = len(process_sequence)
    gantt_chart = []

    for i in range(n):
        gantt_chart.append(process_sequence[i])
        if i < n - 1:
            while process_sequence[i] == process_sequence[i + 1]:
                gantt_chart.append(process_sequence[i])
                i += 1

    return gantt_chart

processes = ['P1', 'P2', 'P3', 'P4']
arrival_time = [0, 1, 2, 3]
burst_time = [4, 5, 2, 1]
priority = [2, 1, 3, 4]

print("Non-Preemptive Priority Scheduling:")
comp_time_np, turn_time_np, wait_time_np, process_seq_np = non_preemptive_priority(processes, arrival_time, burst_time, priority)
gantt_chart_np = display_gantt_chart(process_seq_np, comp_time_np)
print("Gantt Chart:", " | ".join(gantt_chart_np))
print("Process\tCompletion Time\tTurnaround Time\tWaiting Time")
for i in range(len(processes)):
    print(f"{processes[i]}\t{comp_time_np[i]}\t\t\t{turn_time_np[i]}\t\t\t{wait_time_np[i]}")

avg_wait_time_np = sum(wait_time_np) / len(processes)
avg_turnaround_time_np = sum(turn_time_np) / len(processes)
print(f"Average Waiting Time (Non-Preemptive): {avg_wait_time_np:.2f}")
print(f"Average Turnaround Time (Non-Preemptive): {avg_turnaround_time_np:.2f}")

print("\nPreemptive Priority Scheduling:")
comp_time_p, turn_time_p, wait_time_p, process_seq_p = preemptive_priority(processes, arrival_time, burst_time, priority)
gantt_chart_p = display_gantt_chart(process_seq_p, comp_time_p)
print("Gantt Chart:", " | ".join(gantt_chart_p))
print("Process\tCompletion Time\tTurnaround Time\tWaiting Time")
for i in range(len(processes)):
    print(f"{processes[i]}\t{comp_time_p[i]}\t\t\t{turn_time_p[i]}\t\t\t{wait_time_p[i]}")


avg_wait_time_p = sum(wait_time_p) / len(processes)
avg_turnaround_time_p = sum(turn_time_p) / len(processes)
print(f"Average Waiting Time (Preemptive): {avg_wait_time_p:.2f}")
print(f"Average Turnaround Time (Preemptive): {avg_turnaround_time_p:.2f}")
