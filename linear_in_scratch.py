import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/content/Salary_Data.csv")

print(data)

df.head()

def gradient_descent(m_now,b_now,points,L):
  m_gradient = 0
  b_gradient = 0

  n = len(points)

  for i in range(n):
    x = points.iloc[i].YearsExperience
    y = points.iloc[i].Salary

    m_gradient = -(2/n) * x * (y-(m_now*x+b_now)) # use now
    b_gradient = -(2/n)* (y-(m_now*x+b_now)) # use now

  m = m_now - m_gradient * L
  b = b_now - b_gradient * L
  return m,b

m = 0
b = 0
L = 0.001

epochs = 1000

for i in range(epochs):
  if i % 50 == 0:
    print(f"Epochs: {i}")
  m,b = gradient_descent(m,b,df,L)
print(m,b)

plt.scatter(df.YearsExperience,df.Salary,color="Black")
plt.plot(df.YearsExperience, [m * x + b for x in df.YearsExperience], color="red")
plt.xlabel("YearsExperience")
plt.ylabel("Salary")
plt.title("Salary vs Years of Experience")
plt.show()

# def gradient_descent(m,b,points,L):
#   m_gradient = 0;
#   b_gradient = 0;

#   n = len(points)

#   for i in range(n):
#     x = df.iloc[i].YearsExperience
#     y = df.iloc[i].Salary

#     m_gradient += -(2/n) * x *  (y - (m * x + b))
#     b_gradient += -(2/n) * (y-(m*x+b))

#   m_now = m - m_gradient * L
#   b_now = b - b_gradient * L
#   return m_now,b_now

m = 0
b = 0
L = 0.0001
epochs = 50

for i in range(epochs):
  if i % 50 == 0:
    print(f"Epoch: {i}")
  m,b = gradient_descent(m,b,df,L)
print(m,b)

plt.scatter(df.YearsExperience,df.Salary,color="Black")
# Use the YearsExperience values as x-values and calculate corresponding y-values
plt.plot(df.YearsExperience, [m * x + b for x in df.YearsExperience], color="red")
plt.xlabel("YearsExperience")
plt.ylabel("Salary")
plt.title("Salary vs Years of Experience")
plt.show()
