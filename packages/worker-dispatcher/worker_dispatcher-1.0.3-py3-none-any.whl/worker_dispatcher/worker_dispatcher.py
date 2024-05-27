import multiprocessing, concurrent.futures
import time, datetime, copy, requests

# Sample callback function
def callback_sample(id: int, config=None, task=None):
    if id == 1:
        print("Runing sample task function, please customize yours according to the actual usage.")
    result = {
        'taskId': id
    }
    return result

# Sample result callback function
def result_callback_sample(id: int, config=None, result=None, log: dict=None):
    if id == 1:
        print("Runing sample result function, please customize yours according to the actual usage.")
    return result

# Default configuration
default_config = {
    'debug': False,
    'task': {
        'list': [],                     # Support list and integer. Integer represent the number of tasks to be generated.
        'callback': callback_sample,
        'config': {},
        'result_callback': False
    },
    'worker': {
        'number': multiprocessing.cpu_count(),
        'per_second': 0,                # If greater than 0, the specified number of workers run at set intervals.
        'cumulative': False,            # Cumulative mode for per_second method.
        'multiprocessing': False
    },
    'runtime': None,                    # Dispatcher max runtime in seconds
    'verbose': True
}

# Global variable
results = []
logs = []
result_info = {}

# Start function
def start(user_config: dict) -> list:

    global results, logs, result_info
    results = []
    logs = []

    # Merge config with 2 level
    config = copy.deepcopy(default_config)
    for level1_key in config.keys():
        if level1_key in user_config:
            if isinstance(config[level1_key], dict):
                config[level1_key].update(user_config[level1_key])
            else:
                config[level1_key] = user_config[level1_key]

    # Multi-processing handler
    use_multiprocessing = config['worker']['multiprocessing']
    if use_multiprocessing:
        in_child_process = (multiprocessing.current_process().name != 'MainProcess')
        # Return False if is in worker process to let caller handle
        if in_child_process:
            # print("Exit procedure due to the child process")
            return False
        
    # Debug mode
    if config['debug']:
        print("Configuration Dictionary:")
        print(config)

    # Callback check
    if not callable(config['task']['callback']):
        exit("Callback function is invalied")

    # Task list to queue
    task_list = []
    user_task_list = config['task']['list']
    if isinstance(user_task_list, list):
        id = 1
        for task in user_task_list:
            data = {
                'id': id,
                'task': task
            }
            task_list.append(data)
            id += 1
    elif isinstance(user_task_list, int):
        for i in range(user_task_list):
            id = i + 1
            data = {
                'id': id,
                'task': {}
            }
            task_list.append(data)

    # Worker dispatch
    worker_num = config['worker']['number']
    worker_num = worker_num if isinstance(worker_num, int) else 1
    worker_per_second = config['worker']['per_second'] if config['worker']['per_second'] else 0
    max_workers = min(len(task_list) if worker_per_second else worker_num, 32766)
    runtime = float(config['runtime']) if config['runtime'] else None
    if config['verbose']:
        print("Worker Dispatcher Configutation:")
        print("- Tasks Count: {}".format(len(task_list)))
        print("- Runtime: {}".format("{} sec".format(runtime) if runtime else "Unlimited"))
        print("- Worker Type:", "Processing" if use_multiprocessing else "Threading")
        print("- Worker Number: {}".format(worker_num))
        print("- Worker Per Second: {}".format(worker_per_second))
        print("- Max Worker: {}".format(max_workers))
    pool_executor_class = concurrent.futures.ProcessPoolExecutor if use_multiprocessing else concurrent.futures.ThreadPoolExecutor
    result_info['started_at'] = time.time()
    datetime_timezone_obj = datetime.timezone(datetime.timedelta(hours=time.localtime().tm_gmtoff / 3600))
    if config['verbose']: print("\n--- Start to dispatch workers at {} ---\n".format(datetime.datetime.fromtimestamp(result_info['started_at'], datetime_timezone_obj).isoformat()))

    # Pool Executor
    with pool_executor_class(max_workers=max_workers) as executor:
        undispatched_tasks_count = 0
        pool_results = []
        per_second_remaining_quota = worker_num
        per_second_remaining_runtime = runtime
        # Task dispatch
        for i, task in enumerate(task_list):
            pool_result = executor.submit(consume_task, task, config)
            pool_results.append(pool_result)
            # Worker per_second setting
            if worker_per_second and (per_second_remaining_quota := per_second_remaining_quota - 1) <= 0:
                if config['worker']['cumulative']:
                    worker_num += worker_per_second
                per_second_remaining_quota = worker_num
                time.sleep(float(worker_per_second))
                # Max Runtime setting
                if runtime and (per_second_remaining_runtime := per_second_remaining_runtime - worker_per_second) <= 0:
                    undispatched_tasks_count = len(task_list) - (i + 1)
                    if config['verbose']: print(f'Dispathcer timeout reached, {undispatched_tasks_count} remaining tasks were abandoned')
                    break

        # Wait for the pool to complete or timeout
        done, not_done = concurrent.futures.wait(
            pool_results,
            timeout=runtime,
            return_when=concurrent.futures.ALL_COMPLETED
        )
        # Cancel remaining tasks if the timeout was reached
        if not_done:
            if config['verbose']: print(f'Dispathcer timeout reached, cancelling {len(not_done)} remaining tasks...')
            for future in not_done:
                future.cancel()

        # Get results from the async results
        for pool_result in concurrent.futures.as_completed(done):
            log = pool_result.result()
            result = log['result']
            if callable(config['task']['result_callback']):
                result = config['task']['result_callback'](config=config['task']['config'], id=log['task_id'], result=log['result'], log=log)
            logs.append(log)
            results.append(result)
        # results = [result.result() for result in concurrent.futures.as_completed(pool_results)]

    result_info['ended_at'] = time.time()
    result_info['duration'] = result_info['ended_at'] - result_info['started_at']
    if config['verbose']:
        print("\n--- End of worker dispatch at {}---\n".format(datetime.datetime.fromtimestamp(result_info['started_at'], datetime_timezone_obj).isoformat()))
        print("Spend Time: {:.6f} sec".format(result_info['duration']))
        print("Completed Tasks Count: {}".format(len(done)))
        print("Uncompleted Tasks Count: {}".format(len(not_done)))
        print("Undispatched Tasks Count: {}".format(undispatched_tasks_count))
    return results

