import concurrent.futures
import hydrus  # Assuming hydrus is a module you've created for calculations


def execute_in_parallel(functions, *args, max_workers=None):
    if max_workers is None:
        max_workers = (os.cpu_count() or 1) // 2  # Default to half the processors
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(lambda func: func(*args), functions))
    return results


def better_resource_management(task_list, *args):
    successful_executions = []
    failures = []
    
    for result in execute_in_parallel(task_list, *args):
        if isinstance(result, Exception):
            failures.append(result)
        else:
            successful_executions.append(result)
    
    return successful_executions, failures


if __name__ == '__main__':
    # Example usage:
    tasks = [task1, task2, task3]  # Replace with actual task functions
    results, errors = better_resource_management(tasks, *args)  # Replace with actual arguments
    
    if errors:
        print('Errors occurred during execution:', errors)
    else:
        print('All tasks executed successfully!')