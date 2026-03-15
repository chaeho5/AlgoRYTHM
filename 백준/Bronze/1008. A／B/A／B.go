package main

import (
	"fmt"
	"bufio"
	"os"
)

var reader = bufio.NewReader(os.Stdin)

func main() {
	var A, B float64
	fmt.Fscan(reader, &A, &B)
	fmt.Printf("%.10f\n", A / B)
}