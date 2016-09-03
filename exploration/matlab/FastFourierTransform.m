clear all; close all; clc;
%llll.l.l.l.l.l.l...l.ll.l..lllllllll
L = 20;
n = 128;

x2 = linspace(-L/2,L/2,n+1);
% sample time-index domain
x = x2(1:n);
% gaussian funtion
u = exp(-x.^2);
% transformation
ut = fft(u);

subplot(4,1,1)
plot(x,u)
grid on
xlabel('sampled time-index domain');
ylabel('u')
subplot(4,1,2)
plot(abs(ut))
grid on
xlabel('index domain');
ylabel('FFT of u')
subplot(4,1,3)
plot(fftshift(abs(ut)))
grid on
ylabel('FFT of u');
xlabel('index domain')

% we rescale the frequecy domain, since matlab thinks that you are
% working between 2pi periodic domain but we don't so we need to change 
% by incuding this scale. Next [0:n/2-1 -n/2:-1] make a crazy shift in the
% sample index domain,


k = (2*pi/L)*[0:n/2-1 -n/2:-1];
subplot(4,1,4)
plot(k,abs(ut))
grid on
ylabel('FFT of u');
xlabel('sampled frequency-index domain')

figure 
plot(fftshift(k),fftshift(abs(ut)))
grid on
ylabel('FFT of u');
xlabel('sampled frequency-index domain')
