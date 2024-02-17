def prime(n): 
    if n <= 0: 
        return "Not defined" 
    elif n == 1: 
        return "Not prime" 
    for i in range(2, n): 
        if n%i == 0: 
            return "not prime" 
    return "prime" 
 
 
 
def list_prime(lst): 
	prime_list =[ ] 
	for i in lst: 
		x = prime(i) 
		if x == "prime": 
			prime_list.append(i) 
	return prime_list 
	 
print(list_prime([1,2,3,4,5,6,7,8,9])) 