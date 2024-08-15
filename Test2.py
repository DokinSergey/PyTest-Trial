import pywmitool
from rich import print#,inspect

pywmitool -q "SELECT Name FROM Win32_OperatingSystem"
