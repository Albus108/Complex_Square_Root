from sympy import sqrt,cos,sin,I,symbols,atan2,simplify,expand

x,y=symbols("x y",real=True)

x=simplify(input("Re(z): "))
y=simplify(input("Im(z): "))

i=I
z=x+y*i
r=sqrt((x**2+y**2)) # r=|z|
#print(r)

θ=atan2(y,x)

ω1=sqrt(r)*(cos(θ/2)+i*sin(θ/2))

ω2=-sqrt(r)*(cos(θ/2)+i*sin(θ/2))

print(f"|z|: {r}")
print(f"θ: {θ}")
print(f"ω1: {expand(ω1)}")
print(f"ω2: {expand(ω2)}")