package main

import (
	"bufio"
	"fmt"
	"os"
)

var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

func main() {
	defer writer.Flush()

	var n int
	var s string

	fmt.Fscanln(reader, &n)
	fmt.Fscan(reader, &s)

	sum := 0

	for _, v := range s {
		sum += int(v - '0')
	}

	fmt.Fprint(writer, sum)
}