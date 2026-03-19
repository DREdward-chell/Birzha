package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
)

func main() {
	log.Printf("Starting server on http://%s:%s", os.Getenv("HOSTNAME"), os.Getenv("BACKEND_PORT"))

	log.Fatal(http.ListenAndServe(fmt.Sprintf("%s:%s", os.Getenv("HOSTNAME"), os.Getenv("BACKEND_PORT")), nil))
}
