import json
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree
import string
import re
import os
from time import localtime, strftime, gmtime, strptime, mktime

p = ({"Name": "BEXAR COUNTY ELECTIONS(BOTH)", "AddressLine": "10/24/2022-10/28/2022 08:00 AM-06:00 PM", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78207"},)
data = {
    "electionDayVoting": [
        {"Name": "ADAMS ELEMENTARY SCHOOL", "AddressLine": "135 E. SOUTHCROSS", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78214", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ADAMS HILL ELEMENTARY SCHOOL", "AddressLine": "9627 ADAMS HILL DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78245", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ADANTE INDEPENDENT LIVING", "AddressLine": "2702 CEMBALO BLVD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78230", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "AGNES COTTON ACADEMY", "AddressLine": "1616 BLANCO RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78212", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ALAMO HEIGHTS CITY HALL", "AddressLine": "6116 BROADWAY ST.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78209", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ALAMO HEIGHTS UNITED METHODIST", "AddressLine": "825 E. BASSE RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78209", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ALAMO STADIUM CONVOCATION CENTER", "AddressLine": "110 TULETA DR.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78212", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ALAN B. SHEPARD MIDDLE SCHOOL", "AddressLine": "5558 RAY ELLISON BLVD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78242", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ANTONIO MARGIL ELEMENTARY SCHOOL", "AddressLine": "1000 PEREZ STREET", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78207", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ARTEMISIA BOWDEN ACADEMY", "AddressLine": "515 WILLOW ST.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78202", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "AUE ELEMENTARY SCHOOL", "AddressLine": "24750 BAYWATER STAGE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78255", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BALL ACADEMY", "AddressLine": "343 KOEHLER COURT", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78223", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BARKLEY-RUIZ ELEMENTARY SCHOOL", "AddressLine": "1111 S. NAVIDAD STREET", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78207", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BEACON HILL ACADEMY", "AddressLine": "1411 W. ASHBY PL.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78201", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BEARD ELEMENTARY SCHOOL", "AddressLine": "8725 SONOMA PKWY", "Locality": "HELOTES", "AdminDistrict": "TX", "PostalCode": "78023", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BELLA CAMERON ELEMENTARY SCHOOL", "AddressLine": "3635 BELGIUM DR.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78219", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BETHANY ROMANIAN CHURCH", "AddressLine": "26347 BOERNE STAGE RD.", "Locality": "BOERNE", "AdminDistrict": "TX", "PostalCode": "78006", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BEXAR COUNTY ELECTIONS(BOTH)", "AddressLine": "1103 S. FRIO", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78207", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BEXAR COUNTY JUSTICE CENTER(BOTH)", "AddressLine": "300 DOLOROSA", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78205", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BIG COUNTRY ELEMENTARY SCHOOL", "AddressLine": "2250 PUE ROAD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78245", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BLOSSOM ATHLETIC CENTER", "AddressLine": "12002 JONES MALTSBERGER RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78216", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BOB HOPE ELEMENTARY SCHOOL", "AddressLine": "3022 REFORMA", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78211", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BOBBYE BEHLAU ELEMENTARY SCHOOL", "AddressLine": "2355 CAMP LIGHT WAY", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78245", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BODE COMMUNITY CENTER", "AddressLine": "900 RIGSBY", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78210", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BOONE ELEMENTARY SCHOOL", "AddressLine": "6614 SPRING TIME DR.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78249", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BRADLEY MIDDLE SCHOOL", "AddressLine": "14819 HEIMER RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78232", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BRANDEIS HIGH SCHOOL", "AddressLine": "13011 KYLE SEALE PKWY", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78249", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BRAUCHLE ELEMENTARY SCHOOL", "AddressLine": "8555 BOWENS CROSSING", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78250", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BRENTWOOD STEAM SCHOOL OF INNOVATION", "AddressLine": "1626 W. THOMPSON PLACE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78226", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BROOKHOLLOW BRANCH LIBRARY(BOTH)", "AddressLine": "530 HEIMER RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78232", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BULVERDE CREEK ELEMENTARY SCHOOL", "AddressLine": "3839 CANYON PKWY", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78259", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BURKE ELEMENTARY SCHOOL", "AddressLine": "10111 TERRA OAK", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78250", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "BUSH MIDDLE SCHOOL", "AddressLine": "1500 EVANS RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78258", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CANDLEWOOD ELEMENTARY SCHOOL", "AddressLine": "3635 CANDLEGLEN", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78244", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CARLOS COON ELEMENTARY SCHOOL", "AddressLine": "3114 TIMBER VIEW DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78251", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CARNAHAN ELEMENTARY SCHOOL", "AddressLine": "6839 BABCOCK RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78249", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CARSON ELEMENTARY SCHOOL", "AddressLine": "8151 OLD TEZEL RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78250", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CASTLE HILLS CITY HALL(BOTH)", "AddressLine": "209 LEMONWOOD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78213", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CENTRAL LIBRARY", "AddressLine": "600 SOLEDAD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78205", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CHARLES GRAEBNER ELEMENTARY SCHOOL", "AddressLine": "530 HOOVER STREET", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78225", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CHINA GROVE CITY HALL", "AddressLine": "2412 FM 1516 S.", "Locality": "CHINA GROVE", "AdminDistrict": "TX", "PostalCode": "78263", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CHRISTA MCAULIFFE MIDDLE SCHOOL", "AddressLine": "9390 SW LOOP 410", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78242", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CHRISTIAN FAMILY BAPTIST CHURCH(BOTH)", "AddressLine": "1589 GROSSENBACHER", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78245", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CHURCH OF RECONCILIATION", "AddressLine": "8900 STARCREST", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78217", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CHURCHILL HIGH SCHOOL", "AddressLine": "12049 BLANCO RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78216", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CIBOLO GREEN ELEMENTARY SCHOOL", "AddressLine": "24315 BULVERDE GREEN", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78261", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CITY OF SANDY OAKS MUNICIPAL BLDG", "AddressLine": "22780 PRIEST RD.", "Locality": "SANDY OAKS", "AdminDistrict": "TX", "PostalCode": "78112", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CITY OF VON ORMY MUNICIPAL COURT", "AddressLine": "14729 QUARTER HORSE", "Locality": "VON ORMY", "AdminDistrict": "TX", "PostalCode": "78073", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CLARK HIGH SCHOOL", "AddressLine": "5150 DE ZAVALA RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78249", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CLAUDE BLACK COMMUNITY CENTER(BOTH)", "AddressLine": "2805 E. COMMERCE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78202", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CLEAR SPRING ELEMENTARY SCHOOL", "AddressLine": "4311 CLEAR SPRING DR.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78217", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CODY BRANCH LIBRARY(BOTH)", "AddressLine": "11441 VANCE JACKSON", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78230", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CODY ELEMENTARY SCHOOL", "AddressLine": "10403 DUGAS DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78245", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "COLE ELEMENTARY SCHOOL", "AddressLine": "13185 TILLMAN RIDGE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78253", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "COLLIER ELEMENTARY SCHOOL", "AddressLine": "834 W. SOUTHCROSS", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78211", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "COLLINS GARDEN BRANCH LIBRARY", "AddressLine": "200 N. PARK BLVD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78204", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "COLONIAL HILLS UNITED METHODIST CHURCH", "AddressLine": "5247 VANCE JACKSON", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78230", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "COLONIES NORTH ELEMENTARY SCHOOL", "AddressLine": "9915 NORTHHAMPTON", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78230", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "COMMUNITY ALLIANCE FOR TRAFFIC SAFETY", "AddressLine": "7719 PIPERS LANE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78251", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CONNALLY MIDDLE SCHOOL", "AddressLine": "8661 SILENT SUNRISE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78250", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "COPERNICUS COMM. CENTER(BOTH)", "AddressLine": "5003 LORD RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78220", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CORONADO VILLAGE ELEM. SCHOOL", "AddressLine": "213 AMISTAD BLVD.", "Locality": "UNIVERSAL CITY", "AdminDistrict": "TX", "PostalCode": "78148", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CORTEZ BRANCH LIBRARY(BOTH)", "AddressLine": "2803 HUNTER BLVD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78224", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CROCKETT ACADEMY", "AddressLine": "2215 MORALES ST.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78207", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "CROSS MOUNTAIN CHURCH", "AddressLine": "24891 BOERNE STAGE RD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78255", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "DAVIS MIDDLE SCHOOL", "AddressLine": "4702 E. HOUSTON STREET", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78220", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "DAVIS SCOTT YMCA", "AddressLine": "1213 IOWA STREET", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78203", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "DELLVIEW ELEMENTARY SCHOOL", "AddressLine": "7235 DEWHURST RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78213", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "E.T. WRENN MIDDLE SCHOOL", "AddressLine": "627 S. ACME RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78237", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "EAST CENTRAL HIGH SCHOOL", "AddressLine": "7173 FM 1628", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78263", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "EAST CENTRAL ISD ADMIN BUILDING(BOTH)", "AddressLine": "6634 NEW SULPHUR SPRINGS RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78263", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "EAST TERRELL HILLS ELEMENTARY SCHOOL", "AddressLine": "4415 BLOOMDALE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78218", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ED WHITE MIDDLE SCHOOL", "AddressLine": "7800 MIDCROWN", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78218", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "EDGEWOOD GYM", "AddressLine": "4133 ELDRIDGE AVE.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78237", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "EISENHOWER MIDDLE SCHOOL", "AddressLine": "8231 BLANCO RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78216", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "EL DORADO ELEMENTARY SCHOOL", "AddressLine": "12634 EL SENDERO", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78233", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ELLISON ELEMENTARY SCHOOL", "AddressLine": "7132 OAK DR.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78256", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ELMENDORF CITY HALL(BOTH)", "AddressLine": "4133 ELDRIDGE AVE.", "Locality": "ELMENDORF", "AdminDistrict": "TX", "PostalCode": "78237", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ELOISE JAPHET ACADEMY", "AddressLine": "314 ASTOR", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78210", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ELOLF STEAM ACADEMY", "AddressLine": "6335 BEECH TRAIL", "Locality": "CONVERSE", "AdminDistrict": "TX", "PostalCode": "78109", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ELROD ELEMENTARY SCHOOL", "AddressLine": "8885 HEATH CIRCLE DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78250", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ENCINO BRANCH LIBRARY(BOTH)", "AddressLine": "2515 E. EVANS RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78259", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ESPARZA ELEMENTARY SCHOOL", "AddressLine": "5700 HEMPHILL DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78228", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "EVERS ELEMENTARY SCHOOL", "AddressLine": "1715 RICHLAND HILLS DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78251", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "FAITH LUTHERAN CHURCH", "AddressLine": "14819 JONES MALTSBERGER RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78247", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "FERNANDEZ ELEMENTARY SCHOOL", "AddressLine": "6845 RIDGEBROOK ST.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78250", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "FIELDS ELEMENTARY SCHOOL", "AddressLine": "9570 FM 1560", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78254", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "FIRE STATION #3", "AddressLine": "11917 LOWER SEGUIN RD.", "Locality": "SCHERTZ", "AdminDistrict": "TX", "PostalCode": "78154", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "FIRST CHINESE BAPTIST CHURCH", "AddressLine": "5481 PRUE RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78240", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "FIVE PALMS ELEMENTARY SCHOOL", "AddressLine": "7138 FIVE PALMS DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78242", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "FOLKS MIDDLE SCHOOL", "AddressLine": "9855 SWAYBACK RANCH", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78254", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "FRANK GARRETT MULTI SERVICE CENTER(BOTH)", "AddressLine": "1226 NW 18TH STREET", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78207", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "FRANK MADLA ELEMENTARY SCHOOL", "AddressLine": "6100 ROYALGATE DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78242", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "GALM ELEMENTARY SCHOOL", "AddressLine": "1454 SAXOHILL DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78253", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "GARDENDALE EARLY LEARNING PROGRAM", "AddressLine": "1731 DAHLGREEN AVENUE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78237", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "GILLETTE ELEMENTARY SCHOOL", "AddressLine": "625 GILLETTE BLVD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78221", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "GLENOAKS ELEMENTARY SCHOOL", "AddressLine": "5103 NEWCOME DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78229", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "GRANADOS ADULT AND SENIOR CENTER", "AddressLine": "500 FREILING", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78213", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "GREAT NORTHWEST BRANCH LIBRARY(BOTH)", "AddressLine": "9050 WELLWOOD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78250", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "GREY FOREST COMMUNITY CENTER", "AddressLine": "18249 SHERWOOD TRAIL", "Locality": "GREY FOREST", "AdminDistrict": "TX", "PostalCode": "78023", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "GUERRA BRANCH LIBRARY(BOTH)", "AddressLine": "7978 W. MILITARY DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78227", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "GUS GARCIA UNIVERSITY SCHOOL", "AddressLine": "3306 RUIZ STREET", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78228", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HARDY OAK ELEMENTARY SCHOOL", "AddressLine": "22900 HARDY OAK BLVD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78258", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HARMONY ELEMENTARY SCHOOL", "AddressLine": "10625 GREEN LAKE DR.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78223", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HARMONY HILLS ELEMENTARY SCHOOL", "AddressLine": "10727 MEMORY LANE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78216", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HARRY H. ROGERS MIDDLE SCHOOL", "AddressLine": "314 GALWAY DR.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78223", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HARTMAN CENTER II", "AddressLine": "1202 W. BITTERS, BLDG 1", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78216", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HATCHETT ELEMENTARY", "AddressLine": "10700 INGRAM RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78245", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HEALTH CAREERS HIGH SCHOOL", "AddressLine": "4646 HAMILTON WOLFE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78229", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HECTOR GARCIA MIDDLE SCHOOL", "AddressLine": "14900 KYLE SEALE PARKWAY", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78255", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HELOTES CITY HALL(BOTH)", "AddressLine": "12951 BANDERA ROAD", "Locality": "HELOTES", "AdminDistrict": "TX", "PostalCode": "78023", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HELOTES ELEMENTARY SCHOOL", "AddressLine": "13878 RIGGS RD.", "Locality": "HELOTES", "AdminDistrict": "TX", "PostalCode": "78023", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HENDERSON ELEMENTARY SCHOOL", "AddressLine": "14605 KALLISON BEND", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78254", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HERMAN HIRSCH ELEMENTARY SCHOOL", "AddressLine": "4826 SEA BREEZE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78220", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HIDDEN COVE ELEMENTARY", "AddressLine": "5102 TRADING POST DR.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78242", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HIDDEN FOREST ELEMENTARY SCHOOL", "AddressLine": "802 SILVER SPRUCE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78232", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HIGHLAND HILLS ELEMENTARY SCHOOL", "AddressLine": "734 GLAMIS", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78223", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HIGHLANDS HIGH SCHOOL", "AddressLine": "3118 ELGIN AVE.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78210", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HILL COUNTRY RETREAT", "AddressLine": "4550 DEL WEBB BLVD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78253", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HILL COUNTRY VILLAGE CITY HALL", "AddressLine": "116 ASPEN LANE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78232", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HILL MIDDLE SCHOOL", "AddressLine": "21314 BULVERDE RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78259", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HOLLYWOOD PARK CITY HALL", "AddressLine": "2 MECCA DR.", "Locality": "HOLLYWOOD PARK", "AdminDistrict": "TX", "PostalCode": "78232", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HOPE CHURCH", "AddressLine": "18850 REDLAND RD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78259", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HUEBNER ELEMENTARY SCHOOL", "AddressLine": "16311 HUEBNER RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78249", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HUISACHE AVENUE BAPTIST CHURCH", "AddressLine": "1339 HUISACHE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78201", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "HUNTERS CREEK SWIM AND RACQUET CLUB", "AddressLine": "3630 HUNTERS CIRCLE ST.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78230", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "IGO BRANCH LIBRARY(BOTH)", "AddressLine": "13330 KYLE SEALE PARKWAY", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78249", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "INDIAN SPRINGS ELEMENTARY SCHOOL", "AddressLine": "25751 WILDERNESS OAK", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78261", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "INEZ FOSTER ELEMENTARY SCHOOL", "AddressLine": "6718 PECAN VALLEY", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78223", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "JAMES RUSSELL LOWELL MIDDLE SCHOOL", "AddressLine": "919 THOMPSON PLACE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78226", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "JOE WARD RECREATION CENTER", "AddressLine": "435 E. SUNSHINE DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78228", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "JOHN GLENN ELEMENTARY SCHOOL", "AddressLine": "2385 HORAL DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78227", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "JOHN GREENLEAF WHITTIER MIDDLE SCHOOL", "AddressLine": "2101 EDISON DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78201", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "JOHN HOFFMANN ELEMENTARY SCHOOL", "AddressLine": "12118 VOLUNTEER PARKWAY", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78253", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "JOHN MARSHALL HIGH SCHOOL", "AddressLine": "8000 LOBO LN.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78240", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "JOHNSTON BRANCH LIBRARY(BOTH)", "AddressLine": "6307 SUN VALLEY DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78227", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "JUDSON ISD ERC", "AddressLine": "8205 PALISADES DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78233", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "JUDSON ISD PERFORMING ARTS CENTER", "AddressLine": "9443 SCHAEFER RD.", "Locality": "CONVERSE", "AdminDistrict": "TX", "PostalCode": "78109", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "KALLISON ELEMENTARY SCHOOL", "AddressLine": "8610 RANCH VIEW", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78254", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "KATE SCHENCK ELEMENTARY SCHOOL", "AddressLine": "101 KATE SCHENCK", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78233", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "KENWOOD COMMUNITY CENTER", "AddressLine": "305 DORA STREET", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78212", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "KINDER RANCH ELEMENTARY", "AddressLine": "2035 KINDER PKWY.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78260", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "KINGSBOROUGH MIDDLE SCHOOL", "AddressLine": "422 ASHLEY ROAD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78221", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "KIRBY CITY HALL(BOTH)", "AddressLine": "112 BAUMAN ST.", "Locality": "KIRBY", "AdminDistrict": "TX", "PostalCode": "78219", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "KITTY HAWK MIDDLE SCHOOL", "AddressLine": "840 CIMARRON TRAIL", "Locality": "UNIVERSAL CITY", "AdminDistrict": "TX", "PostalCode": "78148", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "KNOWLTON ELEMENTARY SCHOOL", "AddressLine": "9500 TIMBER PATH", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78250", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "KRUEGER ELEMENTARY SCHOOL", "AddressLine": "9900 WILDHORSE PARKWAY", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78254", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "KRUEGER MIDDLE SCHOOL", "AddressLine": "438 LANARK DR.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78218", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "LANIER HIGH SCHOOL", "AddressLine": "1514 W. CESAR CHAVEZ", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78207", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "LARKSPUR ELEMENTARY SCHOOL", "AddressLine": "1802 LARKSPUR", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78213", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "LAS PALMAS BRANCH LIBRARY(BOTH)", "AddressLine": "515 CASTROVILLE RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78237", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "LAUREL HEIGHTS UNITED METHODIST CHURCH", "AddressLine": "227 W WOODLAWN AVE.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78212", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "LEON SPRINGS ELEMENTARY SCHOOL", "AddressLine": "23881 IH 10 W", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78257", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "LEON VALLEY CONFERENCE CENTER(BOTH)", "AddressLine": "6427 EVERS RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78238", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "LEWIS ELEMENTARY SCHOOL", "AddressLine": "1000 SEASCAPE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78251", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "LIONS FIELD ADULT AND SENIOR CENTER(BOTH)", "AddressLine": "2809 BROADWAY ST.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78209", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "LONGFELLOW MIDDLE SCHOOL", "AddressLine": "1130 E. SUNSHINE DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78228", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "LONGS CREEK ELEMENTARY SCHOOL", "AddressLine": "15806 O'CONNOR RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78247", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "LOPEZ MIDDLE SCHOOL", "AddressLine": "23103 HARDY OAK BLVD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78258", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "LUCKEY RANCH ELEMENTARY SCHOOL", "AddressLine": "12045 LUCKEY RIVER", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78252", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "LUTHER BURBANK HIGH SCHOOL", "AddressLine": "1002 EDWARDS STREET", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78204", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MADISON HIGH SCHOOL", "AddressLine": "5005 STAHL RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78247", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MARIN B.FENWICK ACADEMY", "AddressLine": "1930 WAVERLY AVE.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78228", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MARTIN LUTHER KING JR. ACADEMY", "AddressLine": "3501 MARTIN LUTHER KING DR.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78220", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MARY MICHAEL ELEMENTARY SCHOOL", "AddressLine": "3155 QUIET PLAIN DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78245", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MAVERICK BRANCH LIBRARY(BOTH)", "AddressLine": "8700 MYSTIC PARK", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78254", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MAY ELEMENTARY SCHOOL", "AddressLine": "15707 CHASE HILL BLVD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78256", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MCCRELESS LIBRARY(BOTH)", "AddressLine": "1023 ADA ST.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78223", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MCDERMOTT ELEMENTARY SCHOOL", "AddressLine": "5111 USAA BLVD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78240", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MEAD ELEMENTARY SCHOOL", "AddressLine": "3803 MIDHORIZON DR.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78229", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MEADOW VILLAGE ELEMENTARY SCHOOL", "AddressLine": "1406 MEADOW WAY DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78227", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "METZGER MIDDLE SCHOOL", "AddressLine": "7475 BINZ-ENGLEMAN RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78244", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MIGUEL CARRILLO, JR. ELEMENTARY SCHOOL", "AddressLine": "500 PRICE AVE.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78211", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MILLER'S POINT ELEMENTARY SCHOOL", "AddressLine": "7027 MISTY RIDGE", "Locality": "CONVERSE", "AdminDistrict": "TX", "PostalCode": "78109", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MIRABEAU B. LAMAR ELEMENTARY SCHOOL", "AddressLine": "201 PARLAND", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78209", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MIRELES ELEMENTARY SCHOOL", "AddressLine": "12260 ROCKWALL DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78253", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MISSION ACADEMY", "AddressLine": "9210 S. PRESA", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78223", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MISSION BRANCH LIBRARY(BOTH)", "AddressLine": "3134 ROOSEVELT AVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78214", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MISSION DEL LAGO COMMUNITY CENTER", "AddressLine": "2301 DEL LAGO PKWY", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78221", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MONTGOMERY ELEMENTARY SCHOOL", "AddressLine": "7047 MONTGOMERY DR.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78239", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MORA ELEMENTARY SCHOOL", "AddressLine": "1520 AMERICAN LOTUS", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78245", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MOUNT CALVARY LUTHERAN CHURCH", "AddressLine": "308 MOUNT CALVARY DR.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78209", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "MURNIN ELEMENTARY SCHOOL", "AddressLine": "9019 DUGAS", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78251", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "NEFF ELEMENTARY SCHOOL", "AddressLine": "5227 EVERS RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78228", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "NICHOLS ELEMENTARY SCHOOL", "AddressLine": "9560 BRAUN RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78254", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "NIMITZ MIDDLE SCHOOL", "AddressLine": "5426 BLANCO RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78216", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "NORTHEAST LAKEVIEW COLLEGE", "AddressLine": "1201 KITTY HAWK RD", "Locality": "UNIVERSAL CITY", "AdminDistrict": "TX", "PostalCode": "78148", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "NORTHERN HILLS ELEMENTARY SCHOOL", "AddressLine": "13901 HIGGINS RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78217", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "NORTHSIDE ACTIVITY CENTER(BOTH)", "AddressLine": "7001 CULEBRA RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78238", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "NORTHWEST CHURCH OF CHRIST", "AddressLine": "9681 W. LOOP 1604 N.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78254", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "NORTHWEST CROSSING ELEMENTARY SCHOOL", "AddressLine": "10255 DOVER RDG.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78250", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "NORTHWEST VISTA COLLEGE(BOTH)", "AddressLine": "3535 N. ELLISON DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78251", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "NORTHWOOD ELEMENTARY SCHOOL", "AddressLine": "519 PIKE ROAD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78209", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "OAK GROVE ELEMENTARY SCHOOL", "AddressLine": "3250 NACOGDOCHES ROAD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78217", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "OAK HILLS TERRACE ELEMENTARY SCHOOL", "AddressLine": "5710 CARY GRANT DR", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78240", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "OAK MEADOW UNITED METHODIST CHURCH", "AddressLine": "2740 HUNTERS GREEN", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78231", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "OLD CONVERSE CITY HALL(BOTH)", "AddressLine": "405 S. SEGUIN ROAD", "Locality": "CONVERSE", "AdminDistrict": "TX", "PostalCode": "78109", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "OLMOS ELEMENTARY SCHOOL", "AddressLine": "1103 ALLENA DR.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78213", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "OLMOS PARK CITY HALL(BOTH)", "AddressLine": "120 EL PRADO DR. W.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78212", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "OTT ELEMENTARY SCHOOL", "AddressLine": "100 N GROSENBACHER ROAD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78253", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "OUR LADY OF THE LAKE UNIVERSITY(BOTH)", "AddressLine": "411 S.W. 24TH STREET", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78207", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "PALO ALTO COLLEGE(BOTH)", "AddressLine": "1400 W. VILLARET BLVD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78224", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "PARK VILLAGE ELEMENTARY SCHOOL", "AddressLine": "5855 MIDCROWN", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78218", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "PARMAN BRANCH LIBRARY AT STONE OAK(BOTH)", "AddressLine": "20735 WILDERNESS OAK", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78258", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "PASCHALL ELEMENTARY SCHOOL", "AddressLine": "6351 LAKEVIEW DR.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78244", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "PEASE MIDDLE SCHOOL", "AddressLine": "201 HUNT LANE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78245", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "PECAN VALLEY ELEMENTARY SCHOOL", "AddressLine": "3966 E. SOUTHCROSS", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78222", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "PERALES STEAM ELEMENTARY SCHOOL", "AddressLine": "1507 CERALVO STREET", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78237", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "POWELL ELEMENTARY SCHOOL", "AddressLine": "6003 THUNDER RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78238", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "PRE-K ACADEMY AT WEST AVENUE", "AddressLine": "3915 WEST AVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78213", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "PRECINCT 1 SATELLITE OFFICE(BOTH)", "AddressLine": "3505 PLEASANTON ROAD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78221", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "PRECINCT 3 SATELLITE OFFICE(BOTH)", "AddressLine": "320 INTERPARK BLVD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78216", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "RABA ELEMENTARY SCHOOL", "AddressLine": "9740 RABA DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78251", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "RALPH LANGLEY ELEMENTARY SCHOOL", "AddressLine": "14185 BELLA VISTA PLACE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78253", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "RAWLINSON MIDDLE SCHOOL", "AddressLine": "14100 VANCE JACKSON", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78249", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "RAYBURN ELEMENTARY SCHOOL", "AddressLine": "635 RAYBURN DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78214", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "REDLAND OAKS ELEMENTARY SCHOOL", "AddressLine": "16650 REDLAND RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78247", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "REGENCY PLACE ELEMENTARY SCHOOL", "AddressLine": "2635 MACARTHUR VIEW", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78217", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "RESNIK MIDDLE SCHOOL", "AddressLine": "4495 VERANO PKWY.", "Locality": "VON ORMY", "AdminDistrict": "TX", "PostalCode": "78073", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "RHODES ELEMENTARY SCHOOL", "AddressLine": "5714 NORTH KNOLL", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78240", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "RIDGEVIEW ELEMENTARY SCHOOL", "AddressLine": "8223 N. MCCULLOUGH AVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78216", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "RIVERSIDE PARK ELEMENTARY SCHOOL", "AddressLine": "202 SCHOOL STREET", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78210", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ROAN FOREST ELEMENTARY SCHOOL", "AddressLine": "22710 ROAN PARK", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78259", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ROYAL RIDGE ELEMENTARY SCHOOL", "AddressLine": "5933 ROYAL RIDGE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78239", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "RUDDER MIDDLE SCHOOL", "AddressLine": "6558 HORN BLVD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78240", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SAC VICTORY CENTER(BOTH)", "AddressLine": "1819 N. MAIN AVE.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78212", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SAM HOUSTON HIGH SCHOOL", "AddressLine": "4635 E. HOUSTON", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78220", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SAMUEL A. MAVERICK ELEMENTARY SCHOOL", "AddressLine": "107 RALEIGH STREET", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78201", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SAN ANTONIO HOUSING AUTHORITY", "AddressLine": "818 S. FLORES", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78204", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SAN ANTONIO M.U.D. #1", "AddressLine": "16450 WILDLAKE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78023", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SAN ANTONIO SHRINE AUDITORIUM", "AddressLine": "901 N. LOOP 1604 W.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78232", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SARAH KING ELEMENTARY SCHOOL", "AddressLine": "1001 CERALVO STREET", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78207", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SCARBOROUGH ELEMENTARY SCHOOL", "AddressLine": "12280 SILVER POINT", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78254", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SCHAEFER BRANCH LIBRARY(BOTH)", "AddressLine": "6322 US HWY 87 E.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78222", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SCOBEE ELEMENTARY SCHOOL", "AddressLine": "11223 CEDAR PARK", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78249", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SEMMES BRANCH LIBRARY(BOTH)", "AddressLine": "15060 JUDSON RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78247", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SHAVANO PARK CITY HALL(BOTH)", "AddressLine": "900 SADDLETREE CT.", "Locality": "SHAVANO PARK", "AdminDistrict": "TX", "PostalCode": "78231", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SHEPHERD KING LUTHERAN CHURCH", "AddressLine": "303 RAMSEY ROAD W.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78216", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SKY HARBOUR ELEMENTARY SCHOOL", "AddressLine": "5902 FISHERS BEND STREET", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78242", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SMITH ELEMENTARY SCHOOL", "AddressLine": "823 S. GEVERS", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78203", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SOMERSET CITY HALL(BOTH)", "AddressLine": "7360 EAST 6TH ST., SOMERSET", "Locality": "SOMERSET", "AdminDistrict": "TX", "PostalCode": "78069", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SONNY MELENDREZ COMMUNITY CENTER", "AddressLine": "5919 W. COMMERCE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78237", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SOUTH SAN ANTONIO HIGH SCHOOL", "AddressLine": "7535 BARLITE BLVD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78224", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SOUTHSIDE ISD ADMIN BLDG(BOTH)", "AddressLine": "1460 MARTINEZ-LOSOYA RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78221", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SOUTHWEST ISD", "AddressLine": "11914 DRAGON LANE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78252", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SPECHT ELEMENTARY SCHOOL", "AddressLine": "25815 OVERLOOK PKWY", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78260", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SPICEWOOD PARK ELEMENTARY", "AddressLine": "11303 TILSON", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78224", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "SPRING MEADOWS ELEMENTARY SCHOOL", "AddressLine": "7135 ELM TRAIL", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78244", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ST. HEDWIG CITY HALL", "AddressLine": "13065 FM 1346", "Locality": "ST. HEDWIG", "AdminDistrict": "TX", "PostalCode": "78152", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ST. JAMES CATHOLIC CHURCH", "AddressLine": "907 W. THEO AVE.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78225", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ST. LEO THE GREAT CATHOLIC CHURCH", "AddressLine": "4423 S. FLORES", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78214", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ST. MARY'S UNIVERSITY(BOTH)", "AddressLine": "1 CAMINO SANTA MARIA", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78228", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ST. PAUL COMMUNITY CENTER(BOTH)", "AddressLine": "1201 DONALDSON AVE.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78228", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ST. PHILIPS OF JESUS CATHOLIC CHURCH", "AddressLine": "142 E. LAMBERT ST.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78204", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ST. PHILLIPS COLLEGE", "AddressLine": "1801 MARTIN LUTHER KING DR.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78203", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "STAFFORD ELEMENTARY SCHOOL", "AddressLine": "415 SW 36TH STREET", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78237", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "STAHL ELEMENTARY SCHOOL", "AddressLine": "5222 STAHL RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78247", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "STEUBING RANCH ELEMENTARY", "AddressLine": "5100 KNOLL CREEK", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78247", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "STEVENSON MIDDLE SCHOOL", "AddressLine": "8403 TEZEL RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78254", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "STONE OAK ELEMENTARY SCHOOL", "AddressLine": "21045 CRESENT OAKS", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78258", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "STORM ELEMENTARY SCHOOL", "AddressLine": "435 BRADY BLVD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78207", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "TAFT HIGH SCHOOL", "AddressLine": "11600 FM 471 W.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78253", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "TAKAS PARK(BOTH)", "AddressLine": "9310 JIM SEAL DR.", "Locality": "WINDCREST", "AdminDistrict": "TX", "PostalCode": "78239", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "TEJEDA MIDDLE SCHOOL", "AddressLine": "2909 E. EVANS RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78259", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "TERRELL HILLS CITY HALL", "AddressLine": "5100 N. NEW BRAUNFELS", "Locality": "TERRELL HILLS", "AdminDistrict": "TX", "PostalCode": "78209", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "TEXAS A&M SAN ANTONIO MAYS CENTER(BOTH)", "AddressLine": "1 UNIVERSITY WAY", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78224", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "THOMAS EDISON HIGH SCHOOL", "AddressLine": "701 SANTA MONICA DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78212", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "THORNTON ELEMENTARY SCHOOL", "AddressLine": "6450 PEMBROKE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78240", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "THOUSAND OAKS BRANCH LIBRARY(BOTH)", "AddressLine": "4618 THOUSAND OAKS", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78233", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "THOUSAND OAKS ELEMENTARY SCHOOL", "AddressLine": "16080 HENDERSON PASS", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78232", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "TOBIN LIBRARY @ OAKWELL(BOTH)", "AddressLine": "4134 HARRY WURZBACH", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78209", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "TRINITY UNITED METHODIST CHURCH", "AddressLine": "6800 WURZBACH RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78240", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "TUSCANY HEIGHTS ELEMENTARY SCHOOL", "AddressLine": "25001 WILDERNESS OAK", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78260", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "UNIVERSAL CITY HALL", "AddressLine": "2150 UNIVERSAL CITY BLVD.", "Locality": "UNIVERSAL", "AdminDistrict": "TX", "PostalCode": "78148", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "UNIVERSAL CITY LIBRARY(BOTH)", "AddressLine": "100 NORTHVIEW DR.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78148", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "UTSA(BOTH)", "AddressLine": "1 UTSA CIRCLE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78249", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "VALE MIDDLE SCHOOL", "AddressLine": "2120 N. ELLISON DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78251", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "VAN RAUB ELEMENTARY SCHOOL(BOTH)", "AddressLine": "8776 DIETZ ELKHORN RD.", "Locality": "FAIR OAKS RANCH", "AdminDistrict": "TX", "PostalCode": "78015", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "VESTAL ELEMENTARY SCHOOL", "AddressLine": "1111 W. VESTAL PLACE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78221", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "VETERANS MEMORIAL HIGH SCHOOL", "AddressLine": "7618 EVANS RD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78266", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "VILLARREAL ELEMENTARY SCHOOL", "AddressLine": "2902 WHITE TAIL DR.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78228", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "VINEYARD RANCH ELEMENTARY", "AddressLine": "16818 HUEBNER RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78258", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "VIRGINIA A. MYERS ELEMENTARY SCHOOL", "AddressLine": "3031 VILLAGE PKWY", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78251", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "WANKE ELEMENTARY SCHOOL", "AddressLine": "10419 OLD PRUE RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78249", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "WARD ELEMENTARY SCHOOL", "AddressLine": "8400 CAVERN HILL", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78254", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "WESTMINISTER SQUARE MANAGEMENT", "AddressLine": "1838 BASSE RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78213", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "WESTWOOD TERRACE ELEMENTARY SCHOOL", "AddressLine": "2315 HACKAMORE LANE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78227", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "WETMORE ELEMENTARY SCHOOL", "AddressLine": "3250 THOUSAND OAKS", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78247", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "WILSHIRE ELEMENTARY SCHOOL", "AddressLine": "6523 CASCADE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78218", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "WONDERLAND MALL OF THE AMERICAS(BOTH)", "AddressLine": "4522 FRED RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78201", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "WOOD MIDDLE SCHOOL", "AddressLine": "14800 JUDSON RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78233", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "WOODLAKE HILLS MIDDLE SCHOOL", "AddressLine": "6625 WOODLAKE PKWY", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78244", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "WOODLAWN ACADEMY", "AddressLine": "1717 W MAGNOLIA AVE.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78201", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "WOODLAWN HILLS ELEMENTARY SCHOOL", "AddressLine": "110 W QUILL DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78228", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "WOODLAWN POINTE CENTER FOR COMMUNITY(BOTH)", "AddressLine": "702 DONALDSON AVE.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78201", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "WOODS OF SHAVANO COMMUNITY CLUB HOUSE", "AddressLine": "13838 PARKSITE WOODS ST.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78249", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "WOODSTONE ELEMENTARY SCHOOL", "AddressLine": "5602 FOUNTAINWOOD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78233", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "WORTHAM OAKS ELEMENTARY", "AddressLine": "5710 CARRIAGE CAPE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78261", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "WRIGHT ELEMENTARY SCHOOL", "AddressLine": "115 E. HUFF AVENUE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78214", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "YOUNG MENS LEADERSHIP ACADEMY AT PHILIS WHEATLEY", "AddressLine": "415 GABRIEL", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78202", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "YOUNG WOMENS LEADERSHIP ACADEMY", "AddressLine": "2123 W HUISACHE AVE.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78201", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
        {"Name": "ZACHRY MIDDLE SCHOOL", "AddressLine": "9410 TIMBER PATH", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78250", "hours": "11/08/2022-11/08/2022 07:00 AM-07:00 PM"},
    ],
    "earlyVoting": [
        {"Name": "BEXAR COUNTY ELECTIONS(BOTH)", "AddressLine": "1103 S. FRIO", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78207", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "BEXAR COUNTY JUSTICE CENTER(BOTH)", "AddressLine": "300 DOLOROSA", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78205", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-06:00 PM", "", ""]},
        {"Name": "BROOKHOLLOW BRANCH LIBRARY(BOTH)", "AddressLine": "530 HEIMER RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78232", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "CASTLE HILLS CITY HALL(BOTH)", "AddressLine": "209 LEMONWOOD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78213", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "CHRISTIAN FAMILY BAPTIST CHURCH(BOTH)", "AddressLine": "1589 GROSSENBACHER", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78245", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "CLAUDE BLACK COMMUNITY CENTER(BOTH)", "AddressLine": "2805 E. COMMERCE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78202", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "CODY BRANCH LIBRARY(BOTH)", "AddressLine": "11441 VANCE JACKSON", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78230", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "COPERNICUS COMM. CENTER(BOTH)", "AddressLine": "5003 LORD RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78220", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "CORTEZ BRANCH LIBRARY(BOTH)", "AddressLine": "2803 HUNTER BLVD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78224", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "EAST CENTRAL ISD ADMIN BUILDING(BOTH)", "AddressLine": "6634 NEW SULPHUR SPRINGS RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78263", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "ELMENDORF CITY HALL(BOTH)", "AddressLine": "4133 ELDRIDGE AVE.", "Locality": "ELMENDORF", "AdminDistrict": "TX", "PostalCode": "78237", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "ENCINO BRANCH LIBRARY(BOTH)", "AddressLine": "2515 E. EVANS RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78259", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "FRANK GARRETT MULTI SERVICE CENTER(BOTH)", "AddressLine": "1226 NW 18TH STREET", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78207", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "GREAT NORTHWEST BRANCH LIBRARY(BOTH)", "AddressLine": "9050 WELLWOOD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78250", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "GUERRA BRANCH LIBRARY(BOTH)", "AddressLine": "7978 W. MILITARY DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78227", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "HELOTES CITY HALL(BOTH)", "AddressLine": "12951 BANDERA ROAD", "Locality": "HELOTES", "AdminDistrict": "TX", "PostalCode": "78023", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "IGO BRANCH LIBRARY(BOTH)", "AddressLine": "13330 KYLE SEALE PARKWAY", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78249", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "JOHNSTON BRANCH LIBRARY(BOTH)", "AddressLine": "6307 SUN VALLEY DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78227", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "KIRBY CITY HALL(BOTH)", "AddressLine": "112 BAUMAN ST.", "Locality": "KIRBY", "AdminDistrict": "TX", "PostalCode": "78219", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "LAS PALMAS BRANCH LIBRARY(BOTH)", "AddressLine": "515 CASTROVILLE RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78237", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "LEON VALLEY CONFERENCE CENTER(BOTH)", "AddressLine": "6427 EVERS RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78238", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "LIONS FIELD ADULT AND SENIOR CENTER(BOTH)", "AddressLine": "2809 BROADWAY ST.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78209", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "MAVERICK BRANCH LIBRARY(BOTH)", "AddressLine": "8700 MYSTIC PARK", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78254", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "MCCRELESS LIBRARY(BOTH)", "AddressLine": "1023 ADA ST.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78223", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "MISSION BRANCH LIBRARY(BOTH)", "AddressLine": "3134 ROOSEVELT AVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78214", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "NORTHSIDE ACTIVITY CENTER(BOTH)", "AddressLine": "7001 CULEBRA RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78238", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "NORTHWEST VISTA COLLEGE(BOTH)", "AddressLine": "3535 N. ELLISON DRIVE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78251", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "OLD CONVERSE CITY HALL(BOTH)", "AddressLine": "405 S. SEGUIN ROAD", "Locality": "CONVERSE", "AdminDistrict": "TX", "PostalCode": "78109", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "OLMOS PARK CITY HALL(BOTH)", "AddressLine": "120 EL PRADO DR. W.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78212", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "OUR LADY OF THE LAKE UNIVERSITY(BOTH)", "AddressLine": "411 S.W. 24TH STREET", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78207", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "PALO ALTO COLLEGE(BOTH)", "AddressLine": "1400 W. VILLARET BLVD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78224", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "PARMAN BRANCH LIBRARY AT STONE OAK(BOTH)", "AddressLine": "20735 WILDERNESS OAK", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78258", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "PRECINCT 1 SATELLITE OFFICE(BOTH)", "AddressLine": "3505 PLEASANTON ROAD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78221", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "PRECINCT 3 SATELLITE OFFICE(BOTH)", "AddressLine": "320 INTERPARK BLVD", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78216", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "SAC VICTORY CENTER(BOTH)", "AddressLine": "1819 N. MAIN AVE.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78212", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "SCHAEFER BRANCH LIBRARY(BOTH)", "AddressLine": "6322 US HWY 87 E.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78222", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "SEMMES BRANCH LIBRARY(BOTH)", "AddressLine": "15060 JUDSON RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78247", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "SHAVANO PARK CITY HALL(BOTH)", "AddressLine": "900 SADDLETREE CT.", "Locality": "SHAVANO PARK", "AdminDistrict": "TX", "PostalCode": "78231", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "SOMERSET CITY HALL(BOTH)", "AddressLine": "7360 EAST 6TH ST., SOMERSET", "Locality": "SOMERSET", "AdminDistrict": "TX", "PostalCode": "78069", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "SOUTHSIDE ISD ADMIN BLDG(BOTH)", "AddressLine": "1460 MARTINEZ-LOSOYA RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78221", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "ST. MARY'S UNIVERSITY(BOTH)", "AddressLine": "1 CAMINO SANTA MARIA", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78228", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "ST. PAUL COMMUNITY CENTER(BOTH)", "AddressLine": "1201 DONALDSON AVE.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78228", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "TAKAS PARK(BOTH)", "AddressLine": "9310 JIM SEAL DR.", "Locality": "WINDCREST", "AdminDistrict": "TX", "PostalCode": "78239", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "TEXAS A&M SAN ANTONIO MAYS CENTER(BOTH)", "AddressLine": "1 UNIVERSITY WAY", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78224", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "THOUSAND OAKS BRANCH LIBRARY(BOTH)", "AddressLine": "4618 THOUSAND OAKS", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78233", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "TOBIN LIBRARY @ OAKWELL(BOTH)", "AddressLine": "4134 HARRY WURZBACH", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78209", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "UNIVERSAL CITY LIBRARY(BOTH)", "AddressLine": "100 NORTHVIEW DR.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78148", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "UTSA(BOTH)", "AddressLine": "1 UTSA CIRCLE", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78249", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "VAN RAUB ELEMENTARY SCHOOL(BOTH)", "AddressLine": "8776 DIETZ ELKHORN RD.", "Locality": "FAIR OAKS RANCH", "AdminDistrict": "TX", "PostalCode": "78015", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "WONDERLAND MALL OF THE AMERICAS(BOTH)", "AddressLine": "4522 FRED RD.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78201", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
        {"Name": "WOODLAWN POINTE CENTER FOR COMMUNITY(BOTH)", "AddressLine": "702 DONALDSON AVE.", "Locality": "SAN ANTONIO", "AdminDistrict": "TX", "PostalCode": "78201", "hours": ["10/24/2022-10/28/2022 08:00 AM-06:00 PM", "10/29/2022-10/29/2022 08:00 AM-08:00 PM", "10/30/2022-10/30/2022 12:00 PM-06:00 PM", "10/31/2022-11/04/2022 08:00 AM-08:00 PM"]},
    ],
}

ns = "http://www.w3.org/2001/XMLSchema"
ET.register_namespace("xs", ns)
rootTxt = """<?xml version="1.0" encoding="UTF-8"?>
<MainRoot xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:schema xmlns:msdata="urn:schemas-microsoft-com:xml-msdata" id="Place_ds">
    <xs:element name="Place_ds" msdata:IsDataSet="true" msdata:UseCurrentLocale="true">
      <xs:complexType>
        <xs:choice minOccurs="0" maxOccurs="unbounded">
          <xs:element name="Place">
            <xs:complexType>
              <xs:sequence>
                <xs:element name="EntityID" type="xs:string" />
                <xs:element name="AddressLine" minOccurs="0" type="xs:string" />
                <xs:element name="Latitude" minOccurs="0" type="xs:double" />
                <xs:element name="Longitude" minOccurs="0" type="xs:double" />
                <xs:element name="Locality" minOccurs="0" type="xs:string" />
                <xs:element name="AdminDistrict" minOccurs="0" type="xs:string" />
                <xs:element name="PostalCode" minOccurs="0" type="xs:string" />
                <xs:element name="CountryRegion" minOccurs="0" type="xs:string" />
                <xs:element name="Name" minOccurs="0" type="xs:string" />
                <xs:element name="type" minOccurs="0" type="xs:string" />
              </xs:sequence>
            </xs:complexType>
          </xs:element>
        </xs:choice>
      </xs:complexType>
      <xs:unique name="Constraint1" msdata:PrimaryKey="true">
        <xs:selector xpath=".//Place" />
        <xs:field xpath="EntityID" />
      </xs:unique>
    </xs:element>
  </xs:schema>
</MainRoot>"""


Root = ET.fromstring(rootTxt)


electionDayVoting = data["electionDayVoting"]
earlyVoting = data["earlyVoting"]

for n, place in enumerate(electionDayVoting):
    id = re.sub("[\W]", "", place["AddressLine"].title()).lower() + "ElectionDayVoting" + str(n)
    Place = ET.SubElement(Root, "Place")
    Name = ET.SubElement(Place, "Name")
    Name.text = place["Name"].title()
    EntityID = ET.SubElement(Place, "EntityID")
    EntityID.text = id
    type = ET.SubElement(Place, "type")
    type.text = "election-day"
    AddressLine = ET.SubElement(Place, "AddressLine")
    AddressLine.text = place["AddressLine"].title()
    Locality = ET.SubElement(Place, "Locality")
    Locality.text = place["Locality"].title()
    AdminDistrict = ET.SubElement(Place, "AdminDistrict")
    AdminDistrict.text = "TX"
    Nov8Hrs = re.sub("11/08/2022-11/08/2022 ", "", place["hours"])
    hrs = [{}]
    hrs[0]["open"] = strftime("%Y-%m-%dT%H:%M:%S", strptime("11/08/2022 " + Nov8Hrs.split("-")[0], "%m/%d/%Y %I:%M %p"))
    hrs[0]["close"] = strftime("%Y-%m-%dT%H:%M:%S", strptime("11/08/2022 " + Nov8Hrs.split("-")[1], "%m/%d/%Y %I:%M %p"))
    hrs[0]["startDay"] = "11/08/2022"
    hrs[0]["endDay"] = "11/08/2022"

    Hours = ET.SubElement(Place, "Hours")
    Hours.text = json.dumps(hrs)


for n, place in enumerate(earlyVoting):
    id = re.sub("[\W]", "", place["AddressLine"].title()).lower() + "EarlyVoting" + str(n)
    Place = ET.SubElement(Root, "Place")
    Name = ET.SubElement(Place, "Name")
    Name.text = place["Name"].title()
    EntityID = ET.SubElement(Place, "EntityID")
    EntityID.text = id
    type = ET.SubElement(Place, "type")
    type.text = "early-vote"
    AddressLine = ET.SubElement(Place, "AddressLine")
    AddressLine.text = place["AddressLine"].title()
    Locality = ET.SubElement(Place, "Locality")
    Locality.text = place["Locality"].title()
    AdminDistrict = ET.SubElement(Place, "AdminDistrict")
    AdminDistrict.text = "TX"

    hrs = []

    for dayshrs in place["hours"]:
        if dayshrs != "":
            h = {}
            timeRange = dayshrs.split("2022 ")[1]
            dayRange = dayshrs.split("2022 ")[0] + "2022"
            dayStart = dayRange.split("-")[0]
            dayEnd = dayRange.split("-")[1]
            timeStart = strftime("%Y-%m-%dT%H:%M:%S", strptime(f"01/01/2000 " + timeRange.split("-")[0], "%m/%d/%Y %I:%M %p"))
            timeEnd = strftime("%Y-%m-%dT%H:%M:%S", strptime(f"01/01/2000 " + timeRange.split("-")[1], "%m/%d/%Y %I:%M %p"))
            h["open"] = timeStart
            h["close"] = timeEnd
            h["startDay"] = "11/08/2022"
            h["endDay"] = "11/08/2022"
            hrs.append(h)
    Hours = ET.SubElement(Place, "Hours")
    Hours.text = json.dumps(hrs)
    # Nov8Hrs = re.sub("11/08/2022-11/08/2022 ", "", place["hours"])
    # hrs = [{}]
    # hrs[0]["open"] = strftime("%Y-%m-%dT%H:%M:%S", strptime("11/08/2022 " + Nov8Hrs.split("-")[0], "%m/%d/%Y %I:%M %p"))
    # hrs[0]["close"] = strftime("%Y-%m-%dT%H:%M:%S", strptime("11/08/2022 " + Nov8Hrs.split("-")[1], "%m/%d/%Y %I:%M %p"))


dirname = os.path.dirname(__file__)
ET.indent(Root, space="  ", level=0)
Tree = ElementTree(Root)

with open(f"{dirname}/vtr.xml", "wb") as f:
    Tree.write(f, encoding="utf-8", xml_declaration=True)
    f.close()
