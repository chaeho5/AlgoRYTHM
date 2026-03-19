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
	result := 0
	for i:=1; i<=n; i++ {
		result += i
	}
	fmt.Println(result)
}