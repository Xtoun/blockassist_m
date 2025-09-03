from pathlib import Path


def test_train_blockassist_script_last_line():
    script = Path(__file__).resolve().parents[1] / 'scripts' / 'train_blockassist.sh'
    lines = [line.strip() for line in script.read_text().splitlines() if line.strip()]
    assert lines[-1] == 'python -m blockassist.launch +stages=[train,upload_model] > logs/blockassist-train.log 2>&1'
