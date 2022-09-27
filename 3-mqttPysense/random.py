import machine

#--- float random number in range (mini,maxi) ----
def rand(mini, maxi):
    maxValue = 16777216
    val = machine.rng()
    resu = mini + (maxi-mini) * float(val) / maxValue
    return resu

#-- main --
mini = 16
maxi = 24
test = rand(mini,maxi)
print ("random value in range : "+str(mini)+" / "+str(maxi) ,test, type(test))
