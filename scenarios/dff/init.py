# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

import pydevd_pycharm
pydevd_pycharm.settrace('localhost', port=9090, stdoutToServer=True, stderrToServer=True)

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.runner import get_runner
from cocotb.triggers import RisingEdge
from cocotb.types import LogicArray

from src.runner import run_scenario


@cocotb.test()
async def dff_simple_test(dut):
    """Test that d propagates to q"""

    # Assert initial output is unknown
    assert LogicArray(dut.q.value) == LogicArray("X")
    # Set initial input value to prevent it from floating
    dut.d.value = 0

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    # Synchronize with the clock. This will regisiter the initial `d` value
    await RisingEdge(dut.clk)
    expected_val = 0  # Matches initial input value
    for i in range(10):
        val = random.randint(0, 1)
        dut.d.value = val  # Assign the random value val to the input port d
        dut._log.info(f'new value {val}')
        await RisingEdge(dut.clk)
        assert dut.q.value == expected_val, f"output q was incorrect on the {i}th cycle"
        expected_val = val  # Save random value for next RisingEdge

    # Check the final input on the next clock
    await RisingEdge(dut.clk)
    assert dut.q.value == expected_val, "output q was incorrect on the last cycle"


def run_compile_dff():
    sim = "icarus"
    top_level = 'dff'
    test_module = 'src.compile'

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

    run_scenario(sim, verilog_sources, vhdl_sources, top_level, test_module, '')

def test_simple_dff_runner():
    sim = "icarus"
    top_level = 'dff'
    test_module = 'init'

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

    run_scenario(sim, verilog_sources, vhdl_sources, top_level, test_module, scenario_dir)
