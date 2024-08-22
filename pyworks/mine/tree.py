# blank = " "
# star = '*'
# enter = "\n"
#
# def istree():
#     tree = []
#     tree.append('           ********* \n' )
#     tree.append('      *****         **** \n ')
#
#     print(tree)
# istree()

def istree():
    tree = [
        "           *********",
        "      *****         ****",
        "    **                  **",
        "   *                      *",
        " **                        **",
        "*                            *",
        "*                            *",
        "**                          **",
        " **  *    ****  ****    *  **",
        "   ** ***** ****** ***** **",
        "             ****",
        "             ****",
        "             ****",
        "             ****",
        "            ******",
        "           ********"
    ]

    for line in tree:
        print(line)

istree()
