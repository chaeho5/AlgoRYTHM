package main

import (
	"fmt"
	"bufio"
	"os"
)

var reader = bufio.NewReader(os.Stdin)

func main() {
	var n int
	fmt.Fscan(reader, &n)

	for i := 1; i < 10; i++ {
		fmt.Printf("%v * %v = %v\n", n, i, n*i)
	}
}