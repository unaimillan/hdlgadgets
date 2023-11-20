import cocotb.regression
from cocotb.runner import get_runner


def run_scenario(sim: str, verilog_sources: list[str],
                 vhdl_sources: list[str], hdl_toplevel: str, test_module: str, test_dir):
    runner = get_runner(sim)
    runner.build(
        verilog_sources=verilog_sources,
        vhdl_sources=vhdl_sources,
        hdl_toplevel=hdl_toplevel,
        always=True,
    )
    dt = cocotb.handle._handle2obj
    print(dt)
    runner.test(hdl_toplevel=hdl_toplevel, test_module=test_module, test_dir=test_dir)
