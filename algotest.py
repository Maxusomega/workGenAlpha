#algorithm tester
#MAtthew Cole

import algoImp as al
wk = al.workoutGen()

wkls = None
while(True):
    try:
        wkls = wk.generator("none","3")
        break
    except:
        pass

print(wk.formatter(wkls.wk))