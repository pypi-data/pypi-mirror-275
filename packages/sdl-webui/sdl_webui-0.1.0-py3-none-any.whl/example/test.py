import logging
logger = logging.getLogger(__name__)
a = 12

class StandardCurve:
    def __init__(self):
        pass

    def test1(self):
        pass

class Solubility:
    def __init__(self):
        pass
    def test1(self):
        pass
class Reslurry:
    def __init__(self):
        pass
    def test1(self):
        pass

class Cooling_Crystal:
    def __init__(self):
        pass
    def test1(self, temp:int, vial, bool_test:bool):
        logger.info(f'Executing {temp} with {vial}')

cooling_crystal = Cooling_Crystal()
reslurry = Reslurry()
solubility = Solubility()
standard_curve = StandardCurve()
# vial

if __name__ == "__main__":
    from sdl_webui.app import start_gui
    # gui_functions = ["cooling_crystal"]
    start_gui(__name__)
