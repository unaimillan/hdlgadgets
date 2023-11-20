import cocotb
from lib.common.program_class import program
from lib.scenario1_class import scenario1


# import pydevd_pycharm
# pydevd_pycharm.settrace('localhost', port=9090, stdoutToServer=True, stderrToServer=True)

@cocotb.test()
async def my_first_test(hdl):
    scenario = scenario1()
    prog = program(hdl, scenario)
    #prog.logtofile("logfile.txt")
    await prog.run()
    del prog
    del scenario
