import time
from run import wait_for_log_message


def test_wait_for_log_message_found(tmp_path):
    log = tmp_path / "log.txt"
    log.write_text("hello\nStarting model upload!!\n")
    assert wait_for_log_message(str(log), "Starting model upload!!", timeout=0.1, poll_interval=0.01)


def test_wait_for_log_message_timeout(tmp_path):
    log = tmp_path / "log.txt"
    log.write_text("hello\n")
    assert not wait_for_log_message(str(log), "nope", timeout=0.05, poll_interval=0.01)
