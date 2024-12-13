"""
qdarkstyle theme doc
https://qdarkstylesheet.readthedocs.io/en/stable/index.html#

QTStyle doc
https://doc.qt.io/qtforpython-6/tutorials/basictutorial/widgetstyling.html
"""

import qdarkstyle  # type: ignore
from variables import (
    PRIMARY_COLOR, DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR
)

qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
        border-radius: 5px;
        font-weight: 600;
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""


def setupTheme(app):
    # Aplica o estilo escuro do qdarkstyle
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

    # Sobrepõe o QSS personalizado para estilização adicional
    app.setStyleSheet(app.styleSheet() + qss)
