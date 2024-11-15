from Address import Address
from Mailing import Mailing

adress1=Address(12345, "Moscow","Tverskaia","2","1")
adress2=Address(65423, "KRD","Soroka","2","64")
letter=Mailing(adress1,adress2,140,21312312)

letter.print()