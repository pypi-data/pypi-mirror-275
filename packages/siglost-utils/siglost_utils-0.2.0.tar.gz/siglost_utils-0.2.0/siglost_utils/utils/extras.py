import subprocess
from .log_events import error_log, debug_log

class Extras:
    @staticmethod
    def run_command(command, cwd=None, context='', node_id="", show_debug_log=False):
      process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
      output, error = process.communicate()

      if process.returncode != 0:
        error_log(f"Error occurred while {context}: {command} : {error.decode('utf-8')}")
      else:
        conditional_debug_log(f"Output: {output.decode('utf-8')}", node_id, show_debug_log)
