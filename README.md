# HackPadRednadp
I have tried to create a pad similar to the stremdeck, or at least that was the idea. I have never made something similar and I have found some difficulties along the way. If you want to mount yourself the Pad you will need the materials listed bellow and the 3d-printed case.
# Final build
![20260219_220154 (1)](https://github.com/user-attachments/assets/a1d9c116-9c11-411e-a9b5-e431908bc59c)

# Journal
# 2/7/2026 - Mounting the pcb day 1  

_Time spent: 2.0h_  

Hello, today I have been trying to figure out how to solder the components to the PCB. After watching some YouTube tutorials, I have "learned" how to solder, but when I tried to put it into practice, I encountered some problems. The first one was figuring out the positions of the components. Once that was solved, I started soldering the LED, but I had some difficulties because the pins were connecting to each other. Finally, I successfully managed to fix that, but with all those problems, I only had time to connect the LED and the diodes. I spent around 2 hours. I will continue another day. Again, sorry for my English it is not my native language :)
![20260207_195400](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6OTk4OTksInB1ciI6ImJsb2JfaWQifX0=--088d3a9ad476fece6b832865e273369a600180b7/20260207_195400.jpg)

![20260207_181344](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6OTk5MDAsInB1ciI6ImJsb2JfaWQifX0=--7ea3b09df4cace087c942fead3ee6dcb2369e7f9/20260207_181344.jpg)

  

# 2/10/2026 10 PM - Mounting the pcb day 2  

_Time spent: 3.0h_  

Hello, today I have finished mounting all the parts to the pcb. I have found some difficulties in aligning the screen with the top plate perfectly as I have to leave a space between them because if not, the screen is too low to be seen with the cover putted.

![20260210_205520](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTAxODE1LCJwdXIiOiJibG9iX2lkIn19--a1043b808866d296d988f9ab9e9df797a0b0d07e/20260210_205520.jpg)
![20260210_220200](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTAxODE2LCJwdXIiOiJibG9iX2lkIn19--4a00f8d0ad9502ae2a9862f029e44a7758f1fb59/20260210_220200.jpg)![20260210_220321](/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTAxODE3LCJwdXIiOiJibG9iX2lkIn19--ca3ed5c32b82c0f6b9bd10886d1707a3005146cf/20260210_220321.jpg)



Another difficulty that I have encountered has been inserting the inserts into the cover. I have never made it and I have made the error of not watching any tutorial, so I have done horribly bad and I will need to reprint the case and try another form of gathering the top and the bottom. The screws don't enter into the hole as it is deformed.
![20260210_221225](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTAxODE4LCJwdXIiOiJibG9iX2lkIn19--3206ddbabc595c004cb8239fbdd42b7c15ec7922/20260210_221225.jpg)
![20260210_221238](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTAxODE5LCJwdXIiOiJibG9iX2lkIn19--48be502e4ed7fdf840dc6f469eee64965b868f22/20260210_221238.jpg)

I also realize the necessity of modeling some stuff to turn the potentiometer better.

  

# 2/10/2026 11 PM - Making Rotary encoder more beautiful  

_Time spent: 0.5h_  

Hello again. I have designed stuff to put in the rotary encoder to make it more beautiful. Sadly for me I have adjusted the tolerances badly and I have to redo it again setting a compensation of -0,4mm. And, again, I have made bad adjustments so I finall decided to modify the design to make it properly.

Design:
![Captura de pantalla (13)](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTAxOTA1LCJwdXIiOiJibG9iX2lkIn19--8950e6998ce16a4eb077393caebe3316abac3630/Captura%20de%20pantalla%20(13).png)

1st attempt:

![20260210_225834](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTAxOTA0LCJwdXIiOiJibG9iX2lkIn19--1b24db1d7ae864e92db8f9a9a27fa8b0cfeaff79/20260210_225834.jpg)
Other attempts:
![20260210_233629](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTAxOTM0LCJwdXIiOiJibG9iX2lkIn19--1614c330e8af655f157387963e81cd59ee84aea5/20260210_233629.jpg)


  

# 2/17/2026 - Trying to configure the  firmware  

_Time spent: 4.0h_  

Hello, today I have suffered trying to configure the firmware. I have installed KMK into the Xiao and put all the libraries on their site. I have found some difficulties to see the errors (I have tried to use arduino IDE but after a nice talk with Gemini I have given up and I have donwloaded a program called Mu editor). I have copied the code that I did and I have realised the first problem, the pins. They were different from the diagram, (or thats what I think after intensive research on the internet and with Gemini). Finally, I have gotten the pin layout (d1, d2, etc). Then I had changed the pinout only to realise that the last row of keys was not working. Fixing that has been a terrible task. I have spent around 2 whole hours trying to figure out what was happening, if it was the pinout, another thing in the code or the hardware itself. Finally, it has resulted in one solder of the chip. This has cost me a lot of time because I was checking the connections between the keys and the connections of the pins that went to the xiao but not the connections with the pins and the Xiao (which was the real problem).

![20260217_192003](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA2MzE2LCJwdXIiOiJibG9iX2lkIn19--679b29071f5eec1579e13f50d475d46843e0a7c6/20260217_192003.jpg)

