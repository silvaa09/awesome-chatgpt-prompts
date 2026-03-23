"""Streamlit UI for BitLab QA Trainer."""

from __future__ import annotations

import textwrap
import time

import streamlit as st

from bitlab_qa_trainer.bit_engine import check_bit, flip_bit, reverse_bits
from bitlab_qa_trainer.challenge_engine import run_challenge
from bitlab_qa_trainer.debug_mode import debug_challenge
from bitlab_qa_trainer.fundamentals import get_fundamentals_content
from bitlab_qa_trainer.interview import generate_interview
from bitlab_qa_trainer.scenarios import evaluate_answer, generate_scenario
from bitlab_qa_trainer.visualizer import visualize_bit_operation


st.set_page_config(page_title="BitLab QA Trainer", layout="wide")
st.title("BitLab QA Trainer")

mode = st.sidebar.selectbox(
    "Choose Mode",
    [
        "Python Fundamentals",
        "Bit Manipulation Lab",
        "System Scenarios (QA/DPU)",
        "Interview Mode",
        "Debug & Fix Mode",
    ],
)

if mode == "Python Fundamentals":
    st.header("Python Fundamentals")
    content = get_fundamentals_content()
    topic = st.selectbox("Topic", list(content.keys()))
    card = content[topic]
    st.markdown(f"**Scenario**: {card['scenario']}")
    st.code(card["example"], language="python")
    st.markdown(f"**Exercise**: {card['exercise']}")
    with st.expander("Show Solution"):
        st.code(card["solution"], language="python")

elif mode == "Bit Manipulation Lab":
    st.header("Bit Manipulation Lab")
    col1, col2, col3 = st.columns(3)
    num = col1.number_input("Number", min_value=0, value=10, step=1)
    n = col2.number_input("Bit Position", min_value=0, value=1, step=1)
    operation = col3.selectbox("Operation", ["flip", "reverse", "check"])

    if st.button("Run Bit Operation"):
        if operation == "flip":
            result = flip_bit(int(num), int(n))
        elif operation == "reverse":
            result = reverse_bits(int(num), bits=max(4, int(num).bit_length()))
        else:
            result = check_bit(int(num), int(n))

        st.write(f"Result: **{result}**")
        st.text(visualize_bit_operation(int(num), operation, int(n)))

elif mode == "System Scenarios (QA/DPU)":
    st.header("System Scenarios")
    if "scenario" not in st.session_state:
        st.session_state.scenario = generate_scenario()

    scenario = st.session_state.scenario
    st.subheader(scenario["name"])
    st.json(scenario["logs"])
    st.write(scenario["question"])

    user_answer = st.text_area("Your Root Cause Analysis")
    if st.button("Evaluate Scenario"):
        evaluation = evaluate_answer(user_answer, scenario["keywords"])
        st.write(f"Passed: **{evaluation['passed']}**")
        st.write(f"Score: **{evaluation['score']}**")
        st.write(f"Matched keywords: {', '.join(evaluation['matched_keywords']) or 'None'}")
        st.info(f"Reference answer: {scenario['answer']}")

    if st.button("New Scenario"):
        st.session_state.scenario = generate_scenario()
        st.experimental_rerun()

elif mode == "Interview Mode":
    st.header("Interview Mode")
    questions = generate_interview()

    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    elapsed = int(time.time() - st.session_state.start_time)
    st.metric("Timer (seconds)", elapsed)

    system_answer = st.text_area("System Question", questions["system"])
    coding_answer = st.text_area("Coding Question", questions["coding"])
    debugging_answer = st.text_area("Debugging Question", questions["debugging"])

    if st.button("Score Interview"):
        score = sum(
            bool(ans.strip())
            for ans in [system_answer, coding_answer, debugging_answer]
        ) * 33
        st.success(f"Interview score: {min(score, 100)}/100")

else:
    st.header("Debug & Fix Mode")
    broken = st.text_area(
        "Paste buggy code",
        textwrap.dedent(
            """
            def flip_bit(num, n):
                return num & (1 << n)
            """
        ).strip(),
        height=160,
    )

    if st.button("Analyze Bug"):
        result = debug_challenge(broken)
        st.error(result["issue"])
        st.info(result["fix"])
        st.code(result["corrected_code"], language="python")

st.caption("Sample outputs: flip_bit(10,1)=8, reverse_bits(13,8)=176, check_bit(10,1)=1")

if st.checkbox("Run quick coding challenge sample"):
    sample = "print(2 + 3)"
    challenge_result = run_challenge(sample, "5")
    st.json(challenge_result)
