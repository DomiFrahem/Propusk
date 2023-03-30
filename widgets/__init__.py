from .PStackedWidget import *
from .PLineEdit import *
from .PCamChecked import *



def create_widget_cam_shecked(obj, layout, name_object: str, mode: str = 'video', ) -> PCamChecked:
    widget = PCamChecked(obj, mode=mode)
    widget.setObjectName(name_object)
    layout.addWidget(widget)
    return widget
    
def create_widget_stacked(obj, layout, name_object: str,  mode: str = 'video') -> PStackedWidget:
    widget = PStackedWidget(obj, mode=mode)
    widget.setObjectName(name_object)
    layout.addWidget(widget)
    return widget