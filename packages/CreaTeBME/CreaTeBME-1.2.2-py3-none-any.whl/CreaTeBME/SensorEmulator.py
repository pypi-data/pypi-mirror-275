import json
import copy
import time
import warnings
from threading import Timer, Lock
from typing import Callable, Dict, List


class SensorEmulator:
    """
    An emulator for the SensorManager that reads from a recording file instead.
    """
    def __init__(self, filename: str, loop: bool = False):
        """
        Construct a SensorEmulator

        :param filename: The name of the recording file
        :param loop: Whether to loop the recorded data when it finishes
        """
        with open(filename+'.tb', 'r') as f:
            text_content = f.read()
        text_data = json.loads(text_content)
        self._sample_rate: int = text_data['sample_rate']
        self._recorded_data: Dict[str, List[float]] = text_data['data']
        self._data = copy.deepcopy(self._recorded_data)
        self._loop = loop
        self._lock = Lock()
        self._timer = None
        self._queue = {name: [] for name in self._data.keys()}
        self._callback = None
        self._is_running = False

        self._start_time = None
        self._counter = 0

    def start(self) -> None:
        """
        Start the SensorEmulator
        """
        self._timer = Timer(1/self._sample_rate, self._step)
        self._timer.start()
        self._is_running = True
        self._start_time = time.perf_counter()
        self._counter = 0

    def stop(self) -> None:
        """
        Stop the SensorEmulator
        """
        self._timer.cancel()
        self._is_running = False

    def is_running(self) -> bool:
        """
        Check whether the SensorEmulator is running.
        :return: Boolean representing the running state of the SensorEmulator.
        """
        return self._is_running

    def get_measurements(self) -> Dict[str, List[List[float]]]:
        """
        Get the measurements since the last time this method was called.

        :return: A dictionary containing a list of measurements for each sensor
        """
        with self._lock:
            queue_copy = copy.deepcopy(self._queue)
            for sensor in self._queue.values():
                sensor.clear()
            return queue_copy

    def set_callback(self, callback: Callable[[str, List[float]], None]) -> None:
        """
        Set a callback to be run when a sensor measurement comes in.

        :param callback: A callback function that takes the sensor name and sensor measurement
        """
        self._callback = callback

    def set_sample_rate(self, sample_rate: int) -> None:
        """
        Not implemented.

        :param sample_rate: The sample frequency
        """
        warnings.warn(f"Emulating sensor, using recorded sample rate of {self._sample_rate}Hz.", RuntimeWarning)

    def record(self) -> None:
        """
        Not implemented
        """
        warnings.warn(f"Emulating sensor, recording not supported.", RuntimeWarning)

    def _step(self):
        self._counter += 1
        self._timer = Timer((self._start_time + self._counter * 1 / self._sample_rate) - time.perf_counter(), self._step)
        self._timer.start()
        with self._lock:
            for name in self._data.keys():

                if len(self._data[name]) < 1:
                    if self._loop:
                        self._data = copy.deepcopy(self._recorded_data)
                    else:
                        self.stop()
                        return

                data = self._data[name].pop()
                self._queue[name].append(data)
                if self._callback:
                    self._callback(name, data)



