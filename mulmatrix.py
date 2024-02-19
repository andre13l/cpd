import time
import numpy as np

def on_mult(m_ar, m_br):
    start_time = time.time()
    
    pha = np.ones((m_ar, m_ar))
    phb = np.array([[i + 1 for _ in range(m_br)] for i in range(m_br)])

    phc = np.zeros((m_ar, m_br))
    for i in range(m_ar):
        for j in range(m_br):
            temp = 0
            for k in range(m_ar):
                temp += pha[i, k] * phb[k, j]
            phc[i, j] = temp

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time: {elapsed_time:.3f} seconds")

    print("Result matrix:")
    for i in (phc[:1, :min(10, m_br)]):
        print (i)

lin = int(input("number of lines\n"))
col = lin
on_mult(col, lin)
