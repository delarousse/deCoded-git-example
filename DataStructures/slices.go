package main

import "fmt"

func main() {

	slice := make([]string, 3)
	fmt.Println("emp:", slice)

	slice[0] = "a"
	slice[1] = "b"
	slice[2] = "c"
	fmt.Println(slice)

	fmt.Println(slice[2])

	fmt.Println(len(slice))

	slice = append(slice, "d")
	slice = append(slice, "e", "f")
	fmt.Println("apd:", slice)

}
