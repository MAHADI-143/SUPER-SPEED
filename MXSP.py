import os, sys
try:
    __import__("MAHADI").__mahadi()
except Exception as e:
    exit(str(e))
