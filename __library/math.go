// TODO modify getDivisors in python code. Incorrectly handles 1, 3 numbers
// TODO	getDivisorSieve for i in range(2, n + 1, 2): sieve[i] = 2
package main

import (
	"fmt"
	"math"
	_ "time"
	"strconv"
)

// ============== GCD =====================
func gcd(a, b int) int {
	for b > 0 {
		a, b = b, a % b
	}
	return a
}

func lcm(a, b int) int {
	return a / gcd(a, b) * b
}

func gcd_multiple(list [] int) int {
	res := list[0]
	for _, val := range list {
		res = gcd(res, val)
	}
	return res
}

func lcm_multiple(list [] int) int {
	res := 1
	for _, val := range list {
		res = lcm(res, val)
	}
	return res
}

// ============== Primes ==================
func isPrime(n uint64) bool {
	// takes approximately 3 times slower than normal
	// 9132651973611377347 takes approximately 10 sec
	if n == 1 {
		return false
	}
	if n < 4 {
		return true
	}
	if n % 2 == 0 || n % 3 == 0 {
		return false
	}

	w, max := uint64(5), uint64(math.Sqrt(float64(n))) + 1
	for i := uint64(2); i <= max; i += w {
		if n % i == 0 {
			return false
		}
		w = 6 - w
	}
	return true
}

func sieveEratosthenes(n int) []bool {
	/**
	 10^7 	77 ms
	 10^8	1.13 s
	 10^9	14.4 s

	 https://numericalrecipes.wordpress.com/2009/03/24/prime-numbers-3-wheel-factorization/
	 http://en.wikipedia.org/wiki/Wheel_factorization
	 http://programmingpraxis.com/2012/01/06/pritchards-wheel-sieve/
	 http://www.primesdemystified.com/
	 */

	is_primes := make([]bool, n+1)
	for i := 2; i <= n; i++ {
		is_primes[i] = true
	}

	for i := 2; i*i <= n; i++ {
		if is_primes[i] {
			for j := i * i; j <= n; j += i {
				is_primes[j] = false
			}
		}
	}
	return is_primes
}

func factorize(n uint64) []uint64 {
	/**
	 factorize the number into multiplication of prime numbers
	 takes approximately 2.5 seconds for a 17 digit prime
	 51975335556428597
	 */
	factors := []uint64{}
	for i := uint64(2); i*i <= n; i++ {
		for n % i == 0 {
			factors = append(factors, i)
			n /= i
		}
	}
	if n > 1 {
		factors = append(factors, n)
	}
	return factors
}

func divisorSieve(n uint64) []uint64 {
	/**
	 generates an array that has a divisor of an element in the array do not try to optimize

	 this is helpful to quickly factorize any number with getDivisorsFromSieve
	 10^8 takes 1.5 seconds
	 */
	sieve := make([]uint64, n + 1)
	for i := uint64(0); i < n+1; i++ {
		if i % 2 == 0 {
			sieve[i] = 2
		}
	}
	sieve[0] = 0

	p := uint64(3)
	for p*p <= n {
		for i := p; i <= n; i += p {
			if sieve[i] == 0 {
				sieve[i] = p
			}
		}

		for p < n+1 && sieve[p] > 0 {
			p += 2
		}
	}

	for p < n+1 {
		if sieve[p] == 0 {
			sieve[p] = p
		}
		p += 2
	}
	return sieve
}

func getDivisorsFromSieve(sieve []uint64, num uint64) []uint64 {
	/**
	 having dict from divisorSieve find a factorization of the number
	 */
	divisors := []uint64{}
	for num > 1 {
		divisors = append(divisors, sieve[num])
		num /= sieve[num]
	}
	return divisors
}

func totient(n uint64) uint64 {
	/**
	 number of integers that are less then N and are coprime with it. It is as fast as the speed of
	 factorization explanation and the proof http://en.wikipedia.org/wiki/Euler's_totient_function

	 If we know the factorization, we can do it much faster.
	 also if we need many totients, we can take advantage of factorize many
	 and if we need totientRecursive - take a look at infinum_11 totient
	 */
	res := n
	primesSet := map[uint64]bool{}
	for _, v := range factorize(n) {
		primesSet[v] = true
	}

	for k, _ := range primesSet {
		res = res / k * (k-1)
	}
	return res
}

