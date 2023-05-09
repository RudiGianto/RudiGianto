# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
Nederland = 'Gullit'
Nederland = 'van Basten'
goal_0 = 32
goal_1 = 54
scorers = 'Ruud Gullit ' + str(32) + ', Marco van Basten ' + str(54)
report = f'Ruud Gullit scored in the {goal_0}nd minute\nMarco van Basten scored in the {goal_1}th minute' 
print(report)
player ='Ruud Gullit'
first_name = player[:player.find(' ')]  
last_name = player[player.find(' '):]                # https://www.w3schools.com/python/python_strings_slicing.asp
last_name_len =len(last_name[1:11])                 #https://www.w3schools.com/python/ref_func_len.asp
name_short = first_name[0]+'.'+ last_name
chant = (first_name+'! ')*3 + (first_name+'!')*1
good_chant = (2!=3) 
print(first_name)
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)