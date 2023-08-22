import time
import concurrent.futures
import asyncio

def target_function(*args, **kwargs):
    time.sleep(10)
    return sum(args) + sum(kwargs.values())

def evaluate_with_multiprocessing(target_function, num_processes, tasks):
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        results = list(executor.map(target_function, *zip(*tasks)))
    return results

def evaluate_with_multithreading(target_function, num_threads, tasks):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(target_function, *zip(*tasks)))
    return results

async def evaluate_async(target_function, tasks):
    loop = asyncio.get_event_loop()
    coroutines = [loop.run_in_executor(None, target_function, *task) for task in tasks]
    results = await asyncio.gather(*coroutines)
    return results

def main():
    target_function_name = input("Enter the target function (e.g., 'target_function'): ")
    num_processes = int(input("Enter the number of processes: "))
    num_threads = int(input("Enter the number of threads: "))
    num_tasks = int(input("Enter the number of tasks: "))

    tasks = [(tuple(range(1, num_tasks + 1)), {}) for _ in range(num_tasks)]

    # Using multiprocessing
    start_time = time.time()
    multiprocessing_results = evaluate_with_multiprocessing(
        globals()[target_function_name], num_processes, tasks
    )
    multiprocessing_time = time.time() - start_time

    # Using multithreading
    start_time = time.time()
    multithreading_results = evaluate_with_multithreading(
        globals()[target_function_name], num_threads, tasks
    )
    multithreading_time = time.time() - start_time

    # Using asyncio
    start_time = time.time()
    asyncio_results = asyncio.run(evaluate_async(globals()[target_function_name], tasks))
    asyncio_time = time.time() - start_time
    
    print("Multiprocessing results:", multiprocessing_results)
    print("Multithreading results:", multithreading_results)
    print("Asyncio results:", asyncio_results)

    print("Time taken for multiprocessing:", multiprocessing_time)
    print("Time taken for multithreading:", multithreading_time)
    print("Time taken for asyncio:", asyncio_time)

if __name__ == "__main__":
    main()
