/**
 dynamic programming, every number is the sum of one above and one to the left
 */
package main
import (
	"fmt"
)

const (
	N = 5
)

func lattice()[N][N]int{
	var m [N][N]int
	for i := 0; i < N; i++{
		m[i][0] = 1
		m[0][i] = 1
	}

	for i := 1; i < N; i++{
		for j := 1; j < N; j++{
			m[i][j] = (m[i - 1][j] + m[i][j - 1]) % 1000000007
		}
	}
	return m
}

func main(){
	matrix := lattice()
	var T, n, m int
	fmt.Scanf("%d", &T)
	for T > 0{
		T--
		fmt.Scanf("%d %d", &n, &m)
		fmt.Println(matrix[n][m])
	}
}
