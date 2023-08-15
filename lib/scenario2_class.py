import curses
from lib.common.scenariotop_class import scenariotop
from lib.gadgets.gadget_fifo_class import gadget_fifo
from lib.gadgets.gadget_fifotr_class import gadget_fifotr
from lib.gadgets.gadget_modelqueue_class import gadget_modelqueue
from lib.gadgets.gadget_check_class import gadget_check
from lib.gadgets.gadget_control_class import gadget_control
from lib.gadgets.gadget_fplate_sc2_class import gadget_fplate_sc2

class scenario2(scenariotop):

        def __init__(self):
                super().__init__()
                self._fifo = gadget_fifo()
                self._fifotr = gadget_fifotr()
                self._modelqueue = gadget_modelqueue()
                self._check = gadget_check()
                self._control = gadget_control()
                self._fplate = gadget_fplate_sc2()

        def __del__(self):
                del self._fifo
                del self._fifotr
                del self._modelqueue
                del self._check
                del self._control
                del self._fplate
                super().__del__()

        def setup_2d_model (self, ctx):
                #IN 3D VERSION THIS METHOD WILL BE USED TO PROVIDE 3D MODEL MESH, IN 2D THERE IS ONLY SUBWINDOW LAYOUTS
                self._ctx = ctx

                self._fifo.setup_2d_model(self._ctx.subwin(3, 5))
                self._fifotr.setup_2d_model(self._ctx.subwin(3, 5))
                self._modelqueue.setup_2d_model(self._ctx.subwin(3, 60))
                self._check.setup_2d_model(self._ctx.subwin(16, 71))
                self._control.setup_2d_model(self._ctx.subwin(20, 5))
                self._fplate.setup_2d_model(self._ctx.subwin(0, 0))

        def process_input_stimulus (self, hdl, key):
                self._fifo.process_input_stimulus (hdl, key)
                self._fifotr.process_input_stimulus (hdl, key)
                self._modelqueue.process_input_stimulus (hdl, key)
                self._check.process_input_stimulus (hdl, key)
                self._control.process_input_stimulus (hdl, key)
                self._fplate.process_input_stimulus (hdl, key)

        def get_logic_state_data_from_simulator (self, hdl):
                self._fifo.get_logic_state_data_from_simulator (hdl.RTL1.FIFO1)
                self._fifotr.get_logic_state_data_from_simulator (hdl.RTL1.FIFO1)
                self._modelqueue.get_logic_state_data_from_simulator (hdl.MDL1)
                self._check.get_logic_state_data_from_simulator (hdl.CHK1)
                self._control.get_logic_state_data_from_simulator (hdl)
                self._fplate.get_logic_state_data_from_simulator (hdl)

        def post_process_logic_state (self, phase):
                self._fifo.post_process_logic_state (phase)
                self._fifotr.post_process_logic_state (phase)
                self._modelqueue.post_process_logic_state (phase)
                self._check.post_process_logic_state (phase)
                self._control.post_process_logic_state (phase)
                self._fplate.post_process_logic_state (phase)

        def write_to_log (self, logfile):
                self._fifo.write_to_log ("FIFO1", logfile)
                self._fifotr.write_to_log ("FIFOTR1", logfile)
                self._modelqueue.write_to_log ("MDLQ1", logfile)
                self._check.write_to_log ("CHK1", logfile)
                self._control.write_to_log ("CONTROL", logfile)
                self._fplate.write_to_log ("FPLATE", logfile)

        def drive_2d_model (self):
                self._fifo.drive_2d_model ()
                self._fifotr.drive_2d_model ()
                self._modelqueue.drive_2d_model ()
                self._check.drive_2d_model ()
                self._control.drive_2d_model ()
                self._fplate.drive_2d_model ()
