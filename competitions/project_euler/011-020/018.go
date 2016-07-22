/**
 dynamic programming, taking in to the account that any number

 a0, a1, a2
 b0, b1, b2, b3

 b0 = a0 + matrix(b0)
 b1 = max(a0 + matrix(b1), a1 + matrix(b1))
 */
package main
import (
	"fmt"
)

func best(matrix [][]int)int{
	res := [][]int{}
	for i := 0; i < len(matrix); i++{
		tmp := []int{}
		for j := 0; j < len(matrix); j++{
			tmp = append(tmp, 0)
		}
		res = append(res, tmp)
	}
	res[0][0] = matrix[0][0]


	for i := 1; i < len(matrix); i++{
		for j := 0; j < len(matrix[i]); j++{
			if j > 0{
				if res[i - 1][j - 1] > res[i - 1][j]{
					res[i][j] = res[i - 1][j - 1] + matrix[i][j]
				} else {
					res[i][j] = res[i - 1][j] + matrix[i][j]
				}
			} else {
				res[i][j] = res[i - 1][j] + matrix[i][j]
			}
		}
	}

	var max = 0
	for i:=0; i < len(matrix); i++{
		if res[len(matrix) - 1][i] > max {
			max = res[len(matrix) - 1][i]
		}
	}
	return max
}

func main(){
    var T, l, d int
    fmt.Scanf("%d", &T)
    for T > 0 {
        T--
        fmt.Scanf("%d", &l)
        matrix := [][]int {}
        for i := 0; i < l; i++{
            tmp := []int{}
            for j := 0; j <= i; j++{
                fmt.Scanf("%d", &d)
                tmp = append(tmp, d)
            }
            
            matrix = append(matrix, tmp)
        }
        fmt.Println(best(matrix))
    }
}
