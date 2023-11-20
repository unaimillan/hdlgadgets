from src.runner import run_scenario
import os
from pathlib import Path


def run_scenario_1():
    sim = "icarus"

    top_level = 'tb'
    test_py = '/home/user/digital-circuit-design/unaimillan-hdlgadgets/init_scenario1.py'

    scenario_dir = Path(__file__).resolve().parent
    print('proj path:', scenario_dir)

    verilog_sources = []
    vhdl_sources = []

    scenario_verilog = scenario_dir / "verilog"
    scenario_vhdl = scenario_dir / "vhdl"

    if scenario_verilog.exists():
        # TODO: Replace with proper pattern
        verilog_sources += list(scenario_verilog.glob("*"))

    if scenario_vhdl.exists():
        # TODO: Replace with proper pattern
        vhdl_sources += list(scenario_vhdl.glob("*"))

    assert len(verilog_sources+vhdl_sources) > 0, "No HDL sources provided"

    run_scenario(sim, verilog_sources, vhdl_sources, top_level, test_py)
