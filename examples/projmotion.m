function [dragrange,maxheight,Tf] = projmotion(v0,theta,H,drag)
% PROJMOTION(H,V0,THETA) plots the motion of a projectile with initial
% height H, initial velocity v0 and launch angle of theta (in Degrees!!)
% drag = [c,rho,A,m]
%% Error checking
if nargin<3
    disp('Using default values')
end
switch nargin
    case 0
        v0=10;
        theta=45;
        H=0;
        drag=[0.25,1.29,0.25,1]
    case 1
        H=0;
        theta=45;
        drag=[0.25,1.29,0.25,1]
    case 2
        H=0;
        drag=[0.25,1.29,0.25,1]
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
opts = odeset('events',@events);
[t,w] = ode45(@dwdt,[0 inf],[0; H; v0*cos(theta);v0*sin(theta)],opts,drag);
maxheight = max(w(:,2))
dragrange= w(end,1)
Tf = t(end)
%% Graphinge the trajectory with rough animation
clf
h = animatedline(x(0),y(0));
title('Projectile Trajectory')
xlabel('horizontal distance (m)')
ylabel('vertical distance (m)')
axis([0,1.05*x(T),0,1.05*maxh])
hold on
%plot(t,w(:,2)) %y vs t fro drag
plot(w(:,1),w(:,2),x(t),y(t)) %y vs x for drag
hold off
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

function wsol = dwdt(t,w,drag)
    g=9.81;
    wsol = [w(3);w(4);-drag(1)*drag(2)*drag(3)/(2*drag(4))*w(3)*sqrt(w(3)^2+w(4)^2);-g-drag(1)*drag(2)*drag(3)/(2*drag(4))*w(4)*sqrt(w(3)^2+w(4)^2)]
end

 function [value,isterminal,direction] = events(t,w,drag)
    % EVENTS locates the time when height is zero
    value = w(2);     % detect time when height =0
    isterminal = 1;   % stop the integration
    direction = -1;   % ends going down 
end
