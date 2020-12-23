# サブパッケージからインポートする場合の記述例
# https://note.nkmk.me/python-relative-import/
from .samplepackage import *

if __name__ == '__main__':
    samplemodule.samplefanc()
