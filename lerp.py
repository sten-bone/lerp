############################################################
# LEFRP takes as paramaters two tuples, A and B, which
# represent two points, and returns a linear representation
# between points A and B normalized in the range t = [0, 1].
# The interpolation is returned as a tuple of Strings
# in the form (x(t), y(t)), where x(t) defines the x
# parametric linear path and y(t) defines the y parametric
# linear path, both in the form mt + b. Rounds values to
# 3 decimal places
def LERP(A, B):
    '''Create a linear parametric representation of two points
        A and B, returned as a tuple (x(t), y(t))'''
    # checks to be sure A and B are properly formatted with
    # two integers
    if (len(A) != 2 or len(B) != 2):
        print("Please enter valid coordinates")
        return
    # calls on createParamRep while casting coordinates to
    # int to prevent type issues
    return((createParamRep(float(A[0]), float(B[0])),
            createParamRep(float(A[1]), float(B[1]))))

############################################################
# createParamRep takes as paramaters two floats a and b
# and returns a string parametric representation of a linear 
# path in the form mt + b
def createParamRep(a, b):
    return(formatLinearPath(b - a, a))


############################################################
# formatLinearPath takes as parameters two floats m and b
# and returns a String in the form mt + b formatted for
# positive, negative, or zero values of m and b. Rounds to
# three decimal places
def formatLinearPath(m, b):
    return((str(round(m, 3)) + "t" + (" + " if b > 0 else " - ") +
            str(round(abs(b), 3))) if m != 0 else (str(round(b, 3)) if b != 0 else '0'))

############################################################
########## Q U A D R A T I C # C U R V A T U R E ###########
############################################################

############################################################
# quadraticLERP takes as parameters three tuples, A, B, and
# C, which represent three points, and returns a quadratic
# parametric representation between points A and B with C as
# a guide normalized in the range t = [0, 1]. The
# representation is returned as a tuple of Strings in the
# form (Lx, Ly), where Lx defines the x quadratic parametric
# path and Ly defines the y quadratic parametric path, both
# in the form at^2 + bt + c. Rounds values to three decimal
# places
def quadraticLERP(A, B, C):
    '''Create a quadratic parametric representation of three
        points A, B, and C, returned as a tuple (Lx, Ly)'''
    # check to be sure coordinates are valid
    if (len(A) != 2 or len(B) != 2 or len(C) != 2):
        print("Please enter valid coordinates")
        return
    return((createQuadraticParamRep(float(A[0]), float(B[0]), float(C[0])),
            createQuadraticParamRep(float(A[1]), float(B[1]), float(C[1]))))

############################################################
# createQuadraticParamRep takes as parameters three floats
# a, b, and c and returns a string quadratic parametric
# representation of a path in the form at^2 + bt + c
def createQuadraticParamRep(a, b, c):
    return(formatQuadraticPath(a + b - (2 * c), (2 * c) - (2 * a), a))

############################################################
# formatQuadraticPath takes as parameters three floats a,
# b, and c and returns a String in the form at^2 + bt + c
# formatted for positive, negative, or zero values of a, b,
# and c. Rounds to three decimal places
def formatQuadraticPath(a, b, c):
    # check to see if all points are zero
    if (a == 0 and b == 0 and c == 0):
        return("0")
    s = ""
    if (a != 0):
        s += str(round(a, 3)) + "t^2"
    # format b according to sign
    if (b != 0):
        if (a != 0):
            if (b > 0):
                s += " + " + str(round(b, 3)) + "t"
            else:
                s += " - " + str(round(abs(b), 3)) + "t"
        else:
            s += str(b) + "t"
    # format c according to sign
    if (c != 0):
        if (b != 0 or a != 0):
            if (c > 0):
                s += " + " + str(round(c, 3))
            else:
                s += " - " + str(round(abs(c), 3))
        else:
            s += str(round(c, 3))
    return(s)
