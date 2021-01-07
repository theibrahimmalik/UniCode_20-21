# Challenge Details: 

I am Devvie. Over recent units of time I have been tasked with moving my physical forms using commands given to me by my controllers. I can process 3 commands:



`F - take a step forward`
`L - turn 90 degrees to the left`
`R - turn 90 degrees to the right`


An example: "FLF" instructs me to take one step forward, then turn left by 90 degrees, then take one step forward.



A major inefficiency: I have calculated that my controllers are not providing me with optimal instructions to return to my starting position.



A proposition: I task you with writing a function that returns the number of commands that I will need to return to my starting point, so that I may evaluate their intent.



`"RF" must return 3 - I must RRF in order to return to 0,0`

`"LFRFRFR" must return 1 - I must F to return to 0,0`


An unhandled command: Sometimes my controllers provide me with unhandled parameters, take care to ignore any unwanted noise in the commands.

