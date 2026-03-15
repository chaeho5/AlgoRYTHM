package main

import (
	"fmt"
	"bufio"
	"os"
)

var reader = bufio.NewReader(os.Stdin)

func main() {
	var A, B int
	fmt.Fscan(reader, &A, &B)
	fmt.Println(A * B)
}