clear all; close all; clc;

L=10; 
N=2048;
t2 = linspace(0,L,N+1); t=t2(1:N);
k=((2*pi)/L)*[0:N/2-1 -N/2:-1]; ks=ifftshift(k);

S = (2*sin(2*t)+0.5*tanh(0.5*(t-3))+0.28*exp(-(t-4).^2)...
    +1.5*sin(5*t)+4*cos(3*(t-6).^2))/10;
St = fft(S);
width = 10.1;
slide = 0:0.1:10;
for j=1:length(slide)
    f=exp(-width*(t-slide(j)).^2);
    Sf=f.*S;
    Sft = fft(Sf);
    
    subplot(3,1,1) , plot(t,S,'k',t,f,'r')
    subplot(3,1,2) , plot(t,Sf,'k')
    subplot(3,1,3) , plot(ks,abs(fftshift(Sft))/max(abs(fftshift(Sft))));
    axis([-60 60 0 1])
    drawnow
    pause(0.1)
end