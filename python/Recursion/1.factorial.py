"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
def fact(num:int)->int:
    if num ==0 or num==1:
        return 1
    return num*fact(num-1)

print(fact(10))

"""
fact(5)
  |
  |--> fact(4)
        |
        |--> fact(3)
              |
              |--> fact(2)
                    |
                    |--> fact(1)
                          |
                          |--> return 1
                    |
                    |--> return 2 * 1 = 2
              |
              |--> return 3 * 2 = 6
        |
        |--> return 4 * 6 = 24
  |
  |--> return 5 * 24 = 120
"""
