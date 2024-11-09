from pylab import *

##set figure properties
aw = 2
fs = 18
lw = 3
ms = 6
alpha = 0.6
font = {'size'   : fs}
matplotlib.rc('font', **font)
matplotlib.rc('axes' , lw=aw)

def set_fig_properties(ax_list):
    tl = 8
    tw = 2
    tlm = 4
    
    for ax in ax_list:
        ax.tick_params(which='major', length=tl, width=tw)
        ax.tick_params(which='minor', length=tlm, width=tw)
        ax.tick_params(which='both', axis='both', direction='out', right=False, top=False)


loss = loadtxt('./loss.out')
loss[:,0] = np.arange(1, len(loss) + 1)*100
print("We have run %s steps!"%loss[-1, 0])
energy_train = loadtxt('./energy_train.out')
energy_test = loadtxt('./energy_test.out')
force_train = loadtxt('./force_train.out')
force_test = loadtxt('./force_test.out')

figure(figsize=(16, 14))
subplot(2, 1, 1)
set_fig_properties([gca()])
# loglog(loss[:, 0], loss[:, 1],  ls="-", lw=lw, c = "C0", label="Total")
# loglog(loss[:, 0], loss[:, 2],  ls="-", lw=lw, c = "C1", label="L1")
# loglog(loss[:, 0], loss[:, 3],  ls="-", lw=lw, c = "C2", label="L2")
loglog(loss[:, 0], loss[:, 4],  ls="-", lw=lw, c = "C0", label="E-train")
loglog(loss[:, 0], loss[:, 7],  ls="-", lw=lw, c = "C1", label="E-test")
loglog(loss[:, 0], loss[:, 5],  ls="-", lw=lw, c = "C2", label="F-train")
loglog(loss[:, 0], loss[:, 8],  ls="-", lw=lw, c = "C3", label="F-test")
xlim([1e2, 1e6])
ylim([1e-3, 1e0])
xlabel('Generation')
ylabel('Loss')
legend(loc="lower left", ncol=2)
title("(a)")


subplot(2, 2, 3)
set_fig_properties([gca()])
plot(energy_train[:, 1], energy_train[:, 0], 'o', c="C0", ms=ms, alpha=alpha, label="Train")
plot(energy_test[:, 1], energy_test[:, 0], 'o', c="C1", ms=ms, alpha=alpha, label="Test")
# emin = min([np.min(energy_train), np.min(energy_test)])
# emax = max([np.max(energy_train), np.max(energy_test)])
emin = -7.2
emax = -6.4
plot([emin, emax], [emin, emax], c = "grey", lw = 1)
xlim([emin, emax])
ylim([emin, emax])
gca().set_xticks(np.linspace(emin, emax, 5))
gca().set_yticks(np.linspace(emin, emax, 5))
xlabel('DFT energy (eV/atom)')
ylabel('NEP energy (eV/atom)')
legend(loc="upper left")
title("(b)")


subplot(2, 2, 4)
set_fig_properties([gca()])
plot(np.concatenate(force_train[:, 3:6]), np.concatenate(force_train[:, 0:3]), 'o', c="C2", ms=ms, alpha=alpha, label="Train")
plot(np.concatenate(force_test[:, 3:6]), np.concatenate(force_test[:, 0:3]), 'o', c="C3", ms=ms, alpha=alpha, label="Test")
# fmin = min([np.min(force_train), np.min(force_test)])
# fmax = max([np.max(force_train), np.max(force_test)])
fmin = -20
fmax = 20
plot([fmin, fmax], [fmin, fmax], c = "grey", lw = 1)
xlim([fmin, fmax])
ylim([fmin, fmax])
gca().set_xticks(np.linspace(fmin, fmax, 5))
gca().set_yticks(np.linspace(fmin, fmax, 5))
xlabel(r'DFT force (eV/$\rm{\AA}$)')
ylabel(r'NEP force (eV/$\rm{\AA}$)')
legend(loc="upper left")
title("(c)")


subplots_adjust(wspace=0.3, hspace=0.25)
savefig("RMSE.png", bbox_inches='tight')
