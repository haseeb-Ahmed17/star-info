print("---JADU WALA HOROSCOPE PROGRAM ---")
naam = input("Apka naam kya hai?") 
star =input("Apka star kya hai? (jaise ARIES,TAURUS,LEO):")
print("/nApka horoscope nikal raha hai...")
print("---------------------------------")
if star == "ARIES" or star == "aries":
    print(f"Wah {naam}! Aap ARIES ho, aap bohot bhadur ho!")
    print("Aaj apko ko burger kahne ko milay ga !")
elif star == "TAURUS" or star == "taurus":
    print(f"{naam}, aap TAURUS ho, aap bhot mahnati ho!")
    print(f"Apko aik good news milay gi jaldi!")
elif star == "LEO" or star == "leo":
    print(f"{naam}, Ap LEO ho AP bhot aqal mand ho!")
    print(f"AP INSALLAH BHOT KAMYAB HO GAYE")
    print("--------------------------------")
    print("THANK YOU!")
    