import threading
import time

from constants import WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN
from states import idle_state, work_state, short_break_state, long_break_state

class Timer:
    _num_work_sessions = 4

    # pass in a method to update the remaining time
    def __init__(self, update_remaining_time, on_state_change, on_work_session_complete):
        self.reset()
        self._update_remaining_time = update_remaining_time
        self._on_state_change = on_state_change
        self._on_work_session_complete = on_work_session_complete
        self._timer_thread = None

    def start(self):
        self._update_state()
        self._start_timer()

    def _update_state(self):
        if self.state == idle_state:
            self.state = work_state
        elif self.state == work_state:
            self._work_sessions += 1
            # print(f"Work sessions completed: {self._work_sessions}")

            if self._work_sessions % self._num_work_sessions == 0:
                self.state = long_break_state
            else:
                self.state = short_break_state
            
            self._on_work_session_complete()
        else:
            self.state = work_state

        self._on_state_change(self.state)

    def _start_timer(self):
        self._end_at = time.time() + self._get_duration()
        self._timer_thread = threading.Thread(target=self._run_timer)
        self._timer_thread.start()
        # self._run_timer()

    def _get_duration(self):
        if self.state == work_state:
            return WORK_MIN * 60
        elif self.state == short_break_state:
            return SHORT_BREAK_MIN * 60
        elif self.state == long_break_state:
            return LONG_BREAK_MIN * 60
        # if self.state == work_state:
        #     return 10
        # elif self.state == short_break_state:
        #     return 3
        # elif self.state == long_break_state:
        #     return 5

    def _run_timer(self):
        while self.state != idle_state:
            remaining_time = self._end_at - time.time()
            # print(f"Remaining time: {remaining_time:.2f} seconds")

            if remaining_time <= 0:
                self._update_state()

                if self._work_sessions > 0 and self._work_sessions % self._num_work_sessions == 0:
                    self._work_sessions = 0

                self._start_timer()
                return
            else:
                self._update_remaining_time(remaining_time)
            
            time.sleep(1)

    def reset(self):
        self.state = idle_state
        self._work_sessions = 0
        self._end_at = None
