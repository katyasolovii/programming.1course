x = abs (int(input()))

first_dig = x%10
second_dig = x//10%10
third_dig = x//100 

print(first_dig * second_dig * third_dig) 