import faulthandler
import os
import signal

os.environ["PYAPPIFY_PYTHON_TEST"] = "1"

# Dump Python stacks on fatal signals (same as main.py).
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
    config['debug'] = True
    # config['click_screenshots_folder'] = "click_screenshots"  # debug用 点击后截图文件夹]
    ok = OK(config)
    ok.start()
