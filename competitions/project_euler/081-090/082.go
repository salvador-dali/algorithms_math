package main
import (
	"fmt"
	"bufio"
	"os"
    "strconv"
	"strings"
)

func print(m [][]uint64){
	for _, v := range(m){
		fmt.Println(v)
	}
}

func path(m, n [][]uint64)uint64{
	for j := 1; j < len(m[0]); j++{
		for i := 0; i < len(m); i++{
			min := m[i][j - 1]
			if i > 0{
				attempt := m[i - 1][j]
				if attempt < min{
					min = attempt
				}
			}
			m[i][j] += min
		}

		for i := len(m) - 2; i >= 0; i--{
			n[i][j] += n[i + 1][j] + n[i + 1][j - 1]
			if n[i][j] < m[i][j]{
				m[i][j] = n[i][j]
			}
		}
		fmt.Println()
	}

	min := m[0][len(m[0]) - 1]
	for i := 0; i < len(m); i++ {
		if m[i][len(m[0]) - 1] < min{
			min = m[i][len(m[0]) - 1]
		}
	}

	print(m)
	return min
}

func readMatrix()[][]uint64{
    scanner := bufio.NewScanner(os.Stdin)
    matrix  := [][]uint64{}
	for scanner.Scan() {
        line := []uint64{}
        for _, v := range(strings.Fields(scanner.Text())){
            num, _ := strconv.Atoi(v)
            line = append(line, uint64(num))
        }
        matrix = append(matrix, line)
    }
    return matrix
}

func main(){
//	matrix := readMatrix()

	m1 := [][]uint64{
		[]uint64{9, 9, 9, 9, 9},
		[]uint64{3, 0, 0, 0, 5},
		[]uint64{4, 0, 5, 0, 6},
		[]uint64{4, 0, 3, 0, 0},
		[]uint64{2, 0, 3, 1, 9},
	}

	m2 := [][]uint64{
		[]uint64{9, 9, 9, 9, 9},
		[]uint64{3, 0, 0, 0, 5},
		[]uint64{4, 0, 5, 0, 6},
		[]uint64{4, 0, 3, 0, 0},
		[]uint64{2, 0, 3, 1, 9},
	}
	fmt.Println(path(m1, m2))
}
