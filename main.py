from pyteal import *


program = App.globalPut(Bytes("Teepy"), Int(50))

print(compileTeal(program, Mode.Application))