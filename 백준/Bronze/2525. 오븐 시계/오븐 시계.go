package main

import (
	"fmt"
	"bufio"
	"os"
)

var reader = bufio.NewReader(os.Stdin)

func main() {
	var h, m, needtime int
	fmt.Fscan(reader, &h, &m, &needtime)
	lastminute := m + needtime

	h = (h +  lastminute/60) % 24
	lastminute = lastminute % 60

	fmt.Printf("%v %v", h, lastminute)
}