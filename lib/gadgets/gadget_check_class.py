import curses
from lib.common.gadgettop_class import gadgettop
from lib.common.helper_class import helper

class gadget_check(gadgettop):

        def __init__(self):
                super().__init__()

                #Logic state
                self.logicstate_pre = {'rtl_data':[None,None,None,None,None,None], 'rtl_valid':[None], 'model_data':[None,None,None,None,None,None]}
                self.logicstate_post = {'rtl_data':[None,None,None,None,None,None], 'rtl_valid':[None], 'model_data':[None,None,None,None,None,None]}

                #Check state
                self.checkstate_pre = {'no_match':[None]}
                self.checkstate_post = {'no_match':[None]}

        def __del__(self):
                super().__del__()

        def setup_2d_model (self, wctx):
                self._wctx = wctx
                self._wctx.erase()
                self._wctx.bkgd(' ', curses.color_pair(1))
                self._wctx.refresh()

        def process_input_stimulus (self, hdlpath, key):
                pass

        def get_logic_state_data_from_simulator (self, hdlpath):
                #Copy post logic state into pre logic state
                helper.dictcopy(self.logicstate_post, self.logicstate_pre)

                helper.put_hdl_vector_to_dict(self.logicstate_post['rtl_data'], hdlpath.rtl_data.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['rtl_valid'], hdlpath.rtl_valid.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['model_data'], hdlpath.model_data.value.binstr)

        def post_process_logic_state (self, phase):
                #Copy post transaction state into pre transaction state
                helper.dictcopy(self.checkstate_post, self.checkstate_pre)

                if (self.logicstate_post['rtl_valid'][0] == '1' and self.logicstate_post['rtl_data'] != self.logicstate_post['model_data']):
                    self.checkstate_post['no_match'][0] = '1'
                else:
                    self.checkstate_post['no_match'][0] = '0'


        def write_to_log (self, strprefix, logfile):
                logfile.write(strprefix + ", logicstate_pre:" + str(self.logicstate_pre) + "\n")
                logfile.write(strprefix + ", checkstate_pre:" + str(self.checkstate_pre) + "\n")

                logfile.write(strprefix + ", logicstate_post:" + str(self.logicstate_post) + "\n")
                logfile.write(strprefix + ", checkstate_post:" + str(self.checkstate_post) + "\n")

        def drive_2d_model (self):
                ####BASE####
                ###########################0#####1#####2#####3#####4#####5#####6#####7#####8#####9#####10####11####12####13####14####
                self._wctx.addstr(0,0,  u'\u250C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(1,0,  u'\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(2,0,  u'\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518'.encode('utf-8'), curses.color_pair(1))
                if (self.checkstate_post['no_match'][0] == '1'):
                    self._wctx.addstr(1,2,  u'\u004E\u004F\u005F\u004D\u0041\u0054\u0043\u0048\u0021\u0021\u0021'.encode('utf-8'), curses.color_pair(4))
                else:
                    self._wctx.addstr(1,2,  u'\u002D\u002D\u002D\u002D\u002D\u002D\u002D\u002D\u002D\u002D\u002D'.encode('utf-8'), curses.color_pair(1))

                self._wctx.refresh()
