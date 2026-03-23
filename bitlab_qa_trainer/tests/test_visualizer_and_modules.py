from bitlab_qa_trainer.challenge_engine import run_challenge
from bitlab_qa_trainer.debug_mode import debug_challenge
from bitlab_qa_trainer.fundamentals import get_fundamentals_content
from bitlab_qa_trainer.scenarios import evaluate_answer
from bitlab_qa_trainer.visualizer import visualize_bit_operation


def test_visualize_flip():
    output = visualize_bit_operation(10, "flip", 1)
    assert "Original:" in output
    assert "Result:" in output
    assert "1000" in output


def test_run_challenge_success():
    result = run_challenge("print(2 + 2)", "4")
    assert result["passed"] is True
    assert result["error"] == ""


def test_run_challenge_disallowed_import():
    result = run_challenge("import os\nprint('x')", "x")
    assert result["passed"] is False
    assert "Disallowed syntax" in result["error"]


def test_evaluate_answer_pass():
    result = evaluate_answer("This points to queue overflow and cpu bottleneck", ["queue", "cpu", "bottleneck"])
    assert result["passed"] is True


def test_debug_challenge_fix():
    broken = "def flip_bit(num, n):\n    return num & (1 << n)"
    result = debug_challenge(broken)
    assert "XOR" in result["fix"]
    assert "^" in result["corrected_code"]


def test_fundamentals_topics_present():
    content = get_fundamentals_content()
    for topic in ["data_types", "operators", "data_structures", "control_flow", "functions", "io", "error_handling"]:
        assert topic in content
        assert set(content[topic].keys()) == {"scenario", "example", "exercise", "solution"}
