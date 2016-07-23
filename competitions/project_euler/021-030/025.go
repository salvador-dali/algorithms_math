/**
 number N has floor(log10(n)) + 1 digits
 fibonacci number is written as
 there is a fib formula which tells that  $$F_n = \frac{\varphi ^n - \psi ^n}{\sqrt{5}}$$, where
 \varphi = \frac{1 + \sqrt{5}}{2}
 \psi  = \frac{1 - \sqrt{5}}{2}

 the first one is bigger then one and increases with n, the second one is smaller and decreases.
 Because of this F_n \approx  \frac{\varphi ^n}{\sqrt{5}}


 taking log of it one will see that the number of digits is equal to
 floor( n \cdot \log_{10} \varphi - \log_{10}\sqrt{5} ) + 1
 */

package main
import (
	"fmt"
	"math"
)

func fibDigits(n float64)int{
	if n < 6{
		return 1
	}
	return int(math.Floor(n * 0.20898764024997873 - 0.34948500216800943)) + 1
}

func main(){
	digits := []int{1}
	for i := 5; true; i++{
		digit := fibDigits(float64(i))
		if digit > len(digits){
			digits = append(digits, i)
		}
		if digit > 5000{
			break
		}

	}
	var T, n int
    fmt.Scanf("%d", &T)
	for T > 0{
		T--
        fmt.Scanf("%d", &n)
        fmt.Println(digits[n - 1])
	}
}