# Worker function
def consume_task(data, config) -> dict:
    started_at = time.time()
    return_value = config['task']['callback'](config=config['task']['config'], id=data['id'], task=data['task'])
    ended_at = time.time()
    duration = ended_at - started_at
    log = {
        'task_id': data['id'],
        'started_at': started_at,
        'ended_at': ended_at,
        'duration': duration,
        'result': return_value
    }
    return log

# TPS report
def get_tps(logs: dict=None, debug: bool=False, peak_duration: float=0, peak_logs: bool=False) -> dict:
    logs = logs if logs else get_logs()
    if not isinstance(logs, list):
        return False
    started_at = 0
    ended_at = 0
    total_count = len(logs)
    invalid_count = 0
    success_count = 0
    success_id_set = set()
    exec_time_sum = 0
    exec_time_max = 0
    exec_time_min = 0
    exec_time_success_sum = 0
    exec_time_success_max = 0
    exec_time_success_min = 0
    # Data processing
    for log in logs:
        if not _validate_log_format(log):
            invalid_count += 1
            continue
        started_at = log['started_at'] if log['started_at'] < started_at or started_at == 0 else started_at
        ended_at = log['ended_at'] if log['ended_at'] > ended_at else ended_at
        exec_time = log['duration'] if 'duration' in log else log['ended_at'] - log['started_at']
        exec_time_sum += exec_time
        exec_time_max = exec_time if not exec_time_max or exec_time > exec_time_max else exec_time_max
        exec_time_min = exec_time if not exec_time_min or exec_time < exec_time_min else exec_time_min
        result = log['result']
        if (isinstance(result, requests.Response) and result.status_code != 200) or not result:
            continue
        success_count += 1
        success_id_set.add(log['task_id'])
        exec_time_success_sum += exec_time
        exec_time_success_max = exec_time if not exec_time_success_max or exec_time > exec_time_success_max else exec_time_success_max
        exec_time_success_min = exec_time if not exec_time_success_min or exec_time < exec_time_success_min else exec_time_success_min
    
    valid_count = total_count - invalid_count
    duration = ended_at - started_at
    exec_time_avg = exec_time_sum / valid_count if exec_time_sum else 0
    exec_time_success_avg = exec_time_success_sum / success_count if exec_time_success_sum else 0
    tps = success_count / duration if success_count else 0

    # Peak TPS
    peak_tps_data = {}
    peak_log_list = []
    if success_count > 0:
        peak_duration = peak_duration if peak_duration else round(exec_time_avg * 3, 2) if (exec_time_avg * 3) >= 1 else 5
        peak_success_count = 0
        peak_ended_at = ended_at
        peak_started_at = peak_ended_at
        if debug:
            print("Peak - vaild count:{}, duration/interval:{}".format(valid_count, peak_duration));
        while peak_started_at > started_at:
            current_count = 0
            current_success_count = 0
            current_invalid_count = 0
            peak_ended_at = peak_started_at
            peak_started_at -= peak_duration
            peak_exec_time_sum = 0
            peak_exec_time_max = 0
            peak_exec_time_min = 0
            peak_exec_time_success_sum = 0
            peak_exec_time_success_max = 0
            peak_exec_time_success_min = 0
            if peak_started_at <= started_at:
                peak_started_at = started_at
                peak_duration = peak_ended_at - peak_started_at
            for log in logs:
                if not _validate_log_format(log):
                    current_invalid_count += 1
                    continue
                if log['started_at'] < peak_started_at or log['ended_at'] > peak_ended_at:
                    continue
                current_count += 1
                exec_time = log['duration'] if 'duration' in log else log['ended_at'] - log['started_at']
                peak_exec_time_sum += exec_time
                peak_exec_time_max = exec_time if not peak_exec_time_max or exec_time > peak_exec_time_max else peak_exec_time_max
                peak_exec_time_min = exec_time if not peak_exec_time_min or exec_time < peak_exec_time_min else peak_exec_time_min
                # Success case
                if log['task_id'] in success_id_set:
                    current_success_count += 1           
                    peak_exec_time_success_sum += exec_time
                    peak_exec_time_success_max = exec_time if not peak_exec_time_success_max or exec_time > peak_exec_time_success_max else peak_exec_time_success_max
                    peak_exec_time_success_min = exec_time if not peak_exec_time_success_min or exec_time < peak_exec_time_success_min else peak_exec_time_success_min
            if debug:
                print("Each Peak - count:{}, start:{}, end:{}".format(current_success_count, peak_started_at, peak_ended_at))

            current_valid_count = current_count - current_invalid_count
            peak_exec_time_avg = peak_exec_time_sum / current_valid_count if peak_exec_time_sum else 0
            peak_exec_time_success_avg = peak_exec_time_success_sum / current_success_count if peak_exec_time_success_sum else 0
            current_tps = current_success_count / peak_duration
            tps_data = {
                'tps': "{:.2f}".format(current_tps, 2),
                'started_at': peak_started_at,
                'ended_at': peak_ended_at,
                'duration': peak_duration,
                'metrics': {
                    'execution_time': {
                        'avg': peak_exec_time_avg,
                        'max': peak_exec_time_max,
                        'min': peak_exec_time_min
                    },
                    'success_execution_time': {
                        'avg': peak_exec_time_success_avg,
                        'max': peak_exec_time_success_max,
                        'min': peak_exec_time_success_min
                    },
                },
                'count': {
                    'success': current_success_count,
                    'total': current_count,
                    'invalidity': current_invalid_count
                },
            }
            peak_log_list.append(tps_data)
            # Find the peak
            if current_success_count and current_success_count > peak_success_count:
                peak_success_count = current_success_count
                if debug:
                    print(" - peak_tps:{}, tps:{}".format(current_tps, tps))
                # Comparing with avg TPS
                if current_tps > tps:
                    peak_tps_data = tps_data

    result = {
        'tps': "{:.2f}".format(tps, 2),
        'started_at': started_at,
        'ended_at': ended_at,
        'duration': duration,
        'metrics': {
            'execution_time': {
                'avg': exec_time_avg,
                'max': exec_time_max,
                'min': exec_time_min
            },
            'success_execution_time': {
                'avg': exec_time_success_avg,
                'max': exec_time_success_max,
                'min': exec_time_success_min
            },
        },
        'count': {
            'success': success_count,
            'total': total_count,
            'invalidity': invalid_count
        },
        'peak': peak_tps_data
    }
    if peak_logs:
        result['peak_logs'] = peak_log_list
    return result

def _validate_log_format(log) -> bool:
    return all(key in log for key in ('started_at', 'ended_at', 'result'))

def get_results() -> list:
    return results

def get_logs() -> list:
    return logs

def get_result_info() -> dict:
    return result_info

def get_duration() -> float:
    return result_info['started_at'] if 'started_at' in result_info else None