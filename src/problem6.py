"""
Final exam, problem 3.

Authors: David Mutchler, Dave Fisher, Matt Boutell, their colleagues,
         and Todd Kuebelbeck.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_shape()


def run_test_shape():
    """ Tests the    shape    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   SHAPE   function:')
    print('--------------------------------------------------')

    print()
    print('Test 1 of shape: n=5')
    shape(5)

    print()
    print('Test 2 of shape: n=3')
    shape(3)

    print()
    print('Test 3 of shape: n=14')
    shape(14)


def shape(n):
    ####################################################################
    # IMPORTANT: In solving this problem,
    #   You must NOT use string multiplication.
    ####################################################################
    """
    Prints a shape with numbers on the left side of the shape,
    other numbers on the right side of the shape,
    and stars in the middle,per the pattern in the examples below.
    When the pattern calls for a number with more than one digit,
    just use the last (rightmost) digit when you print that number.

    It looks like this example for n=5:
    1 ** 54321
   12 *** 4321
  123 **** 321
 1234 ***** 21
12345 ****** 1

    And this one for n=3:
  1 ** 321
 12 *** 21
123 **** 1


And this one for n=14:
             1 ** 43210987654321
            12 *** 3210987654321
           123 **** 210987654321
          1234 ***** 10987654321
         12345 ****** 0987654321
        123456 ******* 987654321
       1234567 ******** 87654321
      12345678 ********* 7654321
     123456789 ********** 654321
    1234567890 *********** 54321
   12345678901 ************ 4321
  123456789012 ************* 321
 1234567890123 ************** 21
12345678901234 *************** 1

    :type n: int
    """
    # ------------------------------------------------------------------
    # TODO: Implement and test this function.
    #          Some tests are already written for you (above).
    ####################################################################
    # IMPORTANT: In solving this problem,
    #   You must NOT use string multiplication.
    ####################################################################
    #
    # HINT:
    #   If you're having trouble with the spaces on the left,
    #   print Xs for the spaces until you figure out where the problem is
    #   (and then change the Xs back to spaces).
    # ------------------------------------------------------------------

    for row in range(1,n+1,1):


        if n > 9:
            for space in range(n - (row)):
                print(' ', end='')
            for num in range(row):
                print(num + 1, end='')
            for r in range((row-9)+1):
                print(r, end='')

        else:
            for space in range(n-(row)):
                print(' ', end='')
            for num in range(row):
                print(num+1, end='')


        for star in range(row+1):
            print('*', end='')



        if n > 9:
            n_string = str(n)
            n_last = int(n_string[len(n_string)-1])

            for i in range(n_last-row+1, -1, -1):
                print(i, end='')


            if row <= n_last+1:
                for p in range(9, 0, -1):
                    print(p, end='')

            for g in range(9+((n_last+1)-row)+1,0,-1):
                    print(g, end='')

        else:
            for k in range((n-row)+1, 0, -1):
                print(k, end='')

        print('')

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
