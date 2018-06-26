# # error_handling_examples.py 6/20/18
#
# # def crash(n):
# #     if n < 0:
# #         raise ValueError("I cant be lower than 0")
# #     print(n)
# #
# # crash(-1)
#
# while True:
#     try:
#         query = int(input("Press 1 2 or 3: "))
#     except ValueError:
#         print("Please enter 1 2 or 3 as integers")
#         continue
#
#     if query == 1:
#         print("You pressed 1")
#     elif query == 2:
#         print("You pressed 2")
#     elif query == 3:
#         print("You pressed 3, goodbye.")
#         quit()
#     else:
#         print("I did not understand that.")
