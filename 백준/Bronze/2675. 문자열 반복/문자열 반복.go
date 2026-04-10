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

	var t, r int
	var s string
	fmt.Fscan(reader, &t)
	for i := 0; i < t; i++ {
		fmt.Fscan(reader, &r, &s)
		for _, v := range s {
			for i := 0; i < r; i++ {
				fmt.Fprintf(writer, "%c", v)
			}
		}
		fmt.Fprintln(writer)
	}
}
