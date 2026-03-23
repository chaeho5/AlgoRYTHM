package main

import (
	"fmt"
	"bufio"
	"os"
)

var reader = bufio.NewReader(os.Stdin)

func main() {
	var x, n, a, b int
	fmt.Fscan(reader, &x, &n)
	result := 0

	for i := 0; i < n; i++{
		fmt.Fscan(reader, &a, &b)

		result += a*b
	}

	if result == x {
		fmt.Print("Yes")
	} else {
		fmt.Print("No")
	}


}