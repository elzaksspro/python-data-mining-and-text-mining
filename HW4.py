__author__ = 'zhuchao'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
def delta(k,N_windows):
    response=pd.Series([0]*N_windows)
    if k>=0 and N_windows-1>=k:
        response[k]=1
    return response

def unitstep(N_windows):
    response=pd.Series([1]*N_windows)
    return response

def box(N_box,N_windows):
    response=pd.Series([1]*N_windows)/N_box
    response[N_box:N_windows]=0
    return response

def ema(Neff,N_windows):
    u=unitstep(N_windows)
    p=Neff/(1+Neff)
    h=pd.Series([(1-p)*p**n*u[n] for n in range(N_windows)])
    return h

def macd(Neff_pos,Neff_neg,N_windows):
    response = ema(Neff_pos, N_windows) - ema(Neff_neg, N_windows)
    return response

def macd_m1(Neff_pos,Neff_neg,N_windows):
    response=delta(Neff_pos,N_windows)-delta(Neff_neg,N_windows)
    return response
def make_h_impulse_comb(N_period, N_window):
    h = pd.Series([0]*N_window)
    for x in range(N_window):
        if(x%N_period==0):
            h[x]=1
    return h
if __name__ == "__main__":
  ###1
  N_windows=1024
  N_period=4
  Neff = 128;
  # (a)
  h_ema=ema(Neff,N_windows)
  # (b)
  N_box=Neff/(1-pow(math.e,-1))
  h_box=box(N_box,N_windows)
  #(c)
  h_comb=make_h_impulse_comb(N_period,N_windows)
  #(d)
  h_ema_sampled=np.multiply(h_comb,h_ema)
  # (e)
  h_box_sampled=np.multiply(h_comb,h_box)
  # (f)
  H_box = abs(np.fft(h_box));
  H_ema = abs(np.fft(h_ema));
  H_box_sampled = N_period * abs(np.fft(h_box_sampled));
  H_ema_sampled = N_period * abs(np.fft(h_ema_sampled));
  # (g)
  













