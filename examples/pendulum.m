function [y,t] = pendulum(L,grph,theta0,thetad0) 
% Finds the period of a nonlinear pendulum given the length of the pendulum
% arm and initial conditions. All angles in radians.

%Setting initial conditions
if nargin==0
    error('Must input length')
end
if nargin == 1
   grph=1;
   theta0 = 0.05;
   thetad0 = 0;
end
if nargin == 2
   theta0 = 0.05;
   thetad0 = 0;
end
g=9.81;
% define period for small-angle approximation period
omega = sqrt(g/L);
T= 2*pi/omega;
% specify the number of oscillations to graph ~approximately
N = 10;
t = linspace(0,N*T,100)';
% finds the phase angle
delta = atan(theta0/(omega*thetad0));
% small angle solution
y = theta0*sin(omega*t+delta);

if grph % Plot Solution
    plot(t,y,'b')
    title('Approximate Pendulum Solution')
    xlabel('t')
    ylabel( '\Delta\theta')
end
end
%-------------------------------------------




