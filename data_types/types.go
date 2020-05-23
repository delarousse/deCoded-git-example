package main

import (
	"fmt"
)

func main() {
	// STRING
	nickname := "Debby Debs"

	// INT
	var moneyInChecking int64
	// because we declared the variable as an int64 we have to use an '=' instead of ':=' because it is not actually an int64 so you can't make it an exactly value without getting an error
	moneyInChecking = 14

	// FLOAT
	money_in_savings := 3.50

	// BOOL
	am_i_broke := true

	fmt.Printf("%T\n", nickname)
	fmt.Printf("%T\n", moneyInChecking)
	fmt.Printf("%T\n", money_in_savings)
	fmt.Printf("%T\n", am_i_broke)

}
