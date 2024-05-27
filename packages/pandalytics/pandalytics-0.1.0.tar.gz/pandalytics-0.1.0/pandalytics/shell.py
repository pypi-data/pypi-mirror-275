import subprocess
import threading
import time


class PythonShell:
    def __init__(self):
        self.process = None
        self.output = ""
        self.error = ""

    def execute_code(self, code):
        try:
            self.process = subprocess.Popen(
                ["python", "-c", code],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                shell=False,
            )
            self._capture_output()
            self.process.wait()
        except Exception as e:
            print(f"Error executing command: {e}")

    def _capture_output(self):
        self.output, self.error = self.process.communicate()

    def get_output(self):
        return self.output

    def get_error(self):
        return self.error
