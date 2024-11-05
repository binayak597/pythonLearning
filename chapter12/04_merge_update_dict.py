
l1 = {'a': 1, 'b': 2}
l2 = {'b': 3, 'c': 4}
merged = l1 | l2

print(merged)


# inorder to open multiple files together

with(
    open('file1.txt') as f1,
    open('file2.txt') as f2
):
    f1.read()
    f2.read()