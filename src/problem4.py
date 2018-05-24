"""
Final exam, problem 4.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Todd Kuebelbeck.  May 2018.

"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


###############################################################################
# DONE: 2.
#   In this problem, you will go through the methods of the  Pig  class
#   that is defined below, one by one, in the order that they appear.
#   For each method:
#      (a) Read the method's doc-string (i.e., specification in double-quotes).
#            If you do not understand WHAT the method is to do,
#            ask your instructor to clarify it.
#      (b) Implement the method.
#      (c) Write at least SOME code  in  main  that tests your code.
#
###############################################################################

def main():
    """ Tests the  Pig  class. """
    # -------------------------------------------------------------------------
    # WRITE CODE HERE AS NEEDED to TEST the code that you write
    #   in the  Pig  class.  At the least, you must:
    #     -- Construct two Pig objects
    #     -- Call each method that you implement below.
    # -------------------------------------------------------------------------

    #Testing Pig class
    print('-------------------------')
    print('Testing Pig class')
    print('-------------------------')

    #Testing weight
    test_weight = 150
    piggly_wiggly = Pig(test_weight);
    print('Getting weight through self.')
    print('Expected: ', test_weight, 'Actual: ', piggly_wiggly.weight)
    print('')
    print('Getting weight through calling get_weight')
    print('Expected: ', test_weight, 'Actual: ', piggly_wiggly.get_weight())
    print('')
    print('')

    #Testing eat
    print('Testing eat function')
    increase = 100
    print('Increasing weight by: ', increase)
    print('Current weight: ', piggly_wiggly.get_weight())
    print('Expected: ', increase + test_weight, 'Actual: ', end='')
    piggly_wiggly.eat(increase)
    print(piggly_wiggly.get_weight())
    print('')
    print('')

    # Testing eat for a year
    print('Testing eat for a year function')
    print('Current weight: ', piggly_wiggly.get_weight())
    print('returned: ', end='')
    piggly_wiggly.eat_for_a_year()
    print(piggly_wiggly.get_weight())
    print('')
    print('')

    #Testing heavier pig
    print('Testing heavier pig')
    new_pig = Pig(200)
    print('self pig weight: ', piggly_wiggly.get_weight())
    print('new pig weight: ', new_pig.get_weight())
    test_pig = piggly_wiggly.heavier_pig(new_pig)
    print('Expected: ', piggly_wiggly.get_weight(), 'Actual: ', test_pig.get_weight())
    print('')
    print('')

    # Testing new pig
    print('Testing new pig')
    new_pig = Pig(200)
    print('self pig weight: ', piggly_wiggly.get_weight())
    print('new pig weight: ', new_pig.get_weight())
    newest_pig = piggly_wiggly.new_pig(new_pig)
    print('Expected: ', new_pig.get_weight() + piggly_wiggly.get_weight(), 'Actual: ', newest_pig.get_weight())
    print('')
    print('')



class Pig(object):
    def __init__(self, weight):
        """
        What comes in:  The Pig's weight (in pounds).
        Side effects: Sets instance variables as needed by the other methods.
        """
        # DONE: Implement and test this method.
        self.weight = weight

    def get_weight(self):
        """ Returns this Pig's weight. """
        # DONE: Implement and test this method.
        return self.weight

    def eat(self, pounds_of_slop):
        """
        Increments this Pig's weight by the given pounds_of_slop.
        """
        # DONE: Implement and test this method.
        self.weight = self.weight + pounds_of_slop

    def eat_for_a_year(self):
        """
        Calls the   eat   method as many times as needed to make this Pig:
          -- eat 1 pound of slop, then
          -- eat 2 pounds of slop, then
          -- eat 3 pounds of slop, the
          -- eat ... [4 pounds, then 5, then 6, then ... ]
          -- eat 364 pounds of slop, then
          -- eat 365 pounds of slop.
        """
        # DOEN: Implement and test this method.

        for k in range(1, 365):
            self.weight = self.weight + k

    def heavier_pig(self, other_pig):
        """
        Returns either this Pig object or the other given Pig object,
        whichever is heavier.
        """
        # DONE: Implement and test this method.

        if self.weight > other_pig.get_weight():
            return self
        else:
            return other_pig

    def new_pig(self, other_pig):
        """
        Returns a new Pig whose weight is the weight of the heavier
          of this Pig and the other_Pig.
        """
        # DONE: Implement and test this method.
        return Pig(other_pig.get_weight() + self.weight)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
