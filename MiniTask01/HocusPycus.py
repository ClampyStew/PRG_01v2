#For Qn C HocusPycus

path = "YOUR PATH TO THE FILE"
spellfiles = open(path+'HocusPycusSpells.txt', 'r')
spells = spellfiles.read()
print(spells)  # Print the entire content of the file

SpellCasted = str(input("Enter 5 spell numbers for activation (space-separated): "))
#Good idea to strip the space away from input first before splitting
spellSummoned = SpellCasted.replace(" ", '').replace('1','Rain of Fire,',5).replace('2','Ice Lance,',5).replace('3','Teleport,').replace('4','Mana Ward,').replace('5','Arcane Missiles,')
spellSummoned = spellSummoned.split(",")
Sp1, Sp2, Sp3, Sp4, Sp5 = spellSummoned[0:5]
#As it turns out, adding space in front of the curly bracket does get interpreted in the output
print(f"Activation Sequence:{"\n"}{Sp1}{"\n"}{Sp2}{"\n"}{Sp3} {"\n"}{Sp4}{"\n"}{Sp5}")
print("Ultimate Secret Spell: %s + %s + %s" %(Sp1, Sp3, Sp5))
