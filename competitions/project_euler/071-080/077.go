package main
import "fmt"


func sieveEratosthenes(n int)[]int{
	c := make([]bool, n)
	c[1] = true
	var p int = 2
	var i, p2 int

	for {
		p2 = p * p
		if p2 >= n {
			break
		}
		for i = p2; i < n; i += p {
			c[i] = true
		}
		for {
			p++
			if !c[p] {
				break
			}
		}
	}

	primes := []int{}
	for i = 1; i < n; i++{
		if c[i] == false {
			primes = append(primes, i)
		}
	}
	return primes
}

func solution(coins []int, n int)[]int{
	result := make([]int, n + 1)
	result[0] = 1

    for _, coin := range(coins){
		for i:=coin; i<=n; i++{
            result[i] += result[i - coin]
		}
	}
	return result
}

func main(){
    var T, n int
    fmt.Scanf("%d", &T)
	coins := sieveEratosthenes(1000)
	res := solution(coins, 1000)
    for T > 0{
        T--
        fmt.Scanf("%d", &n)
        fmt.Println(res[n])
    }
}
