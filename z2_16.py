#   line="to GvR jest ojcem pythona"
#   znajduje indeks podlacnucha GvR
#   gdzie_gvr=line.find("GvR")
#   poniewaz string jest niezmienny to tworze nowy
#   musze tylko uwzglednic odstep na spacje, wiec odejmuje 1/dodaje 3+1 do indeksu GvR
#   line_nowy=line[:gdzie_gvr-1]+"Guido van Rossum"+line[gdzie_gvr+4:]

#   print(line)
#   print(line_nowy)

line="to GvR jest ojcem pythona"

#tworze nowy line, poniewaz lancuchy sa niezmienne
#wiec podmieniam libe metodą replace()

nowy_line=line.replace("GvR", "Guido van Rossum")

print(line)
print(nowy_line)
