package main

import (
	"fmt"
	"bufio"
	"os"
)

var reader = bufio.NewReader(os.Stdin)

func main() {
	var t, a, b int
	fmt.Fscan(reader, &t)

	for i:=0; i < t; i++ {
		fmt.Fscan(reader, &a, &b)
		fmt.Println(a + b)
	}
}