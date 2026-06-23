import time
from random import randint
from rich import print as rpn
from rich.progress import Progress
from rich.console import Console
console = Console()
progress = Progress(transient=True)
# progress.set_spinner('dots', spinner_style='progress.spinner', speed=1.0)
# progress.start()
try:
    # task1 = progress.add_task("[red]Downloading...", total=1000)
    task2 = progress.add_task("[green]Выполнено...",total=100)
    # task3 = progress.add_task("[cyan]Cooking...", total=1000)
    progress.start()
    rpn(b := randint(1,10))
    for i in range(0,100):
    # while not progress.finished:
        a = int(i/10)
        if not i%10:
            rpn(f'step {a+1:2}')
            if a+1 == b:break
        progress.update(task2, advance=1)
        # progress.update(task3, advance=0.9)
        time.sleep(1)

finally:
    progress.stop()
rpn('Вот и промчался карнавал,\n где маски пляшут и вуаль')
console.input(' [b]:-)> ')
