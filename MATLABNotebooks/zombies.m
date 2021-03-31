function [time,Nz,Np] = zombies(Nz,Np,p)
%ZOMBIES models a zombie attack on Np people by Nz zombies, each zombie
%attacks one person each time step and has a probability of p of turning
%that person into a new zombie
clf
time =0;
pop0 = Np+Nz;
pgraph = animatedline(0,Np,'Color','Blue','Marker','o');
zgraph = animatedline(0,Nz,'Color','Red','Marker','*');
axis([0,50,0,Np+Nz])
xlabel('Time (Days)')
ylabel('Numbers')
legend('People','Zombies')
while Nz>0 & Np>0 & time<100
    pdz = makedist('Binomial','N',min([Nz Np]),'p',p);
    zsuccess = random(pdz);
    psuccess = Nz - zsuccess;
    Nz = Nz+zsuccess - psuccess;
    Np = Np - zsuccess;
    % Np = Np - zsuccess + psuccess; % Can zombies be turned back?
    time = time+1;
    addpoints(pgraph,time,Np)
    addpoints(zgraph,time,Nz)
    axis([0,time+2,0,pop0])
    drawnow
end

if Np<=0
    sprintf('%i Zombies win in %i days',Nz+Np,time)
elseif Nz<=0
    sprintf('%i people triumph in %i days',Np,time)
elseif time>100
    sprintf('Stalemale in %i days',time)
end

end


