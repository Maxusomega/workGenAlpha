#Matthew Cole
#Storage tester

import storeWk as st
import algoImp as a



wk = a.workoutGen()
wkls = None
while(True):
    try:
        wkls = wk.generator("swim")
        break
    except:
        pass

wk1,wk2 = wk.formatter(wkls.wk)

arch = st.archive()

arch.archive(wk1,wk2,"swsmatthew@gmail.com")

wk1,wk2 = arch.get("swsmatthew@gmail.com")

print(wk1)
print()
print(wk2)