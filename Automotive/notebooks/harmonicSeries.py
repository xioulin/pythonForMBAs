









# I know the series, 4−4/3+4/5−4/7...
#  converges to 𝜋
#  but I have heard many people say that while this is a classic example, there are series that converge much faster. Does anyone know of any?

















#the harmonic series is not convergent.
def harmonicSeriesSumUpTo(input):
    approx1overN = 0
    for i in range(1, input):
        approx1overN += (1 / i)
    return approx1overN




# print(harmonicSeriesSumUpTo(84))
def findHarmonicSeriesSummation(number):
    counter=0
    while harmonicSeriesSumUpTo(counter)< number:
        counter+=1
    return str(counter)+" is the harmonic series index for "+str(number)

# print(findHarmonicSeriesSummation(11))