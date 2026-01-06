from .. import ClassManager
from ..services import UiService
from .abstractpanel import Abstract_Panel

class MPFB_PT_New_Panel(Abstract_Panel):
    bl_label = "New Human"
    bl_category = UiService.get_value("MODELCATEGORY")

    def draw(self, context):
        layout = self.layout
        scn = context.scene

ClassManager.add_class(MPFB_PT_New_Panel)
