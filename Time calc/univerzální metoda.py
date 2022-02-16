def converter(h, m, s):

    m = m * 60

    mZbytek = m % 60

    s = s + mZbytek
    sZbytek = s % 60

    m2 = (s - sZbytek) / 60
    m = (m - mZbytek) / 60 + m2

    s = s % 60


    labelSekundy.config(text=s)
    labelMinuty.config(text=m)
    
    
# txt
s = 15
m = 2.5

m = 2.5 * 60 = 150

mZbytek = m(150) % 60 = 30

s = s(15) + mZbytek(30) = 45
sZbytek = s(45) % 60 = 45

m2 = (s(45) - sZbytek(45)) / 60 = 0
m = (m(150) - mZbytek(30)) / 60 + m2(0) = 2

s = s(45) % 60 = 45

print(m)
print(s)
