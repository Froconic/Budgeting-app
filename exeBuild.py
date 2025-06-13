import PyInstaller.__main__


PyInstaller.__main__.run([
    'budget.py',
    '--noconfirm',
    '--onedir',
    '--windowed',
    '--icon=CustomTkinter_icon_Windows.ico',
    '--add-data=C:/Users/akira/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0/LocalCache/local-packages/Python313/site-packages/customtkinter;budget.py',
    '--add-data=CustomTkinter_icon_Windows.ico;budget.py/assets/icons',
])