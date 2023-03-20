t <html><head><title>RTC</title>
t <script language=JavaScript type="text/javascript" src="xml_http.js"></script>
t <script language=JavaScript type="text/javascript">
# Define URL and refresh timeout
t var formUpdate = new periodicObj("rtc.cgx", 500);
t function plotADGraph() {
t  hourVal = document.getElementById("hour").value;
t  dateVal = document.getElementById("date").value;
t  document.getElementById("hour").value = (hourVal);
t  document.getElementById("date").value = (dateVal);
t }
t function periodicUpdateAd() {
t  if(document.getElementById("TiChkBox").checked == true) {
t   updateMultiple(formUpdate,plotADGraph);
t   Ti_elTime = setTimeout(periodicUpdateAd, formUpdate.period);
t  }
t  else
t   clearTimeout(Ti_elTime);
t }
t </script></head>
i pg_header.inc
t <h2 align="center"><br>RTC</h2>
t <p><font size="2">This page shows you the hour and date, which is also displayed on LCD Module. 
t It also allows you to configure this parameters.</font></p>
t <form action="rtc.cgi" method="post" name="rtc">
t <input type="hidden" value="rtc" name="rtc">
t <table border=0 width=99%><font size="3">
t <tr style="background-color: #aaccff">
t  <th width=15%>Hour</th>
t <td align="center"><input type="text" readonly style="background-color: transparent; border: 0px"
c h 1  size="10" id="hour" value="%s"></td></tr>
t  <th width=15%>Date</th>
t <td align="center"><input type="text" readonly style="background-color: transparent; border: 0px"
c h 2  size="10" id="date" value="%s"></td>
t </font></table>
t <p align=center>
t <input type=button value="Refresh" onclick="updateMultiple(formUpdate,plotADGraph)">
t Periodic:<input type="checkbox" id="TiChkBox" onclick="periodicUpdateAd()">
t </p></form>
i pg_footer.inc
. End of script must be closed with period.