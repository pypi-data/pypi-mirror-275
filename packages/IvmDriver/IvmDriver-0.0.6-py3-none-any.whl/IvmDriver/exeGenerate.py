import cx_Freeze, sys

base = None
inlude_packages = []
with open('./requirements.txt','r') as file :
    inlude_packages = [i.strip('\n').strip() for i in file.readlines() ]
    
if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("mainDriver.py", base=base, icon='assets/logo.ico')]

cx_Freeze.setup(
    name="Matrix",
    options={"build_exe": {"packages": [], "include_files": [
        "styles","assets"
    ]}},
    version="1.0",
    description="mainDriver",
    executables=executables
)