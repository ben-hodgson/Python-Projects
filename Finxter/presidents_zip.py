presidents = ["Roosevelt",
              "Jefferson",
              "Obama"]
            
time_in_office = [4422,
                  2922,
                  2922]

x = list(zip(presidents, time_in_office))
print(x[2][1])

pres = list(zip(*x))[0]
print(pres[-1])