# Izitafauxty Keyboard

<img src="https://github.com/ElKinoflop/Izitafauxty/blob/main/images/PXL_20241116_132735092~2.jpg" alt="Izitafauxty Keyboard Photo">

Stacked acrylic keyboard case designed for handwiring with a <a href="https://www.waveshare.com/wiki/RP2040-Tiny" target="_blank">Waveshare RP2040-Tiny</a>. Main cluster is minivan sized (12.75u) with an added F-Row and numpad (standard or southpaw).

Feel free to do whatever you want with the files. If you have any questions just ask (Discord username elkinoflop) and if you make one then share a photo with me!

<h1>Layout</h1>
<img src="images/Izitafauxty Southpaw KLE.jpg" alt="Izitafauxty KLE Image">

<h1>KLE Raw Data</h1>
Standard:
[{y:1},"F1\n1","F2\n2","F3\n3","F4\n4",{x:0.375},"F5\n5","F6\n6","F7\n7","F8\n8",{x:0.375},"F9\n9","F10\n0","F11","F12\nDel",{x:0.375},"Num Lock","/\n-","*\n+"],
[{y:0.375},"Esc","Q","W","E","R","T","Y","U","I","O","P",{a:6,w:1.75},"Backspace",{x:0.375,a:4},"7\nHome","8\n↑","9\nPgUp"],
[{w:1.25},"Caps Lock","A","S","D","F","G","H","J","K","L","@\n'",{a:6,w:1.5},"Enter",{x:0.375,a:4},"4\n←","5","6\n→"],
[{w:1.75},"Shift","Z","X","C","V","B","N","M","<\n,",">\n.","↑",{x:1.375},"1\nEnd","2\n↓","3\nPgDn"],
[{y:-0.995,x:11.75},"Shift"],
[{y:-0.005},"Ctrl",{w:1.25},"Win","Alt",{a:7,w:1.25},"",{x:4.75,a:4,w:1.25},"←",{x:2.625},"0\nIns",".\nDel",{a:6},"Enter"],
[{y:-0.995,x:4.5,a:7,w:1.75},"",{x:1.75,w:1.25},"",{x:1.25,a:4},"↓",{w:1.25},"→"],
[{y:-0.99,x:6.25,a:7,w:1.75},""]
<p></p>
  Southpaw:
[{x:0.13},"Num Lock","/\n-","*\n+",{x:0.37},"F1\n1","F2\n2","F3\n3","F4\n4",{x:0.38},"F5\n5",{x:0},"F6\n6","F7\n7","F8\n8",{x:0.37},"F9\n9","F10\n0","F11","F12\nDel"],
[{y:0.38,x:0.13},"7\nHome","8\n↑","9\nPgUp",{x:0.37},"Esc","Q","W","E","R","T","Y","U","I","O","P",{a:6,w:1.75},"Backspace"],
[{x:0.13,a:4},"4\n←","5","6\n→",{x:0.37,w:1.25},"Caps Lock","A","S","D","F","G","H","J","K","L","@\n'",{a:6,w:1.5},"Enter"],
[{x:0.13,a:4},"1\nEnd","2\n↓","3\nPgDn",{x:0.37,w:1.75},"Shift","Z","X","C","V","B","N","M","<\n,",">\n.","↑","Shift"],
[{x:0.13},"0\nIns",".\nDel",{a:6},"Enter",{x:0.37,a:4},"Ctrl",{w:1.25},"Win","Alt",{a:7,w:1.25},"",{w:1.75},"",{x:1.75,w:1.25},"",{a:4,w:1.25},"←","↓",{w:1.25},"→"],
[{y:-0.99,x:9.75,a:7,w:1.75},""]

<h1>Case</h1>
<ul>
  <li>Designed to be cut from 3mm acrylic</li>
</ul>

<img src="https://github.com/ElKinoflop/Izitafauxty/blob/main/images/izitafauxtycasecombined.png" alt="Izitafauxty Case Layers">

<h1>Bill of Materials</h1>
<ul>
  <li>One of each DXF file (except for the plate) cut from 3mm acrylic. You only need 1x layer 1 and 1x layer 2 piece cut depending on whether you want standard or southpaw</li>
  <li>Plate DXF file cut from 1.5mm/1.6mm material of your choice. I've only tested this with carbon, plastic might be too flexy.</li>
  <li><a href="https://www.waveshare.com/wiki/RP2040-Tiny" target="_blank">Waveshare RP2040-Tiny</a></li>
  <li>M2 Standoffs with a outside diameter of 3mm. Various lengths. <a href="https://amzn.eu/d/8H1HG6Y" target="_blank">Amazon Standoffs</a></li></li>
  <li>M2 Hex socket button head bolts. Various lengths. <a href="https://www.aliexpress.com/item/32969042589.html" target="_blank">AliExpress bolts</a></li>
  <li>M2 Washers. To space the plate downwards to tune the keycap height (normally 2mm worth under each plate mounting bolt). Also for under the bolt heads that hold the daughterboard in.<a href="https://www.aliexpress.com/item/1005003697132040.html" target="_blank">AliExpress M2 0.5mm thickness plastic washers</a></li>
<li>M2 nuts to hold the daughterboard. Included with the standoffs linked above</li>
  <li>Wire! Solid core 22 AWG suggested</li>
  <li>73x MX Switches</li>
  <li>73x 1N4148 Diodes</li>
</ul>

<h1>Firmware</h1>
I used <a href="https://github.com/JanLunge/pog" target="_blank">POG</a>  to create <a href="https://github.com/KMKfw/kmk_firmware" target="_blank">KMK</a> firmware. POG makes creating firmware super simple but I might learn how to create QMK/VIAL firmware at some point!
I have included my firmware files (generated by POG). 

If you have wired up the matrix and connected it to the same controller pins as I have then you should be able to use my firmware. Install <a href="https://circuitpython.org/board/waveshare_rp2040_tiny/" target="_blank">Circuit Python</a> onto the controller first and then copy all the files from <a href="https://github.com/ElKinoflop/Izitafauxty/tree/main/KMK%20Firmware" target="_blank">'KMK Firmware'</a> onto the drive

<h1>Handwired Matrix</h1>
This is how I handwired the Matrix.
<img src="https://github.com/ElKinoflop/Izitafauxty/blob/main/images/izitafauxty%20matrix.jpg" alt="Izitafauxty Handiwired Matrix">

<h1>Case Assembly</h1>
If you find some of the standoffs tight to push through don't force them. Use a small round file if you need to slightly widen any holes. The small round file from Draper 'Soft Grip Needle File Set, 140mm (6 Piece) (83982)' is the perfect size.

<img src="https://github.com/ElKinoflop/Izitafauxty/blob/main/images/PXL_20241116_132842963~2.jpg" alt="Izitafauxty Keyboard Photo">
