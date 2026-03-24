package main

import (
	"fmt"
	"bufio"
	"os"
)

var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

func main() {
	defer writer.Flush()
	var t, a, b int
	fmt.Fscan(reader, &t)

	for i := 0; i < t; i++ {
		fmt.Fscan(reader, &a, &b)
		fmt.Fprintln(writer, a + b)
	}
}