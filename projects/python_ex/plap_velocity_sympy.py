#PLAP
from sympy import symbols, sqrt, solve, cos, sin, acos, Abs, Function, diff
 
# inputs, ax, ay, bx, by and bac are possibly function of t
ax, ay, bx, by, bac, ac, t = symbols('ax ay bx by bac ac t')
ax = Function('ax')(t)
ay = Function('ay')(t)
bx = Function('bx')(t)
by = Function('by')(t)
bac = Function('bac')(t)

# intermediate variables
ab, dab = symbols('ab dab')
ad, bd = symbols('ad bd')
# outputs
cx, cy = symbols('cx cy')
# velocities
vcx, vcy = symbols('vcx vcy')
# accelerations
acx, acy = symbols('acx acy')

# for ccw = 1

cx= ac*cos(bac - acos((ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2 + Abs(ax - bx)**2 - Abs(ay - by)**2)/(2*sqrt(ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2)*Abs(ax - bx)))) + ax 

cy= ac*sin(bac - acos((ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2 + Abs(ax - bx)**2 - Abs(ay - by)**2)/(2*sqrt(ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2)*Abs(ax - bx)))) + ay

vcx = diff(cx, t)
vcy = diff(cy, t)
acx = diff(cx, t, t)
acy = diff(cy, t, t)
print("vcx=", vcx)
print()
print("vcy=", vcy)
print()
print("acx=", acx)
print()
print("acy=", acy)

