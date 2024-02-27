# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 17:17:49 2024

@author: swatc
"""

def truth_table():
    print("P\tQ\tP AND Q\tP OR Q\tNOT P\tP XOR Q")
    print("-" * 40)
    
    # 所有可能的P和Q取值
    values = [True, False]
    
    for p in values:
        for q in values:
            p_and_q = p and q
            p_or_q = p or q
            not_p = not p
            p_xor_q = (p and not q) or (not p and q)
            
            print(f"{p}\t{q}\t{p_and_q}\t{p_or_q}\t{not_p}\t{p_xor_q}")

truth_table()
