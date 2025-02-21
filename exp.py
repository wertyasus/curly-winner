import time
import sys

def progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()

total_time_seconds = 20 * 60  # 20 минут
for i in range(total_time_seconds):
    progress_bar(i + 1, total_time_seconds, prefix="Загрузка:", suffix="Complete", length=50)
    time.sleep(1)

print("\n[+] Процесс не был завершен, клиент не зашел в чат пожалуйста повторите")
