lst = list(map(str,input("Enter the list values by space : ").split()))
result = []
visited = {}
for i in lst:
   visited[i] = False
for i in lst:
   for j in lst:
      if i != j:
         if sorted(i) == sorted(j) and visited[j] == False:
             result.append([i,j])
             visited[i] = True
print(result)

# OUTPUT

# Enter the list values by space : abd cte dab ect
# [['abd', 'dab'], ['cte', 'ect']]