The diagram that I have make to have clear the pins: (I know, I am an artist)

![arte](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA2MzI3LCJwdXIiOiJibG9iX2lkIn19--0322eb8fa9cc3ae3ebf527b38ee32b6cc25f5cb3/arte.jpg)

Then, I have written the code to display things on the oled display. This has cost me another horrible hour of debugging as I had used a wrong library that was called exactly the same :). Then the text in the display was the other way around. Gemini was saying something about rotate and this has only confused me. Finally, checking the cases of the library, I have discovered that it was flip instead of rotate.

![20260217_185203](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA2MzE3LCJwdXIiOiJibG9iX2lkIn19--f85855abdd8e20ec45208f28034a620870e07dc7/20260217_185203.jpg)


Finally, when I wrote the code to use the leds these have not been put on. I have spent another hour trying to figure out that when I was designing the pcb I used a footprint that was intended for underglow the key. 

I am really tired after debugging problems all the afternoon so I will need to desolder all the leds and solder them all the other way around other day as I cannot redesign the pcb. This is an unexpected change so probably I will have to redesign the case to make it more finer the base to let the ligh pass though it.  

# 2/18/2026 - Give up on LEDS  

_Time spent: 1.5h_  

Bad news, I won't be able to make work the leds. Today I have started trying to desolder the first led (what a difficult task). After literally destroying the led and scratching a lot to expose the connections I have been able to solder a new led.

Leds before solding:
![20260218_210817](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA2ODcwLCJwdXIiOiJibG9iX2lkIn19--e40496d2f216359928a6e2ed035cce58f50c8935/20260218_210817.jpg)

Fist led solded and comparison with the destroyed one:
![20260218_215222](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA2ODcxLCJwdXIiOiJibG9iX2lkIn19--5fd479d42236305ee9cb1abad68951900819163c/20260218_215222.jpg)

I have made all the continuity checks with the multimeter and checked that it receives 5v. For my desperation, the led was still not working so I started to realise that maybe the only problem was not the position of the led (that the blueprint that I have used is for underlight the key, not for the key itself) but the pins order. Comparing with the docs of the led I started to suspect that even changing the direction of the led the information pins (In and Out) were upside down so it would be impossible making them work without redesigning the pcb (something impossible, unfortunately). To corroborate that theory, I have asked the help of my brother and my dad to connect another led with cables directly (tanks for your help :) and, by the way, discarding code or other types of errors.

![20260218_223222](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA2ODcyLCJwdXIiOiJibG9iX2lkIn19--7383f3d2dd9efaaf8f4c12a481cf6fce874f21a2/20260218_223222.jpg)
![20260218_223239](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA2ODczLCJwdXIiOiJibG9iX2lkIn19--738ef19bedb66b8b7710781550678ad05f29b7ea/20260218_223239.jpg)


Sadly, my theory was confirmed. The layout of the pins in the pcb was incorrect and there was no way of putting them in a way that they would work. I have had to refuse to use them. With all this, I will make the final touches, and I will test everything.  

# 2/19/2026 - Final touches  

_Time spent: 0.5h_  

Hello, this is my last Journal (or thats what I hope so). I have finished the proyect :))) I'm super happy as it has been my first hadware proyect, and also my first proyect in all hackclub. Thanks to all people making this possible.

I have mount the pad again and I have made some changes to the code to show in the screen the current volume.

![20260219_212836](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA3NTI5LCJwdXIiOiJibG9iX2lkIn19--6b07031cd3431d1b6790e111fb3a6053f2c37042/20260219_212836.jpg)
  

# 3/4/2026 - Updated Readme  

_Time spent: 0.5h_  

Hello, I have updated the readme to show the final build as it has been especified by the reviewer. I hope this will make able to ship the HackPad finally.

![Captura de pantalla (15)](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTE1MjQwLCJwdXIiOiJibG9iX2lkIn19--6ef350771498b9d412eec89aa49499775cc51965/Captura%20de%20pantalla%20(15).png)
  

# Bill of Materials
 - Seeed XIAO RP2040
 - Through-hole 1N4148 Diodes (x9)
 - MX-Style switches (x9)
 - EC11 Rotary encoder
 - 0.91 inch OLED display
 - Blank DSA keycaps
 - SK6812 MINI-E LEDs (x8)
 - M3x16mm screws (x4)
 - M3x5mx4mm heatset inserts (x4)
 - Printed parts
# Photos
<img width="1188" height="580" alt="image" src="https://github.com/user-attachments/assets/6097e26a-490d-4440-aa4d-e0c80050fb1e" />
<img width="818" height="495" alt="image" src="https://github.com/user-attachments/assets/28b65bcf-719f-423a-bc1a-a4aba5319f37" />
<img width="1116" height="589" alt="image" src="https://github.com/user-attachments/assets/ed2fe187-7325-48d8-896c-186fbd04d0ca" />
<img width="803" height="552" alt="image" src="https://github.com/user-attachments/assets/360a4907-e82d-4bb7-bf7b-5ea82a1f7def" />


