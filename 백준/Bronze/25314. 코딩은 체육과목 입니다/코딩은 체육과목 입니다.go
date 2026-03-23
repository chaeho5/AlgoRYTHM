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
	longstring := "long "
	result := ""

	for i:=0; i < n/4; i++ {
		result += longstring
	}

	fmt.Print(result + "int")
}