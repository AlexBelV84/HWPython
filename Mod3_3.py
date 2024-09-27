def  print_params(a = 1, b = 'строка', c = True):
     print (a,b,c)

print_params(2,3)
print_params('Str')
print_params()

print_params(b=25) # done
print_params(c=[1,2,3]) #done

value_list =[3,"example",False]

values_dict={'a':1,'b':'Text','c': True }

print_params(*value_list) # done
print_params(**values_dict) # done

values_list_2=[2,False]
print_params(*values_list_2, 42)


