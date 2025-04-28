
# use try in every input. if the code is not accepted
# there is no severeness to make the code complicated future me
try:
    t = int(input())     # 'case: ' | part 1: 1 / test case

    for o in range(t):

        try:
            n = int(input())   # 'bit range: ' | range of bits/ part 2: 1

            max_in = 0
            count = 0
            lisp = []
            a = []
            h = 0

            ki = input().split()    # 'bit: '

            for j in range(n):
               a.append(int(ki[j]))

            # for j in range(n):   # the bits input part 2: 1
            #
            #     ki = int(input('bit: '))
            #
            #     if ki == 1 or ki == 0:  # only 0 or 1 is allowed
            #         a.append(ki)
            #         print(a)  # to see into the list
            #
            # fine below form here
            for i in range(len(a)):     # bs begins form here

                if a[i] == 0:           # checks if there is any 0 then put it into the count not as zero but index
                    count += 1
                    lisp.append(count)  # inserts the ongoing input
                else:
                    max_in = count      # max_in is not needed. it is way too boring now. Future me good luck clearing and testing it

                    lisp.append(max_in) # inserts the saved value

                    # --for error handling--
                    # print(max_in,'= max in 16')
                    # print(count,'= count in 17')

                    count = 0   # resets the counter

            # --error handle welcome future me--
            # print(f'{max_in} = max in 20')
            # print(f'{count} =  count in 21')
            # print(f'{lisp} = mix in 26')
            print(max(lisp))    # prints the main output the blank spaces or how many 0's

        except ValueError:
            pass

except ValueError:
    pass