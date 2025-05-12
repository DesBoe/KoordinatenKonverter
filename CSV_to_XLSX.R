library(xlsx)
#
#
#

########## Hier den Dateipfad angeben
Eingang = "/Volumes/Dennis_OTG/LEPMON/Versiegelung_Kopernicus/Sealing_Trap_sites_EPSG3035.csv"

Ausgang <- sub("\\.csv$", ".xlsx", Eingang)

Tabelle <- read.csv(Eingang,
                    header = T,
                    sep = ";",
                    dec = ".")

write.xlsx(Tabelle, Ausgang, row.names = FALSE)
print("Datei exportiert")