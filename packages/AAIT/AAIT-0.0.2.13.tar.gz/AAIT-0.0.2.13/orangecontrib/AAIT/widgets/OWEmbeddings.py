import os
import sys

import Orange.data
from Orange.widgets import widget
from Orange.widgets.utils.signals import Input, Output
from orangecontrib.AAIT import llm

from PyQt5 import uic
from AnyQt.QtWidgets import QApplication


class OWCreateEmbeddings(widget.OWWidget):
    name = "Create Embeddings"
    description = "Create embeddings on the column 'content' of a Table"
    icon = "icons/owembeddings.svg"
    gui = os.path.join(os.path.dirname(os.path.abspath(__file__)), "designer/owembeddings.ui")
    want_control_area = False

    class Inputs:
        data = Input("Data", Orange.data.Table)

    class Outputs:
        data = Output("Data", Orange.data.Table)

    @Inputs.data
    def set_data(self, in_data):
        self.data = in_data
        self.run()

    def __init__(self):
        super().__init__()

        # Qt Management
        self.setFixedWidth(470)
        self.setFixedHeight(300)
        uic.loadUi(self.gui)

        # Data Management
        self.data = None

    def run(self):
        if self.data is not None:
            out_data = llm.embeddings.create_embeddings(self.data)
        else:
            out_data = None
        self.Outputs.data.send(out_data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_widget = OWCustom()
    my_widget.show()
    app.exec_()
