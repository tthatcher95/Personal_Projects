def print_letter(letter) :
    if letter == 'A' or letter == 'a':
        print " *** "
        print "*   *"
        print "*****"
        print "*   *"

    if letter == 'B' or letter == 'b':
        print "***"
        print "*  *"
        print "***"
        print "*  *"
        print "***",

    if letter == 'C' or letter == 'c':
        print " ***"
        print "*   "
        print "*   "
        print " ***",

    if letter == 'D' or letter == 'd':
        print "***"
        print "*  *"
        print "*  *"
        print "***",

    if letter == 'E' or letter == 'e':
        print "***"
        print "*"
        print "***"
        print "*"
        print "***",

    if letter == 'F' or letter == 'f':
        print "****"
        print "*"
        print "****"
        print "*"
        print "*",

    if letter == 'G' or letter == 'g':
        print " ***"
        print "*"
        print "* ***"
        print "*   *"
        print " ***",

    if letter == 'H' or letter == 'h':
        print "*    *"
        print "*    *"
        print "******"
        print "*    *"
        print "*    *",

    if letter == 'I' or letter == 'i':
        print "*****"
        print "  * "
        print "  * "
        print "  *"
        print "*****",

    if letter == 'J' or letter == 'j':
        print " *****"
        print "   *  "
        print "   *  "
        print "*  *  "
        print " **   ",

    if letter == 'K' or letter == 'k':
        print "*  *"
        print "* * "
        print "**  "
        print "* * "
        print "*  *",

    if letter == 'L' or letter == 'l':
        print "*    "
        print "*    "
        print "*    "
        print "*    "
        print "*****",

    if letter == 'M' or letter == 'm':
        print "*       *"
        print "* *   * *"
        print "*   *   *"
        print "*       *"
        print "*       *",

    if letter == 'N' or letter == 'n':
        print "*     *"
        print "* *   *"
        print "*  *  *"
        print "*   * *"
        print "*     *",

    if letter == 'O' or letter == 'o':
        print " *** "
        print "*   *"
        print "*   *"
        print "*   *"
        print " *** ",

    if letter == 'P' or letter == 'p':
        print "***"
        print "*  *"
        print "* *"
        print "*"
        print "*",

    if letter == 'Q' or letter == 'q':
        print " *** "
        print "*   *"
        print "* * *"
        print "*   *"
        print " ***  *",

    if letter == 'R' or letter == 'r':
        print "***"
        print "*  *"
        print "***"
        print "* *"
        print "*  *",

    if letter == 'S' or letter == 's':
        print "  ***"
        print " *"
        print "  ***"
        print "     *"
        print "  ***",

    if letter == 'T' or letter == 't':
        print "*******"
        print "   *  "
        print "   *  "
        print "   *  ",

    if letter == 'U' or letter == 'u':
        print "*   *"
        print "*   *"
        print " ***",

    if letter == 'V' or letter == 'v':
        print "*   *"
        print " * * "
        print "  *  ",

    if letter == 'W' or letter == 'w':
         print "*       * "
         print "*       *"
         print "*   *   *"
         print "* *   * *"
         print "*       *",

    if letter == 'X' or letter == 'x':
        print "*   *"
        print " * * "
        print "  * "
        print " * * "
        print "*   *",

    if letter == 'Y' or letter == 'y':
        print "*   *"
        print " * * "
        print "  *  "
        print "  *  ",

    if letter == 'Z' or letter == 'z':
        print " ***** "
        print "    *  "
        print "   *   "
        print "  *    "
        print " ***** ",
