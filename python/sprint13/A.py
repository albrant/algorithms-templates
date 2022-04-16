def gen_brackets(count, prefix='', left=0, right=0):
    if left == count and right == count:
        print(prefix)
    else:
        if left < count:
            gen_brackets(count, prefix + '(', left+1, right)
        if right < left:
            gen_brackets(count, prefix + ')', left, right+1)


gen_brackets(int(input()))
