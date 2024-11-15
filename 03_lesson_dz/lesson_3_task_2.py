from smartphone import Smartphone

catalog = [
    Smartphone("iphone", "se", 89034324234),
    Smartphone("iphone", "8+", 567567567),
    Smartphone("iphone", "14 pro", 3453453345),
    Smartphone("xuawau", "12s", 8903324234), 
    Smartphone("iphone", "15", 67567567567),
    Smartphone("pocp", "8", 12334435)
]

# Печатаем библиотеку
for Smartphone in catalog:
    print(f"{Smartphone.marka} - {Smartphone.madel} - {Smartphone.nomer}")