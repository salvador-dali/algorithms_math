package main
import (
	"fmt"
)

func permutations(arr []int)[][]int{
	// http://en.wikipedia.org/wiki/Heap%27s_algorithm
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

func rectanglesInRectangle(x, y uint64) uint64{
	/**
	 there are 18 rectangles in the 3x2 grid

	 there are n * (n + 1) / 2 rectangles in the 1xn grid
	 if it is 2xn grid, we will have n * (n + 1) * 3 / 2.
	 So for nxm grid we will get n * (n + 1) * m * (m + 1) / 4
	 */
	return x * (x + 1) / 2 * y * (y + 1) / 2
}

func squaresInSquare(n uint64)uint64{
	/**
	 let's have a square 3x3
	 a b c
	 d e f
	 g h i

	 How many squares you can insert from position A (3).
	 From position B, D, E (2 times). From all other positions 1 squares.

	 3 2 1
	 2 2 1
	 1 1 1

	 so we have n * 1 + (n - 1) * 3 + (n - 2) * 5 + ...
	 By induction one can prove that the sum is n x (2n + 1) x (n + 1) / 6
	 */
	return n * (2 * n + 1) * (n + 1) / 6
}

func squaresInRectangle(n, m uint64)uint64{
	/**
	 using the same logic, as in squaresInSquare one can divide the rectangle in
	 the square and as smaller rectangle:

	 4 4 4 3 2 1    4 4		4 3 2 1
	 3 3 3 3 2 1  = 3 3  +	3 3 2 1
	 2 2 2 2 2 1    2 2		2 2 2 1
	 1 1 1 1 1 1    1 1		1 1 1 1
	 */
	min, delta := uint64(0), uint64(0)
	if n > m{
		min, delta = m, n - m
	} else {
		min, delta = n, m - n
	}

	return min * (2 * min + 1) * (min + 1) / 6 + delta * n * (n + 1) / 2
}

func eulerianNumber(n, m int) int {
	// https://en.wikipedia.org/wiki/Eulerian_number
	A := make([][]int, n + 1)
	a := make([]int, (n + 1) * (m + 1))
	for i := range A {
		A[i] = a[i*(m + 1) : (i+1)*(m + 1)]
	}
	for i := 1; i <= n; i ++ {
		A[i][0] = 1
	}

	for n_ := 2; n_ <= n; n_++{
		for m_ := 1; m_ <= m; m_++ {
			A[n_][m_] = (n_ - m_) * A[n_ - 1][m_ - 1] + (m_ + 1) * A[n_ - 1][m_]
		}
	}

	return A[n][m]
}

func squareMatrixMultiplication(A, B [][]int, mod int) [][]int {
	// Multiplication of 2 NxN matrices modulo mod. Does not check that slices are actual matrices
	n := len(A)

	M := make([][]int, n)
	a := make([]int, n * n)
	for i := range M {
		M[i] = a[i*n:(i+1)*n]
	}

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			for k := 0; k < n; k++ {
				M[i][k] = (M[i][k] + A[i][j] * B[j][k]) % mod
			}
		}
	}

	return M
}

func printMatrix(M [][]int){
	for _, v := range M {
		fmt.Println(v)
	}
}

func matrixExponentiation(A [][]int, n, mod int){
	for ; n > 0; {
		fmt.Println("\t\t", n, n % 2)
		printMatrix(A)
		n /= 2
		A = squareMatrixMultiplication(A, A, mod)
	}
}

func main(){
	a := [][]int{
		[]int{1, 1, 1},
		[]int{0, 0, 1},
		[]int{0, 1, 0},
	}
	mod := 100000
	res := squareMatrixMultiplication(a, a, mod)
	printMatrix(res)
	matrixExponentiation(a, 10, mod)
}