func getTotientFromSieve(sieve []uint64, num uint64) uint64 {
	res, prevDivisor := num, uint64(1)
	for num > 1 {
		k := sieve[num]
		if k != prevDivisor {
			res = res / k * (k-1)
		}
		num /= k
		prevDivisor = k
	}
	return res
}

func generateFarey(n uint64) []uint64 {
	/**
	 Generate the number of fractions in Farey series of order n: http://oeis.org/A005728
	 http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fractions/fareySB.html
	 F_n = F_{n-1} + \phi (n) = 1 + \sum_{i=1}^{n}\phi(i)
	 from http://en.wikipedia.org/wiki/Farey_sequence
	 http://www.cse.iitd.ernet.in/~mcs103480/farey-icip-100525.pdf
	 */
	sieve, farey := divisorSieve(n), make([]uint64, n+1)
	farey[0] = 1
	for i := uint64(1); i < n+1; i++ {
		farey[i] = farey[i-1] + getTotientFromSieve(sieve, uint64(i))
	}
	return farey
}

// ============== Divisors ================
func getDivisors(n uint64) []uint64 {
	/**
	 O(n^0.5)
     Get the list of divisors of a number in a sorted order the main idea is to divide divisors
     into big and small and to remember that they come in pairs. So big = n / small
	 */
	small, big := []uint64{}, []uint64{}
	for i := uint64(1); i < uint64(math.Sqrt(float64(n)))+1 ; i++ {
		if n % i == 0 {
			small = append(small, i)
			if i != n / i {
				big = append(big, n / i)
			}
		}
	}
	for j := 0; j < len(big); j++ {
		small = append(small, big[len(big) - j - 1])
	}
	return small
}

func divisorsNum(n uint64) uint64 {
	/**
	 calculate the total number of divisors of the number
	 important property of a divisor function
	 if n = a * b and a is a coprime to b, then div(n) = div(a) * div(b)

	 read also this: http://en.wikipedia.org/wiki/Divisor_function
	 and implement getDivisors from factorization
	 */
	dict, res := map[uint64]uint64{}, uint64(1)
	for _, v := range factorize(n) {
		dict[v] += 1
	}
	for _, v := range dict {
		res *= v + 1
	}
	return res
}

func divisorsSum(n uint64) uint64 {
	dict, res := map[uint64]uint64{}, 1.0
	for _, v := range factorize(n) {
		dict[v] += 1
	}
	for p, a := range dict {
		res *= (math.Pow(float64(p), float64(a) + 1.0) - 1) / (float64(p) - 1)
	}
	return uint64(res) - n
}

func divisorsFunc(n uint64, x float64) uint64 {
	/**
	http://en.wikipedia.org/wiki/Divisor_function
	if x = 1, then it calculates sum of all divisors way more efficient than a bruteforce solution
	 */
	dict, res := map[uint64]uint64{}, uint64(1)
	for _, v := range factorize(n) {
		dict[v] += 1
	}
	for p, a := range dict {
		res *= uint64((math.Pow(float64(p), (float64(a)+float64(1))*x) - 1) / (math.Pow(float64(p), x) - 1))
	}
	return res
}