file = open("ascii.txt", "w")
def write_letter(letter) :
    if letter == 'A' or letter == 'a':
        file.write( " *** \n"),
        file.write( "*   *\n"),
        file.write( "*****\n"),
        file.write( "*   *\n"),
        file.write("\n")

    if letter == 'B' or letter == 'b':
        file.write( "*** \n"),
        file.write( "*  *\n"),
        file.write( "*** \n"),
        file.write( "*  *\n"),
        file.write( "*** \n"),
        file.write("\n")

    if letter == 'C' or letter == 'c':
        file.write( " ***\n"),
        file.write( "*   \n")
        file.write( "*   \n")
        file.write( " ***\n"),
        file.write("\n")

    if letter == 'D' or letter == 'd':
        file.write( "***\n")
        file.write( "*  *\n")
        file.write( "*  *\n")
        file.write( "***\n"),
        file.write("\n")

    if letter == 'E' or letter == 'e':
        file.write( "***\n")
        file.write( "*\n")
        file.write( "***\n")
        file.write( "*\n")
        file.write( "***\n"),
        file.write("\n")

    if letter == 'F' or letter == 'f':
        file.write( "****\n")
        file.write( "*\n")
        file.write( "****\n")
        file.write( "*\n")
        file.write( "*\n"),
        file.write("\n")

    if letter == 'G' or letter == 'g':
        file.write( " ***\n")
        file.write( "*\n")
        file.write( "* ***\n")
        file.write( "*   *\n")
        file.write( " ***\n"),
        file.write("\n")

    if letter == 'H' or letter == 'h':
        file.write( "*    *\n")
        file.write( "*    *\n")
        file.write( "******\n")
        file.write( "*    *\n")
        file.write( "*    *\n"),
        file.write("\n")

    if letter == 'I' or letter == 'i':
        file.write( "*****\n")
        file.write( "  * \n")
        file.write( "  * \n")
        file.write( "  *\n")
        file.write( "*****\n"),
        file.write("\n")

    if letter == 'J' or letter == 'j':
        file.write( " *****\n")
        file.write( "   *  \n")
        file.write( "   *  \n")
        file.write( "*  *  \n")
        file.write( " **   \n"),
        file.write("\n")

    if letter == 'K' or letter == 'k':
        file.write( "*  *\n")
        file.write( "* * \n")
        file.write( "**  \n")
        file.write( "* * \n")
        file.write( "*  *\n"),
        file.write("\n")

    if letter == 'L' or letter == 'l':
        file.write( "*    \n" )
        file.write( "*    \n" )
        file.write( "*    \n" )
        file.write( "*    \n" )
        file.write( "*****\n" ),
        file.write("\n")

    if letter == 'M' or letter == 'm':
        file.write( "*       *\n" )
        file.write( "* *   * *\n" )
        file.write( "*   *   *\n" )
        file.write( "*       *\n" )
        file.write( "*       *\n" ),
        file.write("\n")

    if letter == 'N' or letter == 'n':
        file.write( "*     *\n" )
        file.write( "* *   *\n" )
        file.write( "*  *  *\n" )
        file.write( "*   * *\n" )
        file.write( "*     *\n" ),
        file.write("\n")

    if letter == 'O' or letter == 'o':
        file.write( " *** \n" )
        file.write( "*   *\n" )
        file.write( "*   *\n" )
        file.write( "*   *\n" )
        file.write( " *** \n" ),
        file.write("\n")

    if letter == 'P' or letter == 'p':
        file.write( "***\n" )
        file.write( "*  *\n" )
        file.write( "* *\n" )
        file.write( "*\n" )
        file.write( "*\n" ),
        file.write("\n")

    if letter == 'Q' or letter == 'q':
        file.write( " *** \n" )
        file.write( "*   *\n" )
        file.write( "* * *\n" )
        file.write( "*   *\n" )
        file.write( " ***  *\n" ),
        file.write("\n")

    if letter == 'R' or letter == 'r':
        file.write( "***\n" )
        file.write( "*  *\n" )
        file.write( "***\n" )
        file.write( "* *\n" )
        file.write( "*  *\n" ),
        file.write("\n")

    if letter == 'S' or letter == 's':
        file.write( "  ***\n" )
        file.write( " *\n" )
        file.write( "  ***\n" )
        file.write( "     *\n" )
        file.write( "  ***\n" ),
        file.write("\n")

    if letter == 'T' or letter == 't':
        file.write( "*******\n" )
        file.write( "   *  \n" )
        file.write( "   *  \n" )
        file.write( "   *  \n" ),
        file.write("\n")

    if letter == 'U' or letter == 'u':
        file.write( "*   *\n" )
        file.write( "*   *\n" )
        file.write( " ***\n" ),
        file.write("\n")

    if letter == 'V' or letter == 'v':
        file.write( "*   *\n" )
        file.write( " * * \n" )
        file.write( "  *  \n" ),
        file.write("\n")

    if letter == 'W' or letter == 'w':
         file.write( "*       * \n" )
         file.write( "*       *\n" )
         file.write( "*   *   *\n" )
         file.write( "* *   * *\n" )
         file.write( "*       *\n" ),
         file.write("\n")

    if letter == 'X' or letter == 'x':
        file.write( "*   *\n" )
        file.write( " * * \n" )
        file.write( "  * \n" )
        file.write( " * * \n" )
        file.write( "*   *\n" ),
        file.write("\n")

    if letter == 'Y' or letter == 'y':
        file.write( "*   *\n" )
        file.write( " * * \n" )
        file.write( "  *  \n" )
        file.write( "  *  \n" ),
        file.write("\n")

    if letter == 'Z' or letter == 'z':
        file.write( " ***** \n" )
        file.write( "    *  \n" )
        file.write( "   *   \n" )
        file.write( "  *    \n" )
        file.write( " ***** \n" )
        file.write("\n")

def main():
    name = raw_input("Enter your name: ")
    namelist = list(name)
    for x in range(0, len(namelist)):
        print "\n"
        print_letter(namelist[x]),
        write_letter(namelist[x]),

main()