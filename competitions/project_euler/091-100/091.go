/**
 the number of triangles where the right angle is at (0, 0) is 3 * n^2
 then for every point i,j find the number of triangles that can be constructed there
 */

package main
import (
	"fmt"
)

func gcd(a, b int) int {
	for b > 0 {
		a, b = b, a % b
	}
	return a
}

func numberOfTriangles(n int) uint64{
	num := uint64(n) * uint64(n) * 3
	for i := 1; i <= n; i++{
		for j := 1; j <= n; j++{
			gcd_value := gcd(i, j)
			n1, n2 := j * gcd_value / i, (n - i) * gcd_value / j
			if n1 > n2{
				num += 2 * uint64(n2)
			} else {
				num += 2 * uint64(n1)
			}
		}
	}
	return num
}

func main(){
	var n int
	fmt.Scanf("%d", &n)
	fmt.Println(numberOfTriangles(n))
}
