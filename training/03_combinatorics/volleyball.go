package main
import (
	"fmt"
)

func volleyball(n1, n2 int) int {
	mod, max_score := 1000000007, 25
	if n2 == n1 {
		return 0
	}
	
	if n1 > n2 {
		n1, n2 = n2, n1
	}

	if n1 < max_score && n2 < max_score {
		return 0
	}
	
	if n2 > max_score && n2 - n1 != 2 {
		return 0
	}

	diff := 0
	if n1 >= max_score {
		diff = (n1 - max_score + 1) % mod
	}


	if n1 >= max_score {
		n1 = max_score - 1
	}

	if n2 >= max_score {
		n2 = max_score - 1
	}

	arr := make([]int, n1 + 1)
	for i := 0; i < len(arr); i++ {
		arr[i] = 1
	}

	for row := 0; row < n2; row++ {
		arr[0] = 1
		for col := 1; col <= n1; col++ {
			arr[col] = (arr[col] + arr[col - 1]) % mod
		}
	}

	return (arr[len(arr) - 1] + diff * 2) % mod
}

func main(){
	n1, n2, res_ := 748922783, 748922781, 862148271
	n1, n2, res_ := 126187267, 126187269, 256417096
	n1, n2, res_ := 1000000000, 999999998, 575548948
	_ = res_
	res := volleyball(n1, n2)
	fmt.Println(res)
}
