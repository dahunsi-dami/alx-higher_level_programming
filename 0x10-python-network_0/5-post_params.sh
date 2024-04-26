#!/bin/bash
# Takes in URL, sends POST request & show response body
curl -X POST -sd "email=test@gmail.com&subject=I will always be here for PLD" $1
