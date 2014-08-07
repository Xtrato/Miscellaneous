MasscanWebshot
===========
<h2>About</h2>
This program takes a masscan XML file and iterates through it taking screenshots of the webpages. You can also input files generated by Nmap. It uses the <a href="http://wkhtmltopdf.org/">wkhtmltopdf</a> software to do this.

<h2>Installation:</h2>
First install the wkhtmltopdf program<br>
<code>wget https://wkhtmltopdf.googlecode.com/files/wkhtmltoimage-0.11.0_rc1-static-i386.tar.bz2</code><br>
copy the program to /usr/local/bin<br>
<code>cp wkhtmltoimage-i386 /usr/local/bin</code><br>
If you havent already download git<br>
<code>sudo apt-get install git</code><br>
And then download this script<br>
<code>git clone https://github.com/Xtrato/MassscanShots</code><br>
<code>cd MassscanShots</code>

<h2>Usage</h2>
Perform an Nmap or Masscan for decives hosting web content. (Usually scan for port 80 or 8080). Use the -oX tag to produce an XML output that can be imported into this script.<br>
Execute the MassscanShots with -x /loc/to/xml/file.xml<br>
Example: <code>python massscanShots -x result.xml</code><br>
Screenshots of each webpade will be saved in the current directory.