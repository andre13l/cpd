import time
import numpy as np

def on_mult(m_ar, m_br):
    start_time = time.time()
    
    pha = np.ones((m_ar, m_ar))
    phb = np.array([[i + 1 for _ in range(m_br)] for i in range(m_br)])

    phc = np.dot(pha, phb)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time: {elapsed_time:.3f} seconds")

    print("Result matrix:")
    for i in (phc[:1, :min(10, m_br)]):
        print (i)

lin = int(input("number of lines\n"))
col = lin
on_mult(col, lin)
