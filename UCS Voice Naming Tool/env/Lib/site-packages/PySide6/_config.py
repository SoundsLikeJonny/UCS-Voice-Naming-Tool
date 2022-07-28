built_modules = list(name for name in
    "Core;Gui;Widgets;PrintSupport;Sql;Network;Test;Concurrent;Designer;Xml;Help;Multimedia;MultimediaWidgets;OpenGL;OpenGLWidgets;Positioning;NetworkAuth;Nfc;Qml;Quick;Quick3D;QuickControls2;QuickWidgets;RemoteObjects;Scxml;Sensors;SerialPort;StateMachine;Charts;Svg;SvgWidgets;DataVisualization;Bluetooth;UiTools;AxContainer;WebChannel;WebEngineCore;WebEngineWidgets;WebEngineQuick;WebSockets;3DCore;3DRender;3DInput;3DLogic;3DAnimation;3DExtras"
    .split(";"))

shiboken_library_soversion = str(6.3)
pyside_library_soversion = str(6.3)

version = "6.3.1"
version_info = (6, 3, 1, "", "")

__build_date__ = '2022-06-14T06:53:31+00:00'




__setup_py_package_version__ = '6.3.1'
