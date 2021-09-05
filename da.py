# # # #
# # # #
# # # #
# # # #

# for i in range(4):
#     for x in range(4):
#         print("#", end=" ")
#     print()

# ---------------------------------

#
##
###
####

# for i in range(4):
#     for x in range(i + 1):
#         print("#", end="")
#     print()

# -------------------------------

# for i in range(4):
#     for j in range(4 - i):
#         print("#", end="")
#     print()

# --------------------------------

#
# # # #
# #
# # #
# # #
# #
# # # #
#

# lets go!

for i in range(4):
    for x in range(i + 1):
        print("#", end=" ")
    print()
    for j in range(4 - x):
        print("#", end=" ")
    print()
