for x in range(1,11):
    for y in range(1,11):
        print(x*y, end=" ")
    print()

#nested while
i, j = 1, 1
while j != 11:
    i = 1  # Reset i so the inner loop can run again
    while i != 11:
        # Using f-strings helps keep the spacing consistent
        print(i*j, end=" ")
        i += 1
    print() # New line after each row
    j += 1
