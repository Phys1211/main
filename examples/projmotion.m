function [Range,maxh,T] = projmotion(v0,theta,H)
% PROJMOTION(H,V0,THETA) plots the motion of a projectile with initial
% height H, initial velocity v0 and launch angle of theta (in Degrees!!)

%% Error checking
if nargin<3
    disp('Using default values')
end
switch nargin
    case 0
        v0=10;
        theta=45;
        H=0;
    case 1
        H=0;
        theta=45;
    case 2
        H=0;
end
if theta>90 | theta<0
    disp('Please specify a launch angle between 0 and 90 degrees')
end
%% Setup using kinematic equations
g=9.81;
theta = (pi/180)*theta;
x = @(t) v0*cos(theta)*t;
y = @(t) H + v0*sin(theta)*t - (1/2)*g*t.^2;
sol = quad(-1/2*g, v0*sin(theta),H);
T = max(sol);
maxh = H+(v0*sin(theta))^2/(2*g);
%% Graphing the trajectory with rough animation
clf
h = animatedline(x(0),y(0));
title('Projectile Trajectory')
xlabel('horizontal distance (m)')
ylabel('vertical distance (m)')
axis([0,1.05*x(T),0,1.05*maxh])

for k=0.01:0.1:T
    addpoints(h,x(k),y(k));
    drawnow
    if y(k)<0
        break
    end
end
hold on
% putting red circle at place of impact
plot(x(T),0,'ro') 
hold off
time=0:0.01:T;
maxh=max(y(time));
Range = x(T);
end
%% Nested function used to solve a quadratic equation
function sol =  quad(a,b,c)
x1 = -b./(2.*a) + sqrt(b.^2-4*a*c)/(2*a);
x2 = -b./(2.*a) - sqrt(b.^2-4*a*c)/(2*a);
sol = [x1; x2];
end