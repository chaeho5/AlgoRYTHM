package main

import (
	"fmt"
	"bufio"
	"os"
)

var reader = bufio.NewReader(os.Stdin)

func main() {
	var h, m int
	fmt.Fscan(reader, &h, &m)

	if m < 45 {
		h -= 1
		m = 60-45+m
	} else {
		m = m-45
	}

	if h < 0 {
		h = 24 + h
	}
	fmt.Printf("%v %v", h, m)
}