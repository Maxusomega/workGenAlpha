#MAtthew Cole
#workout array archival and retreival

import pickle as p

class archive:

    def __init__(self):
        pass

    def archive(self,wk1,wk2,email):
        
        wkArr = [wk1,wk2] #put into list

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

    #note to future self: DON'T USE TUPLES INSIDE ARRAYS INSIDE ARRAYS or just don't be an idiot when coding
    def adjustWeight(self,email,wkNum,exNum,weight):

        p_in = open("workoutArchive.pickle","rb") #loading in email wit read only
        arch = p.load(p_in)
        p_in.close() #closing the archive

        #i made a a mistake using tuples 
        exercise = list(arch[email][wkNum][exNum]) #exercise is equal to the tuple but turning it into a list so i can change it

        #print(exercise)
        exercise[7] = weight         #changing the weight

        arch[email][wkNum][exNum] = tuple(exercise)    #changing it back and putting it back

        p_out = open("workoutArchive.pickle","wb")  #dumping the diciotnary again
        p.dump(arch, p_out)
        p_out.close() #closing the archive
        



