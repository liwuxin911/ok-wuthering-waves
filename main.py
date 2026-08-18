import faulthandler
import os
import signal

# Dump Python stacks to a file on fatal signals (e.g. a native access
# violation in a graphics backend) instead of the process dying silently.
# pythonw.exe has no console, so write to the logs folder explicitly.
_fault_log = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs', 'ok-ww_fault.log')
try:
    os.makedirs(os.path.dirname(_fault_log), exist_ok=True)
    _fault_file = open(_fault_log, 'a', encoding='utf-8')
    faulthandler.enable(file=_fault_file)
    faulthandler.register(signal.SIGSEGV, file=_fault_file)
except Exception:
    try:
        faulthandler.enable()
    except Exception:
        pass


if __name__ == '__main__':
    from config import config
    from ok import OK

    config = config
    ok = OK(config)
    ok.start()
