package main

import (
	"fmt"
	"bufio"
	"os"
)

var reader = bufio.NewReader(os.Stdin)

func main() {
	var A, B, C int

	fmt.Fscan(reader, &A, &B, &C)

	fmt.Println((A+B)%C)
	fmt.Println(((A%C)+(B%C))%C)
	fmt.Println((A*B)%C)
	fmt.Println(((A%C)*(B%C))%C)
}