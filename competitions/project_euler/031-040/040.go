/**
 if one will write the constant, it will look like
 1234567891011121314..
 note that first 9 numbers are of length 1
 then follows 90 numbers of length 2
 then 900 numbers of length 3 and so on

 so the first step is to find out on which number were are currently
 this can be done by subtracting 9 * 10^i * i from the pos till the difference is
 smaller than the next number to subtract.

 the number will be the difference with 99..9 and the position
 will be difference % i.
 For some reason this does not give correct result if n % 10 == 9 && pos % 10 != 9
 */

package main
import (
    "fmt"
    "os"
    "bufio"
    "strings"
    "strconv"
    "bytes"
)

func getPos(pos uint64)uint64{
	num := uint64(9)
	i := uint64(1)
	dec := uint64(1)
	for num < pos{
		i++
		dec *= 10
		num += i * dec * 9
	}

	pos2 := pos - num + i * dec * 9
	n := pos2 / i + dec - 1
	k := int(pos2 % i) - 1

	if n % 10 == 9 && pos % 10 != 9{
		n++
	}
	arr := []uint64{}
	for n > 0{
		arr = append([]uint64{n % 10}, arr...)
		n /= 10
	}

	if k < 0{
		k += len(arr)
	}
	return arr[k]
}

func makeCalc(arr []string)uint64{
    pos := uint64(1)
    for _, v := range(arr){
        n, _ := strconv.Atoi(v)
        pos *= getPos(uint64(n))
    }
    return pos
}

func main(){
    var T int
    fmt.Scanf("%d", &T)
    var scanner = bufio.NewScanner(os.Stdin)
    var buffer bytes.Buffer
    for T > 0 {
        T--
        scanner.Scan()
        res := makeCalc(strings.Fields(scanner.Text()))
        a := strconv.Itoa(int(res)) + "\n"
		buffer.WriteString(a)
    }
    fmt.Print(buffer.String())
}
