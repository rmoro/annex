#Project Annex

##Description
Annex aims to add to the many other studies in keystroke dynamics by providing a slightly different
approach to authentication. By continously logging a users keystrokes we can feed them into a
recurrent neural network (RNN) in the form of a summation of the dwell and flight times between
each key press event. After training with only 100,000 key events our RNN was able to detect the
user it was trained on within a 0.7% accuracy.


Initially ANNEX must be trained with the desired users trusted keystrokes. This can be ac-
complised over a few logged typinging sessions. Once the RNN is trained to the desired accuracy
the program is put into monitoring mode where it decideds every 50 keystrokes if the user typing
matches that of the accepted user

Initially ANNEX must be trained with the desired users trusted keystrokes. This can be ac-
complised over a few logged typinging sessions. Once the RNN is trained to the desired accuracy
the program is put into monitoring mode where it decideds every 50 keystrokes if the user typing
matches that of the accepted user


##RNN
ANNEX is built on top of tensorflow recurrent neural netork. Each keyevent is inputted through
the network with 3 normalized values. The three inputs are the first key pressed, the second key
pressed and the summation of the dwell time and flight time between the 2 press events. Each input
is normalized to a range of
0.0000000 to 1.0000000. This was done through a process called unity
based normalization where a known range can be reduced to [0,1].


##Contact
- AUTHORS:   Robert Morouney, David Rusu
- EMAILS:    robert@morouney.com, davidrusu.me@gmail.com