// ============== Other    ================
func isPermutation(n, m uint64) bool {
	/**
	checks that one number is a permutation of another
	 */
	if math.Floor(math.Log10(float64(n))) != math.Floor(math.Log10(float64(m))) {
		return false
	}

	arr1 := [10]uint8{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
	arr2 := [10]uint8{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
	for n > 0 {
		arr1[uint8(n % 10)]++
		n /= 10
	}

	for m > 0 {
		arr2[uint8(m % 10)]++
		m /= 10
	}

	return arr1 == arr2
}

func isTriangular(n uint64) bool {
	// check if the number is a triangular number
	x := (math.Sqrt(float64(8 * n + 1)) - 1) / 2
	return x == math.Floor(x)
}

func isPentagonal(n uint64) bool {
	// check if the number is a pentagonal number
	// is s-gonal number http://en.wikipedia.org/wiki/Polygonal_number#Hexagonal_numbers
	x := (math.Sqrt(float64(24 * n + 1)) + 1) / 6
	return x == math.Floor(x)
}

func fromFactorial(digits []uint8) uint64 {
	// convert a number from a factorial number system to decimal
	f, res, l := uint64(10), uint64(0), len(digits)
	for i := 0; i < l; i++ {
		res += f * uint64(digits[l - 1 - i])
		f *= uint64(i + 1)
	}
	return res
}

func toFactorial(n uint64) []uint8 {
	// convert a digit to a factorial number system
	digits := []uint8{}
	for i := uint64(1); n > 0; i++ {
		digits = append([]uint8{uint8(n % i)}, digits...)
		n /= i
	}
	return digits
}

func digitsToNumber(arr []int) int {
	/**
	 convert array of digits to number [1, 2, 3] will be 123
	 */
	tmp, res := 1, 0
	for i := len(arr); i > 0; i-- {
		res += arr[i-1] * tmp
		tmp *= 10
	}
	return res
}

func fraction(a, b int64) string {
	// http://en.wikipedia.org/wiki/Repeating_decimal
	nonRepeating, repeating, digits := strconv.Itoa(int(a / b)) + ".", "", []int64{}
	numbersSeen, pos := map[int64]int64{}, int64(0)
	startRepeating, isRepeating := int64(-1), false
	a = a % b

	for a > 0 {
		start, ok := numbersSeen[a]
		if ok {
			startRepeating, isRepeating = start, true
			break
		}
		numbersSeen[a] = pos
		a *= 10

		if a < b {
			digits = append(digits, int64(0))
		} else {
			digits = append(digits, a/b)
			a %= b
		}
		pos++
	}

	for i, v := range(digits) {
		if i < int(startRepeating) {
			nonRepeating += strconv.Itoa(int(v))
		} else {
			repeating += strconv.Itoa(int(v))
		}
	}
	if isRepeating {
		return nonRepeating + "(" + repeating + ")"
	}
	return nonRepeating + repeating
}

func extended_gcd(a, b int64) (int64, int64, int64) {
	if a == 0 { return b, 0, 1 }

	g, y, x := extended_gcd(b % a, a)
	return g, x - b / a * y, y
}

func modInv(a, m int64) int64 {
	g, x, _ := extended_gcd(a, m)
	if g != 1 { return 0 }

	return x % m
}

func powMod(base, exponent, modulo int)int{
	res := 1
	base %= modulo
	for exponent > 0{
		if exponent % 2 == 1{
			res = (res * base) % modulo
		}
		exponent /= 2
		base = (base * base) % modulo
	}
	return res
}

func youngStandard(n int)int64{
	/**
	Find the number obtained by placing the numbers 1, ..., n in the n boxes of the diagram,
	where the numbers form an increasing sequence along each line and along each column.

	This is the number of ways you can represent a standard Young tablaux

	http://mathworld.wolfram.com/YoungTableau.html
	https://en.wikipedia.org/wiki/Involution_(mathematics)
	 */
	if n < 3{
		return int64(n)
	}

	y1, y2 := int64(1), int64(2)
	for i := 3; i <= n; i++{
		y2, y1 = y2 + int64(i - 1) * y1, y2
	}
	return y2
}

func permutation_sign(arr []int) int {
	// https://en.wikipedia.org/wiki/Parity_of_a_permutation
	// can be done in O(n)
	total := 0
	for i := 0; i < len(arr); i++ {
		for j := i + 1; j < len(arr); j++ {
			if arr[i] > arr[j] {
				total += 1
			}
		}
	}
	if total % 2 == 1 {
		return -1
	}
	return 1
}

func main() {
//	start := time.Now()
//	elapsed := time.Since(start)
	res := divisorSieve_2(uint64(100000000))
	fmt.Println(res)
}



