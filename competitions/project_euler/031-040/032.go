/**
 it is too much to check all the possible numbers.
 But if one would generate all the permutations of numbers from 1 to n
 then taking each permutation, one can try all the number in O(n^2)
 by trying all possible breaking points
 1, 2, 3, | 4, 5, 6, | 7, 8, 9
 */

package main
import (
	"fmt"
)

func permutations(arr []int)[][]int{
	var helper func([]int, int)
	res := [][]int{}

	helper = func(arr []int, n int){
        if n == 1{
			tmp := make([]int, len(arr))
			copy(tmp, arr)
			res = append(res, tmp)
		} else {
			for i := 0; i < n; i++{
				helper(arr, n - 1)
				if n % 2 == 1{
					tmp := arr[i]
					arr[i] = arr[n - 1]
					arr[n - 1] = tmp
				} else {
					tmp := arr[0]
					arr[0] = arr[n - 1]
					arr[n - 1] = tmp
				}
			}
		}
    }

	helper(arr, len(arr))
	return res
}

func num(arr []int)int{
	tmp := 1
	res := 0
	for i := len(arr); i > 0; i--{
		res += arr[i - 1] * tmp
		tmp *= 10
	}
	return res
}

func main(){
    var n int
    fmt.Scanf("%d", &n)
	arr := []int{}
    for i:=1; i <= n; i++{
        arr = append(arr, i)
    }

	dict := map[int]bool{}
	for _, perm := range(permutations(arr)){
		for i := 1; i < len(perm); i++{
			for j := i + 1; j < len(perm); j++{
				d1 := num(perm[:i])
				d2 := num(perm[i:j])
				d3 := num(perm[j:])
				if d1 * d2 == d3 {
					dict[d3] = true
				}
			}
		}
	}

	sum := 0
	for k, _ := range(dict){
		sum += k
	}

    fmt.Println(sum)
}
