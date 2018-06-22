# loop_examples.py 06/19/18

# for: use with iterators. list,, tuple, string, dictionary, set
# while: loop until condition is false

names = ["Chris", "Katie", "Chelsea", "Sheri"]

times_ran = 0
for name in names:
    times_ran += 1
    print(name)

print("Times loop ran: {}".format(times_ran))

nums = [1, 2, 3, 4, 5, 6]
for n in range(len(nums)):
    nums[n] = nums[n] ** nums[n]
print(nums)

# # infinite loop
# for i in nums:
#     nums.append(i)
#     print(nums)

x = 0
while x < 10:
  x += 1
  print(x)

while True:
    q = input("Enter 1 to search, 2 to quit: ")
    if q == '1':
        # search()
        pass
    elif q == '2':
        break
    else:
        print("That is not a valid entry. Please try again.")

print("goodbye")


numss = [5, 6, 7, 8, 9, 10]
for i in numss:
    if i % 2 == 1:
        continue # stops current loop and goes to next iteration
    print("{} is even".format(i))
