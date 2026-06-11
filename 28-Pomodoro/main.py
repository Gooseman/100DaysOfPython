from states import idle_state, work_state, short_break_state, long_break_state
from timer import Timer
from ui import PomodoroUI

def on_start():
    print("Start")
    timer.start()

def on_reset():
    print("Reset")
    ui.reset()
    timer.reset()

if __name__ == "__main__":
    ui = PomodoroUI(on_start, on_reset)
    timer = Timer(ui.update_time_remaining, ui.set_state, ui.add_check_mark)

    ui._start_loop()
