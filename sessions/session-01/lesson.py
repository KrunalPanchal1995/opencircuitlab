"""Session 1 (Level 1): a battery, a switch and bulbs - series and parallel.

Run:  python start.py 1
Low-voltage educational circuits only (never mains). A simplified model: a bulb is a fixed resistor.
"""
# %% [markdown]
# # Session 1: a battery, a switch and bulbs
# **A. Real-world problem.** Old festival lights were wired in a chain: when one bulb died, the
# whole string went dark. A torch with two cells and two bulbs behaves differently. Why does the
# same battery make bulbs glow dim in one wiring and bright in another?
#
# **Plan.** (1) model a bulb as a resistor, (2) wire N bulbs in series and find the current
# and the voltage across each, (3) wire them in parallel, (4) compare brightness.

# %%
import pathlib

import numpy as np

# where figures are saved (works as a script and in Jupyter/Colab)
OUT = (pathlib.Path(__file__).resolve().parent if "__file__" in globals() else pathlib.Path(".")) / "out"

R_BULB = 10.0     # ohm: our model bulb is a fixed 10 ohm resistor (a real filament gets hotter and changes)


# %% [markdown]
# ## Step 1: one bulb
# Ohm's law: current I = V / R. Power (heat and light) P = V * I. We take brightness to be
# proportional to the power P in the bulb.
#
# ## Step 2: bulbs in series (one path)
# The same current has to pass through every bulb, one after another, so the resistances add:
# R_total = N * R. The battery voltage is shared: each identical bulb gets V / N.
# Check by hand: 6 V and 3 bulbs of 10 ohm give R_total = 30 ohm, I = 6 / 30 = 0.2 A,
# each bulb gets 6 / 3 = 2 V and P = 2 V * 0.2 A = 0.4 W.

# %%
def series_chain(v, n, r=R_BULB, switch_closed=True):
    """N identical bulbs in series on a battery of v volts.

    Returns a dict with the current i (A), the voltage across each bulb (V), the power in
    each bulb (W) and the total power (W). An open switch means no current at all.
    """
    if n < 1 or r <= 0:
        raise ValueError("need at least one bulb and a positive resistance")
    i = v / (n * r) if switch_closed else 0.0
    v_each = i * r
    return {"i": i, "v_each": v_each, "p_each": v_each * i, "p_total": n * v_each * i}


# %% [markdown]
# ## Step 3: bulbs in parallel (several paths)
# Each bulb is connected straight across the battery, so each one gets the full V and carries
# its own current V / R. The battery has to supply all the currents added together:
# I_total = N * V / R.
# Check by hand: 6 V and 3 bulbs: each bulb gets 6 V, 0.6 A, 3.6 W; the battery supplies 1.8 A.

# %%
def parallel_bank(v, n, r=R_BULB, switch_closed=True):
    """N identical bulbs in parallel on a battery of v volts. Same keys as series_chain."""
    if n < 1 or r <= 0:
        raise ValueError("need at least one bulb and a positive resistance")
    i_each = v / r if switch_closed else 0.0
    v_each = i_each * r
    return {"i": n * i_each, "v_each": v_each, "p_each": v_each * i_each, "p_total": n * v_each * i_each}


# %% [markdown]
# ## Step 4: compare
# Series: more bulbs make every bulb dimmer (voltage shared). Parallel: every bulb keeps its
# full brightness but the battery works harder (current grows). Unplug one bulb: in series the
# current stops for all; in parallel the others do not care.

# %%
def compare_table(v=6.0, counts=(1, 2, 3, 4)):
    rows = []
    for n in counts:
        s, p = series_chain(v, n), parallel_bank(v, n)
        rows.append((n, s["i"], s["p_each"], p["i"], p["p_each"]))
    return rows


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    OUT.mkdir(exist_ok=True)
    print("N  series I(A)  series P/bulb(W)  parallel I(A)  parallel P/bulb(W)   (battery 6 V)")
    for n, si, sp, pi, pp in compare_table():
        print(f"{n}  {si:10.3f}  {sp:15.3f}  {pi:13.3f}  {pp:17.3f}")

    ns = np.arange(1, 7)
    fig, ax = plt.subplots(1, 2, figsize=(9, 3.8))
    ax[0].plot(ns, [series_chain(6, n)["p_each"] for n in ns], "o-", label="series")
    ax[0].plot(ns, [parallel_bank(6, n)["p_each"] for n in ns], "s-", label="parallel")
    ax[0].set_xlabel("number of bulbs N")
    ax[0].set_ylabel("power in each bulb (W)")
    ax[0].set_title("Brightness of each bulb (6 V battery)")
    ax[0].grid(alpha=0.3)
    ax[0].legend()
    ax[1].plot(ns, [series_chain(6, n)["i"] for n in ns], "o-", label="series")
    ax[1].plot(ns, [parallel_bank(6, n)["i"] for n in ns], "s-", label="parallel")
    ax[1].set_xlabel("number of bulbs N")
    ax[1].set_ylabel("battery current (A)")
    ax[1].set_title("Current drawn from the battery")
    ax[1].grid(alpha=0.3)
    ax[1].legend()
    fig.tight_layout()
    fig.savefig(OUT / "bulbs_compare.png", dpi=120)

    fig2, ax2 = plt.subplots(figsize=(6, 3.8))
    v = np.linspace(0, 12, 49)
    for n in (1, 2, 3):
        ax2.plot(v, [series_chain(x, n)["p_each"] for x in v], label=f"{n} in series")
    ax2.set_xlabel("battery voltage (V)")
    ax2.set_ylabel("power in each bulb (W)")
    ax2.set_title("Series bulbs: brightness grows with the square of voltage")
    ax2.grid(alpha=0.3)
    ax2.legend()
    fig2.tight_layout()
    fig2.savefig(OUT / "series_power_vs_voltage.png", dpi=120)
    print("saved figures in", OUT)

# %% [markdown]
# ## Try it
# Do the coding tasks, answer the four questions in the README (section F), then run the
# checkpoint.
