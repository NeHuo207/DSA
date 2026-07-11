from collections import deque


def round_robin(processes, quantum):
    q = deque(processes)
    time = 0
    completion = {}

    while q:
        pid, remaining = q.popleft()
        run = min(quantum, remaining)
        time += run
        remaining -= run

        if remaining == 0:
            completion[pid] = time
        else:
            q.append((pid, remaining))

    return completion


if __name__ == "__main__":
    processes = [(1, 5), (2, 3), (3, 8)]
    result = round_robin(processes, quantum=2)
    for pid in sorted(result):
        print(f"P{pid}: hoan thanh luc {result[pid]}")

    burst = dict(processes)
    print("\nturnaround time:")
    for pid in sorted(result):
        print(f"P{pid}: {result[pid]} (burst={burst[pid]})")
