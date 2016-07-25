/**
 find all the prime numbers below approximately squareRoot of N. Square root because
 sum of first prime growth n^2 * log(n). After that precalculate cumulative sum to be able to quickly
 get sum from i-th to j-th number. Then my idea was to go through all the numbers and check if the number
 is a prime and length is good, but it took too much time. I analysed the answers off-line and found that
 the biggest consecutive sum of primes is really close to the starting position.

 So I just started with the difference of 50 and found out that 20 is enough.
 */
package main
import "fmt"

func sieve(n int)[]bool{
	is_primes := make([]bool, n + 1)
	for i := 2; i <= n; i++{
		is_primes[i] = true
	}

	for i := 2; i * i <= n; i++{
		if is_primes[i]{
			for j := i * i; j <= n; j += i{
				is_primes[j] = false
			}
		}
	}
	return is_primes
}

func isPrime(n int64)bool{
	if n == 1{
		return false
	}
	if n > 2 && n % 2 == 0{
		return false
	}

	for i := int64(3); i * i <= n; i++{
		if n % i == 0{
			return false
		}
	}
	return true
}

func main(){
    is_prime := sieve(8000000)
    T, n := 0, uint64(0)
    fmt.Scanf("%d", &T)
    
    for T > 0{
        T--
        fmt.Scanf("%d", &n)
        cumSum := []int64{0}
        for k, v := range(is_prime){
            if v {
                newEl := cumSum[len(cumSum) - 1] + int64(k)
                if newEl > int64(n){
					cumSum = append(cumSum, newEl)
					cumSum = append(cumSum, cumSum[len(cumSum) - 1] + int64(k))
					cumSum = append(cumSum, cumSum[len(cumSum) - 1] + int64(k))
					cumSum = append(cumSum, cumSum[len(cumSum) - 1] + int64(k))
					cumSum = append(cumSum, cumSum[len(cumSum) - 1] + int64(k))
					cumSum = append(cumSum, cumSum[len(cumSum) - 1] + int64(k))
					break
				}
                cumSum = append(cumSum, newEl)
            }
        }
        maximumDiff, bestPrime, bestLength := 22, int64(0), 0
        for j := 0; j < maximumDiff && j < len(cumSum) - 1; j++{
            for i := len(cumSum) - 1; i > 0 && i > len(cumSum) - maximumDiff && cumSum[i] > cumSum[j]; i--{
                attempt := cumSum[i] - cumSum[j]
                if attempt <= int64(n) && isPrime(attempt){
                    if i - j > bestLength{
                        bestLength = i - j
                        bestPrime = attempt
                    } else if i - j == bestLength{
						if attempt < bestPrime{
							bestPrime = attempt
						}
					}
                }
            }
        }
        fmt.Println(bestPrime, bestLength)
    }
}
