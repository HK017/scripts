from easydict import EasyDict as edict
import os

__C = edict()

__C.ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
__C.DATA_DIR = os.path.abspath(os.path.join(__C.ROOT_DIR, 'data'))


print(__C)
print(os.path.join(os.path.dirname(__file__)))
print(os.path.join(os.path.dirname(__file__), '..', '..'))