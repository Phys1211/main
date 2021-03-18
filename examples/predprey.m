function  e = predprey(r0,f0,tf,varargin)
% Lotka-Volterra predator-prey model simulator. PREDPREY(r0,f0,tf) accepts
% initial numbers of rabbits/foxes and the time period of simulation. It
% returns each population at end of tf. It also produces a
% plot of both populations over time and a phase plot.

if isempty(varargin)
    varargin{1} = 'classic'
end

y0 = [r0; f0];
opts = odeset('reltol',1.e-5,'stats','on');
% These particular 
alpha = 2;
beta=0.01;
delta = 0.01;
gamma=1;
% Allows the choice between two classic predator-prey models. 'mod' allows
% the specification of general parameters
switch varargin{1}
    case 'classic'
        [t,y] = ode45(@f,[0 tf],y0,opts);
    case 'mod'
        [t,y] = ode45(@fmod,[0 tf],y0,opts,beta);
end

close all
figure(1)
plot(t,y)
xlabel('t')
ylabel('populations')
legend('rabbits','foxes')

figure(2)
plot(y(1,1),y(1,2),'bo',y(end,1),y(end,2),'ro',y(:,1),y(:,2),'-')
xlabel('rabbits')
ylabel('foxes')
if (r0 == 1/alpha && f0 == 2/alpha)
    axis([0 tf 0.90*r0 1.1*f0])
end

e = y(end,:);

function ydot = fmod(t,y,beta)
ydot = [2*y(1)*(1-y(1)/500)-beta*y(1)*y(2);-y(2)+beta*y(1)*y(2)];
end

function ydot = f(t,y)
ydot = [alpha*y(1)-beta*y(1)*y(2);-gamma*y(2)+delta*y(1)*y(2)];
end

end
% ------------------------------------------




