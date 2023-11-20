import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.font_registry():
    default_font = dpg.add_font("fonts/JetBrainsMono-Regular.ttf", 18)
    dpg.bind_font(default_font)

with dpg.window(tag="Primary Window"):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

with dpg.window(tag='graph'):
    dpg.add_plot(parent='graph', no_menus=True)

dpg.create_viewport(title='Custom Title', width=1280, height=720)
dpg.show_font_manager()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
