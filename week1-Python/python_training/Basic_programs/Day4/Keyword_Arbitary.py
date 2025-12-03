def add(**nums):
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    n3= int(input("Enter third number: "))
    print(add(fn=n1, sn=n2, tn=n3))
    #type(nums))
    res=nums[fn]+nums[sn]+nums[tn]
    return res
