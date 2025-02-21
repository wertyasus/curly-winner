\from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.panel import Panel
from rich.console import Console
import time
import random

# Создание консоли
console = Console()

# Текст, который будет выводиться во время выполнения
texts = [
    "install geo.hs",
    "Настройка локального хранилища",
    "install org/",
    "Установка дополнительных инструментов для exploit-DB",
    "Установка дополнительных инструментов для удаленного подключения",
    "Инициализирую ifconfig",
    "Настройка arch-repo",
    "Установка TCP подключения",
    "install exploit-AH",
    "Проверка на наличие exploit"
]

def main():
    # Общее время выполнения в секундах (20 минут)
    total_time_seconds = 20 * 60
    
    # Создание индикатора прогресса
    with Progress(
        SpinnerColumn(),  # Анимация спиннера
        "[progress.description]{task.description}",
        BarColumn(),      # Прогресс-бар
        "[progress.percentage]{task.percentage:>3.0f}%",
        transient=True     # Индикатор исчезает после завершения
    ) as progress:
        task = progress.add_task("[cyan]Инициализация системы...", total=total_time_seconds)

        for i in range(total_time_seconds):
            # Обновление прогресса
            progress.update(task, advance=1)
            
            # Вывод случайного текста каждые 5 секунд
            if i % 5 == 0:  # Каждые 5 секунд
                console.print(Panel.fit(random.choice(texts), style="bold green"))
            
            # Имитация работы (пауза в 1 секунду)
            time.sleep(1)

    console.print("\n[bold magenta]Процесс не был завершен второй пользователь не открыл чат пожалуйста повторите[/bold magenta]")

if __name__ == "__main__":
    main()
