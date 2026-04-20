package main

import (
    "fmt"
    "bufio"
    "os"
    "strings"
)

var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

func main() {
    defer writer.Flush()
    var s1 string
    var a int
    fmt.Fscan(reader, &s1, &a)
    fmt.Fprint(writer, strings.Repeat(s1, a))
    
}