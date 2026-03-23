# BitLab QA Trainer

BitLab QA Trainer is a modular Python + Streamlit training platform focused on:

- Python fundamentals
- Bit manipulation
- QA/system scenarios
- Interview preparation
- Debugging practice

## Project Structure

- `bit_engine.py` – core helper engine (`flip_bit`, `reverse_bits`, `check_bit`, `reverse_number`)
- `visualizer.py` – bit-level operation visualizations
- `fundamentals.py` – topic cards (scenario/example/exercise/solution)
- `challenge_engine.py` – safe-ish coding challenge runner
- `scenarios.py` – scenario generator + answer evaluator
- `interview.py` – interview question generation and scoring support
- `debug_mode.py` – debugging challenge analyzer and suggested fixes
- `app.py` – Streamlit UI with 5 modes
- `tests/` – pytest coverage

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install streamlit pytest
```

## Run

```bash
streamlit run bitlab_qa_trainer/app.py
```

## Run tests

```bash
pytest bitlab_qa_trainer/tests -q
```

## Required sample outputs

```text
flip_bit(10,1) -> 8
reverse_bits(13,8) -> 176
check_bit(10,1) -> 1
reverse_number(1234) -> 4321
```

## Sample usage

```python
from bitlab_qa_trainer.bit_engine import flip_bit, reverse_bits, check_bit, reverse_number
from bitlab_qa_trainer.visualizer import visualize_bit_operation

print(flip_bit(10, 1))                  # 8
print(reverse_bits(13, 8))              # 176
print(check_bit(10, 1))                 # 1
print(reverse_number(1234))             # 4321
print(visualize_bit_operation(10, "flip", 1))
```
