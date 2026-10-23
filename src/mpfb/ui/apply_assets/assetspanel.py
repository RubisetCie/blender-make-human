"""This is the root panel for the asset library."""

from ... import ClassManager
from ...services import UiService
from ...services import AssetService
from ..abstractpanel import Abstract_Panel
from ..systemassets import get_system_assets_status, get_system_assets_lines, STATUS_OK
from ...services import SceneConfigSet

FILTER_PROPERTIES = SceneConfigSet([
    {
    "type": "string",
    "name": "filter",
    "description": "Only list assets with this term in the title",
    "label": "Title must contain",
    "default": ""
    },
    {
    "type": "string",
    "name": "packname",
    "description": "Only list assets belonging to an asset pack matching this name",
    "label": "Pack name must contain",
    "default": ""
    },
    {
    "type": "boolean",
    "name": "only_equipped",
    "description": "Only show assets which are currently equipped",
    "label": "Only equipped",
    "default": False
    }
    ], 'APAS_')

class MPFB_PT_Assets_Panel(Abstract_Panel):
    bl_label = "Apply Assets"
    bl_category = UiService.get_value("MATERIALSCATEGORY")
    bl_order = 40

    def system_assets(self, layout):
        status = get_system_assets_status()
        if status == STATUS_OK:
            return
        box = layout.box()
        box.label(text="System Assets Status:")
        box.label(text=get_system_assets_lines(status))

    def draw(self, context):
        layout = self.layout

        self.system_assets(layout)

        box = layout.box()
        box.label(text="Filter")
        show_props = ["filter"]
        if AssetService.get_pack_names():
            show_props.append("packname")
        show_props.append("only_equipped")
        FILTER_PROPERTIES.draw_properties(context.scene, box, show_props)

ClassManager.add_class(MPFB_PT_Assets_Panel)
