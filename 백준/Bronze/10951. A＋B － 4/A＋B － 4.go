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

	for {
		_, err := fmt.Fscan(reader, &a, &b)

		if err != nil {
			break
		}

		fmt.Fprintln(writer, a + b)
	}
}