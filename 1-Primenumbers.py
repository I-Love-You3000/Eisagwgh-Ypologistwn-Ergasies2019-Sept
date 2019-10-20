start = 1
end = 1000
i = 0
print("Priem numbers from 1 to 1000 are:")
for val in range(start, end + 1):

    if val > 1:
        for n in range(2, val):
            if (val % n) == 0:
                break
        else:
            print(val)
            i=i+1

primelist=list(range(0,i))
i=0

for rip in range(start, end + 1):

    if rip > 1:
        for n in range(2, rip):
            if (rip % n) == 0:
                break
        else:
            primelist[i]=rip
            i=i+1

maxdif=primelist[i-1]-primelist[0]
print("The maximum difference of the numbers is:", maxdif)