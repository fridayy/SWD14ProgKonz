#!/usr/bin/env python3
# Benjamin 'bnjm ' Krenn [krennben14]
name = "krennben14"

f = open("ex01_{}.out".format(name), "w")
f.write("A first python3 script by '{0}':\nMy uppercase login name is: "
        "'{1}'.\nDone!".format(name, name.upper()))
f.close()
