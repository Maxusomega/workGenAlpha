#MAtthew Cole
#workout array archival and retreival

import pickle as p

class archive:

    def __init__(self):
        pass

    def archive(self,wk1,wk2,email):
        
        wkArr = [wk1,wk2] #put into dictionary

        #open old archive
        p_in = open("workoutArchive.pickle","rb")
        arch = p.load(p_in)

        p_in.close() #closing the archive

        arch[email] = wkArr #adding the new workout based on email

        p_out = open("workoutArchive.pickle","wb")
        p.dump(arch, p_out)
        p_out.close() #closing the archive
        print("Workout @ {} was insertd into archive".format(email))


    def get(self, email):
        
        p_in = open("workoutArchive.pickle","rb")
        arch = p.load(p_in)
        wkArr = arch[email]
        p_in.close()
        #print(wkArr)
        return(wkArr[0],wkArr[1])
