package main
import (
	"fmt"
)

/**
 the duplicate numbers will appear when x^y = (x ^ a) ^ b
 where y = a * b
 for example 6 ^ 8 == 36 ^ 4
 */
func main(){
	var N int
	fmt.Scanf("%d", &N)

	unique := map[int]bool{}
	num_unique := [17]int{}
	is_base := [100001]bool{}
	// array whose value is true, if the number one if the number can not be presented
	// as some prev number ^ something. For example 6 is true, 36 is false, because it is 6^2

	for i := 1; i < 17; i++{
		for b := 2; b <= N; b++{
			unique[i * b] = true
		}
		num_unique[i] = len(unique)
	}



	for i := 0; i < 100001; i++{
		is_base[i] = true
	}


	result := 0
	for i := 2; i <= N; i++{
		if is_base[i]{
			pw := 0
			for j := i; j <= N; j *= i{
				is_base[j] = false
				pw += 1
			}
			// for each i, we find the last number that was thrown away. For example if
			// i = 2 and N = 17, the last one we throw away was 16.
			result += num_unique[pw]
		}
	}

	fmt.Println(result)
}
