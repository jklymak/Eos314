load hotctd_data

jmkfigure(1,1,0.45);clf

plot(hotctd_squish.temp(:,1),hotctd_squish.depth,'linewi',1.5,'col',[1 1 1]*0.6);
axis ij;
set(gca,'ylim',[0 200]);
xlabel('T [^oC]');
ylabel('DEPTH [m]');

legend('Jul','Jan',4);
title('Hawaiian Ocean Time Series');

print -djpeg95 -r250 ../images/HotsT.jpg