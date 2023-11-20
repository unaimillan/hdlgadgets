import json

import cocotb
from mypy.stubgen import generate_stub_for_py_module, StubSource

# DO NOT WORK, because HierarchyObject is not directly convertable to json

print('module:', cocotb.top)
json.dump(cocotb.top, open('top.json', 'w'))
