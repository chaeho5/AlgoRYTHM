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

	var n, score int
	fmt.Fscan(reader, &n)

	scoreBasket := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &score)
		scoreBasket[i] = score
	}

	maxScore := scoreBasket[0]
	for _, v := range scoreBasket {
		if v > maxScore {
			maxScore = v
		}
	}

	var sum float64
	for _, v := range scoreBasket {
		sum += (float64(v) / float64(maxScore)) * 100
	}


	fmt.Fprintf(writer, "%.10f\n",sum/float64(n))
}