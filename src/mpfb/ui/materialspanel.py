from .. import ClassManager
from ..services import UiService
from .abstractpanel import Abstract_Panel

class MPFB_PT_Materials_Panel(Abstract_Panel):
    bl_label = "Materials"
    bl_category = UiService.get_value("MATERIALSCATEGORY")

    def draw(self, context):
        layout = self.layout
        scn = context.scene

ClassManager.add_class(MPFB_PT_Materials_Panel)
