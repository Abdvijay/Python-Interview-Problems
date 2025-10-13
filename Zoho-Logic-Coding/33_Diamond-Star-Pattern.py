#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 

n = 5
mid = n + 1 // 2
for i in range(1,mid+1):
    print(" " * (mid - i) + "* " * i)
for i in range(mid,0,-1):
    print(" " * (mid - i) + "* " * i)