//https://www.hackerrank.com/challenges/sherlock-and-moving-tiles
package main

import (
    "fmt"
    "math"
)

func main() {
    var L, S, S1, S2, Q, q int
    fmt.Scan(&L, &S1, &S2, &Q)
    S = S2 - S1
    if S < 0 {
        S = -S
    }
    s := float64(S) / math.Sqrt(2)
    for i := 0; i < Q; i++ {
        fmt.Scan(&q)
        fmt.Println((float64(L) - math.Sqrt(float64(q)))/s)
    }
}
