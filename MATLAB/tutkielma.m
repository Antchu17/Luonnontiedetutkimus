load jyyni
teksti = input("Anna tekstitiedoston nimi")
fits = input("Anna fits tiedoston nimi")
fits = fits;
crval = teksti{1,2};
cdelt = teksti{1,3};
naxis = teksti{1,4} - 1;
fits(end) = [];

lambdaMax = crval + (cdelt*(naxis-1));
lambdaMin = crval;

lambda = [lambdaMin:cdelt:lambdaMax];

sprintf('%0.3f',fmin);
sprintf('%0.3f',fmax);

loglog(lambda, fits,'.-')
xlabel("Aallonpituus")
ylabel("Intensiivisyys")

sHa = min(fits);
idx = find(fits==sHa);
lambdaHa = lambda(idx);

hold on
loglog(lambdaHa,sHa, 'rs', 'MarkerSize',8)
sprintf('%0.3f',sHa);

lambdaDelta = 6562.8 - lambdaHa

disp(lambdaHa)
z = (lambdaHa/6562.8) - 1 
v = z * 299792.458
%jos v (nopeus) on negatiivinen niin tähti lähestyy havaitsijaa
