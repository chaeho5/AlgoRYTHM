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
	var a, b int
	fmt.Fscan(reader, &a, &b)

	for a != 0 && b != 0 {
		fmt.Fprintln(writer, a + b)
		fmt.Fscan(reader, &a, &b)
	}
}