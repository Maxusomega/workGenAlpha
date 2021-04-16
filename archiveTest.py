#Matthew Cole
#Storage tester

import storeWk as st
import algoImp as a

"""

wk = a.workoutGen()
wkls = None
while(True):
    try:
        wkls = wk.generator("baseball")
        break
    except:
        pass

wk1,wk2 = wk.formatter(wkls.wk)

arch = st.archive()

arch.archive(wk1,wk2,"test@gmail.com")
"""

arch = st.archive()
wk1,wk2 = arch.get("test@gmail.com")

print(wk1)
print()
print(wk2)
print()
print("adding value to workout")
arch.adjustWeight("test@gmail.com",0,0,69)
arch.adjustWeight("test@gmail.com",0,1,42)
arch.adjustWeight("test@gmail.com",0,2,"hello")

wk1,wk2 = arch.get("test@gmail.com")

print(wk1)
print()
print(wk2)
