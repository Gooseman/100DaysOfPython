import threading
import time

from constants import WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN
from states import IDLE_STATE, WORK_STATE, SHORT_BREAK_STATE, LONG_BREAK_STATE

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
        if self.state == IDLE_STATE:
            self.state = WORK_STATE
        elif self.state == WORK_STATE:
            self._work_sessions += 1
            # print(f"Work sessions completed: {self._work_sessions}")

            if self._work_sessions % self._num_work_sessions == 0:
                self.state = LONG_BREAK_STATE
            else:
                self.state = SHORT_BREAK_STATE

            self._on_work_session_complete()
        else:
            self.state = WORK_STATE

        self._on_state_change(self.state)

    def _start_timer(self):
        self._end_at = time.time() + self._get_duration()
        self._timer_thread = threading.Thread(target=self._run_timer)
        self._timer_thread.start()
        # self._run_timer()

    def _get_duration(self):
        if self.state == WORK_STATE:
            return WORK_MIN * 60

        if self.state == SHORT_BREAK_STATE:
            return SHORT_BREAK_MIN * 60

        if self.state == LONG_BREAK_STATE:
            return LONG_BREAK_MIN * 60
        # if self.state == work_state:
        #     return 10
        # elif self.state == short_break_state:
        #     return 3
        # elif self.state == long_break_state:
        #     return 5

        return IDLE_STATE

    def _run_timer(self):
        while self.state != IDLE_STATE:
            remaining_time = self._end_at - time.time()
            # print(f"Remaining time: {remaining_time:.2f} seconds")

            if remaining_time <= 0:
                self._update_state()

                if self._work_sessions > 0 and self._work_sessions % self._num_work_sessions == 0:
                    self._work_sessions = 0

                self._start_timer()
                return

            self._update_remaining_time(remaining_time)
            time.sleep(1)

    def reset(self):
        self.state = IDLE_STATE
        self._work_sessions = 0
        self._end_at = None
