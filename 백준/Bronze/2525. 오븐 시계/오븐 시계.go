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

	if lastminute % 60 == 0 {
		h += lastminute/60
		if lastminute >= 60 {
			lastminute = lastminute -60
			if lastminute == 60 {
				lastminute = 0
			}
		}
	} else if lastminute >= 60 {
		h += lastminute/60
		lastminute = lastminute%60
	}

	if h > 23 {
		h = h%24
	}

	fmt.Printf("%v %v", h, lastminute)
}