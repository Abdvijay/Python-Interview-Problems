# Input: "abcabcbb"
# Output: 3 → ("abc")

word = input("Enter the string : ")
result = {}
current = []
for i in word:
   if i not in current:
      current.append(i)
   else:
      sub_str = "".join(current)
      if sub_str not in result:
        result[sub_str] = len(sub_str)
        current = []

values = []
for key,value in result.items():
    values.append(value)

max_value = max(values)
for key,value in result.items():
   if value == max_value:
      print(f"Longest sub string is {key} -> {result[key]}")