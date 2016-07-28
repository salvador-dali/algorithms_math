/**
 http://en.wikipedia.org/wiki/Partition_(number_theory)
*/
package main
import "fmt"

func solution(n int)[]int{
	MOD := 1000000007
	result := make([]int, n + 1)
	result[0] = 1

    for j:=1; j<=n; j++{
		for i:=j; i<=n; i++{
            result[i] = (result[i] + result[i - j]) % MOD
		}
	}
	return result
}

func main(){
    var T, n int
    fmt.Scanf("%d", &T)
	res := solution(1005)
    for T > 0{
        T--
        fmt.Scanf("%d", &n)
        fmt.Println(res[n] - 1)
    }
}