'''
vcx= -ac*(Derivative(bac(t), t) + (-((re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) + (im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)))*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/(2*sqrt(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t))**3) + (2*(re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) - 2*(re(ay(t)) - re(by(t)))*(Derivative(re(ay(t)), t) - Derivative(re(by(t)), t)) + 2*(im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)) - 2*(im(ay(t)) - im(by(t)))*(Derivative(im(ay(t)), t) - Derivative(im(by(t)), t)) + 2*ax(t)*Derivative(ax(t), t) - 2*ax(t)*Derivative(bx(t), t) + 2*ay(t)*Derivative(ay(t), t) - 2*ay(t)*Derivative(by(t), t) - 2*bx(t)*Derivative(ax(t), t) + 2*bx(t)*Derivative(bx(t), t) - 2*by(t)*Derivative(ay(t), t) + 2*by(t)*Derivative(by(t), t))/(2*sqrt(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t))) + (-ax(t)*Derivative(ax(t), t) + ax(t)*Derivative(bx(t), t) - ay(t)*Derivative(ay(t), t) + ay(t)*Derivative(by(t), t) + bx(t)*Derivative(ax(t), t) - bx(t)*Derivative(bx(t), t) + by(t)*Derivative(ay(t), t) - by(t)*Derivative(by(t), t))*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/(2*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)**(3/2)*Abs(ax(t) - bx(t))))/sqrt(1 - (ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)**2/(4*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t))**2)))*sin(bac(t) - acos((ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/(2*sqrt(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t))))) + Derivative(ax(t), t)


vcy= ac*(Derivative(bac(t), t) + (-((re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) + (im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)))*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/(2*sqrt(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t))**3) + (2*(re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) - 2*(re(ay(t)) - re(by(t)))*(Derivative(re(ay(t)), t) - Derivative(re(by(t)), t)) + 2*(im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)) - 2*(im(ay(t)) - im(by(t)))*(Derivative(im(ay(t)), t) - Derivative(im(by(t)), t)) + 2*ax(t)*Derivative(ax(t), t) - 2*ax(t)*Derivative(bx(t), t) + 2*ay(t)*Derivative(ay(t), t) - 2*ay(t)*Derivative(by(t), t) - 2*bx(t)*Derivative(ax(t), t) + 2*bx(t)*Derivative(bx(t), t) - 2*by(t)*Derivative(ay(t), t) + 2*by(t)*Derivative(by(t), t))/(2*sqrt(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t))) + (-ax(t)*Derivative(ax(t), t) + ax(t)*Derivative(bx(t), t) - ay(t)*Derivative(ay(t), t) + ay(t)*Derivative(by(t), t) + bx(t)*Derivative(ax(t), t) - bx(t)*Derivative(bx(t), t) + by(t)*Derivative(ay(t), t) - by(t)*Derivative(by(t), t))*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/(2*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)**(3/2)*Abs(ax(t) - bx(t))))/sqrt(1 - (ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)**2/(4*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t))**2)))*cos(bac(t) - acos((ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/(2*sqrt(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t))))) + Derivative(ay(t), t)


acx= -ac*(2*Derivative(bac(t), t) - (((re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) + (im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)))*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/Abs(ax(t) - bx(t))**2 - 2*(re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) + 2*(re(ay(t)) - re(by(t)))*(Derivative(re(ay(t)), t) - Derivative(re(by(t)), t)) - 2*(im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)) + 2*(im(ay(t)) - im(by(t)))*(Derivative(im(ay(t)), t) - Derivative(im(by(t)), t)) - 2*ax(t)*Derivative(ax(t), t) + 2*ax(t)*Derivative(bx(t), t) - 2*ay(t)*Derivative(ay(t), t) + 2*ay(t)*Derivative(by(t), t) + 2*bx(t)*Derivative(ax(t), t) - 2*bx(t)*Derivative(bx(t), t) + 2*by(t)*Derivative(ay(t), t) - 2*by(t)*Derivative(by(t), t) + (ax(t)*Derivative(ax(t), t) - ax(t)*Derivative(bx(t), t) + ay(t)*Derivative(ay(t), t) - ay(t)*Derivative(by(t), t) - bx(t)*Derivative(ax(t), t) + bx(t)*Derivative(bx(t), t) - by(t)*Derivative(ay(t), t) + by(t)*Derivative(by(t), t))*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2))/(sqrt(1 - (ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)**2/(4*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t))**2))*sqrt(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t))))**2*cos(bac(t) - acos((ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/(2*sqrt(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t)))))/4 - ac*(8*Derivative(bac(t), t, t) + 4*(3*((re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) + (im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)))**2*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/Abs(ax(t) - bx(t))**4 - 4*((re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) + (im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)))*((re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) - (re(ay(t)) - re(by(t)))*(Derivative(re(ay(t)), t) - Derivative(re(by(t)), t)) + (im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)) - (im(ay(t)) - im(by(t)))*(Derivative(im(ay(t)), t) - Derivative(im(by(t)), t)) + ax(t)*Derivative(ax(t), t) - ax(t)*Derivative(bx(t), t) + ay(t)*Derivative(ay(t), t) - ay(t)*Derivative(by(t), t) - bx(t)*Derivative(ax(t), t) + bx(t)*Derivative(bx(t), t) - by(t)*Derivative(ay(t), t) + by(t)*Derivative(by(t), t))/Abs(ax(t) - bx(t))**2 + 2*((re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) + (im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)))*(ax(t)*Derivative(ax(t), t) - ax(t)*Derivative(bx(t), t) + ay(t)*Derivative(ay(t), t) - ay(t)*Derivative(by(t), t) - bx(t)*Derivative(ax(t), t) + bx(t)*Derivative(bx(t), t) - by(t)*Derivative(ay(t), t) + by(t)*Derivative(by(t), t))*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/((ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t))**2) + 2*(re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t, t) - Derivative(re(bx(t)), t, t)) - 2*(re(ay(t)) - re(by(t)))*(Derivative(re(ay(t)), t, t) - Derivative(re(by(t)), t, t)) + 2*(im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t, t) - Derivative(im(bx(t)), t, t)) - 2*(im(ay(t)) - im(by(t)))*(Derivative(im(ay(t)), t, t) - Derivative(im(by(t)), t, t)) + 2*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t))**2 - 2*(Derivative(re(ay(t)), t) - Derivative(re(by(t)), t))**2 + 2*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t))**2 - 2*(Derivative(im(ay(t)), t) - Derivative(im(by(t)), t))**2 - ((re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t, t) - Derivative(re(bx(t)), t, t)) + (im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t, t) - Derivative(im(bx(t)), t, t)) + (Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t))**2 + (Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t))**2)*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/Abs(ax(t) - bx(t))**2 + 2*ax(t)*Derivative(ax(t), t, t) - 2*ax(t)*Derivative(bx(t), t, t) + 2*ay(t)*Derivative(ay(t), t, t) - 2*ay(t)*Derivative(by(t), t, t) - 2*bx(t)*Derivative(ax(t), t, t) + 2*bx(t)*Derivative(bx(t), t, t) - 2*by(t)*Derivative(ay(t), t, t) + 2*by(t)*Derivative(by(t), t, t) + 2*Derivative(ax(t), t)**2 - 4*Derivative(ax(t), t)*Derivative(bx(t), t) + 2*Derivative(ay(t), t)**2 - 4*Derivative(ay(t), t)*Derivative(by(t), t) + 2*Derivative(bx(t), t)**2 + 2*Derivative(by(t), t)**2 - 4*(ax(t)*Derivative(ax(t), t) - ax(t)*Derivative(bx(t), t) + ay(t)*Derivative(ay(t), t) - ay(t)*Derivative(by(t), t) - bx(t)*Derivative(ax(t), t) + bx(t)*Derivative(bx(t), t) - by(t)*Derivative(ay(t), t) + by(t)*Derivative(by(t), t))*((re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) - (re(ay(t)) - re(by(t)))*(Derivative(re(ay(t)), t) - Derivative(re(by(t)), t)) + (im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)) - (im(ay(t)) - im(by(t)))*(Derivative(im(ay(t)), t) - Derivative(im(by(t)), t)) + ax(t)*Derivative(ax(t), t) - ax(t)*Derivative(bx(t), t) + ay(t)*Derivative(ay(t), t) - ay(t)*Derivative(by(t), t) - bx(t)*Derivative(ax(t), t) + bx(t)*Derivative(bx(t), t) - by(t)*Derivative(ay(t), t) + by(t)*Derivative(by(t), t))/(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2) - (ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)*(ax(t)*Derivative(ax(t), t, t) - ax(t)*Derivative(bx(t), t, t) + ay(t)*Derivative(ay(t), t, t) - ay(t)*Derivative(by(t), t, t) - bx(t)*Derivative(ax(t), t, t) + bx(t)*Derivative(bx(t), t, t) - by(t)*Derivative(ay(t), t, t) + by(t)*Derivative(by(t), t, t) + Derivative(ax(t), t)**2 - 2*Derivative(ax(t), t)*Derivative(bx(t), t) + Derivative(ay(t), t)**2 - 2*Derivative(ay(t), t)*Derivative(by(t), t) + Derivative(bx(t), t)**2 + Derivative(by(t), t)**2)/(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2) + 3*(ax(t)*Derivative(ax(t), t) - ax(t)*Derivative(bx(t), t) + ay(t)*Derivative(ay(t), t) - ay(t)*Derivative(by(t), t) - bx(t)*Derivative(ax(t), t) + bx(t)*Derivative(bx(t), t) - by(t)*Derivative(ay(t), t) + by(t)*Derivative(by(t), t))**2*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)**2)/(sqrt(1 - (ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)**2/(4*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t))**2))*sqrt(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t))) + (ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)*(((re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) + (im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)))*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/Abs(ax(t) - bx(t))**2 - 2*(re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) + 2*(re(ay(t)) - re(by(t)))*(Derivative(re(ay(t)), t) - Derivative(re(by(t)), t)) - 2*(im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)) + 2*(im(ay(t)) - im(by(t)))*(Derivative(im(ay(t)), t) - Derivative(im(by(t)), t)) - 2*ax(t)*Derivative(ax(t), t) + 2*ax(t)*Derivative(bx(t), t) - 2*ay(t)*Derivative(ay(t), t) + 2*ay(t)*Derivative(by(t), t) + 2*bx(t)*Derivative(ax(t), t) - 2*bx(t)*Derivative(bx(t), t) + 2*by(t)*Derivative(ay(t), t) - 2*by(t)*Derivative(by(t), t) + (ax(t)*Derivative(ax(t), t) - ax(t)*Derivative(bx(t), t) + ay(t)*Derivative(ay(t), t) - ay(t)*Derivative(by(t), t) - bx(t)*Derivative(ax(t), t) + bx(t)*Derivative(bx(t), t) - by(t)*Derivative(ay(t), t) + by(t)*Derivative(by(t), t))*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2))**2/((1 - (ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)**2/(4*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t))**2))**(3/2)*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)**(3/2)*Abs(ax(t) - bx(t))**3))*sin(bac(t) - acos((ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/(2*sqrt(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t)))))/8 + Derivative(ax(t), t, t)


acy= -ac*(2*Derivative(bac(t), t) - (((re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) + (im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)))*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/Abs(ax(t) - bx(t))**2 - 2*(re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) + 2*(re(ay(t)) - re(by(t)))*(Derivative(re(ay(t)), t) - Derivative(re(by(t)), t)) - 2*(im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)) + 2*(im(ay(t)) - im(by(t)))*(Derivative(im(ay(t)), t) - Derivative(im(by(t)), t)) - 2*ax(t)*Derivative(ax(t), t) + 2*ax(t)*Derivative(bx(t), t) - 2*ay(t)*Derivative(ay(t), t) + 2*ay(t)*Derivative(by(t), t) + 2*bx(t)*Derivative(ax(t), t) - 2*bx(t)*Derivative(bx(t), t) + 2*by(t)*Derivative(ay(t), t) - 2*by(t)*Derivative(by(t), t) + (ax(t)*Derivative(ax(t), t) - ax(t)*Derivative(bx(t), t) + ay(t)*Derivative(ay(t), t) - ay(t)*Derivative(by(t), t) - bx(t)*Derivative(ax(t), t) + bx(t)*Derivative(bx(t), t) - by(t)*Derivative(ay(t), t) + by(t)*Derivative(by(t), t))*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2))/(sqrt(1 - (ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)**2/(4*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t))**2))*sqrt(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t))))**2*sin(bac(t) - acos((ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/(2*sqrt(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t)))))/4 + ac*(8*Derivative(bac(t), t, t) + 4*(3*((re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) + (im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)))**2*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/Abs(ax(t) - bx(t))**4 - 4*((re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) + (im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)))*((re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) - (re(ay(t)) - re(by(t)))*(Derivative(re(ay(t)), t) - Derivative(re(by(t)), t)) + (im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)) - (im(ay(t)) - im(by(t)))*(Derivative(im(ay(t)), t) - Derivative(im(by(t)), t)) + ax(t)*Derivative(ax(t), t) - ax(t)*Derivative(bx(t), t) + ay(t)*Derivative(ay(t), t) - ay(t)*Derivative(by(t), t) - bx(t)*Derivative(ax(t), t) + bx(t)*Derivative(bx(t), t) - by(t)*Derivative(ay(t), t) + by(t)*Derivative(by(t), t))/Abs(ax(t) - bx(t))**2 + 2*((re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) + (im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)))*(ax(t)*Derivative(ax(t), t) - ax(t)*Derivative(bx(t), t) + ay(t)*Derivative(ay(t), t) - ay(t)*Derivative(by(t), t) - bx(t)*Derivative(ax(t), t) + bx(t)*Derivative(bx(t), t) - by(t)*Derivative(ay(t), t) + by(t)*Derivative(by(t), t))*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/((ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t))**2) + 2*(re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t, t) - Derivative(re(bx(t)), t, t)) - 2*(re(ay(t)) - re(by(t)))*(Derivative(re(ay(t)), t, t) - Derivative(re(by(t)), t, t)) + 2*(im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t, t) - Derivative(im(bx(t)), t, t)) - 2*(im(ay(t)) - im(by(t)))*(Derivative(im(ay(t)), t, t) - Derivative(im(by(t)), t, t)) + 2*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t))**2 - 2*(Derivative(re(ay(t)), t) - Derivative(re(by(t)), t))**2 + 2*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t))**2 - 2*(Derivative(im(ay(t)), t) - Derivative(im(by(t)), t))**2 - ((re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t, t) - Derivative(re(bx(t)), t, t)) + (im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t, t) - Derivative(im(bx(t)), t, t)) + (Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t))**2 + (Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t))**2)*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/Abs(ax(t) - bx(t))**2 + 2*ax(t)*Derivative(ax(t), t, t) - 2*ax(t)*Derivative(bx(t), t, t) + 2*ay(t)*Derivative(ay(t), t, t) - 2*ay(t)*Derivative(by(t), t, t) - 2*bx(t)*Derivative(ax(t), t, t) + 2*bx(t)*Derivative(bx(t), t, t) - 2*by(t)*Derivative(ay(t), t, t) + 2*by(t)*Derivative(by(t), t, t) + 2*Derivative(ax(t), t)**2 - 4*Derivative(ax(t), t)*Derivative(bx(t), t) + 2*Derivative(ay(t), t)**2 - 4*Derivative(ay(t), t)*Derivative(by(t), t) + 2*Derivative(bx(t), t)**2 + 2*Derivative(by(t), t)**2 - 4*(ax(t)*Derivative(ax(t), t) - ax(t)*Derivative(bx(t), t) + ay(t)*Derivative(ay(t), t) - ay(t)*Derivative(by(t), t) - bx(t)*Derivative(ax(t), t) + bx(t)*Derivative(bx(t), t) - by(t)*Derivative(ay(t), t) + by(t)*Derivative(by(t), t))*((re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) - (re(ay(t)) - re(by(t)))*(Derivative(re(ay(t)), t) - Derivative(re(by(t)), t)) + (im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)) - (im(ay(t)) - im(by(t)))*(Derivative(im(ay(t)), t) - Derivative(im(by(t)), t)) + ax(t)*Derivative(ax(t), t) - ax(t)*Derivative(bx(t), t) + ay(t)*Derivative(ay(t), t) - ay(t)*Derivative(by(t), t) - bx(t)*Derivative(ax(t), t) + bx(t)*Derivative(bx(t), t) - by(t)*Derivative(ay(t), t) + by(t)*Derivative(by(t), t))/(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2) - (ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)*(ax(t)*Derivative(ax(t), t, t) - ax(t)*Derivative(bx(t), t, t) + ay(t)*Derivative(ay(t), t, t) - ay(t)*Derivative(by(t), t, t) - bx(t)*Derivative(ax(t), t, t) + bx(t)*Derivative(bx(t), t, t) - by(t)*Derivative(ay(t), t, t) + by(t)*Derivative(by(t), t, t) + Derivative(ax(t), t)**2 - 2*Derivative(ax(t), t)*Derivative(bx(t), t) + Derivative(ay(t), t)**2 - 2*Derivative(ay(t), t)*Derivative(by(t), t) + Derivative(bx(t), t)**2 + Derivative(by(t), t)**2)/(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2) + 3*(ax(t)*Derivative(ax(t), t) - ax(t)*Derivative(bx(t), t) + ay(t)*Derivative(ay(t), t) - ay(t)*Derivative(by(t), t) - bx(t)*Derivative(ax(t), t) + bx(t)*Derivative(bx(t), t) - by(t)*Derivative(ay(t), t) + by(t)*Derivative(by(t), t))**2*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)**2)/(sqrt(1 - (ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)**2/(4*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t))**2))*sqrt(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t))) + (ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)*(((re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) + (im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)))*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/Abs(ax(t) - bx(t))**2 - 2*(re(ax(t)) - re(bx(t)))*(Derivative(re(ax(t)), t) - Derivative(re(bx(t)), t)) + 2*(re(ay(t)) - re(by(t)))*(Derivative(re(ay(t)), t) - Derivative(re(by(t)), t)) - 2*(im(ax(t)) - im(bx(t)))*(Derivative(im(ax(t)), t) - Derivative(im(bx(t)), t)) + 2*(im(ay(t)) - im(by(t)))*(Derivative(im(ay(t)), t) - Derivative(im(by(t)), t)) - 2*ax(t)*Derivative(ax(t), t) + 2*ax(t)*Derivative(bx(t), t) - 2*ay(t)*Derivative(ay(t), t) + 2*ay(t)*Derivative(by(t), t) + 2*bx(t)*Derivative(ax(t), t) - 2*bx(t)*Derivative(bx(t), t) + 2*by(t)*Derivative(ay(t), t) - 2*by(t)*Derivative(by(t), t) + (ax(t)*Derivative(ax(t), t) - ax(t)*Derivative(bx(t), t) + ay(t)*Derivative(ay(t), t) - ay(t)*Derivative(by(t), t) - bx(t)*Derivative(ax(t), t) + bx(t)*Derivative(bx(t), t) - by(t)*Derivative(ay(t), t) + by(t)*Derivative(by(t), t))*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2))**2/((1 - (ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)**2/(4*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t))**2))**(3/2)*(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)**(3/2)*Abs(ax(t) - bx(t))**3))*cos(bac(t) - acos((ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2 + Abs(ax(t) - bx(t))**2 - Abs(ay(t) - by(t))**2)/(2*sqrt(ax(t)**2 - 2*ax(t)*bx(t) + ay(t)**2 - 2*ay(t)*by(t) + bx(t)**2 + by(t)**2)*Abs(ax(t) - bx(t)))))/8 + Derivative(ay(t), t, t)
>Exit code: 0
'''

